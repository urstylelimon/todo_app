import function
import PySimpleGUI as sg

level = sg.Text("Type in To-do")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values=function.file_read(),key="todos",
                      enable_events=True,size=[45,10])
edit_btn = sg.Button("Edit")


window = sg.Window("My To-Do App",
                   layout = [[level],[input_box,add_button],[list_box,edit_btn]],
                   font=('Helvetica',20))
while True:
    event,value = window.read()
    print(1,event)
    print(2,value)
    print(3,event,value)
    print(4, value['todos'])
    match event:
        case "Add":
            todos = function.file_read()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            function.file_write(todos)
            window['todos'].update(values=todos)

        case "Edit":
            edit_todo = value['todos'][0]
            new_todo = value['todo']

            todos = function.file_read()
            index = todos.index(edit_todo)
            todos[index] = new_todo
            function.file_write(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=value['todos'][0])

        case sg.WIN_CLOSED:
            break



window.close()
