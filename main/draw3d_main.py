from mathlib.draw3d import *


def test_draw3d():
    draw3d(
        Points3D((2, 2, 2), (1, -2, -2)),
        Arrow3D((2, 2, 2)),
        Arrow3D((1, -2, -2)),
        Segment3D((2, 2, 2), (1, -2, -2))
    )


def test_render():
    render(octahedron, color_map=matplotlib.colormaps.get_cmap('Blues'), lines=black)


def test_draw_polyhedron():
    draw_polyhedron(3)


if __name__ == '__main__':
    print(matplotlib.__version__)
    test_render()
    test_draw_polyhedron()
