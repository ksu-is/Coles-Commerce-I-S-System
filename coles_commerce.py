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
        print("\n--- New Transaction ---")
        # Collect quantities from user
        num_burgers = int(input("Enter number of Burgers: "))
        num_soda = int(input("Enter number of Sodas: "))
        num_fries = int(input("Enter number of Fries: "))
        
        # Day 2: Commit 4 - Core Math Logic
        subtotal = (num_burgers * burger_price) + (num_soda * soda_price) + (num_fries * fries_price)
        
        # Commit 5 - Tax Calculation
        total_tax = subtotal * tax_rate
        
        # Commit 7 - Adding Delivery Logic
        use_delivery = input("Is this for delivery? (y/n): ")
        
        print("\n--- Sales Receipt ---")
        # Using classic % formatting for two decimal places
        print("Subtotal:     Rs. %.2f" % subtotal)
        print("Tax (5%%):     Rs. %.2f" % total_tax)
        
        if use_delivery.lower() == 'y':
            final_total = subtotal + total_tax + delivery_fee
            print("Delivery Fee: Rs. %.2f" % delivery_fee)
        else:
            final_total = subtotal + total_tax
            
        print("--------------------------------")
        print("TOTAL:        Rs. %.2f" % final_total)
        print("--------------------------------")

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
        print("\n[!] Invalid selection. Please enter 1, 2, or 3.")