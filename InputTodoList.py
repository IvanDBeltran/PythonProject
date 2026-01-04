import utils

user_prompt = "Type add, show, edit, complete, clear or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        to_do = user_action[4:]
        if len(to_do) == 0:
            to_do = input("Enter task: ").strip()

        toDos = utils.get_list_from_file()
        toDos.append(to_do + "\n")

        utils.write_todos(toDos)

        print(f"You have added {to_do.upper()} to your list.")

    elif user_action.startswith("show"):
        toDos = utils.get_list_from_file()

        if len(toDos) == 0:
            print("List is empty")
            continue

        utils.print_todos()
        print(f"You have {len(toDos)} todos.")

    elif user_action.startswith("edit"):
        toDos = utils.get_list_from_file()

        if len(toDos) == 0:
            print("List is empty")
            continue

        utils.print_todos()
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
                    f"Please enter a valid number between 1 and {len(toDos)}."
                )
                has_updated = True
                continue

            if task_index < 0 or task_index >= len(toDos):
                print(
                    f"Please enter a number between 1 and {len(toDos)}."
                )
                continue

            toDos[task_index] = input("Enter new task: ") + "\n"


            utils.write_todos(toDos)
            utils.print_todos()

            has_updated = True

    elif user_action.startswith("complete"):
        if len(user_action[8:].strip()) == 0:
            temp_index = utils.process_index_input()
        else:
            try:
                temp_index = int(user_action[8:].strip()) - 1
            except ValueError:
                temp_index = utils.process_index_input()

        toDos = utils.get_list_from_file()

        if temp_index < 0 or temp_index >= len(toDos):
            utils.print_todos()
            print(
                f"Please enter a valid number between 0 and {len(toDos)}."
            )
            continue

        completed_task = toDos[temp_index]
        utils.remove_item(toDos, temp_index)

        utils.write_todos(toDos)

    elif user_action.startswith("clear"):
        toDos = utils.get_list_from_file()
        toDos.clear()
        utils.write_todos(toDos)

    elif user_action.startswith("exit"):
        break

    else:
        print("Please enter a valid command.")

print("Bye bye")
