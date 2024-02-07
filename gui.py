import functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


sg.theme("DarkBlue13")

clock = sg.Text('', key="clock")
label = sg.Text("Type in a Todo please")
input_box = sg.InputText(tooltip="Enter ToDo", key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My ToDos APP",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Impact", 13))
while True:
    event, values = window.read(timeout=400)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]

                new_todo = values['todo'].replace('\n',"")

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'

                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please chose an item first", font=("Impact", 15))

        case "Complete":
            try:
                todo_to_delete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_delete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please chose an item first", font=("Impact", 15))
        case "todos":
            window["todo"].update(value=values['todos'][0])
        case "Exit":
            break
        case sg.WINDOW_CLOSED:
            break
# set-executionpolicy remotesigned -scope currentuser
# pyinstaller --onefile --windowed --clean gui.py
window.close()
