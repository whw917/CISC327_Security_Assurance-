import csv


accFile = open('accounts.csv', 'r+')
ticketFile = open('tickets.csv', 'r+')
new_accFile = open('updated_accounts.csv', 'w+', newline='')
new_ticketFile = open('updated_tickets.csv', 'w+', newline='')
accReader = list(csv.reader(accFile))
ticketReader = list(csv.reader(ticketFile))
accWriter = csv.writer(new_accFile)
ticketWriter = csv.writer(new_ticketFile)

location_arg = open('backend_locations.txt', 'r').readline().split(',')     # read every transactions by input location args
location_arg.sort()                                                         # sort in an alphabetical order
tranReader = list(csv.reader(open(location_arg[0]+'_transactions.csv')))
for x in location_arg:
    if x == location_arg[0]:
        continue
    for y in list(csv.reader(open(x+'_transactions.csv', 'r'))):            # append all transactions into one list
        tranReader.append(y)


def main():
    register_process()
    sell_process()
    buy_process()
    update_process()
    accWriter.writerows(accReader)
    ticketWriter.writerows(ticketReader)
    accFile.close()
    ticketFile.close()
    new_accFile.close()
    new_ticketFile.close()


def register_process():
    # write registration in transaction file into updated account
    # skip any repeated email registration in transaction file
    for line in tranReader:
        if not line:
            continue
        # print(i[0])
        if line[0] == 'registration':
            n = 0
            for i in accReader:
                if not i:
                    continue
                if line[2] == i[0]:
                    n += 1
            if n != 0:
                print('repeated email account')
                continue
            # write the file in the order of email, name, password, balance
            accReader.append([line[2], line[1], line[3], line[4]])


def sell_process():
    for i in tranReader: # read transaction.csv
        if not i:
            continue
        if i[0] == "selling": # process selling transaction
            #get info
            user_email = i[1]
            ticket_name = i[2]
            price = i[3]
            quantity = i[4]
            # append the selling info to ticketReader list
            ticketReader.append([ticket_name, price, quantity, user_email])


def buy_process():
    for i in tranReader:
        if not i:
            continue
        if i[0] == 'buying':
            user_email = i[1]
            ticket_name = i[2]
            price = eval(i[3])
            buyquantity = eval(i[4])
            owneremail = ''
            for j in ticketReader: # look for the ticket of this owner
                if not j:
                    continue
                if ticket_name == j[0]:
                    quantity = int(j[2])
                    if buyquantity > quantity:
                        print('Maximum purchase quantity exceeded')
                        continue
                    elif buyquantity <= quantity:
                        totalquantity = quantity - buyquantity
                        j[2] = totalquantity
                        owneremail = j[3]
                for k in accReader:
                    if not k:
                        continue
                    if user_email == k[0]:
                        balance = float(k[3])
                        total_price = price * buyquantity * 1.35 * 1.05
                        balance = balance - total_price
                        k[3] = round(balance,2)
                for k in accReader:
                    if not k:
                        continue
                    if owneremail == k[0]:
                        balance = float(k[3])
                        total_earning = price * buyquantity
                        balance = balance + total_earning
                        k[3] = round(balance,2)


def update_process():
    for i in tranReader:                    # read over transactions
        if not i:
            continue
        if i[0] == 'updating':              # process updating only
            user_email = i[1]               # read transaction info
            ticket_name = i[2]
            price = i[3]
            quantity = i[4]
            for j in ticketReader:          # look for the ticket of this owner
                if not j:
                    continue
                if ticket_name == j[0] and user_email == j[3]:
                    j[1] = price            # modify the info
                    j[2] = quantity


if __name__ == "__main__":
    main()



