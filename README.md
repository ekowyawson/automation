# LAB - Class 19

## Project: Automation

- *Version: 1.0*

### Author: Ekow Yawson

**Project Overview**:

This utility script provides a set of tools designed for efficient file and log management within a specified directory. It includes functions for:

- creating folders
- moving documents
- sorting documents by type
- parsing log files for errors and warnings
- counting file types
- gracefully exiting the program

This script aims to automate and streamline common file management tasks using Python, enhancing productivity and maintaining organization.

### Features

- **Create Folder**: Creates a new folder if it doesn't already exist, offering visual feedback on the operation.
- **Move Documents**: Moves documents from one directory to another, handling errors gracefully.
- **Sort Documents**: Automatically sorts documents into predefined categories (logs and mail) based on their file type.
- **Parse Log File**: Parses given log files to identify and segregate errors and warnings, facilitating easier log management.
- **Count File Types**: Counts and displays the number of files of specific types within a directory, providing a summary of the content.
- **Exit Program**: Includes functionality to gracefully exit the script, ensuring any necessary cleanup is performed.

### Setup

**Environment Setup Steps**:

To use this utility script:

1. Clone the repository to your local machine and ensure Python 3.6 or later is installed.

   ```sh
   git clone [repository-url]
   cd [repository-directory]
   ```

2. To install the required libraries/modules, run the following command:
   - `pip install -r requirements.txt`.

### How to Run the Application

To run the script, create a virtual environment then run `python main.py`.

- A menu will be displayed automation choices.

### Links and Resources

- [shutil](https://pymotw.com/3/shutil/)
- [Python Regular Expressions Tutorial](https://www.datacamp.com/community/tutorials/python-regular-expression-tutorial)
- [Python `os` Module](https://pymotw.com/3/os/)
- [Automation Ideas](https://www.youtube.com/watch?v=qbW6FRbaSl0&t=69s)
- [Automating Your Browser and Desktop Apps](https://www.youtube.com/watch?v=dZLyfbSQPXI)
- [Watchdog](https://pythonhosted.org/watchdog/)

### Tests

Tests are provided in the `tests` directory. To run the tests, create an virtual environment with **venv** at the root of the project and run pytest:

**Example**:

```python
python3 -m venv .venv
source .venv/bin/activate
pytest
```

### Contributors

- Stephanie G Johnson
- Latherio Kidd
