"""
Demonstration of differences between Iterators and Generators in Python
"""

# 1. Iterator Example
class NumberIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter >= self.limit:
            raise StopIteration
        self.counter += 1
        return self.counter - 1

# 2. Generator Example
def number_generator(limit):
    counter = 0
    while counter < limit:
        yield counter
        counter += 1

# Testing both approaches
if __name__ == "__main__":
    print("1. Using Iterator:")
    numbers_iter = NumberIterator(5)
    for num in numbers_iter:
        print(num, end=' ')
    print("\n")
    
    print("2. Using Generator:")
    numbers_gen = number_generator(5)
    for num in numbers_gen:
        print(num, end=' ')
    print("\n")
    
    # Memory state demonstration
    iterator_obj = NumberIterator(1000000)
    generator_obj = number_generator(1000000)
    
    print("3. Memory/Object Representation:")
    print(f"Iterator object: {iterator_obj}")  # Shows class instance
    print(f"Generator object: {generator_obj}") # Shows generator object
    
    # State management demonstration
    print("\n4. State Management:")
    gen = number_generator(3)
    print(f"First value: {next(gen)}")
    print(f"Second value: {next(gen)}")
    print(f"Third value: {next(gen)}")
    try:
        print(f"Fourth value: {next(gen)}")
    except StopIteration:
        print("Generator exhausted!")