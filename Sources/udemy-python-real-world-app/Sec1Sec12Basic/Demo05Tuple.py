# Tuple

# this is Tuple
monday_temperatures = (20.5, 25.3, 18.4)
# this is List
monday_temperatures2 = [20.5, 25.3, 18.4]

# hmm... List is mutable, Tuple is immutable
monday_temperatures2.append(10.7)
print(monday_temperatures2)
monday_temperatures2.remove(25.3)
print(monday_temperatures2)