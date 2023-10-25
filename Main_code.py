# Function used to print a decreasing pattern starting from the positive input number

def print_pattern():
    n = int(input("please Enter a positive number of rows for the  Pattern: "))
    if n <= 0:
        print("Please enter a POSITIVE number.")
    else:
        
    # Using for loop to generate a decreasing counting (using -1) starting from the input number to 1 (where 0 is excluded)
        
        for i in range(n, 0, -1):    
            print("*" * i)


#Function used to rotate the array to the right by specified number of steps.
def rotate_array(arr,n,k):
    k=k%n                       # To ensure that k is whithin the range and preventing excessive rotations                 
    arr = arr[n-k:]+arr[:n-k]   # Rotate the array
    return arr
    
#Function used to establish the program
def start_menu():
    print("Please select an Option:")
    print("1. Print Pattern")
    print("2. Rotate Array")
    print("3. Help")
    print("4. Exit")

# Function used to generate a Help menu for the user
def print_help():
    print("---Help Menue---")
    print("1. Print a pattern with n raws of decreasing asterisks.")
    print("2. Rotate array of n elements to the right by k steps.")
    print("3. Display this help message.")
    print("4. Exit the program.")

#Main function of the program
def main():
    while True:
        print("\nWelcome to the Menu-Based Program!")
        start_menu()
        choice = input("Please select an Option:")

        if choice == '1':
            print_pattern()
        elif choice == '2':
            n= int(input('Enter the number of elements (n)'))
            k= int(input('Enter the number of steps (k)'))
            array= [int(x) for x in input('Enter the array elements seperated by space').split()]
            rotated_array=rotate_array(array,n,k)
            print('Rotated Array:', rotated_array)
            
        elif choice == '3':
            print_help()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1,2,3,4).")

if __name__ == "__main__":
    main()
