# mock ATM project
# python backend task

import datetime
import random

options = ["1. Withdraw",
           "2. Deposit",
           "3. Send Money",
           "4. Check Balance",
           "5. Complaint",
           "6. Pay bills",
           "7. Log out",
           "8. Exit"]  # this list out the available actions on the atm (Bank Operations)
options1 = ["1. NEPA(PHED) Bill",
            "2. Airtime recharge",
            "3. Fund Betting accounts",
            "4. Quickteller",
            "5. Back"]
NetworkOptions = ["1. Airtel",
                  "2. Glo",
                  "3. MTN",
                  "4. 9mobile"]
BettingOptions = ["1. Nairabet",
                  "2. BetKing",
                  "3. Bet9ja"]
account_balance = 10000000  # this is the initial balance

database = {}


def welcome_note():
    IsValidOptionSelected = False
    print('You are welcome to the bank of ZURI')
    print('creating happiness for all')

    while IsValidOptionSelected == False:
        CustomerAccount = int(input('Do you have an account with us?: 1 (Yes), 2 (No) \n'))

        if (CustomerAccount == 1):
            IsValidOptionSelected = True
            log_in()
        elif (CustomerAccount == 2):
            IsValidOptionSelected = True
            print(register())
        else:
            print('You have entered an invalid option')
            welcome_note()

def register():
    print('********--REGISTER--*********')
    email = input('Input your email?\n')
    first_name = input('What is your first name?\n')
    last_name = input('What is your last name?\n')
    password = input('create your password?\n')

    account_number = generateAccountnumber()

    database[account_number] = [email, first_name, last_name, password]

    print('your account has been validated and created')
    print('your account number is ', account_number, "\n keep safe for security purposes")

    log_in()


def log_in():
    print('***************---LOGIN---**************')
    AccountNumberFromUser = int(input('what is your account number?\n'))
    password = input('what is your password')

    for accountNumber, userdetails in database.items():
        if accountNumber == AccountNumberFromUser:
            if userdetails[3] == password:
                BankOperations(userdetails)
            else:
                print("invalid account or password")
                log_in()



def BankOperations(user):
    print('===============================')
    print('INTERNATIONAL BANK OF ZURI')
    print('===============================')
    print('welcome ', user[0], user[1])

    print(datetime.datetime.now())  # this prints the current date and time

    for items in options:
        print(items)
    SelectedOption = int(input('what would you like to do?'))

    if SelectedOption == 1:
        WithdrawalOperation()
    elif SelectedOption == 2:
        DepositOperation()
    elif SelectedOption == 3:
        SendMoneyOperation()
    elif SelectedOption == 4:
        print('Your current account balance is: ', account_balance)
    elif SelectedOption == 5:
        ComplaintOperation()
    elif SelectedOption == 6:
        PayBillsOperation()
    elif SelectedOption == 7:
        log_in()
    elif SelectedOption == 8:
        exit()
    else:
        print('you have entered an invalid value')
        BankOperations(user)


def generateAccountnumber():
    print('Generating account number')
    return random.randrange(2222222222, 8888888888)


def WithdrawalOperation():
    withdrawal_amount = int(input('How much would you like to withdraw: \n'))
    print('take your cash', withdrawal_amount)
    print('current balance: ', account_balance - withdrawal_amount)  # prints out the current balance after withdrawa

def DepositOperation():
    deposit = int(input('How much will you like to deposit: \n'))
    print('current balance: ', account_balance + deposit)  # prints out the current balance after deposit


def ComplaintOperation():
    complaint = str(input('what issue would you like to report?\n'))
    print('thank you for contacting us')
    return complaint


def SendMoneyOperation():
    print('this service is unavailable at the moment please try again later')


def PayBillsOperation():
    for items in options1:
        print(items)
    billsselection = int(input('please input a selection from above\n'))
    if billsselection == 1:
        print('please wait while we fetch your PHED Bill Details for this month')
        print("*********************LOADING************************")
        print(datetime.datetime.month)
        print('your Bill is ', 20000)
        billselection2 = int(input('1. pay bill, 2. cancel\n'))
        if billselection2 == 1:
            account_balance - 20000
            print('you have successfully paid your bill')
        elif billselection2 == 2:
            PayBillsOperation()
        else:
            print('invalid input')
    elif billsselection == 2:
        print('please select network')
        for items in NetworkOptions:
            print(items)
        networkselection = int(input('Select network\n'))
        while networkselection >= 1 and networkselection <= 4:
            phonenumber = int(input('Your phone number \n'))
            amount = int(input('how much do you want to recharge\n'))
            print(phonenumber, "has been recharged of the amount: ", amount)
            networkselection = 50
    elif billsselection == 3:
        print('select from list below')
        for items in BettingOptions:
            print(items)
        BettingOptionsSelection = int(input('your selection\n'))
        print(BettingOptionsSelection)
        fundamount = int(input('how much do you wish to fund account\n'))
        print('your betting account has been funded by ', fundamount)
    elif billsselection == 4:
        print('quickteller is unavailable at the moment\n please try again later')
    elif billsselection == 5:
        welcome_note()
    else:
        print('invalid option selected')


welcome_note()  # this calls in the welcome function defined above
