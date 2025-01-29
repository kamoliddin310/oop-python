class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.age = 2025 - birth_year


users = [
    User("Ali", 1999),
    User("Vali", 2003),
    User("John", 1997),
    User("Doe", 1991),
    User("Alex", 2002),
    User("Bob", 2000),
    User("Felix", 2001),
]
# lambda bilan ishlash yuli 

# a = max(users, key=lambda user: user.age)

# for if bilan ishlash yuli
# a = users[0]
# for user in users:
#     if a.age < user.age:
#         a = user

# print(a.name, a.age)

# mx = max(users, key=lambda user: user.age)

# print(mx.name, mx.age)
