from importlib import reload
import pytest
import os
import io
import sys
import qa327.app as app

path = os.path.dirname(os.path.abspath(__file__))

'''test case for R1.1: Test if user is logged in'''


def test_loggedIn(capsys):
    if app.status:
        terminal_input = ['logout', 'exit']
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'your balance: 1000',
                                            'type your choice:',
                                            'sell  buy  update  logout',
                                            'logout successfully',
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.2: Test if user is not logged in'''


def test_notlogged(capsys):
    if not app.status:
        terminal_input = ["exit"]
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.3.1: enter buy can go to buy session when user is logged in'''


def test_goBuy_logged(capsys):
    if app.status:
        terminal_input = ["buy", 'logout', 'exit']
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'your balance: 1000',
                                            'type your choice:',
                                            'sell  buy  update  logout',
                                            'buying session started successfully',
                                            'please type ticket name, quantity:',
                                            'please retype',
                                            'the number of inputs should be 2',
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit'
                                            ]

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.3.2: enter sell can go to sell session when user is logged in'''


def test_goSell_logged(capsys):
    if app.status:
        terminal_input = ["sell", 'logout', 'exit']
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'your balance: 1000',
                                            'type your choice:',
                                            'sell  buy  update  logout',
                                            'selling session started successfully',
                                            'please type ticket name, price, quantity, date:',
                                            'please retype',
                                            'the number of inputs should be 4',
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.3.3: enter update can go to update session when user is logged in'''


def test_goUpdate_logged(capsys):
    if app.status:
        terminal_input = ["update", 'logout', 'exit']
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'your balance: 1000',
                                            'type your choice:',
                                            'sell  buy  update  logout',
                                            'updating session started successfully',
                                            'please type ticket name, price, quantity, date:',
                                            'please retype',
                                            'the number of inputs should be 4',
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.3.4: enter logout can go to out session when user is logged in'''


def test_logout_successfully(capsys):
    if app.status:
        terminal_input = ["logout", 'exit']
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'your balance: 1000',
                                            'type your choice:',
                                            'sell  buy  update  logout',
                                            'please retype',
                                            'the number of inputs should be 2'
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.3.5:  enter login can go to login session when user is not logged in'''


def test_login_whenNotLoggedIn(capsys):
    if not app.status:
        terminal_input = ["login", "logout", "exit"]
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'type your choice:',
                                            'register  login  exit',
                                            'login session started successfully',
                                            'please type your email and password:',
                                            'please retype',
                                            'the number of inputs should be 2',
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.3.6: enter register can go to register session when user is not logged in'''


def test_register_successfully(capsys):
    if not app.status:
        terminal_input = ["register", 'logout', 'exit', 'exit']
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'type your choice:',
                                            'register  login  exit',
                                            'register session started successfully',
                                            'please enter your email, user name, password and '
                                            'confirm your password:',
                                            'please retype',
                                            'the number of inputs should be 4 or exit',
                                            'do you want to exit register session(type exit to leave):type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.3.7: enter exit can exit the program when user is not logged in'''


def test_exit_successfully(capsys):
    if not app.status:
        terminal_input = ["exit"]
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.4.1: when user is not logged in, buy command are not accepted'''


def test_goBuy_notLogged(capsys):
    if not app.status:
        terminal_input = ["buy", 'exit']
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'type your choice:',
                                            'register  login  exit',
                                            'invalid command',
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.4.2: when user is not logged in, sell command are not accepted'''


def test_goSell_notLogged(capsys):
    if not app.status:
        terminal_input = ["sell", 'exit']
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'type your choice:',
                                            'register  login  exit',
                                            'invalid command',
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.4.3: when user is not logged in, update command are not accepted'''


def test_goUpdate_notLogged(capsys):
    if not app.status:
        terminal_input = ["update", 'exit']
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'type your choice:',
                                            'register  login  exit',
                                            'invalid command',
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.4.4: when user is not logged in, logout command are not accepted'''


def test_logout_fail(capsys):
    if not app.status:
        terminal_input = ["logout", 'exit']
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'type your choice:',
                                            'register  login  exit',
                                            'invalid command',
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.5.1: when user is logged in, login command are not accepted'''


def test_login_fail(capsys):
    if app.status:
        terminal_input = ["login", "logout", "exit"]
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'your balance: 1000',
                                            'type your choice:',
                                            'sell  buy  update  logout',
                                            'invalid command'
                                            'your balance: 1000',
                                            'type your choice:',
                                            'sell  buy  update  logout',
                                            "logout successfully",
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.5.2: when user is logged in, register command are not accepted'''


def test_register_fail(capsys):
    if app.status:
        terminal_input = ["register", "logout", "exit"]
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'your balance: 1000',
                                            'type your choice:',
                                            'sell  buy  update  logout',
                                            'invalid command'
                                            'your balance: 1000',
                                            'type your choice:',
                                            'sell  buy  update  logout',
                                            "logout successfully",
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


'''test case for R1.5.3: when user is logged in, exit command are not accepted'''


def test_exit_fail(capsys):
    if app.status:
        terminal_input = ["exit", "logout", "exit"]

        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'your balance: 1000',
                                            'type your choice:',
                                            'sell  buy  update  logout',
                                            'invalid command'
                                            'your balance: 1000',
                                            'type your choice:',
                                            'sell  buy  update  logout',
                                            "logout successfully",
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output, )


def helper(
        capsys,
        terminal_input,
        expected_tail_of_terminal_output):
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
