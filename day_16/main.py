from day_16.function import get_todos, write_todos
import time
now = time.strftime("%b %d, %Y %H:%M:%S")

while True:
    user_action = input("Type add, show, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action.startswith('show'):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f'{index+1}-{item}')
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[-2:].strip())
            num = number-1
            todos = get_todos()
            print('Here is todos existing', todos)
            new_todo = input('Enter new todo: ')
            todos[num] = new_todo
            print('Here is how it will be', todos)
            write_todos(todos)
        except ValueError:
            print("Your command is not valid. ")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[-2:].strip())
            todos = get_todos()
            index = number - 1
            todo_to_removed = todos[index].strip('\n')
            todos.pop(number-1)
            write_todos(todos)
            message = f"Todo {todo_to_removed} was removed from the list."
            print(message)
        except IndexError:
            print("I can't find this item in todos")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('You entered unknown value')
print('Bye!')

