print "Muhammad Khan"
print "PRG 105-003"
print "Instructor: Professor Cindy Grieb"
print "Final project"

choice = 0


# define function to show the main screen
def main_screen():                                                   # choose 1 value from the given choice
    print '\nHello: Welcome to the ""ALL IN ONE STORE" store.\n'
    print "=======================}"
    print "1.Returning Customer   }"
    print "2.New Customer         }"
    print "3.Guest                }"
    print "=======================}\n"


# define menu for customer to pick
def drink_menu():
    print "\nHere is our Beverages Choose which one you want:"
    print "=============================}"
    print "1.Mango Juice                }"
    print "2.Hot Chocolate              }"
    print "3.Juice                      }"
    print "4.Tea                        }"
    print "5.Coffee                     }"
    print "=============================}\n"


# define function to look up customer with its id number.
def customer_id():
    customer = raw_input('\nPlease enter your customer id number:')
    return customer


# define the function open the file, store the customer information in a list and to look up a
# customer by customer id in the input file
def find_customer(customer):
    fin = open('CustomerList.txt')                                      # open the file name CustomerList.txt
    for line in fin:
        customer_record = line.split(',')                               # will split the information with ','
        if customer == customer_record[0]:
            return customer_record                                      # return to the customer record for returning customer


# define function to confirm customer information is correct
def confirm_customer():
    confirm = raw_input('\nPlease confirm if this information is correct (Y/N): ')                     # make sure with the customer that the given information is correct or not
    return confirm.upper()


# define function to handle the selection for a returning customer
def returning_customer():
    ret_customer = customer_id()                                          # call get_customer to accept user input for customer id
    customer_record = find_customer(ret_customer)                         # call find_customer to look up the customer id in the customer list

    if customer_record == 'none':

        print '\nThere is no record of the customer id you entered, please try again.\n'
        returning_customer()                                                 # call the returning_customer function

    else:

        phone = customer_record[7]                                                 # move phone number from customer list to a variable
        print 'Hy and Welcome Back! ' + customer_record[1]                          # it will print  the welcome statement with customers name
        print 'Here Is Your Information: \n'
        print 'Customer Id: ' + customer_record[0]                                    # display the customer id
        print 'First and Last name: ' + customer_record[2], customer_record[1]            # display the customer first and last name
        print 'Street Address: ' + customer_record[3]
        print 'City, State, Zipcode: ' + customer_record[4] + ' , ' + customer_record[5] + ' , ' + customer_record[6]                                     # print city, state, zipcode
        print 'Phone Number: ' + '(' + phone[0:3] + ') ' + phone[3:6] + '-' + phone[6:10]     # format the phone number in a user friendly display

        response = confirm_customer()                                     # call the confirm_customer function

        if response == 'Y':
            print "\nWelcome to 'ALL IN ONE STORE! Here We Serve You Best Drinks "                     # display the welcome message
            print "\nHow Can I help You Today? "
            drink_menu()
        else:
            print "\nOk, this is not the correct customer information, let's try that again."
            returning_customer()                                     # call returning_customer function to allow user to input another id
    return


# define function to handle the selection for a new customer
def new_customer():
    print '\nYou have selected the New Customer Option'
    return


# define function to handle the selection for a guest
def guest_customer():
    print '\nYou have selected the Guest Customer Option\n'
    print 'Welcome to "ALL IN ONE STORE" where it is our goal to serve you the best Drinks and Beverages from our store!'
    return


def wrong_number():
    print('\nPlease enter the appropriate number for your customer type: 1, 2, or 3. ')
    return


while choice >= 0:                              # choose 1 value from the given choice

    main_screen()
    try:
        choice = int(raw_input('\n\nPlease select your customer type from the choice up there: '))
    except ValueError:
        print("\nSorry, I didn't understand that entry.\n")     # this will handle if a user just hits enter or spacebar
        continue     # continue through the loop

    else:
        if choice < 1 or choice > 3:                            # Choice should be 1, 2, 3
            choice = int(raw_input('Please select your customer type. It must be a number equal to 1, 2, or 3.  '))                          # Print it, if customer select wrong choice

        if choice == 1:                          # Print returning customer if choice 1, And find the customer's information
            returning_customer()                  # call returning_customer from the function
            choice = - 1

        elif choice == 2:                        # print new_customer if choice is 2
            new_customer()                        # call new_customer from the function
            drink_menu()
            choice = - 1

        elif choice == 3:                        # print guest_customer if choice is 3
            guest_customer()                      # call guest_customer from the function and welcome
            drink_menu()
            choice = - 1

        else:                                     # if choice is not from 1, 2, 3 give error message
            wrong_number()                         # call the function wrong_number
