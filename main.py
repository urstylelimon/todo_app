while True:
    user_prompt = input("What do you want ? type add or show or complete or edit or exit : \n")
    user_prompt = user_prompt.strip()

    match user_prompt:
        case 'add':
            todo = input("Enter your todo : ") + "\n"

            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            c_todo = todo.capitalize()
            todos.append(c_todo)



            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('files/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)


            for index, item in enumerate(new_todos):
                items = item.title()

                '''
                This is another method

                print(index + 1 ,'-', items) 
                '''

                output = f"{index + 1} - {items}"
                print(output)

        case 'edit':

            file = open('files/todos.txt','r')
            todos = file.readlines()
            file.close()

            todo_index = int(input("Enter the number : "))
            todo_index = todo_index - 1

            edit_todo = input("Enter your update todo : ") + "\n"

            todos[todo_index] = edit_todo

            file = open('files/todos.txt','w')
            file.writelines(todos)
            file.close()


        case 'complete':

            file = open('files/todos.txt','r')
            todos = file.readlines()
            file.close()

            com_1 = int(input("Enter the todo number witch you complete : \n"))
            todos.pop(com_1 - 1)

            file = open('files/todos.txt','w')
            file.writelines(todos)
            file.close()

        case 'exit':
            break

        case whatever:
            print("Please enter the right key.")

print('Thank you for using our app')