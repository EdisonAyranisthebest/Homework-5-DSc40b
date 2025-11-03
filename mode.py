def mode(numbers):
    
    if not numbers:
        return None
    
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    
    max_freq = 0
    mode_value = None
    
    for num, freq in frequency.items():
        if freq > max_freq:
            max_freq = freq
            mode_value = num
    
    return mode_value