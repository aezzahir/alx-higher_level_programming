#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """Multiplies two matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not any(m_a) or not m_b or not any(m_b):
        raise ValueError(
            "m_a can't be empty" if not m_a or not any(m_a)
            else "m_b can't be empty"
        )

    for row in m_a:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_b should contain only integers or floats")

    row_size_m_a = len(m_a[0])
    if not all(len(row) == row_size_m_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    row_size_m_b = len(m_b[0])
    if not all(len(row) == row_size_m_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if row_size_m_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            sum_val = 0
            for k in range(len(m_b)):
                sum_val += m_a[i][k] * m_b[k][j]
            row_result.append(sum_val)
        result.append(row_result)

    return result
