# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            item = input("Enter the item name to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")

        elif choice == '2':
            item = input("Enter the item name to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")

        elif choice == '3':
            print("\nCurrent Shopping List:")
            if shopping_list:
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is empty.")

        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()
