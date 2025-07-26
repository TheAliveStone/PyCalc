# PyCalc

Welcome to **PyCalc**!
A simple, command-line calculator written in Python, designed to help you perform basic arithmetic and explore foundational programming concepts.

---

## Why I Made This

I created PyCalc as my first Python project to:

* Practice core Python skills in a hands‑on way
* Explore writing clean, modular code
* Learn how to structure functionality using functions
* Understand user input handling and error management

---

## What PyCalc Does

PyCalc lets you interactively perform basic calculations in your terminal:

1. **Enter two numbers** (integer or floating point).
2. **Select an operation**: addition, subtraction, multiplication, or division.
3. **Get the result** printed immediately.
4. **Repeat** or **exit**.

---

## Key Python Concepts Practiced

* **Functions:** Encapsulating each arithmetic operation and input validation into reusable functions.
* **Variables:** Storing and updating user inputs and results.
* **Arithmetic Operators:** Using `+`, `-`, `*`, `/` within function bodies.
* **User Input:** Reading from the terminal with `input()` and converting to numbers.
* **Error Handling:** Using `try`/`except` to catch invalid inputs and division by zero.
* **Modularity:** Organizing code into logically separated functions for clarity and maintainability.

---

## Recent Improvements

* **Replaced conditional logic with dedicated functions** for each operation, improving readability and extensibility.
* **Centralized input validation** in its own function to reduce repetition.
* **Simplified control flow**: the main loop now calls functions directly rather than a series of `if` statements.

---

## How to Run

1. Ensure you have [Python](https://python.org) installed (version 3.6 or higher).
2. Clone or download this repository:

   ```bash
   git clone https://github.com/your-username/pycalc.git
   cd pycalc
   ```
3. Run the calculator:

   ```bash
   python calculator.py
   ```

---

## What I Learned

* How to refactor code by moving logic into functions for better structure
* Techniques for handling invalid user input gracefully
* Strategies for writing a clean main loop that orchestrates function calls
* The value of modular design in making future enhancements easier

---

## Next Steps

* Add more mathematical operations (e.g., exponentiation, modulo)
* Implement a history feature to track past calculations
* Build a simple graphical user interface (GUI)
* Write unit tests for each function to ensure correctness

---

Thank you for exploring PyCalc! 🚀
Contributions, forks, and feedback are welcome—let me know what you think!
