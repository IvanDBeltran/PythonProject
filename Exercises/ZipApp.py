import FreeSimpleGUI as sg

TITLE  = "Zip App"
COLOR = sg.theme_background_color("black")

label1 = sg.Text("Select files to compress: ")
label1.BackgroundColor = COLOR
input1 = sg.Input()
button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder: ")
label2.BackgroundColor = COLOR
input2 = sg.Input("")
button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")


window = sg.Window(title = TITLE,
                   background_color = COLOR,
                   layout = [[label1, input1, button1],
                             [label2, input2, button2],
                             [compress_button]])
window.read();
window.Close()

