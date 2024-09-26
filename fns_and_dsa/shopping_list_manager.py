def display_menu():
    print("\n--- Shopping List Manager ---")
    print(f"1. Add Item")
    print(f"2. Remove Item")
    print(f"3. View List")
    print(f"4. Exit")
    print("-----------------------------")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item name to add: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping list.")

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item name to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")

        elif choice == '3':
            # Display the shopping list
            print("\nCurrent Shopping List:")
            if shopping_list:
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
