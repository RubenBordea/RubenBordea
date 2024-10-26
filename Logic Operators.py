#           not = inverts the condition (not False, not True

temp = -28
is_sunny = True

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is SUNNY")
elif temp <= 0 and is_sunny:
    print("It is COLD outside")
    print("It is SUNNY")
elif temp < 28 and temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is SUNNY")

