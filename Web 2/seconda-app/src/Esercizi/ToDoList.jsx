import React from 'react'
import ToDoItem from './ToDoItem'

const ToDoList = (props) => {
    
  return (
    <div>
        {
            props.tasks.map((task)=>{
                return(<ToDoItem></ToDoItem>)
            })
        }
        

    </div>
  )
}

export default ToDoList