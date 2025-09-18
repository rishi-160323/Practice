def print_matrix_table(matrix):
    # Find maximum row length
    max_cols = max(len(row) for row in matrix)

    # Normalize rows (fill missing with '*')
    normalized = [row + ['*'] * (max_cols - len(row)) for row in matrix]

    # Top border
    border = "+" + "+".join(["---"] * max_cols) + "+"

    print(border)
    for row in normalized:
        row_str = "| " + " | ".join(str(x) for x in row) + " |"
        print(row_str)
    print(border)

input = [[1,1,1,1], 
         [1,0,0,1],
        [1,1,0,1], 
        [1,1,1,1]]


def print_matrix_table_decorator(func):
    def wrapper(*args, **kwargs):
        print("+===============Before Solving the problem===============+")
        print_matrix_table(*args, **kwargs)
        result = func(*args, **kwargs)
        print("+===============After Solving the problem===============+")
        print_matrix_table(result)
    return wrapper

