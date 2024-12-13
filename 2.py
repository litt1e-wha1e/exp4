# 因数碰撞攻击法
# 用于当多个模数 N 之间存在共同因数时。
def factor_collision_attack(moduli):
    from math import gcd
    for i in range(len(moduli)):
        for j in range(i + 1, len(moduli)):
            gcd_value = gcd(moduli[i], moduli[j])
            if gcd_value > 1:  # 找到非平凡因子
                p = gcd_value
                q1 = moduli[i] // p
                q2 = moduli[j] // p
                return (moduli[i], p, q1), (moduli[j], p, q2)
    return None

# 测试因数碰撞攻击法
moduli = [10403, 12307, 10403 * 17]  # 示例模数
result = factor_collision_attack(moduli)
if result:
    for res in result:
        print(f"因数碰撞攻击法结果: N={res[0]}, p={res[1]}, q={res[2]}")
else:
    print("因数碰撞攻击法未找到因子")

# 公共模数攻击法
# 用于当两个密文使用相同的模数 N 但不同的指数加密时。
def common_modulus_attack(N, e1, e2, c1, c2):
    from sympy import gcdex
    # 使用扩展欧几里得算法求解 r, s，使得 r*e1 + s*e2 = 1
    r, s, _ = gcdex(e1, e2)
    if r < 0:
        c1 = pow(c1, -1, N)  # 计算 c1 的模逆
        r = -r
    if s < 0:
        c2 = pow(c2, -1, N)  # 计算 c2 的模逆
        s = -s
    # 计算明文 m
    m = (pow(c1, r, N) * pow(c2, s, N)) % N
    return m

# 测试公共模数攻击法
N = 10403  # 示例模数
e1, e2 = 3, 7  # 示例加密指数
c1, c2 = pow(42, e1, N), pow(42, e2, N)  # 示例密文
m = common_modulus_attack(N, e1, e2, c1, c2)
print(f"公共模数攻击法结果: 明文 m={m}")
