def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    a_t=[]

    for i in range(len(a[0])):
        a_t.append([])

    for i in range(len(a)):
        for j in range(len(a[0])):
            a_t[j].append(a[i][j])

    return a_t
