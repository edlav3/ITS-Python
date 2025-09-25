import React, { useEffect, useState } from 'react'
import ToDoForm from './ToDoForm'
import ToDoList from './ToDoList'

const API_URL = "http://localhost:3000/tasks"

const ToDoApp = () => {
    const [tasks, setTasks] = useState([])
    const getTask = async () => {
        try {
            const response = await fetch(API_URL)
            if (!response.ok) throw new Error("Errore Fetch")

            const data = await response.json();
            console.log(data)
            setTasks(data)
        } catch (err) {
            console.log(err)
        }
    }

    useEffect(()=>{
        getTask()
    },[]) /*Le parentesi quadre a fine comando indicano
            che lo useEffect deve eessere esguito una sola volta*/

    return (
        <div>
            ToDoApp
            <ToDoForm></ToDoForm>
            <ToDoList tasks={tasks}></ToDoList>

        </div>
    )
}

export default ToDoApp