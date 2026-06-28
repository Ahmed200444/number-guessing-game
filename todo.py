tasks=[]
while True:
    print('1. Add Task')
    print('2. View Tasks')
    print('3. Quit')
    choice = input('Choose an option: ')

    if choice == '1':
        task = input('Add a task: ')
        tasks.append(task)
    elif choice == '2':
        for task in tasks:
            print(task)
    elif choice == '3':
        break
    else:
        print('Invalid choice')
