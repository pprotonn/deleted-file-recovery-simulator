# disk.py

class Disk:
    def __init__(self, size=10):
        self.blocks = ["FREE"] * size

    def show_disk(self):
        for i, block in enumerate(self.blocks):
            print(f"Block {i}: {block}")