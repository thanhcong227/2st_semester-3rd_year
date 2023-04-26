# Khớp xâu: Tìm các vị trí xuất hiện của xâu mẫu P trong văn bản T cho trước bằng phương pháp brute force.

def brute_force_matcher(T, P):
    n = len(T)
    m = len(P)
    for s in range(n - m + 1):
        if P == T[s:s + m]:
            print("Pattern occurs with shift", s)


brute_force_matcher('abab', 'ab')
