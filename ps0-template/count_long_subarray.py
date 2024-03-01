def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    ##################
    # YOUR CODE HERE #
    ##################
    max_length = 0
    curr_length = 1
    last_x = A[0]
    for x in A[1:]:
        if x > last_x:
            curr_length += 1
            if curr_length > max_length:
                max_length = curr_length
                count = 0
        else:
            if curr_length == max_length:
                count += 1
            curr_length = 1
        last_x = x

    if curr_length == max_length:
        count += 1
    return count
