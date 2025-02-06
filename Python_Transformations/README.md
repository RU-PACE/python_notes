# List Mapping with Lambda in Python

## Overview
This README explains the use of the `map()` function in Python along with a `lambda` function to square each element in a list. We also compare it with list comprehension for better understanding.

## Syntax
```python
list(map(lambda x: x**2, numbers))
```

### Breaking it Down:
1. **`map(function, iterable)`**
   - `map()` applies a function to every element in the iterable (`numbers`).
   
2. **`lambda x: x**2`**
   - This is an **anonymous function** (lambda function) that takes an input `x` and returns `x²`.

3. **`numbers`**
   - This is the iterable (e.g., a list of numbers) that `map()` processes.

4. **`list(...)`**
   - `map()` returns a map object (an iterator), so `list()` converts it into a list.

## Example Usage
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
```

### Output:
```
[1, 4, 9, 16, 25]
```

## Alternative Using List Comprehension
The same result can be achieved using list comprehension:
```python
squared_numbers = [x**2 for x in numbers]
```

### Benefits of Each Approach
| Approach                 | Pros                                | Cons                               |
|-------------------------|--------------------------------|--------------------------------|
| `map()` with `lambda`  | Functional programming style  | Less readable for complex logic |
| List Comprehension     | More Pythonic & readable    | Can be less efficient for large datasets |

## Conclusion
Both methods effectively transform a list, but list comprehension is generally preferred for readability. However, `map()` is useful when working with built-in functions or when applying transformations to iterables.

---


