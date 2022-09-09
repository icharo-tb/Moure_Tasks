def list_sorted(arr, reverse='Asc'):

    if reverse == 'Desc' or 'desc':
        sorted_numbers = sorted(arr, reverse=True)
        return sorted_numbers
    elif reverse == 'Asc' or 'asc':
        sorted_numbers = sorted(arr, reverse=False)
        return sorted_numbers
    else:
        return 'Error: Second parameter must be Asc/asc or Desc/desc'
pass

numbers = [2, 4, 6, 8, 9]
print(list_sorted(numbers, 'desc'))