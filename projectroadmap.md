# Project Roadmap
## Sprint 1- Basis of Program
- [x] Create GitHub Repository and join KSU-IS organization.
- [x] Initialize README.md with project description.
- [x] Research and clone the udaymistry POS repository for evaluation.
- [x] Complete evaluation of existing code and document findings.
- [x] Plan basic logic for the main menu loop.

## Codebase Evaluation
I evaluated the **udaymistry/Basic-Point-On-Sale-System** repository. 
* **Source:** [udaymistry Basic POS System](https://github.com/udaymistry/Basic-Point-On-Sale-System-)
* **Findings:** The project uses simple mathematical variables to track item prices and totals. It uses functions to clear the screen and reset totals, which is a logic flow I can adapt.
* **Course Alignment:** The original code uses `Tkinter` for a windowed interface. I plan to convert this logic to a command line interface using `while` loops, `input()`, and `print()` statements.
  
I successfully cloned and executed the **udaymistry/Basic-Point-On-Sale-System** reference code.
### Key Technical Findings:
**Mathematical Logic:** The system uses a specific function called `CostOfOrder()` to handle all price calculations. 
It calculates the subtotal by multiplying item quantities by a fixed float value (e.g., `BurgerPrice * 70.00`).
**Tax Calculation:** The code uses a combined tax variable (`gst = 0.025 + 0.025`) to apply a percentage to the subtotal. I will adapt this percentage logic for my project.
**Currency Formatting:** The developer uses `'%.2f'` to ensure all totals are displayed with exactly two decimal places
 This is a technique I plan to implement to keep my commerce system professional.
**Data Resetting:** The `I_Reset()` function demonstrates how to clear variables and return them to a zero state, which will be essential for my sales loop.

### Adaptations for My Project:
**Interface Change:** The reference code uses the `Tkinter` library to create a large windowed GUI. Since this is outside my current course curriculum, I will convert this logic to a text-based Command Line Interface (CLI).
**Input Method:** Instead of using `Entry()` boxes, I will use the `input()` and `int()` functions learned in my recent modules to gather order data from users.

## Sprint 2 - Development 
The goal of this sprint is to establish the core logic and user interface for the Coles Commerce System.

- [x] **Task 1:** Initialize main application file and foundational variables.
- [x] **Task 2:** Create the primary interaction loop (while loop) for the menu.
- [x] **Task 3:** Develop sales logic to handle quantities and subtotal calculations.
- [x] **Task 4:** Integrate tax calculations and apply professional float formatting (`%.2f`).
- [x] **Task 5:** Implement logic for a delivery fee and session resets.
- [x] **Task 6:** Document progress for the sprint and confirm visibility in the ksu-is organization.

## Sprint 3- Dynamic Sytem and Final Adjustments

- [x] **Task 1:** Implement Manager Mode for dynamic price and fee setup.
- [x] **Task 2:** Add input validation to prevent system crashes during setup.
- [x] **Task 3:** Create a text file (sales_log.txt) to save transaction history.
- [x] **Task 4:** Design and upload the project marketing slide for upper management.
      **marketing slide link**-https://kennesawedu-my.sharepoint.com/:p:/r/personal/rlebon1_students_kennesaw_edu/Documents/Final%20Coles%20Commerce%20I%26S%20-%20Copy.pptx?d=wf4d0f0aa4cee45c8ba044dd86f69a977&csf=1&web=1&e=zxcsRt

### Emerging Tasks

 - Resolved `IndentationError` during sales logic implementation.
 - Fixed `ValueError` caused by special character formatting in the tax display.
- Successfully adapted the math logic from the `udaymistry` reference repository into a functional CLI.
- Plan for Sprint 3 to include persistent file storage for transaction history.
- Added View Sales Log and Clear Sales Log features to the main menu.
- Moved price variables from hard-coded constants to user-defined floats.
- Added a system initialization header to separate Admin Setup from the Main Menu.
- Verified tax math remains accurate with new dynamic pricing.
- Built a Manager Mode with input validation to allow for custom pricing and prevent system crashes.
