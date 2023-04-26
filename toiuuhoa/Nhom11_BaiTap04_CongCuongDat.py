"""
    Nhóm 11: Bài tập 04
    Thành viên:     Lê Thành Công - 20000530 - K65TT
                    Lã Mạnh Cường - 20000532 - K65TT
                    Nguyễn Tiến Đạt - 20000542 - K65TT

    Đề bài: Xây dựng một thuật toán (thể hiện bằng mã giả hoặc code Python)
    để tìm giá trị N lớn nhất để tồn tại cách tô màu trong bài toán Color(N, 2).
    Gợi ý: thuật toán sẽ gồm việc giải nhiều mô hình với các giá trị N khác nhau.
"""

from pulp import *


def find_max_n():
    max_n = 0
    while True:
        # Khởi tạo mô hình tối ưu
        model = LpProblem(name="coloring", sense=LpMaximize)

        # Khởi tạo biến quyết định
        colors = LpVariable.dicts("color", range(1, max_n + 1), cat="Binary")

        # Thêm ràng buộc
        for i in range(1, max_n - 1):
            for j in range(i + 1, max_n):
                if i + j in range(1, max_n + 1):
                    model += colors[i] + colors[j] <= 1

        # Giải bài toán tối ưu
        model.solve()

        # Nếu mô hình không có lời giải, trả về giá trị N tìm được
        if model.status == LpStatusInfeasible:
            return max_n - 1

        # Nếu mô hình có lời giải, tăng giá trị N lên và tiếp tục tìm kiếm
        max_n += 1


print('N =', find_max_n())