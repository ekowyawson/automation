import os
import shutil
from collections import Counter
import re
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table

console = Console()

# Combined Utility Functions
def create_folder(folder_name):
    """Create a folder if it doesn't already exist, with enhanced visual feedback."""
    try:
        os.makedirs(folder_name, exist_ok=True)
        console.print(f"[bold green]Folder '{folder_name}' created successfully.[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Error creating folder: {e}[/bold red]")

def move_documents(user_folder, temp_folder):
    """Move documents from a deleted user's folder to a temporary folder, with error handling."""
    if not os.path.exists(user_folder):
        console.print("[bold red]User folder not found.[/bold red]")
        return
    create_folder(temp_folder)
    for item in os.listdir(user_folder):
        shutil.move(os.path.join(user_folder, item), os.path.join(temp_folder, item))
    console.print(f"[bold green]User folder '{user_folder}' moved to '{temp_folder}'.[/bold green]")

def sort_documents(source_folder):
    """Sort documents into logs and mail folders based on file type, with visual feedback."""
    file_types = {"logs": ["log"], "mail": ["mail", "eml"]}
    for filename in os.listdir(source_folder):
        file_extension = filename.split(".")[-1].lower()
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                destination_folder = os.path.join(source_folder, folder)
                create_folder(destination_folder)
                shutil.move(os.path.join(source_folder, filename), os.path.join(destination_folder, filename))
                console.print(f"[bold green]Moved '{filename}' to '{folder}' folder.[/bold green]")

def parse_log_file(log_file, target_folder):
    """Parse a log file for errors and warnings, creating separate files, with error handling."""
    create_folder(target_folder)
    error_file_path = os.path.join(target_folder, "errors.log")
    warning_file_path = os.path.join(target_folder, "warnings.log")
    with open(log_file, 'r') as lf, open(error_file_path, 'w') as ef, open(warning_file_path, 'w') as wf:
        for line in lf:
            if "error" in line.lower():
                ef.write(line)
            elif "warning" in line.lower():
                wf.write(line)
    console.print(f"[bold green]Parsed '{log_file}' for errors and warnings.[/bold green]")

def count_file_types(directory):
    """Count the number of specific file types in a directory, with enhanced feedback."""
    file_types = Counter()
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            file_types[item.split('.')[-1]] += 1
    table = Table(title="File Type Counts")
    table.add_column("File Type", style="bold magenta")
    table.add_column("Count", style="bold green")
    for file_type, count in file_types.items():
        table.add_row(file_type, str(count))
    console.print(table)

# Main function to run application
# def automate_ops():
#     def exit_program():
#         console.print("[bold green]Exiting the program.[/bold green]")
#         exit()

#     actions = {
#         '1': lambda: create_folder(Prompt.ask("Enter the folder name to create")),
#         '2': lambda: move_documents(Prompt.ask("Enter the user folder path"), Prompt.ask("Enter the temporary folder path")),
#         '3': lambda: sort_documents(Prompt.ask("Enter the source folder path to sort documents")),
#         '4': lambda: parse_log_file(Prompt.ask("Enter the path of the log file to parse"), Prompt.ask("Enter the target folder for error and warning logs")),
#         '5': exit_program,
#     }

#     while True:
#         console.print("[bold magenta]DevOps Automation Tasks[/bold magenta]")
#         tasks = ["Create a folder", "Handle a deleted user", "Sort documents into folders", "Parse a log file for errors and warnings", "Exit"]
#         for i, task in enumerate(tasks, 1):
#             console.print(f"{i}. {task}")

#         choice = Prompt.ask("Choose a task (Enter the number)", choices=[str(i) for i in range(1, len(tasks) + 1)])

#         action = actions.get(choice)
#         if action:
#             action()
#         else:
#             console.print("[bold red]Invalid option. Please choose a valid option.[/bold red]")

# if __name__ == "__main__":
#     automate_ops()
