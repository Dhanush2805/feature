import os


message = "This is only sample documentation"
print("talisman")

########################
class FakeCursor:
    def execute(self, query):
        print(query)

cursor = FakeCursor()

user_input = input()

cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")