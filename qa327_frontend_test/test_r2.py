from importlib import reload
import pytest
import os
import io
import sys
import qa327.app as app

path = os.path.dirname(os.path.abspath(__file__))

'''this test aims to test with all requirments satisfied '''


def test_successful_case(capsys):
    terminal_input = ['register', 'test@test1.com,testname,Test_password,Test_password', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'account registered',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = 'registration,testname,test@test1.com,Test_password,3000'

    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test start register session, and then exit the program'''


def test_exit_all(capsys):
    terminal_input = ['register', 'anyword', 'exit', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'please retype',
                                        'the number of inputs should be 4 or exit',
                                        'do you want to exit register session(type exit to leave):'
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case for R2.4.2 negative, input empty email, should return to landing session'''


def test_empty_email(capsys):
    terminal_input = ['register', ',testname,Test_password,Test_password', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'email format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case for R2.4.4 negative, input empty password, should return to landing session'''


def test_empty_password(capsys):
    terminal_input = ['register', 'test@test1.com,testname,,', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'password format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case for R2.5.2, Email doesn't satisfy the requirments (Negative Case)'''


def test_wrong_email(capsys):
    terminal_input = ['register', 'testemail,testname,Test_password,Test_password', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'email format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case for R2.6.2 Password without minimum length 6 (negative case)'''


def test_wrong_length_password(capsys):
    terminal_input = ['register', 'test@test1.com,testname,Test_,Test_', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'password format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case for R2.6.3 Password without Uppercase (negative case)'''


def test_no_Uppercase_password(capsys):
    terminal_input = ['register', 'test@test1.com,testname,test_password,test_password', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'password format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case for R2.6.4 Password without lowercase (negative case)'''


def test_no_Lowercase_password(capsys):
    terminal_input = ['register', 'test@test1.com,testname,TEST_PASSWORD, TEST_PASSWORD', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'password format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case for R2.6.5 Password without special character (negative case)'''


def test_no_specialChar_password(capsys):
    terminal_input = ['register', 'test@test1.com,testname,Testpassword,Testpassword', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'password format is incorrect',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case for R2.7.2 two password ar enot matched'''


def test_unequal_password(capsys):
    terminal_input = ['register', 'test@test1.com,testname,Test_password,Test_passwo', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        "two password doesn't match, please confirm your password",
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case R2.8.2 empty user name'''


def test_empty_usrename(capsys):
    terminal_input = ['register', 'test@test1.com,,Test_password,Test_password', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'user name format is incorrect (User name should be alphanumeric-only)',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case R2.8.3 name with special character (negative)'''


def test_specialChar_usrename(capsys):
    terminal_input = ['register', 'test@test1.com,test_name,Test_password,Test_password', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'user name format is incorrect (User name should be alphanumeric-only)',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case R2.8.5 name with space at first character (negative)'''


def test_space_atFist_usrename(capsys):
    terminal_input = ['register', 'test@test1.com, testname,Test_password,Test_password', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'user name format is incorrect (Space allowed only if it is not the first or the last character)',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case R2.8.5 name with space at last character (negative)'''


def test_space_atLast_usrename(capsys):
    terminal_input = ['register', 'test@test1.com,testname ,Test_password,Test_password', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'user name format is incorrect (Space allowed only if it is not the first or '
                                        'the last character)',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''adding test case name with space in the middle  (positive)'''


def test_space_atMiddle_usrename(capsys):
    terminal_input = ['register', 'test@test1.com,test name,Test_password,Test_password', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'account registered',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = 'registration,test name,test@test1.com,Test_password,3000'

    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case R2.9.2 name less than 3 character (negative)'''


def test_less_length_usrename(capsys):
    terminal_input = ['register', 'test@test1.com,te,Test_password,Test_password', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'user name format is incorrect (User name should be longer than 2 and shorter that 20 characters)',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case R2.9.3 name more than 19 character (negative)'''


def test_less_length_usrename(capsys):
    terminal_input = ['register', 'test@test1.com,testvvvvverylongname,Test_password,Test_password', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'user name format is incorrect (User name should be longer than 2 and shorter that 20 characters)',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


'''test case R2.10.2 email exits in known account in accounts.csv(negative)'''


def test_exit_email_usercsv(capsys):
    terminal_input = ['register', 'test@test.com,test_name,Test_password,Test_password', 'exit']
    intput_valid_accounts = []
    expected_tail_of_terminal_output = ['Welcome the Queens ticket trade machine',
                                        'type your choice:',
                                        'register  login  exit',
                                        'register session started successfully',
                                        'please enter your email, user name, password and confirm your password:',
                                        'account exits',
                                        '',
                                        'type your choice:',
                                        'register  login  exit',
                                        'exit']
    expected_output_transactions = ''
    helper(capsys, terminal_input, intput_valid_accounts, expected_tail_of_terminal_output,
           expected_output_transactions)


def helper(
        capsys,
        terminal_input,
        intput_valid_accounts,
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
