# Project: Coles Commerce Inventory & Sales System
# Name: Robenson Lebon
# Purpose: A functional POS system for managing sales, taxes, and delivery.

# ==========================================================
# STEP 1: MANAGER MODE (ADMIN MODE SETUP)
# ==========================================================
print("========================================")
print("       COLES COMMERCE: ADMIN SETUP      ")
print("========================================")

# Burger Validation
burger_input = ""
while not burger_input.isdigit():
    burger_input = input("Enter Burger price (numbers only): ")
    if not burger_input.isdigit():
        print("Invalid! Please enter a whole number.")
burger_price = float(burger_input)

# Soda Validation
soda_input = ""
while not soda_input.isdigit():
    soda_input = input("Enter Soda price (numbers only): ")
    if not soda_input.isdigit():
        print("Invalid! Please enter a whole number.")
soda_price = float(soda_input)

# Fries Validation
fries_input = ""
while not fries_input.isdigit():
    fries_input = input("Enter Fries price (numbers only): ")
    if not fries_input.isdigit():
        print("Invalid! Please enter a whole number.")
fries_price = float(fries_input)

# Delivery Fee Validation
delivery_input = ""
while not delivery_input.isdigit():
    delivery_input = input("Enter Delivery Fee (numbers only): ")
    if not delivery_input.isdigit():
        print("Invalid! Please enter a whole number.")
delivery_fee = float(delivery_input)

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
        # SPRINT 3: SAVE TO FILE 
        file_path = "sales_log.txt"
        sales_file = open(file_path, "a")
        
        sales_file.write("\n--- Transaction Record ---\n")
        sales_file.write("Burgers: " + str(num_burgers) + "\n")
        sales_file.write("Sodas: " + str(num_soda) + "\n")
        sales_file.write("Fries: " + str(num_fries) + "\n")
        sales_file.write("Total Revenue: Rs. %.2f\n" % final_total) # Using format for the file too
        sales_file.write("--------------------------\n")
        
        sales_file.close()
        print("\n[System] Transaction saved to sales_log.txt")
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
