import { useTranslation } from 'react-i18next'
import Languageselector from './components/language-selector'
import './App.css'


function App() {
  const {t} = useTranslation()
  console.log(t('description'))
  const {line1, line2} =  t('description')
  return(
    <div className='container'>
      <Languageselector />
      <h1>{t("greetings")}</h1>
      <p>{line1}</p>
      <span>{line2}</span>
    </div>
  )
}

export default App
