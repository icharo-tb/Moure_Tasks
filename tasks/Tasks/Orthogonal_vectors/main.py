def is_orthognal(arr1,arr2):
    # arr must be same lenght
    if len(arr1) != len(arr2) or len(arr2) != len(arr1):
        return f'Error: Arrays must be of the same lenght'
    
    # Formula: a1*b1+a2*b2
    check = (arr1[0]*arr2[0])+(arr1[1]*arr2[1])
    if check != 0:
        return f'The vectors are not orthogonal'
    elif check == 0:
        return f'The vectors are orthogonal'
pass

vector1 = [4,-2]
vector2 = [2,1]
print(is_orthognal(vector1,vector2))