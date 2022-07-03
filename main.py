to_do_list_dict = {}
garbage_bin = {}


print("Welcome to Brain Dump! You've got a lot on your mind. \nWhy don't you leave some stuff here? I'll remember it for you and you can retrieve it later.")
print("You have two options. You can toss some thoughts on your remember list. These are things you want to remember. \nOr, if you've got thoughts you need to get rid of, toss them in the garbage bin. \nI'll keep them there for you so you don't have to hold on them!")
print("Psst... Once your remember list or thought garbage bin reaches 1000, the first items you added will be overwritten by new entries.")
exit = False
num = 1
key = 1
while exit == False:
    if num > 1000:
        num = 1
    if key > 1000:
        key = 1
    choice = input("Type 1 to access the REMEMBER list. \nType 2 to access your thought GARBAGE bin. ")
    if choice == "1":
        input1 = input("Type 1 to READ your remember list. \nType 2 to ADD to your remember list. \nType 3 to REMOVE an item from you remember list. ")
        if input1 == "1":
            print(to_do_list_dict)
        elif input1 == "2":
            input2 = input("What to you need to add? ")
            to_do_list_dict[str(num)] = input2
            num += 1
        elif input1 == "3" and len(to_do_list_dict) > 0:
            print(to_do_list_dict)
            remove_item = input("Which number needs to be removed? ")
            del to_do_list_dict[remove_item]
        elif input1 == "3" and len(to_do_list_dict) < 1:
            print("Sorry. There is nothing here to remove. Try again.")
        elif input1 == "exit":
            exit = True
        else:
            print("Sorry. That wasn't one of the options. Try again.")
    elif choice == "2":
        new_choice = input("Type 1 to ADD a thought. \nType 2 to READ old thoughts. \nType 3 if you'd like to REMOVE a thought.")
        if new_choice == "1":
            thought = input("What's on your mind?")
            garbage_bin[str(key)] = thought
            key += 1
        elif new_choice == "2":
            print(garbage_bin)
            print("You might not want to come back here often. You put these thoughts in the garbage for a reason.")
        elif new_choice == "3" and len(garbage_bin) > 0:
            print(garbage_bin)
            removed_item = input("Which number would you like to remove? ")
            del garbage_bin[removed_item]
        elif new_choice == "3" and len(garbage_bin) < 1:
            print("Sorry. There is nothing here to remove. Try again.")
        elif new_choice == "exit":
            exit = True
        else:
            print("Sorry. That wasn't one of the options. Try again.")
    elif choice == "exit":
        exit = True
    else:
        print("Sorry. That wasn't one of the options. Try again.")

print("Thank you for using brain dump! We hope your head feels less full!")