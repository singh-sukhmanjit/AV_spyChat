from spy_details import name, salu, age, rating
import sys

status_messages = ["Bond, James Bond", "I dont give a fuck"]


def add_status(current_status_message):
    if current_status_message != None:
        print "Your status is: {}".format(current_status_message)
    else:
        print "You have no status message "
    default = raw_input("Do want to select from previous status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("Enter new status update ")
        if len(new_status_message) > 0:
            updated_status_message = new_status_message
            status_messages.append(updated_status_message)
    elif default.upper() == "Y":
        status_index = 1
        for status in status_messages:
            print "{}. {}".format(status_index, status)
            status_index = status_index + 1
        status_selected = int(raw_input("Select from above messages "))
        if len(status_messages) >= status_selected:
            updated_status_message = status_messages[status_selected - 1]
    return updated_status_message



def start_chat(spy_name, spy_age, spy_rating):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choices = "What operation you want to perform ?\n 1. Status Update\n 2.\n 3."
        print menu_choices
        choice = int(raw_input("Enter your choice "))
        if choice == 1:
            current_status_message = add_status(current_status_message)
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            show_menu = False


question = "Continue as %s %s (y/n)? " %(salu, name)
existing = raw_input(question)
if existing.upper() == "Y":
    print "Authentication complete. Welcome {}{} age: {} and rating: {} Proud to have you".format(salu, name, age, rating)
    spy_status = True
    start_chat(name, age, rating)
elif existing.upper() == "N":
    spy_name = raw_input("Welcome to spyChat, please enter your spyName ")
    if len(spy_name) > 0:
        print "Welcome " + spy_name
        salu = raw_input("What should i call you Mr or Mrs ")
        print "Hello " + salu + ". " + spy_name

        age = int(raw_input("Enter your age "))
        spy_status = False

        if age > 14 and age < 50:
            spy_rating = raw_input("Enter your spy rating ")
            spy_rating = float(spy_rating)
            if spy_rating > 4.0:
                print "You are pro"
            elif spy_rating < 3.0:
                print "beginner"
            print "Authentication complete. Welcome %s age: %d and rating: %.1f Proud to have you" %(spy_name, age, spy_rating)
            spy_status = True
            start_chat(spy_name, age, spy_rating)
        else:
            print "You are not valid spy"

    else:
        print "Enter name"