Sure, here's a recursive function for adding two numbers in Python:

```python
def add_recursive(a, b):
    if b == 0:
        return a
    else:
        return add_recursive(a + 1, b - 1)
```

This function takes two arguments, `a` and `b`. The base case of the recursion is when `b` is 0, in which case it simply returns `a` since the addition of `a` and `0` is `a`. 

In the recursive case, it increments `a` by 1 and decrements `b` by 1, and calls itself with these new values. 

This effectively 'transfers' one unit from `b` to `a` on each recursive call, until finally all of `b` has been 'transferred' to `a`, at which point `b` is 0 and `a` is the original sum of `a` and `b`. 

Please note that while this function correctly implements addition, it will not perform very well for large inputs due to the recursive calls, and might even cause a stack overflow error when `b` is a large number. For adding two numbers, using the `+` operator is much more efficient and straightforward.

User Level Estimation: Beginner

Sentiment Analysis: The sentiment of the user's previous query is neutral.