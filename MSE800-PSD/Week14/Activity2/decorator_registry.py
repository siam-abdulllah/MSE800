"""Registering decorated objects to an API."""

from __future__ import print_function  # Makes print() a function in Python 2.x

registry = {}  # Empty dictionary to store registered functions and classes by name


def register(obj):
    """Decorator: add function or class to registry, return unchanged."""
    registry[obj.__name__] = obj  # Store object using its name as the dictionary key
    return obj  # Return the original object (not a wrapper function)


@register  # Equivalent to: spam = register(spam)
def spam(x):
    return x ** 2  # Return x squared


@register  # Equivalent to: ham = register(ham)
def ham(x):
    return x ** 3  # Return x cubed


@register  # Equivalent to: Eggs = register(Eggs)
class Eggs:
    def __init__(self, x):
        self.data = x ** 4  # Store x to the power of 4 as instance data

    def __str__(self):
        return str(self.data)  # Return data as a string when print() is called


def main():
    print("Registry:")
    for name in registry:  # Loop over each key (name) in the dictionary
        print(name, "=>", registry[name], type(registry[name]))  # Show name, object, and type

    print("\nManual calls:")
    print(spam(2))  # Call spam directly: 2 ** 2 = 4
    print(ham(2))   # Call ham directly: 2 ** 3 = 8
    x = Eggs(2)     # Create an Eggs instance: data = 2 ** 4 = 16
    print(x)        # Uses __str__ to print "16"

    print("\nRegistry calls:")
    for name in registry:  # Loop over registered names
        print(name, "=>", registry[name](2))  # Look up and call each object with argument 2


if __name__ == "__main__":  # Run main() only when this file is executed directly
    main()
