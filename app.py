import os


message = "This is only sample documentation"
print("talisman")

########################
user_input = input()

queries = "SELECT * FROM users WHERE id=" + user_input
cursor.execute(queries)