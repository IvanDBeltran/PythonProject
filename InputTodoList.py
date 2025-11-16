
user_prompt = "Type add, show, edit, complete or exit: "

todos = []

def print_todos():
    for task in todos:
        index = todos.index(task)
        print(f"{index + 1} .- {task}")

def print_todos_list():
    for index, task in enumerate(todos):
        print(f"{index +1}- {task}")

def process_index_input():
    raw_input = input("What task  number would you like to complete?: \n").strip().lower()
    try:
        index = int(raw_input) - 1
    except ValueError:
        print("Please enter a valid number.")

    return index

def remove_item(index: int):
    if index < 0 or index >= len(todos):
        print("Please enter a valid number.")
        return

    temp = todos.pop(index)
    print(f"{temp} was marked as completed and removed")

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("Enter task: ")
            todos.append(todo)
        case "show":
            if len(todos) == 0:
                print("List is empty")
                continue
            print_todos_list()
        case "edit":
            if len(todos) == 0:
                print("List is empty")
                continue
            print_todos_list()
            has_updated = False

            while not has_updated:
                raw = input("Enter task to update or press enter to cancel ").strip()
                task_index = 0
                if raw == "":
                    print("Edit cancelled.")
                    break

                try:
                    task_index = int(raw)
                    task_index -= 1
                except ValueError:
                    print("Please enter a valid number.")
                    continue


                if task_index < 0 or task_index >= len(todos):
                    print(f"Please enter a number between 1 and {len(todos)}.")
                    continue

                todos[task_index] = input("Enter new task: ")
                print_todos_list()
                has_updated = True
        case "exit":
            break
        case "complete":
            temp_index = process_index_input()
            remove_item(temp_index)

        case _:
            print("Invalid input")

print("Bye bye")