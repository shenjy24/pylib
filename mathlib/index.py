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


if __name__ == '__main__':
    a = 37 * pi / 180
    print(to_cartesian((5, a)))

    print(to_polar((1, 0)))
