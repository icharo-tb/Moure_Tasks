def sets(arr1,arr2,common=True):
    
    if common is True:
        return list(set(arr1).intersection(arr2))
    elif common is False:
        return list(set(arr1)-set(arr2)) + list(set(arr2)-set(arr1))
pass

l1 = [1,2,5,8,3]
l2 = [2,4,6,3,9]
print(sets(l1,l2,common=False))