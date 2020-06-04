def has_negatives(a):
    # dict to hold all nums in a
    storage = {}
    # arr to return matches in absolute value(result)
    result = []
    for num in a:
        # if the num has a corresponding number in dict
        if storage.get(abs(num)): # .get method returns the value for the given key
            result.append(abs(num)) # if so add to results list
        else:
            # if no val is found pass num a new key along with its value
            storage[abs(num)] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
