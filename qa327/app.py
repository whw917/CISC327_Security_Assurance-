import csv
import time
import re

status = False
user_name = ''
user_email = ''
user_password = ''
balance = -1

accFile = open('accounts.csv', 'r+')
ticketFile = open('tickets.csv', 'r+')
accReader = csv.reader(accFile)
ticketReader = csv.reader(ticketFile)

location_arg = open('frontend_locations.txt', 'r').readline()
tranFile = open(location_arg+'_transactions.csv', 'a+', newline='')
tranWriter = csv.writer(tranFile)


def main():
    print('Welcome the Queens ticket trade machine')
    R1()


def R1():
    if status:
        print('your balance:', balance)  # print out the user's balance
        input1 = input('type your choice:\nsell  buy  update  logout\n')
        if input1 == 'sell':  # user wants to go to sell session
            R4()
        elif input1 == 'buy':  # user wants to go to buy session
            R5()
        elif input1 == 'update':  # user wants to go to update session
            R6()
        elif input1 == 'logout':  # user wants to go to logout session
            R7()
        else:  # user enters other invalid commands
            print('invalid command')
            R1()
    if not status:
        input1 = input('type your choice:\nregister  login  exit\n')
        if input1 == 'register':  # user wants to go to register session
            R2()
        elif input1 == 'login':  # user wants to go to login session
            R3()
        elif input1 == 'exit':  # user wants to go to exit session
            R8()
        else:  # user enters other invalid commands
            print('invalid command')
            R1()


def R2():
    # R2 will be the register session, which will allow user to register their account
    print('register session started successfully')
    try:  # if inputs are missing, call R2 again
        register_email, register_name, register_password, register_password2 = input('please enter your email, user '
                                                                                     'name, password and confirm your '
                                                                                     'password:\n').split(',')
    except:
        #optin to exit
        print('please retype\nthe number of inputs should be 4 or exit')
        exitOrNot = input('do you want to exit register session(type exit to leave):')
        if exitOrNot == 'exit':
            R1()
        R2()

    # do the testing for user inputs, and outputs warning if there is any error. finally, go back to R1
    if not (check_register_email(register_email) and check_exits_email(register_email) and check_register_name(
            register_name) and check_register_password(register_password) and check_register_password2(
        register_password, register_password2)):
        R1()

    tranWriter.writerow(['registration', register_name, register_email, register_password,
                         3000])  # write registration information into file
    tranFile.flush()
    print('account registered')
    R1()


def R3():
    print('login session started successfully')
    try:  # if inputs are missing, call R3 again
        login_email, login_password = input('please type your email and password:\n').split(',')
    except:
        print('please retype\nthe number of inputs should be 2')
        R1()
    if not (check_register_email(login_email) and check_register_password(login_password)):
        R1()  # check the format of inputs. return R1 if there is anything invalid
    for i in accReader:  # go over every user info to check login
        if not i:
            continue
        if login_email == i[0] and login_password == i[2]:
            global status, user_name, user_email, user_password, balance
            # set global value to be the user info if login succeeded
            user_name = i[1]
            user_email = i[0]
            user_password = i[2]
            balance = i[3]
            status = True
            print('account logged in')
            R1()
    # return R1 if failed
    print('login failed')
    R1()


def R4():
    print('selling session started successfully')
    try:    # if inputs are missing, call R4 again
        ticket_name, price, quantity, date = input('please type ticket name, price, quantity, date:\n').split(',')
    except:
        print('please retype\nthe number of inputs should be 4')
        R1()
    if not (check_ticket_name(ticket_name) and check_price(price) and check_quantity_sell(quantity) and check_date(
            date)):
        R1()    # check the format of inputs. return R1 if there is anything invalid
    price = eval(price)
    price = round(price, 2)
    # write the transaction
    tranWriter.writerow(['selling', user_email, ticket_name, price, quantity])
    tranFile.flush()
    print('selling transaction was created successfully')
    R1()


def R5():
    print('buying session started successfully')
    try:    # if inputs are missing, call R5 again
        ticket_name, quantity = input('please type ticket name, quantity:\n').split(',')
    except:
        print('please retype\nthe number of inputs should be 2')
        R1()
    if not (check_ticket_name(ticket_name)):
        R1()    # check the format of inputs. return R1 if there is anything invalid
    count = 0
    for i in ticketReader:  # go over every ticket to check if exists
        if not i:
            continue
        if ticket_name == i[0]:
            price = i[1]
            aval_quantity = i[2]
            count += 1
    if count == 0:
        print('the ticket does not exist')
        R1()
    if not (check_quantity_buy(price, quantity, aval_quantity)):
        R1()    # check the format of inputs. return R1 if there is anything invalid
    price = eval(price)
    price = round(price, 2)
    # write the transaction
    tranWriter.writerow(['buying', user_email, ticket_name, price, quantity])
    tranFile.flush()
    print('buying transaction was created successfully')
    R1()


def R6():
    print('updating session started successfully')
    try:    # if inputs are missing, call R6 again
        ticket_name, price, quantity, date = input('please type ticket name, price, quantity, date:\n').split(',')
    except:
        print('please retype\nthe number of inputs should be 4')
        R1()
    if not (check_ticket_name(ticket_name) and check_price(price) and check_quantity_sell(quantity) and check_date(
            date)):
        R1()    # check the format of inputs. return R1 if there is anything invalid
    count = 0
    for i in ticketReader:  # go over every ticket to check if exists
        if not i:
            continue
        if ticket_name == i[0] and user_email == i[3]:
            count += 1
    if count == 0:
        print('the ticket does not exist')
        R1()
    price = eval(price)
    price = round(price, 2)
    # write the transaction
    tranWriter.writerow(['updating', user_email, ticket_name, price, quantity])
    tranFile.flush()
    print('updating transaction was created successfully')
    R1()


def R7():
    global status, user_name, user_email, user_password, balance
    if status:  # user already logged in
        print("logout successfully")
        user_name = ''
        user_email = ''
        user_password = ''
        balance = -1
        status = False
    else:  # user has not logged in
        print("you are not login\nplease enter login")


def R8():
    print('exit')
    # close three resource files
    accFile.close()
    ticketFile.close()
    tranFile.close()
    exit(0)


'''
this function will check the ticket name format
'''


def check_ticket_name(ticket_name):
    if not (ticket_name.replace(' ','').isalnum()):
        print('transaction was created unsuccessfully\nplease retype\nticket name should be '
              'alphanumeric-only')
        return False
    if ticket_name[0].isspace() or ticket_name[len(ticket_name) - 1].isspace():
        print('transaction was created unsuccessfully\nplease retype\nspace allowed only if it is not the '
              'first or the last character')
        return False
    elif len(ticket_name) > 60:
        print('transaction was created unsuccessfully\nplease retype\nthe ticket name should be no longer '
              'than 60 characters')
        return False
    return True


'''
this function will check the price valid
'''


def check_price(price):
    if not (price.isdigit()):
        print('transaction was created unsuccessfully\nplease retype\nthe ticket price should be numeric')
        return False
    price = eval(price)
    if not (10 <= price <= 100):
        print('transaction was created unsuccessfully\nplease retype\nthe ticket price should be of range ['
              '10, 100]')
        return False
    return True


'''
this function will check the quantity valid when selling
'''


def check_quantity_sell(quantity):
    quantity = eval(quantity)
    if not (isinstance(quantity, int)):
        print('transaction was created unsuccessfully\nplease retype\nthe ticket quantity should be an '
              'integer')
        return False
    if not (0 < quantity <= 100):
        print('transaction was created unsuccessfully\nplease retype\nthe quantity of the tickets has to be '
              'more than 0, and less than or equal to 100')
        return False
    return True


'''
this function will check date format
'''


def check_date(date):
    try:
        time.strptime(date, "%Y%m%d")
        return True
    except:
        print('transaction was created unsuccessfully\nplease retype\ndate must be given in the format '
              'YYYYMMDD')
        return False


'''
this function will check the quantity valid when buying
'''


def check_quantity_buy(price, quantity, aval_quantity):
    price = eval(price)
    quantity = eval(quantity)
    aval_quantity = eval(aval_quantity)
    if not (isinstance(quantity, int)):
        print('transaction was created unsuccessfully\nplease retype\nthe ticket quantity should be an '
              'integer')
        return False
    if not (0 < quantity <= aval_quantity):
        print('transaction was created unsuccessfully\nplease retype\nthe quantity of the tickets has to be '
              'more than 0, and less than or equal to the available quantity')
        return False
    elif not (float(balance) >= price * quantity * 1.35 * 1.05):
        print('transaction was created unsuccessfully\nplease retype\nyour balance is insufficient')
        return False
    return True


'''
this function will take an string of user email as input, and True or False as output
it will check if the format of email is correct 
'''


def check_register_email(register_email):
    # if the format of input email is not as follows, return false
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", register_email) is None:
        print("email format is incorrect\n")
        return False
    return True


'''
this function will take an string of user email as input, and True or False as output
it will check  if the email is already exits 
'''


def check_exits_email(register_email):
    accReader = csv.reader(open('accounts.csv', 'r'))  # read the file
    # if input email already exits, return False
    for i in accReader:
        if not i:
            continue
        elif register_email == i[0]:
            print("account exits\n")
            return False
    return True


'''
this function will take an string of user name as input, and True or False as output
it will check if the format of user name is correct
'''


def check_register_name(register_name):
    # name can only be alphanumerical
    if not (register_name.isalnum() or ' ' in register_name):
        print('user name format is incorrect (User name should be alphanumeric-only)\n')
        return False
    # space allowed only if it's not the first and last character
    if (register_name[0] == ' ' or register_name[len(register_name) - 1] == ' '):
        print('user name format is incorrect (Space allowed only if it is not the first or the last character)\n')
        return False
    # length of name should be longer than 2 and shorter than 20
    elif len(register_name) >= 20 or len(register_name) <= 2 :
        print('user name format is incorrect (User name should be longer than 2 and shorter that 20 characters)\n')
        return False
    return True


'''
this function will take an string of user password as input, and True or False as output
it will check if the format of user password is correct
'''


def check_register_password(register_password):
    # if the format of input password is not as follows, return false
    # at least one upper and one lower case with special characters, minimum 6 in length
    #pattern = r'^(?![A-Za-z0-9]+$)(?![a-z0-9\\W]+$)(?![A-Za-z\\W]+$)(?![A-Z0-9\\W]+$)^.{6,}$'
    pattern = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[-+_!@#$%^&*., ?])^.{6,}$'

    # Compile the ReGex
    res = re.compile(pattern)

    if re.search(res, register_password):
        return True
    print('password format is incorrect\n')
    return False


'''
this function will take two string of user password as input, and True or False as output
it will check if two input are the same
'''


def check_register_password2(register_password, register_password2):
    if register_password == register_password2:
        return True
    print("two password doesn't match, please confirm your password\n")
    return False


if __name__ == "__main__":
    main()
