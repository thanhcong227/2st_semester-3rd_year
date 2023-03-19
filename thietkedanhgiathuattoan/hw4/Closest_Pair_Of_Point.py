# Bài toán tìm cặp điểm gần nhất (Closest pair of point) bằng đệ quy chia để trị

# Tìm khoảng cách giữa 2 điểm
def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

# Tìm khoảng cách nhỏ nhất giữa 2 điểm trong 1 mảng
def bruteForce(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            min_dist = min(min_dist, distance(points[i], points[j]))
    return min_dist

# Tìm khoảng cách nhỏ nhất giữa 2 điểm trong 1 mảng
def closestPairOfPoint(points):

    # Sắp xếp theo tọa độ x
    points.sort(key=lambda x: x[0])
    return closestPairOfPointRec(points)

def closestPairOfPointRec(points):

    # Nếu số điểm <= 3 thì dùng thuật toán brute force
    if len(points) <= 3:
        return bruteForce(points)

    # Tìm điểm ở giữa
    mid = len(points) // 2

    # Tìm khoảng cách nhỏ nhất trong 2 nửa
    left = closestPairOfPointRec(points[:mid])
    right = closestPairOfPointRec(points[mid:])
    min_dist = min(left, right)

    # Tìm các điểm trong khoảng cách min_dist
    strip = []
    for i in range(len(points)):
        if abs(points[i][0] - points[mid][0]) < min_dist:
            strip.append(points[i])

    # Tìm khoảng cách nhỏ nhất giữa các điểm trong strip
    strip.sort(key=lambda x: x[1])
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            min_dist = min(min_dist, distance(strip[i], strip[j]))
    return min_dist