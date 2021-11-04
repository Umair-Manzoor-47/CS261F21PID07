
def selection_sort(A, entry):
    n = len(A)       # length            
    for idx in range(n-1):        
        min = idx         
        for j in range(idx+1, n):
            if A[j][entry] <= A[min][entry]: # smaller element found 
                min = j        # store index
        if min != idx:         # swap             
            A[idx], A[min]= A[min], A[idx]

        return A 



def bubble_sort(A, entry):
    n = len(A)  # length of Array
    for i in range(n-1): 
        swaped = False   # flag
        for j in range(n-1):
            if A[j][entry] >= A[j+1][entry]:
                # swap with next element
                A[j], A[j+1]= A[j+1], A[j]
                swaped = True
                    
        # if not swaped then list is in order
        if swaped == False :
                break
    return A

def quick_Sort(A, col, l, h):
    # base case if array length is greater than 1 
    if (l < h):
        # partition index
        pi = partition(A, l, h, col)
        # recursions for sublists
        quick_Sort(A, col, l, pi - 1)
        quick_Sort(A, col, pi + 1, h)

def partition (A, l, h, col):
    pivot = A[h] # last element as pivot
    i = (l - 1) # start from lowest index

    # till highest index
    for j in range(l,h):

        if (A[j][col] < pivot[col]): # compare with pivot
            i += 1                   # if less then increase index 
            A[i], A[j] = A[j], A[i]  # swap 
    
    A[i + 1],A[h]=A[h],A[i + 1] # put pivot to its right position
                                
    return (i + 1)     # return pivot index


def Merge_Sort(A, col, l, r):
    # BASE CASE
    if l < r:  
        m = int(l + (r-l)/2)
        Merge_Sort(A, col, l, m)
        Merge_Sort(A, col, m+1, r)
        Merge(A, l, m, r, col)

def Merge(A, l, m, r, col): 
    size_1 = m - l + 1  # size of left array
    size_2 = r - m      # size of right array
    # temporary arrays
    L = []
    R = []
    # copying elements in temporary arrays
    # and checkng if element < 0
    for i in range(0, size_1):
        L.append(A[l + i])

    for j in range(0, size_2):
        R.append(A[m + 1 + j])
    # indexes of temp arrays 
    i = 0 
    j = 0     
    k = l  

    while i < size_1 and j < size_2:
        if L[i][col] <= R[j][col]: 
            # if element is less put to kth index
            A[k] = L[i]  
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    # copying in first Array
    # if some remains
    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1      
    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1
    
def insertion_sort(A, col):
    
    for i in range(1, len(A)):
        key = A[i] # current is key
        j = i - 1 # precedent idx
    
        while j >= 0 and A[j][col] > key[col]: # down-to loop
            # til previous is greater than current
            A[j+1] = A[j]                      # put previous next to current
            j = j - 1                          # decrease index 
        
        # put current to its place 
        A[j+1] = key

    return A


def shell_sort(A, col):
    # calculate gap (floor division)
    jump = len(A) // 2

    # if list isn't one element 
    while jump > 0:
        
        i = 0         # indexes
        j = jump

        # while gap is less than length of list
        while j < len(A):

            if A[i][col] > A[j][col]:  
                A[i], A[j] = A[j], A[i] # swap if A[i][col] is greater             
            i += 1
            j += 1
            k = i
            while k - jump > -1:  # downto loop till 0
                if A[k - jump][col] > A[k][col]:
                    A[k - jump], A[k] = A[k], A[k - jump]
                k -= 1
        
        jump = jump // 2 # reducing gap



def cocktail_Sort(A, col):
    last  = len(A) - 1 # len
    swap = True
    first = 0
    while swap:
        swap = False #in case array is sorted
 
        # Left to Right
        for idx in range(first, last):

            if (A[idx] [col] > A[idx + 1][col]): # if greater 
                A[idx], A[idx + 1] = A[idx + 1], A[idx] # swap
                swap = True

        # swapping doesn't occur then array is already sorted and break 
        if swap != True:
            break
        
        # now to proceed from right to left (Down-to loop)
        swap = False

        last = last-1 # last number is at its position

        for k in range(last-1, first-1, -1):

            if (A[k][col] > A[k + 1][col]): # if less 
                A[k], A[k + 1] = A[k + 1], A[k] # swap to previous
                swap = True 
        first = first + 1 # first is at its position
    
    return A