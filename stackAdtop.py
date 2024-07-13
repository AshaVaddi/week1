from collections import deque
stack = deque()  # Creating an empty deque to act as stack
while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter item to push onto stack: ")
            stack.append(item)
            print(f"{item} pushed onto stack.")
        elif choice == '2':
            if not stack:
                print("Stack is empty. Cannot pop.")
            else:
                item = stack.pop()
                print(f"Popped item: {item}")
        elif choice == '3':
            if not stack:
                print("Stack is empty.")
            else:
                print("Stack contents:")
                for item in reversed(stack):
                    print(item)
        elif choice == '4':
            print("Exiting program.")
        else:
            print("Invalid choice. Please enter a valid option (1-4).")


