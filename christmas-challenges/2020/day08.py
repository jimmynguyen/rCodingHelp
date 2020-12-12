# Christmas List! (Day 8)
# Challenge :
# Write a program that allows the user to input a list of items they want to Christmas and save it to/load it from a file.
import os


def save_file(filename,lines):
    with open(filename,"w") as file:
        file.writelines("\n".join(lines))


def load_file(filename):
    if not os.path.isfile(filename):
        return []
    with open(filename) as file:
        return [x.strip() for x in file.readlines()]


filename = "day08.txt"
items = load_file(filename)
while True:
    action = input("What do you want to do? (Enter the # for the action)\n  1 - add item\n  2 - remove item\n  3 - show items\n  q - quit\n>> ")
    if action == "1":
        item = input("Enter item to add: ")
        items.append(item)
        print("added item \"{}\"\n".format(item))
        save_file(filename,items)
    elif action == "2":
        item = input("Enter item to remove: ")
        if item not in items:
            print("item \"{}\" not in list\n".format(item))
        while item in items:
            items.remove(item)
        print("removed item(s) \"{}\"\n".format(item))
        save_file(filename,items)
    elif action == "3":
        items = load_file(filename)
        if len(items) == 0:
            print("list is empty\n")
        else:
            print("christmas list:\n{}\n".format("\n".join(items)))
    elif action == "q":
        print("exiting...")
        break
    else:
        print("invalid action: {}\n".format(action))