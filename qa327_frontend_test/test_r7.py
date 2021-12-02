from importlib import reload
import pytest
import os
import io
import sys
import qa327.app as app

path = os.path.dirname(os.path.abspath(__file__))

'''user cannot logout without login first'''
'''test case for R7.1.1	, logout successfully, should return to landing session'''


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
