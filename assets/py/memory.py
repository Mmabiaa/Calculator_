# memory.py

class Memory:
    def _init_(self):
        self.value = 0

    def add(self, amount):
        """Add amount to memory."""
        self.value += amount

    def subtract(self, amount):
        """Subtract amount from memory."""
        self.value -= amount

    def recall(self):
        """Return the current value in memory."""
        return self.value

    def clear(self):
        """Clear the memory."""
        self.value = 0