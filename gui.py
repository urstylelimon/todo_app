import function
import PySimpleGUI as sg

level = sg.Text("Type in To-do")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout = [[level],[input_box,add_button]],
                   font=('Helvetica',20))
while True:
    event,value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = function.file_read()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            function.file_write(todos)

        case sg.WIN_CLOSED:
            break

window.close()
