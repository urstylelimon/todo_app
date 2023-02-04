def file_read():
    file = open('files/todos.txt', 'r')
    todos_local = file.readlines()
    file.close()
    return todos_local

def file_write(todo_list):
    file = open('files/todos.txt', 'w')
    file.writelines(todo_list)
    file.close()

