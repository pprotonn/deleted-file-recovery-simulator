# file_system.py

class FileSystem:
    def __init__(self, disk):
        self.disk = disk
        self.files = {}
        self.deleted_files = {}

    def create_file(self, name, size):
        free_blocks = [i for i, b in enumerate(self.disk.blocks) if b == "FREE"]

        if len(free_blocks) < size:
            print("Not enough space!")
            return

        allocated = free_blocks[:size]

        for i in allocated:
            self.disk.blocks[i] = name

        self.files[name] = allocated
        print(f"File '{name}' created")

    def delete_file(self, name):
        if name not in self.files:
            print("File not found!")
            return

        blocks = self.files.pop(name)

        for i in blocks:
            self.disk.blocks[i] = "FREE"

        self.deleted_files[name] = blocks
        print(f"File '{name}' deleted")

    def recover_file(self, name):
        if name not in self.deleted_files:
            print("No such deleted file!")
            return

        blocks = self.deleted_files[name]

        # Check if blocks still free
        for i in blocks:
            if self.disk.blocks[i] != "FREE":
                print("Recovery failed! Data overwritten")
                return

        for i in blocks:
            self.disk.blocks[i] = name

        self.files[name] = blocks
        del self.deleted_files[name]

        print(f"File '{name}' recovered")