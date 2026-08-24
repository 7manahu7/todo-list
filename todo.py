import os
from sys import argv
from rich import print
from rich.console import Console
from rich.table import Table


TODO_FILE = os.path.expanduser("~/Projects/Python/todo-list/todo/list.txt")
console = Console()


def add_items(task):
    with open(TODO_FILE, "a") as file:
        file.write(f"{task}\n")


def read_list():
    print("")
    table = Table(title="To Do List")

    table.add_column("NO. ")
    table.add_column(" Items ", style="green")
    with open(TODO_FILE, "r") as file:
        lines = file.readlines()

        for i, line in enumerate(lines, start=1):
            table.add_row(str(i), line.strip())
        console.print(table)


def remove_items(index):
    with open(TODO_FILE, "r") as file:
        lines = file.readlines()

        index = int(index) - 1

        if 0 <= index < len(lines):
            saved = lines[index].strip()
            lines.pop(index)

            with open(TODO_FILE, "w") as file:
                lines = file.writelines(lines)

            os.system(f"notify-send 'task: {saved}' removed")


def main():

    if argv[1] == "-rm" or argv[1] == "--remove":
        remove_items(argv[2])

    elif argv[1] == "-a" or argv[1] == "--add":
        add_items(argv[2])

    elif argv[1] == "-r" or argv[1] == "--read":
        read_list()


main()
