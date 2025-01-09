def delayed_delete(input_str, operations):
    # Convert the input string to a list for mutability
    chars = list(input_str)
    delays = [0] * len(chars)  # Track delays for each character (None = no delay)
    
    for index, delay in operations:
        delays[index] = delay
        
    maximum_delay = max(delays)
    
    while maximum_delay > 0:
        
        delays = [(delay - 1) for delay in delays]
        
        for i in range(len(chars)-1, -1,-1):
            
            if delays[i] == 0:
                print(chars)
                chars.pop(i)
                delays.pop(i)
                
        maximum_delay -=1
            
    # Convert the remaining list of characters back to a string
    return ''.join(chars)
    
print(delayed_delete('hello',[[0,1],[1,2],[4,1]]))
