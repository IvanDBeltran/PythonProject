from utils import get_list_from_file, write_todos, print_todos, process_index_input, remove_item

user_prompt = "Type add, show, edit, complete, clear or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        to_do = user_action[4:]
        if len(to_do) == 0:
            to_do = input("Enter task: ").strip()

        to_dos = get_list_from_file()
        to_dos.append(to_do + "\n")

        write_todos(to_dos)

        print(f"You have added {to_do.upper()} to your list.")

    elif user_action.startswith("show"):
        to_dos = get_list_from_file()

        if len(to_dos) == 0:
            print("List is empty")
            continue

        print_todos()
        print(f"You have {len(to_dos)} todos.")

    elif user_action.startswith("edit"):
        to_dos = get_list_from_file()

        if len(to_dos) == 0:
            print("List is empty")
            continue

        print_todos()
        has_updated = False

        while not has_updated:
            if len(user_action[4:].strip()) == 0:
                raw = input(
                    "Enter task to update or press enter to cancel: "
                ).strip()
            else:
                raw = user_action[4:].strip()

            task_index = 0
            if raw == "":
                print("Edit cancelled.")
                break

            try:
                task_index = int(raw)
                task_index -= 1
            except ValueError:
                print(
                    f"Please enter a valid number between 1 and {len(to_dos)}."
                )
                has_updated = True
                continue

            if task_index < 0 or task_index >= len(to_dos):
                print(
                    f"Please enter a number between 1 and {len(to_dos)}."
                )
                continue

            to_dos[task_index] = input("Enter new task: ") + "\n"


            write_todos(to_dos)
            print_todos()

            has_updated = True

    elif user_action.startswith("complete"):
        if len(user_action[8:].strip()) == 0:
            temp_index = process_index_input()
        else:
            try:
                temp_index = int(user_action[8:].strip()) - 1
            except ValueError:
                temp_index = process_index_input()

        to_dos = get_list_from_file()

        if temp_index < 0 or temp_index >= len(to_dos):
            print_todos()
            print(
                f"Please enter a valid number between 0 and {len(to_dos)}."
            )
            continue

        completed_task = to_dos[temp_index]
        remove_item(to_dos, temp_index)

        write_todos(to_dos)

    elif user_action.startswith("clear"):
        to_dos = get_list_from_file()
        to_dos.clear()
        write_todos(to_dos)

    elif user_action.startswith("exit"):
        break

    else:
        print("Please enter a valid command.")

print("Bye bye")
