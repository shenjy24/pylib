# 线性代数工具类
from math import sin, cos, pi, atan2, sqrt


# 极坐标转换为笛卡尔坐标
def to_cartesian(polar_vector):
    length, angle = polar_vector[0], polar_vector[1]
    return (length * cos(angle), length * sin(angle))


# 笛卡尔坐标转极坐标
def to_polar(vector):
    x, y = vector[0], vector[1]
    # 反正切函数，得到弧度
    angle = atan2(y, x)
    return (length((x, y)), angle)


# 获取从原点到坐标的距离
def length(vector):
    x, y = vector[0], vector[1]
    return sqrt(x ** 2 + y ** 2)


# 多维向量的长度
def length_multi(v):
    return sqrt(sum([coord ** 2 for coord in v]))


# 计算点积
def dot(u, v):
    return sum([coord1 * coord2 for coord1, coord2 in zip(u, v)])
