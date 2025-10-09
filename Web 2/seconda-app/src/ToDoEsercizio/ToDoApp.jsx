import React, { useEffect, useState } from "react";
import TodoForm from "./ToDoForm";
import TodoList from "./ToDoList";
import { createTasks, fetchTasks, deleteTasks} from '../Services/api'


const API_URL = "http://localhost:3000/tasks"
const TodoApp = () => {
    const [tasks, setTasks] = useState([])
    const getTask = async () => {
        try {
            const data = await fetchTasks()
            console.log(data)
            setTasks(data)
        } catch (err) {
            console.log(err)
        }
    }

    const addTask = async (text) => {
        await createTasks(text)
        getTask();
    }
    const deleteTask = async (id) => {
        await deleteTasks(id);
        getTask();

    }
    const toggleTask = async (id, completed) => {
        await fetch(API_URL + "/" + id,
            {
                method: "PATCH",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ completed: !completed })
            });
        getTask();
    }
    useEffect(() => {
        getTask()
    }, [])

    return (
        <div>
            TodoApp
            <TodoForm onAddTask={addTask}></TodoForm>
            <TodoList tasks={tasks} onDeleteTask={deleteTask} onToggleTask={toggleTask}></TodoList>

        </div>
    )
}

export default TodoApp