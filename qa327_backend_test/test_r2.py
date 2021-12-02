from importlib import reload
import pytest
import csv
import qa327.backoffice as backend


# test case R2.1 for successfully passing a valid selling transaction
def test_selling_success(capsys):
    input_valid_tickets = []
    input_test_transaction = [["selling", "sell12@test.com", "sell12ticket", "90", "9"]]
    expected_tail_of_terminal_output = []
    expected_output_transaction = "sell12ticket,90,9,sell12@test.com"

    helper(capsys, input_valid_tickets, input_test_transaction, expected_tail_of_terminal_output,
           expected_output_transaction)


# test case R2.2 skip passing sell process when there are no "selling" transaction
def test_selling_fail(capsys):
    input_valid_accounts = ['testticket', 90, 10, 'test@test.com']
    input_test_transaction = [["1selling1", "use2@test.com", "sellticket", "90", "2"]]
    expected_tail_of_terminal_output = []
    expected_output_transaction = "testticket,90,10,test@test.com"
    helper(capsys, input_valid_accounts, input_test_transaction, expected_tail_of_terminal_output,
           expected_output_transaction)


def helper(
        capsys, input_valid_tickets,
        input_test_transaction, expected_tail_of_terminal_output,
        expected_output_transaction):
    """Helper function for testing

    Arguments:
        capsys -- object created by pytest to capture stdout and stderr
        input_test_transaction -- list of string for input transaction
        expected_tail_of_terminal_output list of expected string at the tail of terminal
        expected_output_transactions -- list of expected output transactions
    """

    # write a temp account.csv with test accounts existed
    with open('tickets.csv', 'w')as f:
        ff = csv.writer(f)
        ff.writerow(input_valid_tickets)
        f.close()

    # write a transaction.csv file with test transactions
    with open('Vancouver_transactions.csv', 'w+')as f:
        ff = csv.writer(f)
        for row in input_test_transaction:
            ff.writerow(row)
        f.close()

    # cleanup package
    reload(backend)

    # run the program
    backend.main()

    # capture terminal output / errors
    # assuming that in this case we don't use stderr
    out, err = capsys.readouterr()

    # split terminal output in lines
    out_lines = out.splitlines()

    # compare terminal outputs at the end.`
    for i in range(1, len(expected_tail_of_terminal_output) + 1):
        index = i * -1
        assert expected_tail_of_terminal_output[index] == out_lines[index]

    if expected_output_transaction != '':
        with open('updated_tickets.csv', 'r') as of:
            content = of.read().splitlines()
            # print out the testing information for debugging
            # the following print content will only display if a
            # test case failed:

            for i in content:
                if i == '':
                    continue
                if i != '':
                    print('output transactions:', content)
                    print('output transactions (expected):', expected_output_transaction)
                    assert i == expected_output_transaction
                    break
