from importlib import reload
import pytest
import os
import io
import sys
import qa327.app as app

'''test case for R8.1: when user is logged in, exit command are not accepted'''


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


'''test case for R8.2.: enter exit can exit the program when user is not logged in'''


def test_exit_successfully(capsys):
    if not app.status:
        terminal_input = ["exit"]
        expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                            'type your choice:',
                                            'register  login  exit',
                                            'exit']

        helper(capsys, terminal_input, expected_tail_of_terminal_output)


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
