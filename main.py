spy_name = raw_input("Welcome to spyChat, please enter your spyName ")
if len(spy_name) > 0:
    print "Welcome " + spy_name
    salu = raw_input("What should i call you Mr or Mrs ")
    spy_name = "Hello " + salu + ". " + spy_name
    print spy_name

    age = int(raw_input("Enter your age "))
    spy_rating = 0
    spy_status = False

    if age > 14 and age < 50:
        spy_rating = raw_input("Enter your spy rating ")
        if spy_rating > 4:
            print "You are pro"
        if spy_rating < 3:
            print "beginner"
        print "You are a valid spy"
        spy_status = True
    else:
        print "You are not valid spy"

else:
    print "Enter name"
