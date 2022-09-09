def list_sorted(arr, reverse='Asc'):

    if reverse == 'Desc':
        sorted_numbers = sorted(arr, reverse=True)
        return sorted_numbers
    elif reverse == 'Asc':
        sorted_numbers = sorted(arr, reverse=False)
        return sorted_numbers
    else:
        return 'Error: Second parameter must start with capital letter, i.e: Asc or Desc'
pass

numbers = [2, 4, 6, 8, 9]
print(list_sorted(numbers, 'Desc'))