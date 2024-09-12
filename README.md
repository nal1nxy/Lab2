> **COMP-801 Integrated Computing Practicum**
# Lab 2

## Due Dates
- Assigned Week 3
- Due before midnight before Week 4 class

## Purpose
- Get familiar with Python classes by developing 2 instance methods in the 
  class `Sentence`
- Gain more pracdtice with incremental development, designing and implementing classes, and with version control
- **AR1**, **AR2**, and **AR3** are highly relevant to your preparation this lab.

## Getting Started
1. Open `git-bash` (in Windows OS) or `terminal` utility (in MacOS or Linux)
2. Clone remote repo into your **comp801/labs** directory 
- Do NOT create **lab2** directory. Cloning will do that. 
- Use the `clone` command with TWO arguments as shown below:
```
git clone <URL of your remote repo> lab2
```
3. Open **lab2** folder in VS Code
4. Run `client.py` in two ways:
  - In the VS Code integrated terminal, run `python client.py`
  - Use the Run Python File button in the upper right corner. 
5. Check the erors reported in the **Problems** tab of the VS Code integarted 
terminal: how many errors and types of errors in each of the Python source
files. 
- Install extensions Flake8, Pylint, Pylance, and Black from Microsoft
  - These extension perform static analysis on the Python modules

## Evaluation
### Documentation, 8 pts
3 module docstrings, `client.py`, `sentence.py`, and `tests.py`, and  a Markdown file, `DESIGN.md`
  - enter your name and your collaborator(s) names
  - enter date 


### Testing, 21 pts
3 testing functions in `tests.py`, @ 7 pts each

  - 1 test cases for `only_integers()` method
  - 2 test cases `filter_words()` method

### DESIGN.md, 24 pts
- 2 methods, 12 pts each

### Implementation**, 20 pts
- 2 methods, 10 pts each 

### Incremental development, 18 pts
 6 commits @ 3 pts each:
 
- 3 commits for each method
  - 1 commit to write the testing function(s)
  - 1 commit to design the solution
  - 1 commit to implement the design

### Static Analysis, 9 pts
Submitted work should be free of static analysis problems.

## Guidelines
These guidelines are aligned with the evaluation criteria above. 

1. **Document** ALL modules by completing docstring information.
2. **Understand** what each method is supposed to do, based on the docstring 
   description, BEFORE writing the testing functions.
3. Write **testing functions** to demonstrate your understanding of each method.
4. **Design** before coding.
5. **Write code** incrementally, one method at a time.
6. Run the tests, debug and fix errors as you go.
7. Repeat steps 2 tp 6.
8. **Static analysis**: fix all problems. 

## Collaboration
Collaboration is allowed.

- Ask questions of your collaborator, CAs, and instructor; 
- Answer questions and give advice to your peers via Discord, during study group, or one-on-one collaborations;  
  - Discuss and clarify concepts; 
  - Show or practice concepts on simple examples. 

You are NOT allowed to give your work on this assignment to somebody else,
  or to do it for someone else. 
