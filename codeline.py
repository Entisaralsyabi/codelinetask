
menu_options = {
    1: 'Print Pattern',
    2: 'Rotate Array ',
    3: ' Help',
    4: 'Exit',
}

def print_menu():
    
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
        
def option1():
    n=''
    n = int(input('Enter the number of rows for the pattern: '))

    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()

def option2():
    try:
        n = int(input("Enter the number of elements (n): "))
        k = int(input("Enter the number of steps (k): "))
        arr = list(map(int, input("Enter the array elements seprated by spaces: ").split()))
        temp = []
        for i in range(n-k, n):
            temp.append(arr[i])
        for i in range(0, n-k):
            temp.append(arr[i])
        print("Rotated array: ", temp)
    except ValueError:
        print("Invalid input. Please enter valid integers for n, k, and array elements.")

def option3():
     print(''' --Help-- 
           Option 1: Print a  pattern with 'n' rows of decreasing asterisks.
            Option 2: Rotate an array of  'n' elements of the right by  'k' steps.
            Option 3: Display this help message.
            Option 4: Exit the program.
        ''')
        
def option4():
    print('Exiting the program. Goodbye!')
    exit()  # This will terminate the program immediately

if __name__=='__main__':
    while(True):
        print("\nWelcome to the Menu-Based Program!")
        print_menu()
        option = ''
        try:
            option = int(input("Please select an Option:" ))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           option1()
        elif option == 2:
         option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
