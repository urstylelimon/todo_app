import function
import PySimpleGUI as sg

level = sg.Text("Type in To-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",layout = [[level],[input_box,add_button]])
window.read()
window.close()


