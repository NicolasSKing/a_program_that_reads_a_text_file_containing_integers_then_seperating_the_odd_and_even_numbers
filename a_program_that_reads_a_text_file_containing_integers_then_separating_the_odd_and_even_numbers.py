class NumberProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.numbers = []
        self.odd_numbers = []
        self.even_numbers = []

    def read_numbers(self):
        file = open(self.filename, "r")
        data = file.read()
        file.close()