class Calculator:
    def __init__(self, number_1: float = 0.0, number_2: float = 0.0):
        """
        Initialize the calculator with two numbers.

        :param number_1: First number for operations.
        :param number_2: Second number for operations.
        """
        self.memory = 0.0
        self._number_1 = number_1
        self._number_2 = number_2

    @property
    def number_1(self) -> 'Calculator':
        return self._number_1

    @number_1.setter
    def number_1(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("number_1 must be an int or float")
        self._number_1 = value

    @property
    def number_2(self) -> 'Calculator':
        return self._number_2

    @number_2.setter
    def number_2(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("number_2 must be an int or float")
        self._number_2 = value

    def add(self) -> 'Calculator':
        self.memory = self._number_1 + self._number_2
        return self

    def subtract(self) -> 'Calculator':
        self.memory = self._number_1 - self._number_2
        return self

    def multiply(self) -> 'Calculator':
        self.memory = self._number_1 * self._number_2
        return self

    def divide(self) -> 'Calculator':
        """
        Divides number_1 by number_2 and stores the result in memory.
        Returns None if number_2 is zero.
        """
        if self._number_2 == 0:
            print("error: division by zero")
            self.memory = None
            return self
        self.memory = self._number_1 / self._number_2
        return self

    def nroot(self) -> 'Calculator':

        if self._number_2 == 0:
            print("error: nroot with zero divisor")
            self.memory = None
            return self
        self.memory = self._number_1 ** (1 / self._number_2)
        return self

    def decision(self, user_decision: str) -> 'Calculator':
        """
        :param user_decision: A string representing the operation ('+', '-', '*', '/').
        """
        if user_decision == '+':
            return self.add()
        elif user_decision == '-':
            return self.subtract()
        elif user_decision == '*':
            return self.multiply()
        elif user_decision == '/':
            return self.divide()
        else:
            raise ValueError("Invalid decision")

    def reset(self) -> 'Calculator':
        """ Resets the memory to zero. """
        self.memory = 0.0
        return self
