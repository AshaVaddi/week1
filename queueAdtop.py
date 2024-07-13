from collections import deque
def main():
    queue = deque()  
    while True:
        print("\nQueue Operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter item to enqueue: ")
            queue.append(item)
            print(f"{item} enqueued.")
        elif choice == '2':
            if not queue:
                print("Queue is empty. Cannot dequeue.")
            else:
                item = queue.popleft()
                print(f"Dequeued item: {item}")
        elif choice == '3':
            if not queue:
                print("Queue is empty.")
            else:
                print("Queue contents:")
                for item in queue:
                    print(item)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1-4).")

if __name__ == "__main__":
    main()

