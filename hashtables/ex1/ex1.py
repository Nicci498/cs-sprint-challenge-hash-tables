def get_indices_of_item_weights(weights, length, limit):
    weight = {}
    dupe_check = False # in order to pass test #2
    duplicates = {} # we need to account for duplicat weights ie: [4,4]
    #loop through weights and store them in the dict
    for i in range(0, length):
        current = weights[i]
        weight[current] = i #set the value to the index
        target = limit - current # we subtract the current value from the limit to find which package combines to equal weight limit
        if target in weight:
            if current > target or current < target:
                return (i, weight[target])
            elif target == current: # if it finds a dupe
                if dupe_check is False:
                    dupe_check = True
                    duplicates[current] = i
                elif dupe_check is True:
                    return (i, duplicates[current])
    return None
print(get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 21))