# Write a program for a rollercoaster price for different conditions

# Only those person who are above 120 cm and above are allowed
# For age of 18 year or more price is $12
# For age group of 12 to 18 price is $7
# For age group of below 12 price is $5
# If anyone wants photo then add $3 to their final bill



print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        bill = 5
    elif age <= 18:
        print("Please pay $7.")
        bill = 7
    else:
        print("Please pay $12.")
        bill = 12
    wants_photo=input("If you wants photo press y for yes and press n for no: ")
    if wants_photo == "y":
        bill +=3
    print(f"your final bill = {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")