# Bài toán tìm bao lồi (Convex-Hull problem) bằng đệ quy chia để trị

import math

import math

def orientation(p, q, r):
    # Hàm tính hướng của đoạn thẳng tạo bởi p, q, r
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def convex_hull(points):
    # Sắp xếp danh sách điểm theo tọa độ y tăng dần
    points = sorted(points, key=lambda x: x[1])

    n = len(points)
    # Tìm điểm bên trái nhất và phải nhất
    left_most = points[0]
    right_most = points[-1]

    # Khởi tạo danh sách bao lồi
    hull = [left_most]

    # Xây dựng bao lồi với các điểm bên phải
    idx = points.index(left_most)
    i = idx
    while i != n-1:
        i = (i + 1) % n
        if orientation(left_most, points[i], right_most) == 2:
            hull.append(points[i])

    # Xây dựng bao lồi với các điểm bên trái
    j = idx
    while j != 0:
        j = (j - 1) % n
        if orientation(left_most, points[j], right_most) == 2:
            hull.append(points[j])

    # Loại bỏ điểm cuối cùng trong danh sách bao lồi nếu nó không thuộc bao lồi
    if len(hull) > 2 and hull[-1] == hull[0]:
        hull.pop()

    return hull

def main():
    # Danh sách các điểm
    points = [(0, 3), (2, 2), (1, 1), (2, 1), (3, 0), (0, 0), (3, 3)]

    # Tìm bao lồi
    hull = convex_hull(points)

    # In ra kết quả
    print('Danh sách các điểm:', points)
    print('Danh sách các điểm thuộc bao lồi:', hull)
