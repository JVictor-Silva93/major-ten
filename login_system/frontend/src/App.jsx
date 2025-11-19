import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div className="min-h-screen bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
        <div className="bg-white p-8 rounded-2xl shadow-2xl max-w-md">
          <h1 className="text-4xl font-bold text-gray-800 mb-4">
            Tailwind v4 is Live! 🎉
          </h1>
          <p className="text-gray-600 mb-6">
            Your React + Django + Tailwind v4 project is ready to go!
          </p>
          <button className="w-full bg-blue-600 text-white font-semibold py-3 px-6 rounded-lg hover:bg-blue-700 transition-colors">
            Let's Build!
          </button>
        </div>
      </div>
    </>
  )
}

export default App
