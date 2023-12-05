

def fair_sharer(values, num_iterations, share=0.1):
    """Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. Das am weitesten links liegende Feld gilt 
    als Nachbar des am weitesten rechts liegenden Feldes
    
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    
    Args
    values:
        1D array of values (list or numpy array)

    num_iteration:
        Integer to set the number of iterations
    """
    
    for iteration in range(num_iterations):
        max_value = max(values)
        max_index = values.index(max_value)

        shared_value = max_value * share
        values[max_index - 1] += shared_value
        values[max_index + 1] += shared_value
        values[max_index] = max_value - (2 * shared_value)

    return values
    

print(fair_sharer([0, 1000, 800, 0], 1)) #--> [100, 800, 900, 0]
print(fair_sharer([0, 1000, 800, 0], 2)) #--> [100, 890, 720, 90]

