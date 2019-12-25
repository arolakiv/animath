from manimlib.imports import *


class Bisector(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)

        p1 = Sphere()
        p1.scale(0.05)
        p1.set_color(BLACK)
        p1.move_to(np.array([1, 0, 0]))
        self.play(ShowCreation(p1))

        p2 = Sphere()
        p2.scale(0.05)
        p2.set_color(BLACK)
        p2.move_to(np.array([-1, 0, 0]))
        self.play(ShowCreation(p2))

        biPlane = Polygon(
            np.array([0, 4, 4]),
            np.array([0, 4, -4]),
            np.array([0, -4, -4]),
            np.array([0, -4, 4]),
            color=GREEN, fill_color=GREEN, fill_opacity=0.5
        )
        self.play(ShowCreation(biPlane))


class Bitruncated(ThreeDScene):
    def init(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=20 * DEGREES)

        self.vectors = [
            np.array([1, 1, 1]),
            np.array([1, 1, -1]),
            np.array([1, -1, 1]),
            np.array([1, -1, -1]),
            np.array([-1, 1, 1]),
            np.array([-1, 1, -1]),
            np.array([-1, -1, 1]),
            np.array([-1, -1, -1])]

        self.sectors = [None] * 8

    def drawFirstCube(self):
        cube = Cube()
        cube.set_opacity(0.5)
        cube.scale(2)
        self.play(ShowCreation(cube))
        self.wait()

        center = Sphere()
        center.scale(0.1)
        center.set_color(BLACK)
        self.play(ShowCreation(center))
        self.wait()

    def drawHexagons(self):

        point = Sphere()
        point.scale(0.1)
        point.set_color(RED)
        point.move_to(np.array([2, 2, 2]))
        self.play(ShowCreation(point), run_time=0.25)

        hexagon = Polygon(
            np.array([1, 2, 0]),
            np.array([2, 1, 0]),
            np.array([2, 0, 1]),
            np.array([1, 0, 2]),
            np.array([0, 1, 2]),
            np.array([0, 2, 1]),
            color=GREEN, fill_color=GREEN, fill_opacity=0.7)
        self.play(ShowCreation(hexagon))

        sideXY = Polygon(
            np.array([2, 2, 2]),
            np.array([2, 0, 2]),
            np.array([1, 0, 2]),
            np.array([0, 1, 2]),
            np.array([0, 2, 2]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5)
        self.play(ShowCreation(sideXY))

        sideYZ = Polygon(
            np.array([2, 2, 2]),
            np.array([2, 0, 2]),
            np.array([2, 0, 1]),
            np.array([2, 1, 0]),
            np.array([2, 2, 0]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5)
        self.play(ShowCreation(sideYZ))

        sideZX = Polygon(
            np.array([2, 2, 2]),
            np.array([2, 2, 0]),
            np.array([1, 2, 0]),
            np.array([0, 2, 1]),
            np.array([0, 2, 2]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5)
        self.play(ShowCreation(sideZX))

        smallXY = Polygon(
            np.array([2, 2, 0]),
            np.array([1, 2, 0]),
            np.array([2, 1, 0]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5)
        self.play(ShowCreation(smallXY))

        smallYZ = Polygon(
            np.array([0, 2, 2]),
            np.array([0, 2, 1]),
            np.array([0, 1, 2]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5)
        self.play(ShowCreation(smallYZ))

        smallZX = Polygon(
            np.array([2, 0, 2]),
            np.array([2, 0, 1]),
            np.array([1, 0, 2]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5)
        self.play(ShowCreation(smallZX))

        self.sectors[0] = VGroup()
        self.sectors[0].add(hexagon, sideXY, sideYZ, sideZX, smallXY, smallYZ, smallZX)

        self.begin_ambient_camera_rotation(rate=0.1)

        for i in range(1, 8):  # all 8 coordinates except the 1st one
            vector = self.vectors[i]

            x = vector[0]
            y = vector[1]
            z = vector[2]

            point = Sphere()
            point.scale(0.1)
            point.set_color(RED)
            point.move_to(np.array([2 * x, 2 * y, 2 * z]))
            self.play(ShowCreation(point), run_time=0.25)

            hexagon = Polygon(
                np.array([x, 2 * y, 0]),
                np.array([2 * x, y, 0]),
                np.array([2 * x, 0, z]),
                np.array([x, 0, 2 * z]),
                np.array([0, y, 2 * z]),
                np.array([0, 2 * y, z]),
                color=GREEN, fill_color=GREEN, fill_opacity=0.7)
            self.play(ShowCreation(hexagon))

            sideXY = Polygon(
                np.array([2 * x, 2 * y, 2 * z]),
                np.array([2 * x, 0 * y, 2 * z]),
                np.array([1 * x, 0 * y, 2 * z]),
                np.array([0 * x, 1 * y, 2 * z]),
                np.array([0 * x, 2 * y, 2 * z]),
                color=ORANGE, fill_color=BLUE, fill_opacity=0.5)
            self.play(ShowCreation(sideXY))

            sideYZ = Polygon(
                np.array([2 * x, 2 * y, 2 * z]),
                np.array([2 * x, 0 * y, 2 * z]),
                np.array([2 * x, 0 * y, 1 * z]),
                np.array([2 * x, 1 * y, 0 * z]),
                np.array([2 * x, 2 * y, 0 * z]),
                color=ORANGE, fill_color=BLUE, fill_opacity=0.5)
            self.play(ShowCreation(sideYZ))

            sideZX = Polygon(
                np.array([2 * x, 2 * y, 2 * z]),
                np.array([2 * x, 2 * y, 0 * z]),
                np.array([1 * x, 2 * y, 0 * z]),
                np.array([0 * x, 2 * y, 1 * z]),
                np.array([0 * x, 2 * y, 2 * z]),
                color=ORANGE, fill_color=BLUE, fill_opacity=0.5)
            self.play(ShowCreation(sideZX))

            smallXY = Polygon(
                np.array([2 * x, 2 * y, 0 * z]),
                np.array([1 * x, 2 * y, 0 * z]),
                np.array([2 * x, 1 * y, 0 * z]),
                color=ORANGE, fill_color=BLUE, fill_opacity=0.5)
            self.play(ShowCreation(smallXY))

            smallYZ = Polygon(
                np.array([0 * x, 2 * y, 2 * z]),
                np.array([0 * x, 2 * y, 1 * z]),
                np.array([0 * x, 1 * y, 2 * z]),
                color=ORANGE, fill_color=BLUE, fill_opacity=0.5)
            self.play(ShowCreation(smallYZ))

            smallZX = Polygon(
                np.array([2 * x, 0 * y, 2 * z]),
                np.array([2 * x, 0 * y, 1 * z]),
                np.array([1 * x, 0 * y, 2 * z]),
                color=ORANGE, fill_color=BLUE, fill_opacity=0.5)
            self.play(ShowCreation(smallZX))

            self.sectors[i] = VGroup(hexagon, sideXY, sideYZ, sideZX, smallXY, smallYZ, smallZX)

    def drawSectors(self):

        all = VGroup()

        for i in self.mobjects:
            all.add(i)

        self.play(all.scale, 0.5, {"about_point": ORIGIN})

        for i in range(0, 8):
            self.play(self.sectors[i].shift, self.vectors[i])

        self.wait(3)

        self.stop_ambient_camera_rotation

    def construct(self):

        self.init()

        self.drawFirstCube()

        self.drawHexagons()

        self.drawSectors()


class Truncation(ThreeDScene):
    def init(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=20 * DEGREES)

        # shifted to "center" at (0,0,0)

        # hexagon
        hexagon = Polygon(
            np.array([0, 1, -1]),
            np.array([-1, 1, 0]),
            np.array([-1, 0, 1]),
            np.array([0, -1, 1]),
            np.array([1, -1, 0]),
            np.array([1, 0, -1])
        )

        # sides

        sideXY = Polygon(
            np.array([1, 1, 1]),
            np.array([-1, 1, 1]),
            np.array([-1, 0, 1]),
            np.array([0, -1, 1]),
            np.array([1, -1, 1])
        )

        sideYZ = Polygon(
            np.array([1, 1, 1]),
            np.array([1, -1, 1]),
            np.array([1, -1, 0]),
            np.array([1, 0, -1]),
            np.array([1, 1, -1])
        )

        sideZX = Polygon(
            np.array([1, 1, 1]),
            np.array([1, 1, -1]),
            np.array([0, 1, -1]),
            np.array([-1, 1, 0]),
            np.array([-1, 1, 1])
        )

        # small

        smallXY = Polygon(
            np.array([1, 1, -1]),
            np.array([0, 1, -1]),
            np.array([1, 0, -1])
        )

        smallYZ = Polygon(
            np.array([-1, 1, 1]),
            np.array([-1, 0, 1]),
            np.array([-1, 1, 0])
        )

        smallZX = Polygon(
            np.array([1, -1, 1]),
            np.array([1, -1, 0]),
            np.array([0, -1, 1])
        )

        self.object = VGroup(hexagon, sideXY, sideYZ,
                             sideZX, smallXY, smallYZ, smallZX)

        self.play(ShowCreation(self.object))

    def threePyramid(self):

        pyraXY = VGroup(
            Polygon(np.array([1, 1, -1]),
                    np.array([1, 0, -1]), np.array([1, 1, -2])),
            Polygon(np.array([1, 1, -1]),
                    np.array([1, 1, -2]), np.array([0, 1, -1])),
            Polygon(np.array([1, 1, -1]),
                    np.array([0, 1, -1]), np.array([1, 0, -1])),
            Polygon(np.array([0, 1, -1]),
                    np.array([1, 0, -1]), np.array([1, 1, -2]))
        )

        pyraYZ = VGroup(
            Polygon(np.array([-1, 1, 1]),
                    np.array([-1, 1, 0]), np.array([-2, 1, 1])),
            Polygon(np.array([-1, 1, 1]),
                    np.array([-2, 1, 1]), np.array([-1, 0, 1])),
            Polygon(np.array([-1, 1, 1]),
                    np.array([-1, 0, 1]), np.array([-1, 1, 0])),
            Polygon(np.array([-1, 0, 1]),
                    np.array([-1, 1, 0]), np.array([-2, 1, 1]))
        )

        pyraZX = VGroup(
            Polygon(np.array([1, -1, 1]),
                    np.array([0, -1, 1]), np.array([1, -1, 0])),
            Polygon(np.array([1, -1, 1]),
                    np.array([1, -2, 1]), np.array([0, -1, 1])),
            Polygon(np.array([1, -1, 1]),
                    np.array([1, -1, 0]), np.array([1, -2, 1])),
            Polygon(np.array([1, -1, 0]),
                    np.array([0, -1, 1]), np.array([1, -2, 1]))
        )

        self.play(ShowCreation(pyraXY))
        self.play(ShowCreation(pyraYZ))
        self.play(ShowCreation(pyraZX))

    def twoDProject(self):
        self.wait()

    def construct(self):
        self.init()

        self.threePyramid()
