import time
from function import file_read,file_write

while True:

    print(time.strftime(" \n Date : %b %d %y \n Time : %H hour %S second \n "))
    user_prompt = input("What do you want ? type add or show or complete or edit or exit : ") + "\n"
    user_prompt = user_prompt.strip()

    if user_prompt.startswith("add"):
        todo = user_prompt[4:] + "\n"
        todos = file_read()

        c_todo = todo.capitalize()
        todos.append(c_todo)

        file_write(todos)

        print("\n Sucessfully Added \n")


    if user_prompt.startswith("show"):

        todos = file_read()

        new_todos = []
        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)

        for index, item in enumerate(new_todos):
            items = item.title()
            output = f"{index + 1} - {items}"
            print(output)


    if user_prompt.startswith("edit"):

        todos = file_read()

        new_todos = []
        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)

        for index, item in enumerate(new_todos):
            items = item.title()
            output = f"{index + 1} - {items}"
            print(output)

        todo_index = int(input("Enter the number : "))
        todo_index = todo_index - 1

        edit_todo = input("Enter your update todo : ") + "\n"

        todos[todo_index] = edit_todo

        file_write(todos)

        print("\n Sucessfully Edited \n")


    if user_prompt.startswith("complete"):

        todos = file_read()

        new_todos = []
        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)

        for index, item in enumerate(new_todos):
            items = item.title()
            output = f"{index + 1} - {items}"
            print(output)

        com_1 = int(input("Enter the todo number witch you complete : \n"))
        todos.pop(com_1 - 1)

        file = open('files/todos.txt','w')
        file.writelines(todos)
        file.close()

        print("\n Sucessfully removed \n")


    if user_prompt.startswith("exit"):
        break

    else:
        print(" \n Command is not Valid \n")

print('Thank you for using our app')