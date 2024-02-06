FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    with open(filepath, "r") as file_loc:
        todos_loc = file_loc.readlines()
    return todos_loc


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, "w") as file_loc:
        file_loc.writelines(todos_arg)


if __name__ == "__main__":
    print(get_todos())

