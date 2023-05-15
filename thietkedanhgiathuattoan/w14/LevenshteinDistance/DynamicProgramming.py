# Chương trình Levenshtein distance đo sự khác biệt giữa hai xâu ký tự bằng quy hoạch động và in ra bảng động.

# In[1]:

def print_matrix(matrix, s1, s2):
    m = len(s1)
    n = len(s2)
    print('      ', end='')
    for j in range(n):
        print(s2[j], ' ', end='')
    print()
    for i in range(m + 1):
        if i > 0:
            print(s1[i - 1], ' ', end='')
        else:
            print('  ', end='')
        for j in range(n + 1):
            print(matrix[i][j], ' ', end='')
        print()


def levenshtein_distance_steps(s1, s2):
    m = len(s1)
    n = len(s2)
    # Initialize matrix
    matrix = [[0 for x in range(n + 1)] for y in range(m + 1)]
    for i in range(m + 1):
        matrix[i][0] = i
    for j in range(n + 1):
        matrix[0][j] = j
    # Fill matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:  # s1[i] == s2[j]
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j - 1] + 1,  # Substitute
                                   matrix[i - 1][j] + 1,  # Insert
                                   matrix[i][j - 1] + 1)  # Delete
    print_matrix(matrix, s1, s2)
    # Print steps
    i = m
    j = n
    while i > 0 or j > 0:
        if i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] and s1[i - 1] == s2[j - 1]:
            print('No operation')
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and matrix[i][j] == matrix[i - 1][j - 1] + 1:
            print('Substitute', s1[i - 1], 'by', s2[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + 1:
            print('Delete', s1[i - 1])
            i -= 1
        else:
            print('Insert', s2[j - 1])
            j -= 1

import time

start_time = time.time()
str1 = "kittenabcdedfghijklmnopqrstuvwzjghtgx"
str2 = "sittingcabdedfghijklmnopqrstuvwxydsvsaz"
print(levenshtein_distance_steps(str1, str2))
print("--- %s seconds ---" % (time.time() - start_time))
