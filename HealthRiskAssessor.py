#1
# Password protection
password = input("Enter your password: ")

if password != "1234":
    print("Wrong password - program will terminate!")
    exit()

# If the password is correct, proceed to calculate health information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
smoker = input("Are you a smoker? ").lower()
blood_pressure = input("Do you have high blood pressure? ").lower()
high_fat_diet = input("Do you have a high fat diet? ").lower()

# Calculate total points for cardiovascular disease risk
total_points = 0

if age >= 45:
    total_points += 2

if smoker == "no":
    total_points += 1

if blood_pressure == "no":
    total_points += 1

if high_fat_diet == "no":
    total_points += 1

# Print health report
print("\n*** Health Report for", name, "***")
print("Total Points: ", total_points)
