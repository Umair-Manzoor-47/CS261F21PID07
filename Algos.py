class Selection:
    def Ascending(self, A, entry):
        n = len(A)       # length            
        for idx in range(n-1):        
            min = idx         
            for j in range(idx+1, n):
                if A[j][entry] <= A[min][entry]: # smaller element found 
                    min = j        # store index
            if min != idx:         # swap             
                A[idx], A[min]= A[min], A[idx]

        return A 

    def Descending(self, A, entry):
        n = len(A)       # length            
        for idx in range(n-1):        
            min = idx         
            for j in range(idx+1, n):
                if A[j][entry] >= A[min][entry]: # greater element found 
                    min = j        # store index
            if min != idx:         # swap             
                A[idx], A[min]= A[min], A[idx]

        return A 

class Insertion:   
    def Ascending(self, A, col):
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

    def Descending(self, A, col):
        
        for i in range(1, len(A)):
            key = A[i] # current is key
            j = i - 1 # precedent idx
        
            while j >= 0 and A[j][col] < key[col]: # down-to loop
                # til previous is smaller than current
                A[j+1] = A[j]                      # put previous next to current
                j = j - 1                          # decrease index 
            
            # put current to its place 
            A[j+1] = key

        return A


class Bubble:
    def Ascending(self, A, entry):
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

    def Descending(self, A, entry):
        n = len(A)  # length of Array
        for i in range(n-1): 
            swaped = False   # flag
            for j in range(n-1):
                if A[j][entry] <= A[j+1][entry]:
                    # swap with next element
                    A[j], A[j+1]= A[j+1], A[j]
                    swaped = True
                        
            # if not swaped then list is in order
            if swaped == False :
                    break
 
        return A



class Merge:

    def Ascending(self, A, col, l, r):
        # BASE CASE
        if l < r:  
            m = int(l + (r-l)/2)
            self.Ascending(A, col, l, m)
            self.Ascending(A, col, m+1, r)
            self.Merge_asc(A, l, m, r, col)


    def Merge_asc(self, A, l, m, r, col): 
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

    def Descending(self, A, col, l, r):
        # BASE CASE
        if l < r:  
            m = int(l + (r-l)/2)
            self.Descending(A, col, l, m)
            self.Descending(A, col, m+1, r)
            self.Merge_desc(A, l, m, r, col)
        

    def Merge_desc(self, A, l, m, r, col): 
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
            if L[i][col] >= R[j][col]: 
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

class Quick:   

    def Ascending(self, A, col, l, h):
        # base case if array length is greater than 1 
        if (l < h):
            # partition index
            pi = self.partition_asc(A, l, h, col)
            # recursions for sublists
            self.Ascending(A, col, l, pi - 1)
            self.Ascending(A, col, pi + 1, h)


    def partition_asc (self, A, l, h, col):
        pivot = A[h] # last element as pivot
        i = (l - 1) # start from lowest index

        # till highest index
        for j in range(l,h):

            if (A[j][col] < pivot[col]): # compare with pivot
                i += 1                   # if less then increase index 
                A[i], A[j] = A[j], A[i]  # swap 
        
        A[i + 1],A[h]=A[h],A[i + 1] # put pivot to its right position
                                    
        return (i + 1)     # return pivot index
    
    def Descending(self, A, col, l, h):
        # base case if array length is greater than 1 
        if (l < h):
            # partition index
            pi = self.partition_desc(A, l, h, col)
            # recursions for sublists
            self.Descending(A, col, l, pi - 1)
            self.Descending(A, col, pi + 1, h)


    def partition_desc (self, A, l, h, col):
        pivot = A[h] # last element as pivot
        i = (l - 1) # start from lowest index

        # till highest index
        for j in range(l,h):

            if (A[j][col] > pivot[col]): # compare with pivot
                i += 1                   # if greater then increase index 
                A[i], A[j] = A[j], A[i]  # swap 
        
        A[i + 1],A[h]=A[h],A[i + 1] # put pivot to its right position
                                    
        return (i + 1)     # return pivot index
    
       

class Shell:

    def Ascending(self, A, col):
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
        
        return A


    def Descending(self, A, col):
        # calculate gap (floor division)
        jump = len(A) // 2

        # if list isn't one element 
        while jump > 0:
            
            i = 0         # indexes
            j = jump

            # while gap is less than length of list
            while j < len(A):

                if A[i][col] < A[j][col]:  
                    A[i], A[j] = A[j], A[i] # swap if A[i][col] is greater             
                i += 1
                j += 1
                k = i
                while k - jump > -1:  # downto loop till 0
                    if A[k - jump][col] < A[k][col]:
                        A[k - jump], A[k] = A[k], A[k - jump]
                    k -= 1
            
            jump = jump // 2 # reducing gap

        return A

class Cocktail:

    def Ascending(self, A, col):
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
    
    def Descending(self, A, col):
        last  = len(A) - 1 # len
        swap = True
        first = 0
        while swap:
            swap = False #in case array is sorted
    
            # Left to Right
            for idx in range(first, last):

                if (A[idx] [col] < A[idx + 1][col]): # if greater 
                    A[idx], A[idx + 1] = A[idx + 1], A[idx] # swap
                    swap = True

            # swapping doesn't occur then array is already sorted and break 
            if swap != True:
                break
            
            # now to proceed from right to left (Down-to loop)
            swap = False

            last = last-1 # last number is at its position

            for k in range(last-1, first-1, -1):

                if (A[k][col] < A[k + 1][col]): # if less 
                    A[k], A[k + 1] = A[k + 1], A[k] # swap to previous
                    swap = True 
            first = first + 1 # first is at its position move to next
        
        return A 

class Brick:

    def Ascending(self, A, col):
        n = len(A)
        # Initially array is unsorted
        sorted = False

        while sorted == False: # till array is sorted
            # lets say array is sorted then No condition will run and termination occurs 
            sorted = True 

            for idx in range(1, n-1, 2): # Odd incrementation

                if A[idx][col] > A[idx+1][col]: # swap if current entry is less 
                    A[idx], A[idx+1] = A[idx+1], A[idx]
                    sorted = False
                    
            for idx in range(0, n-1, 2): # Even incrementation
                if A[idx][col] > A[idx+1][col]:
                    A[idx], A[idx+1] = A[idx+1], A[idx]
                    sorted = False
        
        return A

    def Descending(self, A, col):
        n = len(A)
        # Initially array is unsorted
        sorted = False

        while sorted == False: # till array is sorted
            # lets say array is sorted then No condition will run and termination occurs 
            sorted = True 

            for idx in range(1, n-1, 2): # Odd incrementation

                if A[idx][col] < A[idx+1][col]: # swap if current entry is greater
                    A[idx], A[idx+1] = A[idx+1], A[idx]
                    sorted = False
                    
            for idx in range(0, n-1, 2): # Even incrementation
                if A[idx][col] < A[idx+1][col]:
                    A[idx], A[idx+1] = A[idx+1], A[idx]
                    sorted = False
        
        return A