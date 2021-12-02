from importlib import reload
import pytest
import os
import csv
import qa327.backoffice as back

path = os.path.dirname(os.path.abspath(__file__))


# test case R3.1 skip when there are no 'buying' transactions
def test_case1(capsys):
    input_valid_accounts = ['test@test.com','test_name','Pass123..',1000],['buy@test.com','test_name','Pass123..',1000]
    input_valid_tickets = ['testticket',90,10,'test@test.com'],[]
    input_test_transaction = []
    expected_tail_of_terminal_output = []
    expected_output_accounts = ['test@test.com,test_name,Pass123..,1000','buy@test.com,test_name,Pass123..,1000']
    expected_output_tickets = ['testticket,90,10,test@test.com','']
    helper(capsys, input_valid_accounts, input_valid_tickets, input_test_transaction, expected_tail_of_terminal_output, expected_output_accounts, expected_output_tickets)


# test case R3.2 print message and skip when ticket quantity is not enough
def test_case2(capsys):
    input_valid_accounts = ['test@test.com', 'test_name', 'Pass123..', 1000], ['buy@test.com', 'test_name', 'Pass123..',1000]
    input_valid_tickets = ['testticket', 90, 10, 'test@test.com'], []
    input_test_transaction = ['buying', 'buy@test.com', 'testticket', 90, 11], []
    expected_tail_of_terminal_output = ['Maximum purchase quantity exceeded']
    expected_output_accounts = ['test@test.com,test_name,Pass123..,1000','buy@test.com,test_name,Pass123..,1000']
    expected_output_tickets = ['testticket,90,10,test@test.com','']
    helper(capsys, input_valid_accounts, input_valid_tickets, input_test_transaction, expected_tail_of_terminal_output,expected_output_accounts, expected_output_tickets)


# test case R3.3 modify ticket and account info when there are 'updating' transactions
def test_case3(capsys):
    input_valid_accounts = ['test@test.com', 'test_name', 'Pass123..', 1000], ['buy@test.com', 'test_name', 'Pass123..',1000]
    input_valid_tickets = ['testticket', 90, 10, 'test@test.com'], []
    input_test_transaction = ['buying', 'buy@test.com', 'testticket', 90, 1],[]
    expected_tail_of_terminal_output = []
    expected_output_accounts = ['test@test.com,test_name,Pass123..,1090.0','buy@test.com,test_name,Pass123..,872.42']
    expected_output_tickets = ['testticket,90,9,test@test.com','']
    helper(capsys, input_valid_accounts, input_valid_tickets, input_test_transaction, expected_tail_of_terminal_output,expected_output_accounts, expected_output_tickets)


def helper(
        capsys,
        input_valid_accounts,
        input_valid_tickets,
        input_test_transaction,
        expected_tail_of_terminal_output,
        expected_output_accounts,
        expected_output_tickets
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
    with open('accounts.csv', 'w')as f:
        ff = csv.writer(f)
        ff.writerows(input_valid_accounts)
        f.close()

    # write a temp account.csv with test accounts existed
    with open('tickets.csv', 'w')as f:
        ff = csv.writer(f)
        ff.writerows(input_valid_tickets)
        f.close()

    # write a transaction.csv file with test transactions
    with open('Vancouver_transactions.csv', 'w')as f:
        ff = csv.writer(f)
        ff.writerows(input_test_transaction)
        f.close()

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
    if expected_output_tickets:
        with open('updated_accounts.csv', 'r') as of:
            content = of.read().splitlines()
            # print out the testing information for debugging
            # the following print content will only display if a
            # test case failed:
            print('output:', content)
            print('output (expected):', expected_output_accounts)
            assert content == expected_output_accounts

    if expected_output_tickets:
        with open('updated_tickets.csv', 'r') as of:
            content = of.read().splitlines()
            # print out the testing information for debugging
            # the following print content will only display if a
            # test case failed:
            print('output:', content)
            print('output (expected):', expected_output_tickets)
            assert content == expected_output_tickets

