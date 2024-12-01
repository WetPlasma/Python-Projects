print("Welcome to the tip calculator.\n")
bill = int(input("What is your bill?\n"))  
tip = int(input("What percentage tip are you giving, 10, 12, or 15?\n"))
people = int(input("How many people are splitting the bill?\n"))


tip_per_person = round((bill * (tip / 100)) / people, 2)

print(f"The tip each person needs to pay is: ${tip_per_person}")
