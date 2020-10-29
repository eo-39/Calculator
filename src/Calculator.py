def addition(a, b):
    return a + b
class Calculator:
    result = 0

    def _init_(self):
        x = 2 + 2
        self.result = x;
        pass

    def add(self, a, b):
        self.result = a + b
        return addition(a, b)