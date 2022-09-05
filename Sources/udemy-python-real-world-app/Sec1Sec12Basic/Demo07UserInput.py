def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

# User input
user_input = float(input("Enter temperature: "))
print(weather_condition(user_input))

# String Formatting
user_input = input("Please enter your name: ")
message = "Hello %s!" % user_input
print(message)
# Another method (For Python 3.6+):
message = f"Hello {user_input}!"
print(message)
# using format method
message = "Hello {}".format(user_input)
print(message)

# String Formatting with Multiples Variables
name = input("Enter your name: ")
surname = input("Enter your surname: ")
when = "today"

message = "Hello %s %s. What's up %s!" % (name, surname, when)
print(message)
message = f"Hello {name} {surname}. What's up {when}!"
print(message)
message = "Hello {} {}. What's up {}!".format(name, surname, when)
print(message)
