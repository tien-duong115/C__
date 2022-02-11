def pascal_tri(n):
    
    result = [[1]]
    
    
    for i in range(n - 1):
        temp_list = [0] + result[-1] + [0]
        
        new_array = []
        
        for ele in range(len(result[-1]) + 1):
            new_array.append(temp_list[ele] + temp_list[ele + 1])
        result.append(new_array)
    return result


def pascal_recursive(n):
    
    if n == 0:
        return [1]
    
    else:
        new_line = [1]
        
        previous_line = pascal_recursive(n -1)
        for i in range(len(previous_line) - 1):
            new_line.append(previous_line[i] + previous_line[i+1])
        new_line+=[1]
    return new_line
print(pascal_recursive(5))
