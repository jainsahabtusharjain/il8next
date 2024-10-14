import i18n from 'i18next'
import LanguageDetector from 'i18next-browser-languagedetector'
import { initReactI18next } from 'react-i18next'

i18n.use(LanguageDetector).use(initReactI18next).init({
    debug:true,
    fallbackLng: 'en',
    returnObjects : true,
    resources:{
        en: {
            translation:{
                greetings: "Hello Welcome !",
                description: {
                    line1: "Hello every one we are doinig a dummy project",
                    line2: "this is a second line"
                }
            }
        },
        fr: {
            translation:{
                greetings: "Bonjour Bienvenue",
                description: {
                    line1: "Bonjour à tous, nous faisons un projet factice",
                    line2: "c'est une deuxième ligne"
                }
            }
        },
        hi:{
            translation:{
                greetings: "नमस्ते, आपका स्वागत है",
                description: {
                    line1: "सभी को नमस्कार, हम एक डमी प्रोजेक्ट पर काम कर रहे हैं",
                    line2: "यह दूसरी पंक्ति है"
                }
            }
        }
    },
    ar:{
        translation:{
            greetings: "مرحبا، مرحبا",
            description: {
                line1: "مرحبا بالجميع، نحن نعمل على مشروع وهمي",
                line2: "هذا هو السطر الثاني"
            }
        }
    }
})