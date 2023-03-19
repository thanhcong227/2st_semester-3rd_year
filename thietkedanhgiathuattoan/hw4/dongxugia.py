# Bài toán tìm đồng xu giả (Fake Coin problem) bằng đệ quy chia để trị

import random

def fake_coin(coins):
    # Hàm trả về vị trí của đồng xu giả
    # coins là một mảng các số nguyên
    # Mỗi số nguyên tương ứng với một đồng xu
    # Nếu số âm thì đồng xu đó nặng hơn đồng xu giả
    # Nếu số dương thì đồng xu đó nhẹ hơn đồng xu giả
    # Nếu số bằng 0 thì đồng xu đó là đồng xu giả
    return fake_coin_rec(coins, 0, len(coins) - 1)

def fake_coin_rec(coins, left, right):
    # Hàm trả về vị trí của đồng xu giả trong mảng coins[left:right+1]
    # Nếu không có đồng xu giả thì trả về -1
    if left == right:
        return -1
    if right - left == 1:
        if coins[left] == 0:
            return left
        elif coins[right] == 0:
            return right
        else:
            return -1
    mid = (left + right) // 2
    left_sum = sum(coins[left:mid+1])
    right_sum = sum(coins[mid+1:right+1])
    if left_sum < right_sum:
        return fake_coin_rec(coins, left, mid)
    elif left_sum > right_sum:
        return fake_coin_rec(coins, mid+1, right)
    else:
        return -1

def main():
    # Tạo một mảng gồm 100 đồng xu
    coins = [1] * 100
    # Chọn ngẫu nhiên một đồng xu để làm đồng xu giả
    fake = random.randint(0, 99)
    coins[fake] = 0
    # Tìm vị trí của đồng xu giả
    fake = fake_coin(coins)
    print("Đồng xu giả ở vị trí", fake)

main()

