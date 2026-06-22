#
tasks= []  # empty llist 

def show_tasks():
    if len(tasks) == 0: # check the item of list 
        print("No task")

    else:
        for index ,task in enumerate(tasks):
            print(index + 1, task)


while True:
    print("\n TO DO LIST:")
    print("1. Add task")
    print("2. Show task")
    print("3. Delete task")
    print("4. Exit")


    choice = input("choose : ")
    if choice == "4":
        break

    if choice == "1":
        task = input("Enter task : ")
        tasks.append(task)
        print("Task added")


    elif choice == "2":
        show_tasks()
    
    elif choice == "3":
        show_tasks()
        number = int(input ("Delete task number : "))
        tasks.pop(number-1)
        print("Deleted")


    else:
        print("Invlaid choice")    