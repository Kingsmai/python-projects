print('Enter your password:')
typedPassword = input()
if typedPassword == 'swordfish':
    print('Access granted.')
elif typedPassword == 'mary':
    print('Hint: The password is a fish.')
elif typedPassword == '12345':
    print('That is a really obvious password.')
else:
    print('Access denied.')
print('Done.')