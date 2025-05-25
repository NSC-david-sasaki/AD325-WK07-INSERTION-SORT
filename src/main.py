

def insertion_sort(numbers:int) -> None:
    """Sort a list of integers in-place using insertion sort algorithm.
    
    Args:
        numbers: A list of integers to be sorted in-place
        
    Returns:
        None - the input list is modified in-place
        
    Examples:
        >>> nums = [64, 34, 25, 12, 22, 11, 90]
        >>> insertion_sort(nums)
        >>> print(nums)
        [11, 12, 22, 25, 34, 64, 90]
    """
    for i in range(1, len(numbers)):
        current = numbers[i]
        position = i - 1
        
        # Shift elements right while they're greater than current
        while position >= 0 and numbers[position] > current:
            numbers[position + 1] = numbers[position]
            position -= 1
            
        numbers[position + 1] = current