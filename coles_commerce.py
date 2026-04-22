# Project: Coles Commerce Inventory & Sales System
# Student: Robenson Lebon
# Purpose: Foundational setup for item pricing and tax logic

# Step 1: Define our store items and prices
# We are using simple variables to keep the logic clear
burger_price = 70.00
soda_price = 40.00
fries_price = 50.00
delivery_fee = 30.00

# Step 2: Set the tax rate (5% total tax as seen in our research)
tax_rate = 0.05

# Step 3: Initialize sales tracking variables
subtotal = 0.0
total_tax = 0.0
final_total = 0.0

print("--- Coles Commerce System Initialized ---")
# Day 2: Commit 3 - Building the Menu Loop
while True:
    print("\n--- Main Menu ---")
    print("1. Process a Sale")
    print("2. View Inventory Prices")
    print("3. Exit")
    
    choice = input("Select an option (1-3): ")
    
    if choice == '1':
        print("\nStarting a new sale...")
        num_burgers = int(input("Enter number of Burgers: "))
        num_soda = int(input("Enter number of Sodas: "))
        num_fries = int(input("Enter number of Fries: "))
        subtotal = (num_burgers * burger_price) + (num_soda * soda_price) + (num_fries * fries_price)
        total_tax = subtotal * tax_rate
        final_total = subtotal + total_tax + delivery_fee
        print("\nSubtotal calculated: Rs. " + str(subtotal))
        print("Tax: Rs. " + str(total_tax))
        print("Delivery Fee: Rs. " + str(delivery_fee))
        print("Final Total: Rs. " + str(final_total))
    elif choice == '2':
        print("\n--- Current Inventory ---")
        print("Burgers: Rs. 70.00")
        print("Soda: Rs. 40.00")
        print("Fries: Rs. 50.00")
    elif choice == '3':
        print("Exiting the system. Have a great day!")
        break
    else:
        print("Invalid selection. Please try again.")
