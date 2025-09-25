import { useState } from 'react'
import './App.css'
import ToDoApp from './src/Esercizi/ToDoApp.jsx'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <ToDoApp></ToDoApp>
    </>
  )
}

export default App