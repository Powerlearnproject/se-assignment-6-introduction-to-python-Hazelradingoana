1. Python Basics:

**Python** is a high-level, interpreted programming language known for its readability and simplicity.
It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.


__Here are some key features of Python:__

__Readable and Maintainable Code__ -> Python's syntax emphasizes readability, making it easier to write and maintain code.
__Dynamic Typing and Automatic Memory Management__ -> Python manages memory automatically and supports dynamic typing, allowing variables to change types easily.
__Extensive Standard Library and Third-Party Modules__ -> Python comes with a comprehensive standard library and a vast ecosystem of third-party packages, enhancing its functionality.
__Cross-Platform Compatibility__ -> Python runs on various operating systems, including Windows, macOS, and Linux.
__Interpreted Language__ -> Python is an interpreted language, meaning code is executed line by line, which simplifies debugging.


**Use Cases**

__Web Development__
Frameworks like Django and Flask make Python an excellent choice for building web applications.

__Data Science and Machine Learning__ 
Libraries such as NumPy, pandas, scikit-learn, and TensorFlow enable data analysis, scientific computing, and machine learning.

__Automation and Scripting__ 
Python is used for writing scripts to automate repetitive tasks.

__Software Development__
Python is suitable for rapid prototyping and building various applications.



2. Installing Python


The steps to install Python on different operating system (Windows, macOS, or Linux).

**Installing Python on Windows**

__Download the Installer__
Go to the official Python website.
Download the latest stable release for Windows.

__Run the Installer__

Open the downloaded executable file.
Ensure "Add Python to PATH" is checked.
Choose "Install Now" for a simple installation.
Verify Installation:

__Open Command Prompt__
Type python --version and press Enter. You should see the installed Python version.

__Set Up a Virtual Environment__

Install virtualenv if not already installed: pip install virtualenv.
Create a virtual environment -> python -m venv myenv.

__Activate the virtual environment__
On Windows: myenv\Scripts\activate
On macOS/Linux: source myenv/bin/activate


**Installing Python on macOS**

__Download the Installer__

Go to the official Python website.
Download the latest stable release for macOS.
Run the Installer:

Open the downloaded .pkg file and follow the installation instructions.

__Verify Installation__

Open Terminal.
Type python3 --version and press Enter. You should see the installed Python version.


__Set Up a Virtual Environment__

Install virtualenv if not already installed: pip3 install virtualenv.
Create a virtual environment: python3 -m venv myenv.
Activate the virtual environment: source myenv/bin/activate.

**Installing Python on Linux**

__Install Python Using Package Manager__

Open Terminal.
For Debian-based distributions (e.g., Ubuntu): 
sudo apt update && sudo apt install python3
For Red Hat-based distributions (e.g., Fedora): 
sudo dnf install python3


__Verify Installation__

Type python3 --version and press Enter. You should see the installed Python version.

__Set Up a Virtual Environment__

Install virtualenv if not already installed: pip3 install virtualenv.
Create a virtual environment: python3 -m venv myenv.
Activate the virtual environment: source myenv/bin/activate.

3. Python Syntax and Semantics:

A simple Python program that prints "Hello, World!"
Saved in a file named "helloWorld.py"

__Explanation__

__print()__
This is a built-in function in Python used to output text to the console.
"Hello, World!": This is a string, which is a sequence of characters enclosed in double quotes. The print function takes this string as an argument and displays it.

4. Data Types and Variables:

__Basic Data Types in Python:__

int: 
Integer, a whole number (e.g., 42).
float: 
Floating-point number, a number with a decimal point (e.g., 3.14).
str: 
String, a sequence of characters (e.g., "Hello").
bool: 
Boolean, a value representing True or False.
list: 
List, an ordered collection of items (e.g., [1, 2, 3]).
tuple: 
Tuple, an ordered, immutable collection of items (e.g., (1, 2, 3)).
dict: 
Dictionary, a collection of key-value pairs (e.g., {"name": "Alice", "age": 25}).
set: 
Set, an unordered collection of unique items (e.g., {1, 2, 3}).


__A short script that demonstrates how to create and use variables of different data types__
Saved in a file named "dataTypes.py"

5. Control Structures:

__Conditional Statements:__

Conditional statements allow the execution of certain blocks of code based on specific conditions. The primary conditional statements in Python are if, elif, and else.

Example is shown in the file named "conditional.py"

__Loops:__

Loops are used to execute a block of code repeatedly. Python supports for and while loops.

Example of for Loop:
Example is shown in the file named "conditional.py"

Example of while Loop:
Example is shown in the file named "conditional.py"

6. Functions in Python:

Functions are reusable blocks of code that perform a specific task. They allow for code modularity, reuse, and organization. Functions are defined using the def keyword, followed by the function name and parentheses containing parameters.

Example Function
Example is shown in the file named "functions.py"

7. Lists and Dictionaries:

__Differences__

Lists: 
Ordered collections of items, indexed by position (0-based index). Items can be of any data type, and duplicates are allowed.
Dictionaries: 
Unordered collections of key-value pairs, indexed by keys (unique). Keys must be immutable (e.g., strings, numbers, tuples), while values can be of any data type.
Script

Script example is shown in the file named "listsDict.py"

8. Exception Handling:

**Exception Handling** in Python is used to manage and respond to runtime errors. It allows a program to continue running or terminate gracefully instead of crashing. When an error occurs, Python raises an exception. By using try, except, and finally blocks, you can handle these exceptions and execute specific code regardless of whether an error occurred.

Example is shown in the file named "Errors.py"

__Explanation__

try block: 
This block contains code that might throw an exception.
except block: 
This block contains code that handles the exception if it occurs. You can have multiple except blocks to handle different types of exceptions.
finally block: 
This block contains code that will run no matter what, even if an exception is thrown. It is used to release resources or perform cleanup tasks.

9. Modules and Packages

__The concepts of modules and packages in Python.__

__Modules__ in Python are files containing Python code that define functions, classes, and variables. Modules help organize and reuse code. A module can be a single file (with a .py extension) or a group of files (a package).

__Packages__ are collections of modules organized in directories with a special __init__.py file. The __init__.py file can be empty or execute initialization code for the package. Packages allow for hierarchical structuring of the module namespace.

Example Using the math Module:
The math module provides mathematical functions.
Example is shown in the file named "math.py"


10. File I/O

Reading from a file 

Example is shown in the file named "fileReading.py"

__Explanation__

open(file_path, 'r'): 
Opens the file in read mode ('r').
with open(...) as file: 
Ensures the file is properly closed after reading.
file.read(): 
Reads the entire content of the file.
The content is printed to the console.

Writing to a File:
Example is shown in the file named "fileReadWrite.py"

__Explanation__

open(file_path, 'w'): Opens the file in write mode ('w'). If the file doesn't exist, it creates a new one; if it does, it overwrites the content.
with open(...) as file: Ensures the file is properly closed after writing.
file.write(line + '\n'): Writes each string in the list to the file, followed by a newline character.


Reference from:
https://docs.python.org/3/
https://realpython.com/documenting-python-code/
