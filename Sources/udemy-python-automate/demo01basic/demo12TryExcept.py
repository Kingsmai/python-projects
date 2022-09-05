def div42by(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
    # except: # left blank to caught all error
        print("Error: you tried to devide by zero.")

print(div42by(2))
print(div42by(12))
print(div42by(0)) # ZeroDivisionError
print(div42by(1))