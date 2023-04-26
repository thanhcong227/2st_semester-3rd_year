# Nhóm 11_Bài tập 02
# Thông tin nhóm
# Thành viên: Lê Thành Công - 20000530 - K65TT
#            Lã Mạnh Cường - 20000532 - K65TT
#            Nguyễn Tiến Đạt - 20000542 - K65TT

# Danh sách bài tập
# - Bài 1.Tọa độ trên bàn cờ
# - Bài 2. Lấy phần tử ngẫu nhiên
# - Bài 3. Lọc phần tử
# - Bài 4. Nước đi của quân hậu

# Bài 1. Tọa độ trên bàn cờ
# Viết một hàm trả về tọa độ của 64 ô trên bàn cờ.
# Viết một hàm tr về tọa độ của 32 ô trắng của bàn ờ
# Viết một hàm in ra tọa độ của tất cả các ô trên bàn cờ

file = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rank = ['1', '2', '3', '4', '5', '6', '7', '8']

cheesboard = [[0 for i in range(8)] for j in range(8)]


def coordinates():
    for i in range(8):
        for j in range(8):
            cheesboard[i][j] = file[j] + rank[i]


def white():
    print("White coordinates on the chessboard")
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                print(cheesboard[i][j], end=" ")
        print()
    print()


def chessboardCoordinates():
    print("All coordinates on the chessboard")
    for i in range(7, -1, -1):
        for j in range(8):
            print(cheesboard[i][j], end=" ")
        print()
    print()


coordinates()
white()
chessboardCoordinates()

# - Bài 2. Lấy phần tử ngẫu nhiên
# Viết một hàm nhận vào một list và trả về một phần tử ngẫu nhiên trong danh sách đó

import random


def randomElement(list):
    return random.choice(list)


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Random element from list: ", randomElement(list))


# - Bài 3. Lọc phần tử
# Viết một hàm nhận vào hai list A, list B và trả về list C chứa các phần tử thuộc A nhưng không thuộc B

def filterList(listA, listB):
    listC = []
    for i in listA:
        if i not in listB:
            listC.append(i)
    return listC


listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listB = [1, 3, 5, 7, 9]
print("List A: ", listA)
print("List B: ", listB)
print("List C: ", filterList(listA, listB))


# - Bài 4. Nước đi của quân hậu
# Quân hậu trong cờ vua di chuyển theo hàng ngang, hàng dọc
# hoặc đường chéo. Viết một hàm nhận vào một tọa độ trên bàn cờ vua thể hiện cho vị trí của một quân hậu và trả về một list những ô mà quân hậu đó có thể di chuyển tới trong một nước đi hợp lệ.

def queenMove(x, y):
    list = []
    rightCrossSum = ord(x)-ord(y)
    leftCrossSum = ord(x)+ord(y)
    for i in range(1, 9):
        if i != y:
            list.append(x + str(i))
    for i in range(1, 9):
        if file[i - 1] != x:
            list.append(file[i - 1] + str(y))
    for i in range(1, 9):
        for j in range(1, 9):
            if ord(file[i - 1]) - ord(rank[j-1]) == rightCrossSum or ord(file[i - 1]) + ord(rank[j-1]) == leftCrossSum:
                list.append(file[i - 1] + str(j))
    if str(x+y) in list:
        list.remove(str(x+y))
    return list


x = input("Enter x: ")
y = input("Enter y: ")
print("Queen can move to: ", queenMove(x, y))
