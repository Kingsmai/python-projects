import pandas
df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])
print(df1)

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]],columns=["Price", "Age", "Value"],index=["Andrew", "Haiyan"])
print(df1)

print(type(df1))

print(df1.mean())
print(type(df1.mean()))
print(df1.mean().mean())

print(df1.Price)
print(type(df1.Price))
print(df1.Price.mean())
print(df1.Price.max())

df2 = pandas.DataFrame([{"Name": "John"}, {"Name": "Jack"}])
print(df2)

df2 = pandas.DataFrame([{"Name": "John", "Surname": "Philips"}, {"Name": "Jack"}])
print(df2)