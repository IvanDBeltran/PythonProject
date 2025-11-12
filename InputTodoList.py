
user_prompt = "Type add, show or exit: "

todos = []

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
            for task in todos:
                index = todos.index(task)
                print(f"{index} Task: {task}")
        case "exit":
            break
        case _:
            print("Invalid input")

print("Bye bye")