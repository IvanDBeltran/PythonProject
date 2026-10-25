import FreeSimpleGUI as sg
import functions

import functions

label = sg.Text("My To-Do List", background_color="black")
input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
button = sg.Button("Add")

window = sg.Window(title="My To-Do App",
                   layout=[[label], [input_box, button]],
                   font=("Helvetica", 20),
                   background_color="black")

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos();
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.Close()
