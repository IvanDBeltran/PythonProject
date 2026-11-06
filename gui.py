import FreeSimpleGUI as sg
import functions

import functions

button_size = (5,1)

label = sg.Text("My To-Do List")
input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("Add",
                       size=button_size)

list_box = sg.Listbox(values=functions.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=(44,10))

edit_button = sg.Button("Edit",
                        size=button_size)

window = sg.Window(title="My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(f"meh {values["todos"]}")
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = values["todo"] + "\n"
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.Close()
