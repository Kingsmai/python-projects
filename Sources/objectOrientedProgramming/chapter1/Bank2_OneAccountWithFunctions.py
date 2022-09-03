# Non-OOP
# Bank 2
# Single account

accountName = ''
accountBalance = 0
accountPassword = ''

def newAccount(name, balance, password):
    global accountName, accountBalance, accountPassword
    accountName = name
    accountBalance = balance
    accountPassword = password

def show():
    global accountName, accountBalance, accountPassword
    print('    Name:', accountName)
    print('    Balance:', accountBalance)
    print('    Password:', accountPassword)
    print()

def getBalance(password):
    global accountName, accountBalance, accountPassword
    if password != accountPassword:
        print('Incorrect password')
        return None
    return accountBalance

def deposit(amountToDeposit, password):
    global accountName, accountBalance, accountPassword
    if amountToDeposit < 0:
        print('You cannot deposit a negative amount!')
        return None
    if password != accountPassword:
        print('Incorrect password')
        return None
    accountBalance += amountToDeposit
    return accountBalance

def withdraw(amountToWithdraw, password):
    global accountName, accountBalance, accountPassword
    if amountToWithdraw < 0:
        print('You cannot withdraw a negative amount')
        return None
    if password != accountPassword:
        print('Incorrect password for this account')
        return None
    if amountToWithdraw > accountBalance:
        print('You cannot withdraw more than you have in your account')
        return None
    accountBalance -= amountToWithdraw
    return accountBalance

newAccount("Joe", 100, 'soup')

while True:
    print('''
Please select your action:
(B)alance
(D)eposit
(W)ithdrawal
(S)how the account
(Q)uit
''')
    action = input('> ').casefold()
    if action == 'b':
        print('Get Balance:')
        print('Please enter the password:')
        userPassword = input('> ')
        theBalance = getBalance(userPassword)
        if theBalance is not None:
            print('Your balance is:', theBalance)

    elif action == 'd':
        print('Deposit:')
        print('Please enter amount to deposit:')
        userDepositAmount = int(input('> '))
        print('Please enter the password:')
        userPassword = input('> ')
        newBalance = deposit(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

    elif action == 's':
        print('Show:')
        show()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')
        print('Please enter the amount to withdraw:')
        userWithdrawAmount = input('> ')
        print('Please enter the password:')
        userPassword = input('> ')
        newBalance = withdraw(userDepositAmount, userPassword)
        if newBalance is not None:
            print('Your new balance is:', newBalance)

print('Done')