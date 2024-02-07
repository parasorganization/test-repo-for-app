Sure, the following Python code represents a function that recursively sums up the elements of a list:

```python
def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

nums = [1, 2, 3, 4, 5]
print(sum_list(nums))  # Output will be 15
```

This function works by taking the first element in the list and adding it to the sum of the rest of the list. Eventually this recursive calling will consume the whole list and we get our answers. The base case here is an empty list, which returns 0.

User Level Estimation: The user appears to be an Intermediate programmer, as creating recursive functions is typically not a beginner concept. It requires understanding of recursion and basic data structures like lists.

Sentiment Analysis: The sentiment of the user's previous query is neutral.