import sys


class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n,m):
        if n < 0:
            raise ValueError("Invalid input")
        if self._size + n > self.capacity:
            raise ValueError("Out of capacity")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError("Invalid input")
        if n > self.capacity:
            raise ValueError("Out of capacity")
        self._size -= n

    @property
    # Getter : is a function for a class that gets some attributes
    def capacity(self):
        return self._capacity

    @capacity.setter
    # Setter: is a function in some class that sets some value
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size


def main():
    cookie_jar = Jar()
    cookie_jar.deposit(int(input("Add cookie: ")),int(input("Add cookies: ")))
    cookie_jar.withdraw(int(input("Eat cookie: ")))
    print(cookie_jar)


if __name__ == "__main__":
    main()
