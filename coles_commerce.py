# Name: Robenson Lebon
# Purpose: A functional POS system for managing sales, taxes, and delivery.

# --- MANAGER MODE: INITIAL SETUP ---
print("========================================")
print("       COLES COMMERCE: ADMIN SETUP      ")
print("========================================")

# Setting dynamic prices 
burger_price = float(input("Enter current Burger price: "))
soda_price = float(input("Enter current Soda price: "))
fries_price = float(input("Enter current Fries price: "))
delivery_fee = float(input("Enter current Delivery fee: "))
tax_rate = 0.07 

print("\nSystem initialized. Prices updated successfully.")
print("========================================\n")

# ---  Main Application Loop ---
while True:
    #  - Resetting totals for each new session
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
        num_burgers = int(input("Enter number of Burgers: "))
        num_soda = int(input("Enter number of Sodas: "))
        num_fries = int(input("Enter number of Fries: "))
        
        # Core Math with 7% GA Tax
        subtotal = (num_burgers * burger_price) + (num_soda * soda_price) + (num_fries * fries_price)
        total_tax = subtotal * 0.07 # Updated to 7%
        
        use_delivery = input("Is this for delivery? (y/n): ")
        
        print("\n--- Sales Receipt ---")
        print("Subtotal:     Rs. %.2f" % subtotal)
        print("Tax (7%%):     Rs. %.2f" % total_tax) # Updated label
        
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
        # Exit Logic

        print("\n" * 2) # Adds two blank lines
        print("========================================")
        print("Exiting Coles Commerce. System shutdown successful.")
        print("========================================")
        print("\n" * 2)
        break

    else:
        print("Invalid selection. Please try again.")
