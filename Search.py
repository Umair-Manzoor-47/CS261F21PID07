import pandas as pd

def LinearSearch(A, col, entry):
    result = []
    for i in range(len(A)):
        if entry == A[i][col]:
            result.append(A[i])

    return result

def starts(A, col, entry):
    result = []
    for i in range(len(A)):
        idx = A[i][col]
        if len(entry) <= len(idx):
            if entry == idx[0: len(entry)]:
                result.append(A[i])
    
    return result

def ends(A, col, entry):
    result = []
    for i in range(len(A)):
        idx = A[i][col]
        
        if len(entry) <= len(idx):
            
            if entry == idx[len(idx) - len(entry) : len(idx)]:
                result.append(A[i])
    
    return result




