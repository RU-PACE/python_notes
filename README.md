# Python Important Concepts

This repository contains explanations and Python code examples of essential programming concepts that every Python developer should know.

## Table of Contents

1. **Decorators**
2. **Iterators**
3. **List Comprehension**
4. **Lambda Functions**
5. **Cache (functools.lru_cache)**
6. **map(), filter(), and reduce()**
7. **abs() Function**
8. **args and kwargs (*args, **kwargs)**
9. **range vs xrange**
10. **Generators & yield**
11. **split() and join()**
12. **Deep and Shallow Copying**
13. **Garbage Collection**
14. **append() vs extend()**
15. **Mutable vs Immutable Objects**
16. **Type Hinting in Python**
17. **Metaclasses**
18. **Global, Local, and Nonlocal Variables**
19. **Walrus Operator (:=)**
20. **Context Managers (with statement)**
21. **Python Memory Management**
22. **Dataclasses**
23. **Multithreading vs Multiprocessing**
24. **AsyncIO (Asynchronous Programming)**
25. **Python Modules and Packages**
26. **Duck Typing in Python**
27. **Python’s __slots__**
28. **Virtual Environments and Dependency Management**
29. **Unit Testing in Python**
30. **Logging in Python**
31. **zip() Function**
32. **Exception Handling (try, except, finally)**
---

## 1. Decorators

Decorators allow modifying functions dynamically.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something before the function runs")
        result = func(*args, **kwargs)
        print("Something after the function runs")
        return result
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

---

## 2. Iterators

Iterators allow looping over custom objects.

```python
class MyIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value

nums = MyIterator([1, 2, 3, 4])
for num in nums:
    print(num)
```

---

## 3. List Comprehension

List comprehension is a concise way to create lists.

```python
squares = [x**2 for x in range(10)]
print(squares)
```

---

## 4. Lambda Functions

Lambda functions are anonymous functions in Python.

```python
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
```

---

## 5. Cache (functools.lru_cache)

Used for caching function results to improve performance.

```python
from functools import lru_cache

@lru_cache(maxsize=3)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))
```

---

## 6. map(), filter(), and reduce()

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]

# map function
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # [1, 4, 9, 16, 25]

# filter function
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]

# reduce function
sum_all = reduce(lambda x, y: x + y, nums)
print(sum_all)  # 15
```

---

## 7. abs() Function

```python
print(abs(-10))  # 10
print(abs(3.5))  # 3.5
```

---

## 8. *args and **kwargs

```python
def func(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

func(1, 2, 3, name="Python", age=30)
```

---

## 9. range vs xrange

In Python 3, `range()` is optimized, and `xrange()` is removed.

```python
for i in range(5):
    print(i)
```

---

## 10. Generators & yield

```python
def my_generator():
    for i in range(3):
        yield i

for val in my_generator():
    print(val)
```

---

## 11. split() and join()

```python
text = "Hello, world!"
words = text.split()
print(words)  # ['Hello,', 'world!']

joined = "-".join(words)
print(joined)  # "Hello,-world!"
```

---

## 12. Deep and Shallow Copying

```python
import copy

list1 = [[1, 2], [3, 4]]
shallow_copy = list1.copy()
deep_copy = copy.deepcopy(list1)
```

---

## 13. Garbage Collection

Python manages memory automatically, but you can manually invoke it.

```python
import gc
gc.collect()
```

---

## 14. append() vs extend()

```python
list1 = [1, 2, 3]
list1.append([4, 5])
print(list1)  # [1, 2, 3, [4, 5]]

list1.extend([6, 7])
print(list1)  # [1, 2, 3, [4, 5], 6, 7]
```

---

## 15. Mutable vs Immutable Objects

```python
tuple1 = (1, 2, 3)  # Immutable
list1 = [1, 2, 3]  # Mutable
```

---

## Conclusion
This repository provides fundamental and advanced Python concepts with practical examples. Happy Coding! 🚀

