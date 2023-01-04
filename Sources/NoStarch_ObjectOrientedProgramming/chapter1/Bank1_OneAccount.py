# Non OOP
# Bank Version 1
# Single account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

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
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print('Your balance is:', accountBalance)

    elif action == 'd':
        print('Deposit:')
        print('Please enter amount to deposit:')
        userDepositAmount = int(input('> '))
        print('Please enter the password:')
        userPassword = input('> ')
        
        if userDepositAmount < 0:
            print('You cannot deposit a negative amount!')
        elif userPassword != accountPassword:
            print('Incorrect password')
        else: # OK
            accountBalance += userDepositAmount
            print('Your new balance is:', accountBalance)

    elif action == 's':
        print('Show:')
        print('    Name:', accountName)
        print('    Balance:', accountBalance)
        print('    Password:', accountPassword)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw:')
        print('Please enter the amount to withdraw:')
        userWithdrawAmount = input('> ')
        print('Please enter the password:')
        userPassword = input('> ')
        
        if userWithdrawAmount < 0:
            print('You cannot withdraw a negative amount')
        elif userPassword != accountPassword:
            print('Incorrect password for this account')
        elif userWithdrawAmount > accountBalance:
            print('You cannot withdraw more than you have in your account')
        else:
            accountBalance -= userWithdrawAmount
            print('Your new balance is:', accountBalance)

print('Done')