# Bridge of Lanka Problem

This project solves the "Bridge of Lanka" problem inspired by the Ramayana. The goal is to find the longest consecutive subsequence of numbers from a given list where the sum of the subsequence is divisible by 5.

## Problem Description
- You are given a list of integers (representing magical stones).
- Your task is to find the **longest consecutive subsequence** where the sum of the numbers is divisible by 5.
- If no such subsequence exists, return an empty list.

### Example
**Input**: `[3, 2, 7, 1, 5]`  
**Output**: `[2, 7, 1]`  
**Explanation**: The sum of `[2, 7, 1]` is 10, which is divisible by 5, and it is the longest such subsequence.

## Solution Overview
The solution uses a brute-force approach:
1. Iterate through all possible consecutive subsequences.
2. Calculate the sum of each subsequence.
3. Check if the sum is divisible by 5.
4. Track the longest subsequence that satisfies the condition.

## Python Implementation
```python
def find_largest_subsequence(stones):
    n = len(stones)
    max_length = 0
    result = []

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += stones[j]
            if current_sum % 5 == 0:
                current_length = j - i + 1
                if current_length > max_length:
                    max_length = current_length
                    result = stones[i:j+1]

    return result

# Example Usage
stones = [3, 2, 7, 1, 5]
result = find_largest_subsequence(stones)
print("Largest subsequence divisible by 5:", result)
```

## How to Run
1. Copy the Python code into a script.
2. Replace the `stones` list with your input values.
3. Run the script to get the output.

## Edge Cases
- Empty list: Return `[]`.
- No subsequence divisible by 5: Return `[]`.
- Single element divisible by 5: Return `[element]`.

### Example Edge Cases
1. Input: `[]` → Output: `[]`
2. Input: `[1, 2, 3]` → Output: `[]`
3. Input: `[5]` → Output: `[5]`

---

