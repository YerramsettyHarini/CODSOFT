import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_task_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT)

        self.tasks_listbox = tk.Listbox(self.root, width=50, height=10)
        self.tasks_listbox.pack(pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.remove_task_button = tk.Button(self.button_frame, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(side=tk.LEFT, padx=5)

        self.update_task_button = tk.Button(self.button_frame, text="Update Task", command=self.update_task)
        self.update_task_button.pack(side=tk.LEFT, padx=5)

        self.mark_completed_button = tk.Button(self.button_frame, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self):
        try:
            task_index = self.tasks_listbox.curselection()[0]
            del self.tasks[task_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task(self):
        try:
            task_index = self.tasks_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[task_index]['task'] = new_task
                self.update_task_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "You must enter a new task.")
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def mark_completed(self):
        try:
            task_index = self.tasks_listbox.curselection()[0]
            self.tasks[task_index]['completed'] = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "Completed" if task['completed'] else "Not Completed"
            self.tasks_listbox.insert(tk.END, f"{task['task']} - {status}")

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
