import function
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My first todo app", layout=[[label], [input_box, add_button]])
window.read()
print('hello')
window.close()

