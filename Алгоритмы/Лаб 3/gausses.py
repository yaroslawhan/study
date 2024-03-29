import copy
def gausses(a, b):
    n = len(a)
    A = copy.deepcopy(a)  
    B = copy.deepcopy(b)  
    
    for i in range(n):
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
                
        A[i], A[max_row] = A[max_row], A[i]
        B[i], B[max_row] = B[max_row], B[i]
        
        for k in range(i+1, n):
            m = A[k][i] / A[i][i]
            B[k] -= m * B[i]
            for j in range(i, n):
                A[k][j] -= m * A[i][j]
                
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = B[i] / A[i][i]
        for k in range(i-1, -1, -1):
            B[k] -= A[k][i] * x[i]
            
    return x