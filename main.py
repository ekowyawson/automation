from collections import Counter
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from devops.automation import create_folder, move_documents, sort_documents, parse_log_file, count_file_types

console = Console()

# Main function to run application
def automate_ops():
    def exit_program():
        console.print("[bold green]Exiting the program.[/bold green]")
        exit()

    actions = {
        '1': lambda: create_folder(Prompt.ask("Enter the folder name to create")),
        '2': lambda: move_documents(Prompt.ask("Enter the user folder path"), Prompt.ask("Enter the temporary folder path")),
        '3': lambda: sort_documents(Prompt.ask("Enter the source folder path to sort documents")),
        '4': lambda: parse_log_file(Prompt.ask("Enter the path of the log file to parse"), Prompt.ask("Enter the target folder for error and warning logs")),
        '5': exit_program,
    }

    while True:
        console.print("[bold magenta]DevOps Automation Tasks[/bold magenta]")
        tasks = ["Create a folder", "Handle a deleted user", "Sort documents into folders", "Parse a log file for errors and warnings", "Exit"]
        for i, task in enumerate(tasks, 1):
            console.print(f"{i}. {task}")

        choice = Prompt.ask("Choose a task (Enter the number)", choices=[str(i) for i in range(1, len(tasks) + 1)])

        action = actions.get(choice)
        if action:
            action()
        else:
            console.print("[bold red]Invalid option. Please choose a valid option.[/bold red]")

if __name__ == "__main__":
    automate_ops()