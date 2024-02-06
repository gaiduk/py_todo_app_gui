import functions
import PySimpleGUI as sg

label = sg.Text("type in a Todo please")
input_box = sg.InputText(tooltip="Enter ToDo")
add_button = sg.Button("Add")

window = sg.Window("My ToDos APP", layout=[[label], [input_box, add_button]])
window.read()
window.close()