"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """create a start number"""
        self.start = self.sequential = start

    def generate(self):
        """generate the sequential number"""
        self.sequential += 1
        return self.sequential - 1

    def reset(self):
        """reset the number to the original start number"""
        self.sequential = self.start

