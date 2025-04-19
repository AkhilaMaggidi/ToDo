import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_entry = tk.Entry(self.frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=(0, 10))

        self.add_button = tk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Selected Task", command=self.delete_task)
        self.delete_button.pack(pady=(0, 10))

        self.mark_done_button = tk.Button(root, text="Mark as Done", command=self.mark_done)
        self.mark_done_button.pack(pady=(0, 10))

    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Warning", "Please enter a task.")
            return
        self.tasks.append({"task": task, "done": False})
        self.update_listbox()
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_done(self):
        try:
            selected_index = self.listbox.curselection()[0]
            self.tasks[selected_index]["done"] = True
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task_item in self.tasks:
            task_text = task_item["task"]
            if task_item["done"]:
                task_text = "[Done] " + task_text
            self.listbox.insert(tk.END, task_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
