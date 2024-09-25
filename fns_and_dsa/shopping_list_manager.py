

def display_menu():

    print(" Shopping List Manager ")
    print(f"1. Add an item")
    print(f"2. Remove an item")
    print(f"3. View shopping list")
    print(f"4. Exit")
   

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            item = input("Enter the item name to add: ")
            shopping_list.append(item)
            #print(f"{item} has been added to the shopping list.")

        elif choice == '2':
            item = input("Enter the item name to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                #print(f"{item} has been removed from the shopping list.")
            else:
                print(f"{item} not found in the shopping list.")

        elif choice == '3':
           # print("\nCurrent Shopping List:")
            if shopping_list:
                #for idx, item in enumerate(shopping_list, start=1):
                for item in shopping_list:
                  print(item)
            else:
                print("The shopping list is empty.")

        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()
