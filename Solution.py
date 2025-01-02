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
