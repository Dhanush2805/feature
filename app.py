import os
db_url = "postgres://admin:password@localhost:5432/prod"
print("talisman")

########################

formula = input("Enter formula: ")

result = eval(formula)

print(result)
