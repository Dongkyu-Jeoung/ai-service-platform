import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'

export default function App() {
  const [form, setForm] = useState({"title" : "", "price" : "", "isbn" : ""})

  const handleFormChange = (e) => {
    const {name, value} = e.target
    setForm({...form, [name] : value})
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    console.log(form);

    // fastapi 호출 : http://127.0.0.1:8000/book => POST
    const response = await fetch(
      "http://127.0.0.1:8000/book",
      {
        method : "POST",
        headers : {
          "Content-Type" : "application/json"
        },
        body : JSON.stringify(form)
      }
    )

    console.log(response);
  }

  return (
    <>
      <h2>도서 관리 프로그램</h2>
      <form onSubmit={handleSubmit}>
        <ul>
          <li>
            <label>제목</label>
            <input type="text" 
                    name='title'
                    value={form.title}
                    onChange={handleFormChange}/>
          </li>
          <li>
            <label>가격</label>
            <input type="text" 
                    name='price'
                    value={form.price}
                    onChange={handleFormChange}/>
          </li>
          <li>
            <label>ISBN</label>
            <input type="text" 
                    name='isbn'
                    value={form.isbn}
                    onChange={handleFormChange}/>
          </li>
          <li>
            <button type='submit'>등록</button>
          </li>
        </ul>
      </form>
    </>
  )
}
