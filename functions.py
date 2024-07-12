FILEPATH = 'todos.txt'


def get_todos(filename = FILEPATH):
    with open(filename, 'r') as local_file:
        todos_local = local_file.readlines()
    return todos_local

def write_todos(todos_args, filepath = FILEPATH):
    with open(filepath,'w') as  file:
        file.writelines(todos_args)



if __name__ == '__main__':
    todos = get_todos()