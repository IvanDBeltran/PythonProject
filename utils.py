import constants

def get_list_from_file(path: str=constants.FILE_PATH) -> list[str]:
    with open(path, "r") as file_to_open:
        return file_to_open.readlines()

def write_todos(todos_list: list[str], path: str = constants.FILE_PATH):
    with open(path, "w") as file_to_write:
        file_to_write.writelines(todos_list)

def normalize_todos(todos: list[str]) -> list[str]:
    """Return todos without trailing newlines (for display purposes)."""
    return [item.rstrip("\n") for item in todos]

def print_numbered(items: list[str]) -> None:
    """Print items with 1-based numbering (safe with duplicates)."""
    for index, item in enumerate(items, start=1):
        print(f"{index}.- {item}")


def print_todos(path: str = constants.FILE_PATH) -> None:
    todos = get_list_from_file(path)
    display_todos = normalize_todos(todos)
    print_numbered(display_todos)

def read_valid_index(prompt: str, upper_bound: int) -> int:
    """Read a 0-based index from user input within [0, upper_bound)."""
    while True:
        raw = input(prompt).strip()

        try:
            index = int(raw) - 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 0 <= index < upper_bound:
            return index

        print("Please enter a valid number.")

def process_index_input(path: str = constants.FILE_PATH) -> int:
    todos = get_list_from_file(path)
    return read_valid_index(
        "What task number would you like to modify?: \n",
        upper_bound=len(todos),
    )

def remove_item(todos: list[str], index: int) -> None:
    """Remove an item from the provided list (no file IO here)."""
    if not (0 <= index < len(todos)):
        print("Please enter a valid number.")
        return

    removed = todos.pop(index).rstrip("\n")
    print(f"{removed} was marked as completed and removed")


# def print_todos():
#
#     to_dos = get_list_from_file()
#     """Print all tasks from the global `to_dos` list with 1-based numbering.
#
#         Notes:
#             - Uses `to_dos.index(task)` inside the loop, which returns the first
#               matching index. If duplicate tasks exist, numbering may repeat or be
#               incorrect.
#             - This function depends on a global variable named `to_dos`.
#         """
#     for task in to_dos:
#         index = to_dos.index(task)
#         print(f"{index + 1} .- {task}")


# def print_todos_list():
#     toDos = get_list_from_file()
#     """Print all tasks from the global `toDos` list with 1-based numbering.
#
#        Strips newline characters from each task before printing.
#
#        Notes:
#            - This function depends on a global variable named `toDos`.
#        """
#     new_todos = [item.strip("\n") for item in toDos]  # list comprehension
#
#     for index, task in enumerate(new_todos):
#         print(f"{index + 1}- {task}")


# def process_index_input():
#     toDos = get_list_from_file()
#     raw_input = input(
#         "What task  number would you like to modify?: \n"
#     ).strip().lower()
#     try:
#         index = int(raw_input) - 1
#     except ValueError:
#         print("Please enter a valid number.")
#         return process_index_input()
#
#     if index < 0 or index >= len(toDos):
#         return process_index_input()
#
#     return index

#
# def remove_item(todos: list, index: int):
#     toDos = get_list_from_file()
#     if index < 0 or index >= len(toDos):
#         print("Please enter a valid number.")
#         return
#
#     temp = todos.pop(index)
#     print(f"{temp.strip('\n')} was marked as completed and removed")



