# Project: Coles Commerce Inventory & Sales System
# Name: Robenson Lebon
# Purpose: A functional POS system for managing sales, taxes, and delivery.

#  Configuration & Variables ---
burger_price = 70.00
soda_price = 40.00
fries_price = 50.00
delivery_fee = 30.00
tax_rate = 0.05

# ---  Main Application Loop ---
while True:
    # Day 3: Commit 6 - Resetting totals for each new session
    subtotal = 0.0
    total_tax = 0.0
    final_total = 0.0

    print("\n================================")
    print("   COLES COMMERCE MAIN MENU   ")
    print("================================")
    print("1. Process a New Sale")
    print("2. View Inventory Prices")
    print("3. Exit System")
    
    choice = input("\nSelect an option (1-3): ")
    
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
        print("\n--- Current Inventory Prices ---")
        print("Burgers: Rs. %.2f" % burger_price)
        print("Soda:    Rs. %.2f" % soda_price)
        print("Fries:   Rs. %.2f" % fries_price)
        print("Delivery: Rs. %.2f" % delivery_fee)

    elif choice == '3':
        #Commit 3 - Exit Logic

        print("\n" * 2) # Adds two blank lines
        print("========================================")
        print("Exiting Coles Commerce. System shutdown successful.")
        print("========================================")
        print("\n" * 2)
        break

    else:
        print("Invalid selection. Please try again.")
