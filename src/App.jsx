import { useTranslation } from 'react-i18next'
import Languageselector from './components/language-selector'
import './App.css'


function App() {
  const {t} = useTranslation()
  const description =  t('description')
  console.log(description)
  return(
    <div className='container'>
      <Languageselector />
      <h1>{t("greetings")}</h1>
    </div>
  )
}

export default App
