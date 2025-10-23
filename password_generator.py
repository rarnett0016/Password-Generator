# Get input from the user
favorite_color = input('Enter you favorite color')
pet_name = input('Enter your pets name')
number = input('Enter your favorite number')

# Output all three values on one line separated by a space
print('You entered', favorite_color, pet_name, number)

# Step 2: Output the entered values and create the passwords
print("You entered:", favorite_color, pet_name, number)

# Generate and print passwords
first_password = favorite_color + "_" + pet_name
second_password = number + favorite_color + number

print("First password:", first_password)
print("Second password:", second_password)

# Step 3: Output the length of each password
print("Number of characters in", first_password + ":", len(first_password))
print("Number of characters in", second_password + ":", len(second_password))
