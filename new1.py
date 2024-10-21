#!/usr/bin/env python3
import heapq
from typing import List, Tuple

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __lt__(self, other: 'Point') -> bool:
        if self.x != other.x:
            return self.x < other.x
        else:
            return self.y < other.y

    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

class Order:
    def __init__(self, destination: Point, priority: int):
        self.destination = destination
        self.priority = priority

class Robot:
    def __init__(self, start: Point):
        self.current_position = start
        self.route: List[Point] = []

def distance(p1: Point, p2: Point) -> float:
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

def nearest_neighbor(points: List[Point]) -> List[Point]:
    route = [points[0]]  # Start with the first point
    remaining_points = points[1:]
    
    while remaining_points:
        nearest = min(remaining_points, key=lambda p: distance(route[-1], p))
        route.append(nearest)
        remaining_points.remove(nearest)
    
    return route

def two_opt(route: List[Point]) -> List[Point]:
    best_route = route.copy()
    improved = True
    
    while improved:
        improved = False
        for i in range(1, len(best_route) - 2):
            for j in range(i + 1, len(best_route) - 1):
                new_route = best_route[:i] + best_route[j:i:-1] + best_route[j+1:]
                if distance_of_route(new_route) < distance_of_route(best_route):
                    best_route = new_route
                    improved = True
                    break
            if improved:
                break
    
    return best_route

def distance_of_route(route: List[Point]) -> float:
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance(route[i], route[i + 1])
    return total_distance

def heuristic(a: Point, b: Point) -> float:
    # Manhattan distance heuristic
    return abs(a.x - b.x) + abs(a.y - b.y)

def a_star(start: Point, goal: Point, obstacles: List[Point]) -> List[Point]:
    frontier = [(0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            path = [current]
            while current != start:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for next_point in [Point(current.x + 1, current.y),
                          Point(current.x - 1, current.y),
                          Point(current.x, current.y + 1),
                          Point(current.x, current.y - 1)]:
            if next_point not in obstacles:
                new_cost = cost_so_far[current] + distance(current, next_point)
                if next_point not in cost_so_far or new_cost < cost_so_far[next_point]:
                    cost_so_far[next_point] = new_cost
                    priority = new_cost + heuristic(next_point, goal)
                    heapq.heappush(frontier, (priority, next_point))
                    came_from[next_point] = current

    return []  # No path found

class DeliverySystem:
    # import pdb;pdb.set_trace()
    def __init__(self, robot: Robot):
        self.robot = robot
        self.order_queue: List[Tuple[int, Order]] = []  # Priority queue
    
    def add_order(self, order: Order):
        heapq.heappush(self.order_queue, (order.priority, order))
        self.optimize_route()
    
    def optimize_route(self):
        destinations = [order.destination for _, order in self.order_queue]
        initial_route = nearest_neighbor([self.robot.current_position] + destinations)
        optimized_route = two_opt(initial_route)
        self.robot.route = optimized_route[1:]  # Exclude robot's current position
    
    def move_robot(self):
        if self.robot.route:
            next_point = self.robot.route.pop(0)
            path = a_star(self.robot.current_position, next_point, obstacles=[])  # Assume no obstacles for simplicity
            for point in path:
                self.robot.current_position = point
                # Here you would update the robot's actual position
                print(f"Robot moved to {point.x}, {point.y}")
            
            # Check if this was a delivery point
            for i, (priority, order) in enumerate(self.order_queue):
                if order.destination.x == next_point.x and order.destination.y == next_point.y:
                    print(f"Delivered order to {next_point.x}, {next_point.y}")
                    self.order_queue.pop(i)
                    break
            
            self.optimize_route()  # Re-optimize after delivery

# Usage
robot = Robot(Point(0, 0))
system = DeliverySystem(robot)

# Add some orders
system.add_order(Order(Point(3, 4), 1))
system.add_order(Order(Point(-2, 1), 2))
system.add_order(Order(Point(5, -3), 3))

# Simulate robot movement
for _ in range(10):  # Move 10 times
    system.move_robot()