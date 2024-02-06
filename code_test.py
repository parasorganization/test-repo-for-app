Here's how you can write a function that recursively computes the sum of a list in Python:

```python
def recursive_sum(lst):
    # Base case: Empty list
    if not lst:
        return 0
    else:
        # Recursive case: Take the first element and add it to the result of recursive sum on the rest of the list
        return lst[0] + recursive_sum(lst[1:])

# Test the function
numbers = [1, 2, 3, 4, 5]
print(recursive_sum(numbers))  # Output: 15
```

This function works by defining a base case for an empty list (which sum is 0), and a recursive case that takes the first element of the list and adds it to the recursively calculated sum of the rest of the list.

User Level Estimation: The user is a beginner programmer.

Sentiment Analysis: The sentiment of the user's previous query is neutral.