import FreeSimpleGUI as sg
import functions

import functions

label = sg.Text("My To-Do List")
button = sg.Button("Add")
input = sg.Input()

window = sg.Window(title="My First GUI", layout=[[label], [input, button]])
window.read();
window.Close()
