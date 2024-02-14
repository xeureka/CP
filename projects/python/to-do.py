'''
A to do app that allows users to add , view and remove tasks

the applicatioin must provide a menue

save the final result in the file
'''


tasks = []


def add_task():
    try:
        task = input('Enter a task:   ')
    except ValueError as e:
        print(e)
        print("please enter you response in the proper format.")
    else:
        tasks.append(task)
        print("Task added sucessfully")


def delete_task():
    if len(tasks) ==0:
        print('NO tasks to delete')
    else:
        print("Current tasks:  ")

        for i ,task in enumerate(tasks):
            print(f'{i+1}. task')
            try:
                task_number = int(input('Enter the task number to delete: '))

            except ValueError as e:
                print(e)
                print('Please re enter you response')
            else:
                if task_number > 0 and task_number <= len(tasks):
                    del tasks[task_number -1]
                    print("Task deleted sucessfully")
        else:
            print("Invalid input")

def task_view():
    if len(tasks) <0:
        print("No tasks to desplay")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")


while True:
    print("==========TO DO APPLICATION=================")
    print("1.Add task")
    print("2.Delete task")
    print("3.view task")
    print("4.Quit")

    try:
        user = int(input("Select a task number :     "))
    except ValueError as e:
        print(e)

    else:
        if user ==1:
            print()
            add_task()
        elif user ==2:
            print()
            delete_task()
        elif user ==3:
            print("+++++++++++++++++++++++++++++Current runing tasks")
            task_view()
        else:
            if user == "4":
                break
            else:
                print("Invalid input")