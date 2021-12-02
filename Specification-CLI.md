## 💺 Project Requirement - CLI Option

The product you are to design and build is the SeetGeek not SeatGeek online Customer-to-Customer ticket selling system.
A registered user can buy and sell tickets through this online application.

![image](https://user-images.githubusercontent.com/8474647/94140562-689e0980-fe39-11ea-8b75-f160d6931c73.png)

The second option is the original project design in the past. It is a CLI-based application. 
The actor interacts with the system through the terminal, 
and the UI testing is done by running the program with a sequence of coded user inputs. 
There is a front-end component and a backend component.
Unlike the above web application, they are two different programs and not synchronized. 
The front-end first runs during the day in different locations (such as Kingston, Toronto, and Montreal, etc), yield transaction files.
Then the backend merges the transactions and yields the new account details and available tickets for the next day.


If there are any conflicts (such as the same ticket sold to different people, not enough balance), the backend office will simply log errors and let the customer services to call and resolve issues. We also provide a GitHub testing template we created last year with pytest [here](https://github.com/CISC-CMPE-327/CI-Python/tree/python-cli-with-pytest).

:fire: :fire: :fire:   [Template for this option](https://github.com/CISC-CMPE-327/CI-Python/tree/python-cli-with-pytest)

## :fire: Specification - CLI Option

The CLI application handles a sequence of INPUTS performed by the user on their terminal. 
The frontend is a standalone program that takes some arguments, interacts with users, and exits with output files.

|  |  |  |
|-|-|-|
| Program input | 1st argument | String - office location (e.g. Kingston) |
|  | 2nd argument | Path of a CSV file that contains user_email, user_name, user_password, balance. We denote this file as a valid account list file. |
|  | 3rd argument | Path of a CSV file that contains ticket_name, ticket_price, ticket_quality, owner_email. We denote this file as a valid ticket list file. |
|  |  |  |
| Program output |  | A file named [office_location]_transactions.csv (for example, if the program is ran with 1st argument of `kingston`, the file is `kingston_transactions.csv` |
|  |  | This csv file contains the updated list of format:  |
|  |  | for user related transaction (e.g. registration): transaction_name, user_name, user_email, user_password, balance |
|  |  | for ticket related transaction (e.g. sell): transaction_name, user_name, ticket_name, ticket_price, quantity |


The program interacts with the user through different sessions:


|  |  |  |
|-|-|-|
| Sessions | name |  description |
|  | landing | The landing screen (print out available commands) |
|  | login | The user login session (ask for user inputs to login) |
|  | register | The user registration session (ask for user information to register) |
|  | buy | The ticket buying session (ask for ticket info for purchase) |
|  | sell | The ticket selling session (ask for ticket info for sale) |
|  | update | The ticket updating session (ask for ticket info as an update) |


Landing screen details:

|  |  |  |
|-|-|-|
| R1 | landing | If logged in, show the menu item buy, sell, update, and logout. Also, print out the user's balance. |
|  |  | otherwise, show the menu item login, register, and exits. |
|  |  | The landing screen can take commands and go to corresponding sessions |
|  |  | if not logged in, no commands other than login and register are accepted |
|  |  | if logged in, no commands other than buy, sell, logout is accepted |


Sessions and Transactions Detail:

|  | Transaction/Command/Session |  |
|-|-|-|
| R2 | register | Command invalid if the user has logged in. |
|  |  | Starts a registration session |
|  |  | Should ask for email, user name, password, password2 |
|  |  | Email and password both cannot be empty |
|  |  | Email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a human-friendly explanation) |
|  |  | Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character |
|  |  | Password and password2 have to be exactly the same |
|  |  | User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. |
|  |  | User name has to be longer than 2 characters and less than 20 characters. |
|  |  | Email does not exist in the known accounts |
|  |  | For any formatting errors, show message '{} format is incorrect.'.format(the_corresponding_attribute), end the registration session, and print the landing screen |
|  |  | Otherwise, show message 'account registered', end the registration session/process, print the landing screen according to R1 |
|  |  | New account will get a balance of 3000.  |
|  |  | Append a new registration transaction if successfully registered.  |
|  |  |  |
| R3 | login | Command invalid if the user has logged in. |
|  |  | Starts a login session |
|  |  | Should ask for email and password |
|  |  | Email, password all have to satisfy the same required as defined in R1 |
|  |  | For any formatting errors, show message '{} format is incorrect.'.format(the_corresponding_attribute), end the login session, and print the landing screen |
|  |  | If email/password are correct, show message 'account logged in', end the login session/process, and print the landing screen according to R1 |
|  |  | Otherwise, show message 'login failed', end login session/process, and print the landing screen according to R1 |
|  |  |  |
| R4 | sell | Command invalid if the user has not logged in. |
|  |  | Starts a ticket selling session |
|  |  | Should ask for ticket name, price, quantity, date |
|  |  | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. |
|  |  | The name of the ticket is no longer than 60 characters |
|  |  | The quantity of the tickets has to be more than 0, and less than or equal to 100. |
|  |  | Price has to be of range [10, 100] |
|  |  | Date must be given in the format YYYYMMDD (e.g. 20200901) |
|  |  | Append a new registration transaction if successfully sold.  |
|  |  | For any errors, show an error message |
|  |  |  |
| R5 | buy | Command invalid if the user has not logged in. |
|  |  | Starts a ticket selling session |
|  |  | Should ask for ticket name and quantity |
|  |  | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. |
|  |  | The name of the ticket is no longer than 60 characters |
|  |  | The quantity of the tickets has to be more than 0, and less than or equal to the available quantity |
|  |  | The user has more balance than the ticket price * quantity  + service fee (35%) + tax (5%) |
|  |  | Append a new registration transaction if successful.  |
|  |  | For any errors, show an error message |
|  |  |  |
| R6 | update | Command invalid if the user has not logged in. |
|  |  | Starts a ticket updating session |
|  |  | Should ask for ticket name, price, quantity, date |
|  |  | The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. |
|  |  | The name of the ticket is no longer than 60 characters |
|  |  | The quantity of the tickets has to be more than 0, and less than or equal to 100. |
|  |  | Price has to be of range [10, 100] |
|  |  | Date must be given in the format YYYYMMDD (e.g. 20200901) |
|  |  | Append a new update transaction if successful.  |
|  |  | For any errors, show an error message |
|  |  |  |
| R6 | logout | Command invalid if the user has not logged in. |
|  |  | Invalidate login user and go back to the landing session/screen |
|  |  |  |
| R7 | exit | Command invalid if the user has logged in. |
|  |  | Produce output file based on the program output details above. |


### :car: Example frontend test case in natural language:

Resources:
- user.csv
  -  its content is `test@test.com, test_name, test_password, 1000 `
- ticket.csv
  -  its content is  `test_ticket, 39, 3, test@test.com`

Program Arguments:
- Kingston
- user.csv
- ticket.csv

#### R4.4 - The name of the ticket is no longer than 60 characters |

**R4.4.1 Purpose: Test if the ticket name's format (positive case)**

Program Inputs: 
```
login, test@test.com, test_password, sell, another_ticket_name, 30, 30, 20200901, logout, exit
```

Expected Tails of stdout Program Output (match the last several lines of program output):
```
Ticket was created successfully.
Logout successfully.
Exiting program.
```

Expected Output File Content:
 - Not applicable to this requirement. (but will be used for other requirements)
 
 
 
**R4.4.1 Purpose: Test if the ticket name's format (negative case)**

Program Inputs: 
```
login, test@test.com, test_password, sell, vvvvvvvvvvvvvvvvvvvvveryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy_long_ticket, 30, 30, 20200901, logout, exit
```

Expected Tails of stdout Program Output (match the last several lines of program output):
```
Ticket name too long (max 60 characters.)
Logout successfully.
Exiting program.
```

Expected Output File Content:
 - Not applicable to this requirement. (but will be used for other requirements)
 
 
 
 
