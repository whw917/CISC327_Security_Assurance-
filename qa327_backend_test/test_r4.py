from importlib import reload
import pytest
import os
import csv
import qa327.backoffice as back

path = os.path.dirname(os.path.abspath(__file__))


# test case R4.1 modify ticket info when there are 'updating' transactions
def test_case1(capsys):
    input_valid_tickets = ['testticket',90,10,'test@test.com']
    input_test_transaction = ['updating','test@test.com','testticket',80,20]
    expected_tail_of_terminal_output = []
    expected_output_tickets = 'testticket,80,20,test@test.com'
    helper(capsys, input_valid_tickets, input_test_transaction, expected_tail_of_terminal_output, expected_output_tickets)


# test case R4.2 skip when there are no 'updating' transactions
def test_case2(capsys):
    input_valid_tickets = ['testticket',90,10,'test@test.com']
    input_test_transaction = []
    expected_tail_of_terminal_output = []
    expected_output_tickets = 'testticket,90,10,test@test.com'
    helper(capsys, input_valid_tickets, input_test_transaction, expected_tail_of_terminal_output, expected_output_tickets)


def helper(
        capsys,
        input_valid_tickets,
        input_test_transaction,
        expected_tail_of_terminal_output,
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

    # write a temp ticket.csv with test accounts existed
    with open('tickets.csv', 'w')as f:
        ff = csv.writer(f)
        ff.writerow(input_valid_tickets)
        f.close()

    # write a transaction.csv file with test transactions
    with open('Vancouver_transactions.csv', 'w')as f:
        ff = csv.writer(f)
        ff.writerow(input_test_transaction)
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
    if expected_output_tickets != '':
        with open('updated_tickets.csv', 'r') as of:
            content = of.read().splitlines()
            # print out the testing information for debugging
            # the following print content will only display if a
            # test case failed:
            print('output:', content)
            print('output (expected):', expected_output_tickets)

            for i in content:
                if i == '':
                    continue
                if i != '':
                    assert i == expected_output_tickets
                    break
