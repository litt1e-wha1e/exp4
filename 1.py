# 费马因数分解法
# 用于当两个素因数 p 和 q 之间相差较小时，快速分解模数 N。
def fermat_factorization(N):
    import math
    a = math.isqrt(N) + 1  # 从 sqrt(N) 向上开始搜索
    b2 = a * a - N  # b^2 = a^2 - N
    while not math.isqrt(b2)**2 == b2:  # 检查 b^2 是否为完全平方数
        a += 1
        b2 = a * a - N
    b = math.isqrt(b2)
    p = a + b
    q = a - b
    return p, q

# 测试费马因数分解法
N = 10403  # 示例模数
p, q = fermat_factorization(N)
print(f"费马因数分解法结果: p={p}, q={q}")

# Pollard p-1 分解法
# 用于当素因数 p 的 p-1 是 B-smooth 数时。
def pollard_p_minus_1(N, B=1000):
    from math import gcd
    a = 2
    for j in range(2, B + 1):
        a = pow(a, j, N)  # 计算 a^j mod N
        d = gcd(a - 1, N)  # 求最大公因数
        if 1 < d < N:
            return d, N // d  # 找到一个因子
    return None, None  # 如果未能找到因子，返回 None

# 测试 Pollard p-1 分解法
N = 10403  # 示例模数
p, q = pollard_p_minus_1(N)
if p and q:
    print(f"Pollard p-1 分解法结果: p={p}, q={q}")
else:
    print("Pollard p-1 分解法未找到因子")
