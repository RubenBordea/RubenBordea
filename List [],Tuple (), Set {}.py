# List [] = mutable, most flexible
# Tuple () = immutable, faster
# Set {} = mutable (add/remove), unordered,
#            NO duplicates, best for membership testing

fruits = {"apple", "orange", "banana", "coconut"}

if "apple" in fruits:
    print("Apple was found")
else:
    print("Apple was not found")

for fruit in fruits:
    print(fruit, end=" ")

if fruit in fruits:
    print(f"{fruit} was found")
else:
    print(f"{fruit} was not dounf")