import { Trans, useTranslation } from 'react-i18next'
import Languageselector from './components/language-selector'
import './App.css'


function App() {
  const {t} = useTranslation()
  console.log(t('description'))
  const {line1, line2} =  t('description', {
    proJectname : "i18next "
  })
  return(
    <div className='container'>
      <Languageselector />
      <h1>{t("greetings")}</h1>
      <span>
        <Trans 
          i18nKey = {line1}
          values = {{
            proJectname : "i18next",
          }}
          components = {{1: <b />}}
          />
      </span>
      {/* <p>{line1}</p> */}
      <span>{line2}</span>
    </div>
  )
}

export default App
cd