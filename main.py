import sys

todolist = []
    
def main():
    
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
            print("### YOUR TASKS ###")
            listTask(todolist)


        command = input()

        if "list" in command.lower():
            listTask(todolist)

        elif "add" in command.lower():
            task = command.partition(" ")[2].strip("\"")
            todolist.append(task)
            
        elif "remove" in command.lower():
            if(len(todolist) > 0):
                taskIndex = int(command.partition(" ")[2])-1
                removedtask = todolist[taskIndex]
                todolist.pop(taskIndex)
                print(f"\nYou've removed {removedtask}\n")
                removedtask = ""
            else:
                print("\n>> You have no task to remove! Please add a task first ^^!\n")
        
        elif "edit" in command.lower():
            if(len(todolist) > 0):
                # [edit] [1 weewoo weewoo]
                # [1] [wee woo wee woo]
                task = command.partition(" ")[2]
                newTaskIndex = int(task.partition(" ")[0])-1
                newTask = task.partition(" ")[2]
                todolist[newTaskIndex] = newTask
            else:
                print("\n>> You have no task to remove! Please add a task first ^^!\n")
        
        elif "quit" in command.lower():
            print("All in a day's work, good byeeeee ^^")
            active = False
            sys.exit()
                    
### Operation functions! Can this be a util class? 
def listTask(listitem):
    for i in range(len(listitem)):
        print(f"{i+1}. {listitem[i]}")

if __name__ == "__main__":
    app = main()
    app.run()