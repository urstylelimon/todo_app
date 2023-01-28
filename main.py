while True:
    user_prompt = input("What do you want ? type add or show or complete or edit or exit : \n")
    user_prompt = user_prompt.strip()

    match user_prompt:
        case 'add':
            todo = input("Enter your todo : ") + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            c_todo = todo.capitalize()
            todos.append(c_todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            for index, item in enumerate(todos):
                items = item.title()

                '''
                This is another method

                print(index + 1 ,'-', items) 
                '''

                output = f"{index + 1} - {items}"
                print(output)

        case 'edit':
            todo_index = int(input("Enter the number : "))
            todo_index = todo_index - 1
            todos[todo_index] = input("Enter your update todo : ")

        case 'complete':
            com_1 = int(input("Enter the todo name witch you complete : \n"))
            com_2 = todos.pop(com_1 - 1)

        case 'exit':
            break
        case whatever:
            print("Please enter the right key.")

print('Thank you for using our app')