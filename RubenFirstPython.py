age = int(input("Enter your age: "))
has_ticket = True
price = 10

if age >= 65:
    print("You are a senior citizen")
    print(f"The ticket price for a senior citizen is £{price * 0.75}")
elif age >= 18:
    print("You are an adult")
    print(f"The ticket price for an adult is £{price}")

else:
    print("You are a child")
    print(f"The ticket price for a child is £{price * 0.5}")
if has_ticket:
    print("You may enter my dear, you got a ticket")
else:
    print("You need to buy a ticket my dear")