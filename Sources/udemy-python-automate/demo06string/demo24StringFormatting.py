# String concatnation with +
print('Hello ' + 'World')

# But if we got more variable, it will be annoying
name = 'Alice'
place = 'Main street'
time = '6 pm'
food = 'turnips'
print('Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food + '.')

# String Formatting
print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food))