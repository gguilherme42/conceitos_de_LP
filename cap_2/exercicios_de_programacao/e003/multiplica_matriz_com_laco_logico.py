class Matrix(): 
    def __init__(self, matrix: list[list[int]]) -> None:
        self.columns = len(matrix[0]) if matrix else 0 
        self.lines = len(matrix)
        self.elements = matrix
    

matrix_A = Matrix([[2, 3, 1],
            [-1, 0, 2]])

matrix_B = Matrix([ [1,-2],
                    [0,5],
                    [4, 1],])



def multiply_matrix(a: Matrix, b: Matrix) -> Matrix:
    result =[]
    if a.lines == b.columns:
        for i in range(a.lines):
            new_elements = []
            for p in range(b.columns):
                product = 0
                for j in range(a.columns):
                    product += a.elements[i][j] * b.elements[j][p]
                new_elements.append(product)



                  

            result.append(new_elements)

                

        return Matrix(result)

matrix_to_assert = multiply_matrix(matrix_A, matrix_B)

assert matrix_to_assert.elements == Matrix([[6,12], [7,4]]).elements

print(matrix_to_assert.elements)
assert f"{matrix_to_assert.columns}x{matrix_to_assert.lines}" == "2x2"
