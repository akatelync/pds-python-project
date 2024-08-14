import os

class KanbanBoard:
    def __init__(self):
        self.columns = {
            "To Do": [],
            "In Progress": [],
            "Done": []
        }

    def add_task(self, task, column="To Do"):
        self.columns[column].append(task)

    def move_task(self, task, from_column, to_column):
        if task in self.columns[from_column]:
            self.columns[from_column].remove(task)
            self.columns[to_column].append(task)
        else:
            print(f"Task '{task}' not found in {from_column}")

    def display_board(self):
        os.system("cls" if os.name == "nt" else "clear") 
        print("Kanban Board:")
        for column, tasks in self.columns.items():
            print(f"\n{column}:")
            for i, task in enumerate(tasks, 1):
                print(f"  {i}. {task}")

def main():
    board = KanbanBoard()

    while True:
        board.display_board()
        print("\nOptions:")
        print("1. Add task")
        print("2. Move task")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            task = input("Enter task description: ")
            board.add_task(task)
        elif choice == "2":
            from_column = input("Enter source column (To Do/In Progress/Done): ")
            to_column = input("Enter destination column (To Do/In Progress/Done): ")
            task = input("Enter task description: ")
            board.move_task(task, from_column, to_column)
        elif choice == "3":
            print("Thank you for using the Kanban Board. Goodbye!")
            break
        else:
            input("Invalid choice. Press Enter to continue...")

if __name__ == "__main__":
    main()