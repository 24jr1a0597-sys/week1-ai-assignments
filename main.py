import json
from datetime import datetime

# Read data from JSON file
with open("tips.json", "r") as file:
    data = json.load(file)

tips = data["study_tips"]
quotes = data["quotes"]

name = input("Enter your name: ")

greeting = f"Hello, {name}! Welcome to Smart Student Assistant."
print(greeting)

# Save greeting
with open("output.txt", "a") as file:
    file.write(greeting + "\n")

while True:
    print("\n===== MENU =====")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        result = tips[0]
        print(result)

    elif choice == "2":
        result = quotes[0]
        print(result)

    elif choice == "3":
        result = str(datetime.now())
        print(result)

    elif choice == "4":
        print("Thank you for using Smart Student Assistant!")
        break

    else:
        result = "Invalid choice!"
        print(result)

    with open("output.txt", "a") as file:
        file.write(result + "\n")
with open("output.txt", "a") as file:
    file.write(result + "\n")

with open("output.txt", "a") as file:
    file.write(greeting + "\n")