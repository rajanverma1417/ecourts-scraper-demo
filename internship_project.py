"""
eCourts Scraper (Demo Version - Improved)
-----------------------------------------
This version includes:
✅ Data validation using while loops
✅ Option to continue until user types 'no'

Made by: [Your Name]
Date: [Current Date]
"""

import json
import datetime
import random

# Function to simulate fetching case data
def fetch_case_data(cnr_number):
    """This function returns a fake case record for demo purpose."""
    fake_cases = [
        {"CNR": "DL12345678", "Court": "Delhi District Court", "Case Type": "Civil"},
        {"CNR": "MH98765432", "Court": "Mumbai Sessions Court", "Case Type": "Criminal"},
        {"CNR": "UP13579246", "Court": "Lucknow High Court", "Case Type": "Family"},
    ]
    for case in fake_cases:
        if case["CNR"] == cnr_number:
            return case
    return None

# Function to simulate checking if case is listed today or tomorrow
def check_listing():
    """Randomly decide whether the case is listed today or tomorrow."""
    options = ["today", "tomorrow", "not listed"]
    return random.choice(options)

# Function to display and save result
def save_result(case, listing_status):
    """Save case result into a JSON file."""
    data = {
        "CNR": case["CNR"],
        "Court": case["Court"],
        "Case Type": case["Case Type"],
        "Listing Status": listing_status,
        "Serial Number": random.randint(1, 100),
        "Date Checked": str(datetime.date.today())
    }

    # Show output on console
    print("\n----- Case Information -----")
    for key, value in data.items():
        print(f"{key}: {value}")

    # Save JSON file
    with open("case_result.json", "w") as file:
        json.dump(data, file, indent=4)
    print("\n✅ Result saved as 'case_result.json'")

# Function to simulate cause list download
def download_cause_list():
    """Create a fake cause list for today."""
    today = datetime.date.today()
    cases = [
        {"Serial No": i + 1, "Court": random.choice(["Delhi", "Mumbai", "Lucknow"]) + " Court"}
        for i in range(5)
    ]

    with open("cause_list.txt", "w") as file:
        file.write(f"Cause List - {today}\n\n")
        for c in cases:
            file.write(f"Serial {c['Serial No']}: {c['Court']}\n")

    print("\n📄 Fake Cause List saved as 'cause_list.txt'")

# ----------------- MAIN PROGRAM -----------------
print("===========================================")
print("         eCourts Scraper - Demo v2")
print("===========================================\n")

# Outer loop for repeating the program until user says 'no'
while True:
    print("1. Check case listing")
    print("2. Download today's cause list")
    choice = input("Enter your choice (1 or 2): ")

    # Validate input choice
    while choice not in ["1", "2"]:
        print("❌ Invalid input! Please enter 1 or 2 only.")
        choice = input("Enter your choice (1 or 2): ")

    # Option 1: Check case listing
    if choice == "1":
        cnr = input("\nEnter CNR Number (Example: DL12345678): ").strip().upper()

        # Validate CNR input format (must start with 2 letters + 8 digits)
        while not (len(cnr) == 10 and cnr[:2].isalpha() and cnr[2:].isdigit()):
            print("❌ Invalid CNR format! Example: DL12345678")
            cnr = input("Please enter again: ").strip().upper()

        # Check if the case exists in fake data
        case = fetch_case_data(cnr)
        if case:
            listing = check_listing()
            save_result(case, listing)
        else:
            print("\n❌ Case not found in records.")

    # Option 2: Download cause list
    elif choice == "2":
        download_cause_list()

    # Ask user if they want to continue
    again = input("\nDo you want to check another case or cause list? (yes/no): ").strip().lower()
    while again not in ["yes", "no"]:
        print("❌ Please type only 'yes' or 'no'.")
        again = input("Do you want to continue? (yes/no): ").strip().lower()

    if again == "no":
        print("\n👋 Thank you for using eCourts Scraper Demo!")
        break
