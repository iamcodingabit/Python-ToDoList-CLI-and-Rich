import sys
###
# todo add "superiority complex"
# todo remove 1
# todo edit 2 "Skiwhoa kasual"
# todo finish 3 "werewrwerewrwrwrwrwr"
# todo help
###

def main():
    todolist = []
    
    menulist = (
        "Add task",
        "Edit task",
        "Remove task",
    )

    task = ""
    active = True
    command = ""

    print("Welcome to the Obligatory To Do List App!")

    while(active):    
        ### LISTING OUT ALL THE TASKS
        if(len(todolist)>0):
            print("### HERE ARE YOUR TASKS ###")
            listTask(todolist)
            print("###########################\n")
        
        print("What would you like to do?")
        for i in range(len(menulist)):
            print(f"{i+1}. {menulist[i]}")
        print("0. Quit")

        choice = input("\n>> I would like to (Type the number): ")

        if "Add".lower() in menulist[int(choice)-1].lower():
            task = addTask()
            print(f">> You've added: {task}")
            todolist.append(task)
            
        elif "Remove".lower() in menulist[int(choice)-1].lower():
            if(len(todolist) > 0):
                taskindex = removeTask(todolist)-1
                removedtask = todolist[taskindex]
                todolist.pop(taskindex)
                print(f"\nYou've removed {removedtask}\n")
                removedtask = ""
            else:
                print("\n>> You have no task to remove! Please add a task first ^^!\n")
                
        elif "Edit".lower() in menulist[int(choice)-1].lower():
            taskindex = editTask(todolist)-1
            newtask = input(">> What would you like the new task to be? \n")
            todolist[taskindex] = newtask
            
        elif choice == '0':
            print("All in a day's work, good byeeeee ^^")
            active = False
            sys.exit()
            
### Operation functions! Can this be a util class? 
def addTask():
    task = input("What task would you like to add? ")
    return task

def removeTask(todolist):
    print("Which task would you like to remove?")
    listTask(todolist)
    
    choice = input("Which would you like to remove? ")
    return int(choice)

def finishTask(todolist):
    print("You've finished: ")

def editTask(todolist):
    listTask(todolist)
    task = input("Which task would you like to edit? ")
    return int(task)
    
def listTask(listitem):
    for i in range(len(listitem)):
        print(f"{i+1}. {listitem[i]}")

if __name__ == "__main__":
    app = main()
    app.run()