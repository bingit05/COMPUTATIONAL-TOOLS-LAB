class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.series = []

    def generate(self):
        a = 0
        b = 1

        if self.n <= 0:
            print("Please enter a positive integer")
        else:
            for i in range(self.n):
                self.series.append(a)
                c = a + b
                a = b
                b = c

            print("Fibonacci series:")

            for num in self.series:
                print(num, end=" ")


n = int(input("Enter the number of terms: "))

fib = Fibonacci(n)
fib.generate()
