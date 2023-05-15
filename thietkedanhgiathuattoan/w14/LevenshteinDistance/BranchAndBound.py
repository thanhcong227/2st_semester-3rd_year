# Chương trình Levenshtein distance đo sự khác biệt giữa hai xâu ký tự bằng branch and bound.

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


# Chương trình giải bài toán Levenshtein distance bằng đệ quy

def levenshtein_distance_recursive(str1, str2):
    # Base cases
    if len(str1) == 0:
        return len(str2)
    if len(str2) == 0:
        return len(str1)

    # If the last characters are the same, no operation needed
    if str1[-1] == str2[-1]:
        return levenshtein_distance_recursive(str1[:-1], str2[:-1])

    # Otherwise, perform substitution, insertion, and deletion
    substitute = levenshtein_distance_recursive(str1[:-1], str2[:-1])
    insert = levenshtein_distance_recursive(str1, str2[:-1])
    delete = levenshtein_distance_recursive(str1[:-1], str2)

    # Return the minimum of the three operations plus 1
    return min(substitute, insert, delete) + 1


import time

start_time = time.time()
str1 = "kittenabcdedfghijklmnopqrstuvwzjghtgx"
str2 = "sittingcabdedfghijklmnopqrstuvwxydsvsaz"
distance = levenshtein_distance_recursive(str1, str2)
print(distance)
print("--- %s seconds ---" % (time.time() - start_time))

