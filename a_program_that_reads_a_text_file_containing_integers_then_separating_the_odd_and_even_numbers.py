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

        for num in data.split():
            self.numbers.append(int(num))

    def separate_numbers(self):
        for num in self.numbers:
            if num % 2 == 0:
                self.even_numbers.append(num)
            else:
                self.odd_numbers.append(num)
                
