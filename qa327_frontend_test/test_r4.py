from importlib import reload
import pytest
import os
import io
import sys
import qa327.app as app

path = os.path.dirname(os.path.abspath(__file__))

'''test case R4.x.1'''


def test_successful_case(capsys):
    terminal_input = ['login', 'test@test.com,Pass123..', 'sell', 'asd123,50,10,20201010', 'logout', 'exit']
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'login session started successfully',
                                        'please type your email and password:',
                                        'account logged in',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'selling session started successfully',
                                        'please type ticket name, price, quantity, date:',
                                        'selling transaction was created successfully',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'logout successfully',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = 'selling,test@test.com,asd123,50,10'
    helper(capsys, terminal_input, expected_tail_of_terminal_output, expected_output_transactions)


'''test case R4.1.2 check login has been done in landing session, no need and can not test here'''

'''test case R4.2.2 ticket name has to be alphanumeric-only'''


def test_ticket_name_alphanumeric_only(capsys):
    terminal_input = ['login', 'test@test.com,Pass123..', 'sell', 'asd!@#123,50,10,20201010', 'logout', 'exit']
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'login session started successfully',
                                        'please type your email and password:',
                                        'account logged in',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'selling session started successfully',
                                        'please type ticket name, price, quantity, date:',
                                        'transaction was created unsuccessfully',
                                        'please retype',
                                        'ticket name should be alphanumeric-only',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'logout successfully',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, expected_tail_of_terminal_output, expected_output_transactions)


'''test case R4.2.3 space allowed only if it is not the first or the last character'''


def test_ticket_name_space_not_first_last(capsys):
    terminal_input = ['login', 'test@test.com,Pass123..', 'sell', 'asd123 ,50,10,20201010', 'logout', 'exit']
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'login session started successfully',
                                        'please type your email and password:',
                                        'account logged in',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'selling session started successfully',
                                        'please type ticket name, price, quantity, date:',
                                        'transaction was created unsuccessfully',
                                        'please retype',
                                        'space allowed only if it is not the first or the last character',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'logout successfully',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, expected_tail_of_terminal_output, expected_output_transactions)


'''test case R4.3.2 ticket name is no longer than 60 characters'''


def test_ticket_name_no_longer_than_60(capsys):
    terminal_input = ['login', 'test@test.com,Pass123..', 'sell',
                      'asd123asdfasdfasasdjkfhaknschfiawehncfikasnkascfasdfvarfehnsfgbtghsgvdfgbstfdfgbyfdgbdfgvftfdfbgfdvgbgfvgbfgbfdgbfhngbnhgbgghb,50,10,20201010',
                      'logout', 'exit']
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'login session started successfully',
                                        'please type your email and password:',
                                        'account logged in',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'selling session started successfully',
                                        'please type ticket name, price, quantity, date:',
                                        'transaction was created unsuccessfully',
                                        'please retype',
                                        'the ticket name should be no longer than 60 characters',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'logout successfully',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, expected_tail_of_terminal_output, expected_output_transactions)


'''test case R4.4.2 ticket quantity should be more than 0, and less than or equal to 100. <0 case'''


def test_ticket_quantity_more_than_0(capsys):
    terminal_input = ['login', 'test@test.com,Pass123..', 'sell', 'asd123,50,-10,20201010', 'logout', 'exit']
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'login session started successfully',
                                        'please type your email and password:',
                                        'account logged in',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'selling session started successfully',
                                        'please type ticket name, price, quantity, date:',
                                        'transaction was created unsuccessfully',
                                        'please retype',
                                        'the quantity of the tickets has to be more than 0, and less than or equal to 100',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'logout successfully',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, expected_tail_of_terminal_output, expected_output_transactions)


'''test case R4.4.3 ticket quantity should be more than 0, and less than or equal to 100. >100 case'''


def test_ticket_quantity_less_than_100(capsys):
    terminal_input = ['login', 'test@test.com,Pass123..', 'sell', 'asd123,50,110,20201010', 'logout', 'exit']
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'login session started successfully',
                                        'please type your email and password:',
                                        'account logged in',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'selling session started successfully',
                                        'please type ticket name, price, quantity, date:',
                                        'transaction was created unsuccessfully',
                                        'please retype',
                                        'the quantity of the tickets has to be more than 0, and less than or equal to 100',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'logout successfully',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, expected_tail_of_terminal_output, expected_output_transactions)


'''test case R4.5.2 ticket price should be of range [10, 100]'''


def test_ticket_price_10_100(capsys):
    terminal_input = ['login', 'test@test.com,Pass123..', 'sell', 'asd123,150,10,20201010', 'logout', 'exit']
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'login session started successfully',
                                        'please type your email and password:',
                                        'account logged in',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'selling session started successfully',
                                        'please type ticket name, price, quantity, date:',
                                        'transaction was created unsuccessfully',
                                        'please retype',
                                        'the ticket price should be of range [10, 100]',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'logout successfully',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, expected_tail_of_terminal_output, expected_output_transactions)


'''test case R4.6.2 date must be given in the format YYYYMMDD'''


def test_date_format(capsys):
    terminal_input = ['login', 'test@test.com,Pass123..', 'sell', 'asd123,50,10,2020-10-10', 'logout', 'exit']
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'login session started successfully',
                                        'please type your email and password:',
                                        'account logged in',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'selling session started successfully',
                                        'please type ticket name, price, quantity, date:',
                                        'transaction was created unsuccessfully',
                                        'please retype',
                                        'date must be given in the format YYYYMMDD',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'logout successfully',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, expected_tail_of_terminal_output, expected_output_transactions)


def helper(
        capsys,
        terminal_input,
        expected_tail_of_terminal_output,
        expected_output_transactions
):
    """Helper function for testing

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        terminal_input -- list of string for terminal input
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        expected_output_transactions -- list of expected output transactions
    """

    # cleanup package
    reload(app)

    # set terminal input
    sys.stdin = io.StringIO(
        '\n'.join(terminal_input))

    # run the program
    with pytest.raises(SystemExit):
        app.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # compare terminal outputs at the end.`
    for i in range(1, len(expected_tail_of_terminal_output) + 1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]

    # compare transactions:
    if expected_output_transactions != '':
        with open('Kingston_transactions.csv', 'r') as of:
            content = of.read().splitlines()
            # print out the testing information for debugging
            # the following print content will only display if a
            # test case failed:
            print('output transactions:', content)
            print('output transactions (expected):', expected_output_transactions)

            for i in reversed(content):
                if i == '':
                    continue
                if i != '':
                    assert i == expected_output_transactions
                    break
