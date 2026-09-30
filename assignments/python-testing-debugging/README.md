# 📘 Assignment: Python Testing and Debugging

## 🎯 Objective

Learn how to write simple automated tests with Python's `unittest` module and use failing tests to find and fix bugs. You will add edge-case tests to a small set of helper functions and improve the functions until the full test suite passes.

## 📝 Tasks

### 🛠️ Run the Starter Tests

#### Description
Open `starter-code.py` and run the existing tests to see how `unittest.TestCase` checks function results.

#### Requirements
Completed program should:

- Run with `python starter-code.py`
- Pass all provided tests before any changes
- Identify the test class and the assertions that compare expected and actual values


### 🛠️ Add Edge-Case Tests

#### Description
Add tests for cases that are not covered by the starter tests. Vowel counting should ignore letter case, and the average of an empty list should be `0`.

#### Requirements
Completed program should:

- Add a test that checks vowel counting with uppercase letters
- Add a test that checks the average of an empty list is `0`
- Run the tests and observe which new cases fail


### 🛠️ Fix the Bugs

#### Description
Use the failing test output to find and fix the problems in the helper functions. Run the full test suite again after each fix.

#### Requirements
Completed program should:

- Update the vowel-counting function so uppercase and lowercase vowels are counted
- Update the average function so an empty list returns `0` without raising an error
- Pass all provided and added tests when run with `python starter-code.py`
- Add one additional test of your choice and confirm it passes