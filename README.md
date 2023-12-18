# BUDGET MANAGER
#### Video Demo:  <https://youtu.be/JDTDmx3b2Fs>

#### Description:
- The Budget Analyzer and Planner is a Python-based command-line tool that helps users manage their expenses. The tool allows users to record expenses, view their spending habits, and analyze their overall financial patterns in a very simply way.

## Features:
- **Expense Recording:** Users can record their expenses by specifying the amount and choosing a predetermined category.

- **Expense Viewing:** This tool provides options to view expenses based on specific categories or the total overall expenses (of all categories).

- **Expense Analysis:** Users can simply analyze their expenses, getting insights into spending patterns, both for specific categories and for all categories.

## Project Structure:
- **project.py:** This file contains the main logic of the Budget Analyzer and Planner, including 3 functions: for recording expenses, viewing expenses, and conducting a very simple financial analysis.

- **test_project.py:** This file includes unit tests for the 3 functions in `project.py`. These tests ensure that each component of the budget tool works as expected.

## What I Learned:
Throughout this project, I gained even more practical experience in Python programming (aside from the one I gained doig the Cs50 course) and command-line interface (CLI) application development.
Key learning points include:
- How to structure a Python project.
- Working with user input and validating user input considerong all possible options (like the user not typing a valid choice).
- Implementing simple functions for data recording, viewing, and analysis.
- Unit testing using pytest and additional functions inside this litesting library.

## Difficulties Faced:
While developing this project, I encountered challenges, particularly in the testing phase. Issues with the pytest framework and debugging took considerable time. Despite these challenges, I persevered and learned a little bit more about troubleshooting and debugging Python files.

## Design Choices:
- **CLI Interface:** I chose a command-line interface for simplicity and ease of use. (and it was the only available choice. This is also why I couln't use a "graphic" library like matplotlib to show graphs for the analysis part).

- **Modular Functions:** Each major feature (recording, viewing, analysis) is encapsulated in separate functions. This modular design enhances code readability and maintainability. I am very aware it could have been done better and with more function but I didn't want to risk damaging my functional project.

## Future Improvements:
In the future, I plan to enhance this tool by adding features such as data persistence (saving recorded expenses), a time-tracking feature to let the user know how expenses change over time, and a graphical user interface (GUI) for a more user-friendly experience (including graphs). I would also like to refactor the code by adding more functions so the debugging and testing can be done more smootherly and without any issues. Also to make the code more readable.
