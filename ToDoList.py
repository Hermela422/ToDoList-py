tasks = []


print("what do you want to: add, view, remove, quit")


while True:
    command = input("\nWhat do you want to do? ").lower()

    
    if command == "add":
        task = input("Enter a task to add: ")
        tasks.append(task)
        print("Task added: " + task)


    elif command == "view":
        if not tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")


    elif command == "remove":
        if not tasks:
            print("Thereis no tasks to remove.")
        else:
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")


            try:
                number = int(input("Enter the number of the task to remove: "))
                if 1 <= number <= len(tasks):
                    removed_task = tasks.pop(number - 1)
                    print(f"Task removed: {removed_task}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

   
    elif command == "quit":
        print("\n Here's what you had:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
        print("Goodbye!")
        break

    else:
        print("Unknown command. Please type: add, view, remove, or quit.")
