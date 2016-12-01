# Create a function for each option to be called, and have them print what function is called.
# Have the Guest Protocol display a welcome message because that is all the guest function will do.
# Make sure to save this as a separate file on git hub, it can be in the same folder, but make it a different file

choice = 0
# define function to handle the selection for a returning guest


def returning_cust():
    print '\nYou have selected the Returning Customer Option'
    return

# define function to handle the selection for a new guest


def new_cust():
    print '\nYou have selected the New Customer Option'
    return

# define function to handle the selection for a guest


def guest_cust():
    print '\nYou have selected the Guest Customer Option\n'
    print 'Welcome to "ALL IN ONE STORE" where it is our goal to serve you the best Drinks and Beverages from our store!'
    return

# define function to handle when the selection is not 1, 2, or 3


def wrongnumber():
    print('\nplease select our customer type: 1, 2, or 3. ')
    return

while choice >= 0:                              # choose 1 value from the given choice
    print '\nHello: Welcome to the ""ALL IN ONE STORE" store.\n'
    print "======================="
    print "1.Returning Customer"
    print "2.New Customer"
    print "3.Guest"
    print "=======================\n"
    choice = int(raw_input('\nPlease select your customer type from the choice up there: '))

    try:
        if choice < 1 or choice > 3:
            choice = int(raw_input('Please select your customer type. It must be a number equal to 1, 2, or 3.  '))

        if choice == 1:
            returning_cust()
            choice = - 1

        elif choice == 2:
            new_cust()
            choice = - 1

        elif choice == 3:
            guest_cust()
            choice = - 1

        else:
            wrongnumber()

    except ValueError:
        print ('Enter 1, 2, or 3!')
