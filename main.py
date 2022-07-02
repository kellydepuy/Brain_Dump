to_do_list_dict = {}
garbage_bin = {}


print("Welcome to Brain Dump! You've got enough on your mind. Why don't you leave some stuff here? I'll remember it for you and you can retrieve it later.")
exit = False
num = 1
key = 2
while exit == False:
    choice = input("Type 1 to access the to do list. Type 2 to store a thought you want to throw away.")
    if choice == "1":
        input1 = input("Type 1 to read your to do list. Type 2 to add to your to do list. Type 3 to remove an item from you to do list")
        if input1 == "1":
            print(to_do_list_dict)
        elif input1 == "2":
            input2 = input("What to you need to add?")
            to_do_list_dict[num] = input2
            num += 1
        elif input1 == "3":
            print(to_do_list_dict)
            remove_item = input("Which number needs to be removed?")
            del remove_item
        elif input1 == "exit":
            exit = True
        else:
            print("Sorry. That wasn't one of the options. Try again.")
            to_do_list()
    elif choice == "2":
        new_choice = input(
            "Type 1 to add a thought. Type 2 to review old thoughts. Not recommended. You left them here for a reason. Type 3 if you'd like to remove a thought.")
        if new_choice == "1":
            thought = input("What's on your mind?")
            garbage_bin[key] = thought
            key += 1
        elif new_choice == "2":
            print(garbage_bin)
        elif new_choice == "3":
            print(garbage_bin)
            removed_item = input("Which number would you like to remove?")
            del removed_item
        elif new_choice == "exit":
            exit = True
        else:
            print("Sorry. That wasn't one of the options. Try again.")
    elif choice == "exit":
        exit = True
    else:
        print("Sorry. That wasn't one of the options. Try again.")

print("Thank you for using brain dump! We hope your head feels less full!")