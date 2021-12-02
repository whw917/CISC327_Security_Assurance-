from importlib import reload
import pytest
import os
import io
import sys
import qa327.app as app

path = os.path.dirname(os.path.abspath(__file__))

'''test case for R3.5.1, this test aims to test with all requirments satisfied'''


def test_successful_case(capsys):
    terminal_input = ['login', 'test@test.com,Pass123..', 'logout', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'login session started successfully',
                                        'please type your email and password:',
                                        'account logged in',
                                        'your balance: 1000',
                                        'type your choice:',
                                        'sell  buy  update  logout',
                                        'logout successfully',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, expected_tail_of_terminal_output, expected_output_transactions)


'''test case for R3.2.2, input empty email and empty password, should return to landing session'''


def test_empty_both_email_and_password(capsys):
    terminal_input = ['login', ',', 'logout', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please type your email and password:',
                                        'email format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']

    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output)


'''test case for R3.2.3, input empty email, should return to landing session'''


def test_empty_email(capsys):
    terminal_input = ['login', ',Pass123..', 'logout', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please type your email and password:',
                                        'email format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']

    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output)


'''test case for R3.2.4, input empty password, should return to landing session'''


def test_empty_password(capsys):
    terminal_input = ['login', 'test@test.com,', 'logout', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please type your email and password:',
                                        'password format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']

    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output)


'''test case for R3.3.2, input Email does not satisfy the requirements, should return to landing session'''


def test_wrong_email_format(capsys):
    terminal_input = ['login', 'testemail,Pass123..', 'logout', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please type your email and password:',
                                        'email format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']

    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output)


'''test case for R3.5.2, input Email does not satisfy the requirements, should return to landing session'''


def test_wrong_email_address(capsys):
    terminal_input = ['login', 'test@wrong.com,Pass123..', 'logout', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please type your email and password:',
                                        'login failed',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']

    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output)


'''test case for R3.4.1, input Password too long, should return to landing session'''


def test_wrong_length_password(capsys):
    terminal_input = ['login', 'test@test.com,Passverrrrrrrrrylonnnnnnnnnnng123..', 'logout', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please type your email and password:',
                                        'password format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']

    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output)


'''test case for R3.4.2, input Password too short, should return to landing session'''


def test_wrong_short_password(capsys):
    terminal_input = ['login', 'test@test.com,pa', 'logout', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please type your email and password:',
                                        'password format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']

    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output)


'''test case for R3.4.3, input Password without Uppercase, should return to landing session'''


def test_no_Uppercase_password(capsys):
    terminal_input = ['login', 'test@test.com,pass123..', 'logout', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please type your email and password:',
                                        'password format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']

    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output)


'''test case for R3.4.4, input Password without Lowercase, should return to landing session'''


def test_no_Lowercase_password(capsys):
    terminal_input = ['login', 'test@test.com,PASS123..', 'logout', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please type your email and password:',
                                        'password format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']

    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output)


'''test case for R3.4.4, input Password without special characters, should return to landing session'''


def test_no_spcialChar_password(capsys):
    terminal_input = ['login', 'test@test.com,Pass123', 'logout', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please type your email and password:',
                                        'password format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']

    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output)


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
        intput_valid_accounts -- list of valid accounts in the valid_account_list_file
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
