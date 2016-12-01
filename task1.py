choice = 0                                      # initialize the menu choice
# display the menu and get a valid choice
while choice >= 0:                              # choose 1 value from the given choice
    print "\nHello: Welcome to the store.\n"
    print "======================="
    print "1.Returning Customer"
    print "2.New Customer"
    print "3.Guest"
    print "=======================\n"

# i need to check if they give me right choice
# if not i am going to test for the good values
    choice = int(raw_input("Please select your customer type: "))
    try:
        if choice < 1 or choice > 3:                         # choice should be 1, 2, 3
            choice = int(raw_input("Please select your customer type\n Enter a number between 1 and 3 "))
        # if choice is 1 it means returning customer
        elif choice == 1:
            print "Returning Customer"                   # print returning customer
            choice = -1
        # if choice is 2 it means new customer get data from the user and register him/her
        elif choice == 2:
            print "New Customer"                        # print new customer
            choice = -1
        # if choice is 3 it means guest
        elif choice == 3:
            print "Guest"                               # print guest
            choice = -1
        # if choice is not from all these print give him choices from 1, 2, 3
        else:
            print "\n\n Please enter a number\n"                     # print enter a value from the given choices
            #  if user give me a bad value print selection list again
    except ValueError:
            print "Please enter a number"                                # print enter a number from the given choices
