from spy_details import name, salu, age, rating
import sys

def start_chat(spy_name, spy_age, spy_rating):
    menu_choices = "What operation you want to perform ?\n 1. Status Update\n 2.\n 3."
    print menu_choices
    choice = raw_input("Enter your choice ")
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    else:
        sys.exit()


question = "Continue as %s %s (Y/N)? " %(salu, name)
existing = raw_input(question)
if existing=="Y":
    print "Authentication complete. Welcome {}{} age: {} and rating: {} Proud to have you".format(salu, name, age, rating)
    spy_status = True
    start_chat(name, age, rating)
else:
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

# age = -1
# if age>4:
#     print "4 se jada"
# elif age >2:
#     print "2 se jada"
# elif age<2:
#     print"2 se kam"