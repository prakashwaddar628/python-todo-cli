import argparse
import os

TODO_FILE = 'tasks.txt'
COMPLETE_MARKER = '[X]'
PENDING_MARKER = '[ ]'

def load_tasks():
    """Loads the tasks from the todofile."""
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                is_complete = line.startswith(COMPLETE_MARKER)
                description = line[len(COMPLETE_MARKER):].strip() if is_complete else line[len(PENDING_MARKER):].strip()
                tasks.append({'description':description, 'complete': is_complete})
    return tasks

def save_tasks(tasks):
    """save the tasks into the todofile."""
    with open(TODO_FILE,  'w') as f:
        for task in tasks:
            status_marker = COMPLETE_MARKER if task['complete'] else PENDING_MARKER
            f.write(f"{status_marker} {task['description']}\n")

def display_tasks(index, task):
    """Formats and prints a single tasks."""
    status = COMPLETE_MARKER if task['complete'] else PENDING_MARKER
    print(f"{index}. {status} {task['description']}")

def add_tasks(args):
    pass

def list_tasks(args):
    pass

def complete_tasks(args):
    pass

def delete_tasks(args):
    pass

def main():
    pass

if __name__ == '__main__':
    main()