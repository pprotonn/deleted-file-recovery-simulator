import tkinter as tk
from disk import Disk
from file_system import FileSystem

# Initialize disk and file system
disk = Disk(10)
fs = FileSystem(disk)

# Create window
root = tk.Tk()
root.title("Deleted File Recovery Simulator")
root.geometry("500x500")

# Background color
root.configure(bg="black")

# Labels and inputs
tk.Label(root, text="File Name", bg="black", fg="white").pack()
file_entry = tk.Entry(root)
file_entry.pack()

tk.Label(root, text="File Size", bg="black", fg="white").pack()
size_entry = tk.Entry(root)
size_entry.pack()

# Output box
output = tk.Text(root, height=15, width=50, bg="white", fg="black")
output.pack(pady=10)

# Function to display output
def show_output(text):
    output.delete(1.0, tk.END)
    output.insert(tk.END, text)

# Functions
def create_file():
    name = file_entry.get()
    size = int(size_entry.get())
    fs.create_file(name, size)
    show_disk()

def delete_file():
    name = file_entry.get()
    fs.delete_file(name)
    show_disk()

def recover_file():
    name = file_entry.get()
    fs.recover_file(name)
    show_disk()

def show_disk():
    result = ""
    for i, block in enumerate(disk.blocks):
        result += f"Block {i}: {block}\n"
    show_output(result)

# Buttons with colors
tk.Button(root, text="Create File", command=create_file, bg="green", fg="white", width=20).pack(pady=5)

tk.Button(root, text="Delete File", command=delete_file, bg="red", fg="white", width=20).pack(pady=5)

tk.Button(root, text="Recover File", command=recover_file, bg="blue", fg="white", width=20).pack(pady=5)

tk.Button(root, text="Show Disk", command=show_disk, bg="purple", fg="white", width=20).pack(pady=5)

# Run GUI
root.mainloop()