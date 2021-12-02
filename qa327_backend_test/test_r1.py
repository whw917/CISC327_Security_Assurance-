from importlib import reload
import pytest
import os
import csv
import qa327.backoffice as back

path = os.path.dirname(os.path.abspath(__file__))


# test case R1.1 this will test a basic case, with registration in transaction file and no repeated account
def test_first_case(capsys):
    input_valid_accounts = []
    input_test_transaction = [['registration', 'testname1', 'test@test1.com', 'Test_password1', 3001],
                              ['registration', 'testname2', 'test@test2.com', 'Test_password2', 3002]]
    expected_tail_of_terminal_output = []
    expected_output_accounts = ['test@test1.com,testname1,Test_password1,3001',
                                'test@test2.com,testname2,Test_password2,3002']
    helper(capsys, input_valid_accounts, input_test_transaction, expected_tail_of_terminal_output,
           expected_output_accounts)


# test case R1.2 this will test teh case with registration and other transactions in the transaction file,
# and no repeated email the output should only generate the registration account into account.csv
def test_second_case(capsys):
    input_valid_accounts = []
    input_test_transaction = [['registration', 'testname1', 'test@test1.com', 'Test_password1', 3001],
                              ['registration', 'testname2', 'test@test2.com', 'Test_password2', 3002],
                              ['someTransaction', 'testname3', 'test@test3.com', 'Test_password3', 3003],
                              ['someTransaction', 'testname4', 'test@test4.com', 'Test_password4', 3004]]
    expected_tail_of_terminal_output = []
    expected_output_accounts = ['test@test1.com,testname1,Test_password1,3001',
                                'test@test2.com,testname2,Test_password2,3002']
    helper(capsys, input_valid_accounts, input_test_transaction, expected_tail_of_terminal_output,
           expected_output_accounts)


# test case R2.3 this will test the case with registration in transaction file with some repeated email exited in
# account.csv there should be no repeated email should be in the updated_accounts.csv
def test_third_case(capsys):
    input_valid_accounts = [['test@test1.com', 'testname1', 'Test_password1', 3001]]
    input_test_transaction = [['registration', 'testname1', 'test@test1.com', 'Test_password1', 3001],
                              ['registration', 'testname2', 'test@test2.com', 'Test_password2', 3002]]
    expected_tail_of_terminal_output = []
    expected_output_accounts = ['test@test1.com,testname1,Test_password1,3001',
                                'test@test2.com,testname2,Test_password2,3002']
    helper(capsys, input_valid_accounts, input_test_transaction, expected_tail_of_terminal_output,
           expected_output_accounts)


# test case R2.4 this will test the case with registration in transaction file with some repeated email
# exited in both account.csv and transaction.csv, there should no repeated email in update_accounts
# the terminal output should call repeated email and no repeated email should be in the updated_accounts.csv
def test_forth_case(capsys):
    input_valid_accounts = [['test@test1.com', 'testname1', 'Test_password1', 3001]]
    input_test_transaction = [['registration', 'testname1', 'test@test1.com', 'Test_password1', 3001],
                              ['registration', 'testname1', 'test@test1.com', 'Test_password1', 3001],
                              ['registration', 'testname2', 'test@test2.com', 'Test_password2', 3002],
                              ['registration', 'testname2', 'test@test2.com', 'Test_password2', 3002]]
    expected_tail_of_terminal_output = []
    expected_output_accounts = ['test@test1.com,testname1,Test_password1,3001',
                                'test@test2.com,testname2,Test_password2,3002']
    helper(capsys, input_valid_accounts, input_test_transaction, expected_tail_of_terminal_output,
           expected_output_accounts)


def helper(
        capsys,
        input_test_accounts,
        input_test_transaction,
        expected_tail_of_terminal_output,
        expected_output_accounts
):
    """Helper function for testing

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        terminal_input -- list of string for terminal input
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        intput_valid_accounts -- list of valid accounts in the valid_account_list_file
        expected_output_transactions -- list of expected output transactions
    """
    # write a temp account.csv with test accounts existed
    with open('accounts.csv', 'w+')as f:
        ff = csv.writer(f)
        if input_test_accounts != []:
            for row in input_test_accounts:
                ff.writerow(row)

    # write a transaction.csv file with test transactions
    with open('Vancouver_transactions.csv', 'w+')as f:
        ff = csv.writer(f)
        for row in input_test_transaction:
            ff.writerow(row)

    # cleanup package
    reload(back)

    # run the program
    back.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # print out the testing information for debugging
    # the following print content will only display if a
    # test case failed:
    print('terminal output:', out_lines)

    # compare terminal outputs at the end.`
    for i in range(1, len(expected_tail_of_terminal_output) + 1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]

    # compare transactions:
    if expected_output_accounts != '':
        with open('updated_accounts.csv', 'r') as of:
            content = of.read().splitlines()
            # print out the testing information for debugging
            # the following print content will only display if a
            # test case failed:
            print('output transactions:', content)
            print('output transactions (expected):', expected_output_accounts)

            assert content == expected_output_accounts
