# Project Roadmap

- [x] Create GitHub Repository and join KSU-IS organization.
- [x] Initialize README.md with project description.
- [x] Research and clone the udaymistry POS repository for evaluation.
- [x] Complete evaluation of existing code and document findings.
- [ ] Plan basic logic for the main menu loop.

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

## Sprint 2 - Development (April 21 - April 23)
The goal of this sprint is to establish the core logic and user interface for the Coles Commerce System.

- [ ] Task 1: Initialize main application file and foundational variables.
- [ ] Task 2: Create the primary interaction loop (while loop) for the menu.
- [ ] Task 3: Develop sales logic to handle quantities and subtotal calculations.
- [ ] Task 4: Integrate tax calculations and apply professional float formatting.
- [ ] Task 5: Implement input validation to ensure the program handles user errors.
- [ ] Task 6: Document final progress for the sprint and plan for file storage in Sprint 3.

### Emerging Tasks
* (To be updated as issues or new needs arise during coding)
