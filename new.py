import itertools

# Distance matrix
distances = [
    [0, 5, 10],   # Distances from A
    [5, 0, 15],   # Distances from B
    [10, 15, 0]   # Distances from C
]

# City names for reference
cities = ['A', 'B', 'C']

# Function to calculate the total distance of a route
def calculate_distance(route):
    total_distance = 0
    num_cities = len(route)
    for i in range(num_cities):
        # Add distance from current city to the next
        print(str(i)+ "index")
        total_distance += distances[route[i]][route[(i + 1) % num_cities]]
        print(route)
        print(distances[route[i]])
        print("distances[route[i]]")
        print(route[(i + 1) % num_cities])
        print(distances[route[i]][route[(i + 1) % num_cities]])
        print("distances[route[i]][route[(i + 1) % num_cities]]")
        print(distances[route[i]])
        print("distances[route[i]]")
        print(str(i)+" after")
        print("--------------------------------------")
        # import pdb;pdb.set_trace()
    return total_distance

# Find the shortest route
def find_shortest_route():
    shortest_distance = float('inf')
    shortest_route = None
    
    for perm in itertools.permutations(range(len(cities))):
        print([perm for perm in itertools.permutations(range(len(cities)))])
        print(*perm)
        current_distance = calculate_distance(perm)
        
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_route = perm
            
    return shortest_route, shortest_distance

# Main execution
shortest_route, shortest_distance = find_shortest_route()
print("Shortest route:", ' -> '.join(cities[i] for i in shortest_route))
print("Shortest distance:", shortest_distance)
