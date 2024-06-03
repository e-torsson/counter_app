def main_menu():
    print('''
          1. Increment (+)
          2. Decrement (-)
          3. Rest Count (0)
          4. Display Count (x)
          5. Exit
          ------------------------
          ''')
    try:
        user_input = int(input('What would you like to do?\n'))
        if user_input > 5:
            print("Invalid option. Please choose a valid option.")
            return main_menu()
        else:
            return user_input
    except ValueError:
        print('Invalid input. Please enter a number.')
        return main_menu()

def main():
    counter = 0
    while True:
        user_input = main_menu()
        if user_input == 1:
            counter += 1
            print('The count has increased by 1')
        elif user_input == 2:
            counter -= 1
            print('The count has decreased by 1')
        elif user_input == 3:
            counter = 0
            print(f'Counter has been reset to: {counter}')
        elif user_input == 4:
            print(f'Current count: {counter}')
        elif user_input == 5:
            print('Exiting program.')
            break
        else:
            print('Invalid option. Please choose a valid option.')
            

if __name__ == '__main__':
    main()