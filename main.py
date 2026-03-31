# main.py

from disk import Disk
from file_system import FileSystem

disk = Disk(10)
fs = FileSystem(disk)

while True:
    print("\n1. Create File")
    print("2. Delete File")
    print("3. Recover File")
    print("4. Show Disk")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("File name: ")
        size = int(input("Size: "))
        fs.create_file(name, size)

    elif choice == "2":
        name = input("File name: ")
        fs.delete_file(name)

    elif choice == "3":
        name = input("File name: ")
        fs.recover_file(name)

    elif choice == "4":
        disk.show_disk()

    elif choice == "5":
        break
def generate_report(fs):
    with open("report.txt", "w") as f:
        f.write("Files:\n")
        f.write(str(fs.files) + "\n")

        f.write("\nDeleted Files:\n")
        f.write(str(fs.deleted_files) + "\n")