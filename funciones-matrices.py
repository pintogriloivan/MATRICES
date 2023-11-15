def count_columns(m):
    """
    Count the number of columns in a matrix.

    Parameters:
        - m (list of lists): The input matrix.

    Returns:
        - int: The number of columns in the matrix. Returns 0 if the matrix is empty.
    """
    # Check if the matrix is not empty
    if m:
        # Return the number of columns in the first row
        return len(m[0])
    else:
        # Return 0 for an empty matrix
        return 0


def can_be_multiplied(m1, m2):
    """
        Check if two matrices can be multiplied.

        Parameters:
        - m1 (list of lists): The first matrix.
        - m2 (list of lists): The second matrix.

        Returns:
        - bool: True if the number of columns in m1 is equal to the number of rows in m2,
                indicating that the matrices can be multiplied. False otherwise.
        """
    if count_columns(m1) == len(m2):
        return True
    else:
        return False


def product(m1, m2):
    """
    Multiply two matrices.

    Parameters:
        - m1 (list of lists): The first matrix.
        - m2 (list of lists): The second matrix.

    Returns:
        - list of lists or False: If the matrices can be multiplied, the function returns
            a new matrix that is the result of the multiplication. If the matrices cannot be
            multiplied, it prints an error message and returns False.
    """
    if can_be_multiplied(m1, m2):
        # Initialize an empty list to store the result of the multiplication
        res = []
        rows_m1 = len(m1)

        # Iterate over each row in the first matrix
        for a in m1:
            # Initialize an empty list to store the elements of the resulting row
            res_aux = []
            i = 0

            # Perform the matrix multiplication
            while i < rows_m1:
                e = 0
                j = 0
                # Calculate the dot product of the current row of m1 and column of m2
                while j <= rows_m1:
                    e = e + a[j] * m2[j][i]
                    j = j + 1
                i = i + 1
                res_aux.append(e)
            res.append(res_aux)

        # Return the resulting matrix
        return res
    else:
        print("Las matrices no se pueden multiplicar.")
        return False



m1 = ((2, 3, 5), (7, 2, 4))
m2 = ((1, 6), (7, 2), (0, 5))

print(product(m1, m2)) # Res = [[23, 43], [21, 66]]

m3 = ((2, 3, 5, 1), (7, 2, 4, 2), (4, 5, 2, 7))
m4 = ((1, 6, 2), (7, 2, 7), (0, 5, 4), (5, 3, 0))
print(product(m3, m4)) # Res = [[28, 46, 45], [31, 72, 44], [74, 65, 51]]