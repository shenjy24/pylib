from mathlib.draw3d import *


def test_draw3d():
    draw3d(
        Points3D((2, 2, 2), (1, -2, -2)),
        Arrow3D((2, 2, 2)),
        Arrow3D((1, -2, -2)),
        Segment3D((2, 2, 2), (1, -2, -2))
    )


if __name__ == '__main__':
    print(matplotlib.__version__)
    test_draw3d()
