from manimlib.imports import *


class Bisector(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)

        p1 = Sphere()
        p1.scale(0.05)
        p1.set_color(RED)
        p1.move_to(np.array([1, 0, 0]))
        self.play(ShowCreation(p1))

        p2 = Sphere()
        p2.scale(0.05)
        p2.set_color(RED)
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

        self.begin_ambient_camera_rotation(0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()


class Bitruncated(VMobject):
    def __init__(self, scalar, **kwargs):
        VMobject.__init__(self, **kwargs)

        self.vectors = [
            scalar * np.array([1, 1, 1]),
            scalar * np.array([1, 1, -1]),
            scalar * np.array([1, -1, 1]),
            scalar * np.array([1, -1, -1]),
            scalar * np.array([-1, 1, 1]),
            scalar * np.array([-1, 1, -1]),
            scalar * np.array([-1, -1, 1]),
            scalar * np.array([-1, -1, -1])]

        for i in range(0, 8):
            x = self.vectors[i][0]
            y = self.vectors[i][1]
            z = self.vectors[i][2]
            self.add(
                Polygon(
                    np.array([x, 2 * y, 0]),
                    np.array([2 * x, y, 0]),
                    np.array([2 * x, 0, z]),
                    np.array([x, 0, 2 * z]),
                    np.array([0, y, 2 * z]),
                    np.array([0, 2 * y, z]),
                    **kwargs),
                Polygon(
                    np.array([x, 2 * y, 0]),
                    np.array([0, 2 * y, 0]),
                    np.array([0, 2 * y, z]),
                    color=ORANGE, fill_color=BLUE, stroke_opacity=0, **kwargs),
                Polygon(
                    np.array([0, y, 2 * z]),
                    np.array([0, 0, 2 * z]),
                    np.array([x, 0, 2 * z]),
                    color=ORANGE, fill_color=BLUE, stroke_opacity=0, **kwargs),
                Polygon(
                    np.array([2 * x, 0, z]),
                    np.array([2 * x, 0, 0]),
                    np.array([2 * x, y, 0]),
                    color=ORANGE, fill_color=BLUE,  stroke_opacity=0, **kwargs),
            )


class BitruncatedTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=20 * DEGREES)
        self.add(Bitruncated(1, color=ORANGE, fill_color=BLUE, fill_opacity=0.7))


class Sector(VMobject):
    # x, y, z is direction of Sector
    def __init__(self, x, y, z, **kwargs):
        VMobject.__init__(self, **kwargs)
        hexagon = Polygon(
            np.array([x, 2 * y, 0]),
            np.array([2 * x, y, 0]),
            np.array([2 * x, 0, z]),
            np.array([x, 0, 2 * z]),
            np.array([0, y, 2 * z]),
            np.array([0, 2 * y, z]),
            **kwargs)
        #hexagon.scale(0.95, about_point=hexagon.get_center())
        # self.play(ShowCreation(hexagon))

        sideXY = Polygon(
            np.array([2 * x, 2 * y, 2 * z]),
            np.array([2 * x, 0 * y, 2 * z]),
            np.array([1 * x, 0 * y, 2 * z]),
            np.array([0 * x, 1 * y, 2 * z]),
            np.array([0 * x, 2 * y, 2 * z]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
        # sideXY.scale(0.95, about_point=sideXY.get_center())
        # self.play(ShowCreation(sideXY))

        sideYZ = Polygon(
            np.array([2 * x, 2 * y, 2 * z]),
            np.array([2 * x, 0 * y, 2 * z]),
            np.array([2 * x, 0 * y, 1 * z]),
            np.array([2 * x, 1 * y, 0 * z]),
            np.array([2 * x, 2 * y, 0 * z]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
        # sideYZ.scale(0.95, about_point=sideYZ.get_center())
        # self.play(ShowCreation(sideYZ))

        sideZX = Polygon(
            np.array([2 * x, 2 * y, 2 * z]),
            np.array([2 * x, 2 * y, 0 * z]),
            np.array([1 * x, 2 * y, 0 * z]),
            np.array([0 * x, 2 * y, 1 * z]),
            np.array([0 * x, 2 * y, 2 * z]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
        # sideZX.scale(0.95, about_point=sideZX.get_center())
        # self.play(ShowCreation(sideZX))

        smallXY = Polygon(
            np.array([2 * x, 2 * y, 0 * z]),
            np.array([1 * x, 2 * y, 0 * z]),
            np.array([2 * x, 1 * y, 0 * z]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
        # smallXY.scale(0.95, about_point=smallXY.get_center())
        # self.play(ShowCreation(smallXY))

        smallYZ = Polygon(
            np.array([0 * x, 2 * y, 2 * z]),
            np.array([0 * x, 2 * y, 1 * z]),
            np.array([0 * x, 1 * y, 2 * z]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
        # smallYZ.scale(0.95, about_point=smallYZ.get_center())
        # self.play(ShowCreation(smallYZ))

        smallZX = Polygon(
            np.array([2 * x, 0 * y, 2 * z]),
            np.array([2 * x, 0 * y, 1 * z]),
            np.array([1 * x, 0 * y, 2 * z]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
        # smallZX.scale(0.95, about_point=smallZX.get_center())
        # self.play(ShowCreation(smallZX))

        self.add(hexagon, sideXY, sideYZ, sideZX, smallXY, smallYZ, smallZX)


class SectorTest(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=20 * DEGREES)
        self.add(Sector(1, 1, 1, color=ORANGE, fill_color=RED,
                        fill_opacity=0.7, stroke_width=1.3))


class Volume(ThreeDScene):

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

        self.replaceSectors = [None] * 8

        for i in range(0, 8):
            self.replaceSectors[i] = Sector(
                0.5 * self.vectors[i][0],
                0.5 * self.vectors[i][1],
                0.5 * self.vectors[i][2],
                color=ORANGE, fill_color=BLUE, fill_opacity=0.7, stroke_width=1.3)

    def drawFirstCube(self):
        self.cube = Cube()
        self.cube.set_opacity(0.5)
        self.cube.scale(2)
        self.play(ShowCreation(self.cube))
        self.wait()

        center = Sphere()
        center.scale(0.1)
        center.set_color(BLACK)
        self.play(ShowCreation(center))
        self.wait()

    def drawSectors(self):

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
            color=RED, fill_color=RED, fill_opacity=0.7, stroke_width=1.3)
        #hexagon.scale(0.95, about_point=hexagon.get_center())
        self.play(ShowCreation(hexagon))

        sideXY = Polygon(
            np.array([2, 2, 2]),
            np.array([2, 0, 2]),
            np.array([1, 0, 2]),
            np.array([0, 1, 2]),
            np.array([0, 2, 2]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
        # sideXY.scale(0.95, about_point=sideXY.get_center())
        self.play(ShowCreation(sideXY))

        sideYZ = Polygon(
            np.array([2, 2, 2]),
            np.array([2, 0, 2]),
            np.array([2, 0, 1]),
            np.array([2, 1, 0]),
            np.array([2, 2, 0]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
        # sideYZ.scale(0.95, about_point=sideYZ.get_center())
        self.play(ShowCreation(sideYZ))

        sideZX = Polygon(
            np.array([2, 2, 2]),
            np.array([2, 2, 0]),
            np.array([1, 2, 0]),
            np.array([0, 2, 1]),
            np.array([0, 2, 2]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
        # sideZX.scale(0.95, about_point=sideZX.get_center())
        self.play(ShowCreation(sideZX))

        smallXY = Polygon(
            np.array([2, 2, 0]),
            np.array([1, 2, 0]),
            np.array([2, 1, 0]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
        # smallXY.scale(0.95, about_point=smallXY.get_center())
        self.play(ShowCreation(smallXY))

        smallYZ = Polygon(
            np.array([0, 2, 2]),
            np.array([0, 2, 1]),
            np.array([0, 1, 2]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
        # smallYZ.scale(0.95, about_point=smallYZ.get_center())
        self.play(ShowCreation(smallYZ))

        smallZX = Polygon(
            np.array([2, 0, 2]),
            np.array([2, 0, 1]),
            np.array([1, 0, 2]),
            color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
        # smallZX.scale(0.95, about_point=smallZX.get_center())
        self.play(ShowCreation(smallZX))

        self.sectors[0] = VGroup()
        self.sectors[0].add(hexagon, sideXY, sideYZ,
                            sideZX, smallXY, smallYZ, smallZX)

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
                color=RED, fill_color=RED, fill_opacity=0.7, stroke_width=1.3)
            #hexagon.scale(0.95, about_point=hexagon.get_center())
            self.play(ShowCreation(hexagon))

            sideXY = Polygon(
                np.array([2 * x, 2 * y, 2 * z]),
                np.array([2 * x, 0 * y, 2 * z]),
                np.array([1 * x, 0 * y, 2 * z]),
                np.array([0 * x, 1 * y, 2 * z]),
                np.array([0 * x, 2 * y, 2 * z]),
                color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
            # sideXY.scale(0.95, about_point=sideXY.get_center())
            self.play(ShowCreation(sideXY))

            sideYZ = Polygon(
                np.array([2 * x, 2 * y, 2 * z]),
                np.array([2 * x, 0 * y, 2 * z]),
                np.array([2 * x, 0 * y, 1 * z]),
                np.array([2 * x, 1 * y, 0 * z]),
                np.array([2 * x, 2 * y, 0 * z]),
                color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
            # sideYZ.scale(0.95, about_point=sideYZ.get_center())
            self.play(ShowCreation(sideYZ))

            sideZX = Polygon(
                np.array([2 * x, 2 * y, 2 * z]),
                np.array([2 * x, 2 * y, 0 * z]),
                np.array([1 * x, 2 * y, 0 * z]),
                np.array([0 * x, 2 * y, 1 * z]),
                np.array([0 * x, 2 * y, 2 * z]),
                color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
            # sideZX.scale(0.95, about_point=sideZX.get_center())
            self.play(ShowCreation(sideZX))

            smallXY = Polygon(
                np.array([2 * x, 2 * y, 0 * z]),
                np.array([1 * x, 2 * y, 0 * z]),
                np.array([2 * x, 1 * y, 0 * z]),
                color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
            # smallXY.scale(0.95, about_point=smallXY.get_center())
            self.play(ShowCreation(smallXY))

            smallYZ = Polygon(
                np.array([0 * x, 2 * y, 2 * z]),
                np.array([0 * x, 2 * y, 1 * z]),
                np.array([0 * x, 1 * y, 2 * z]),
                color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
            # smallYZ.scale(0.95, about_point=smallYZ.get_center())
            self.play(ShowCreation(smallYZ))

            smallZX = Polygon(
                np.array([2 * x, 0 * y, 2 * z]),
                np.array([2 * x, 0 * y, 1 * z]),
                np.array([1 * x, 0 * y, 2 * z]),
                color=ORANGE, fill_color=BLUE, fill_opacity=0.5, stroke_width=1.3)
            # smallZX.scale(0.95, about_point=smallZX.get_center())
            self.play(ShowCreation(smallZX))

            self.sectors[i] = VGroup(
                hexagon, sideXY, sideYZ, sideZX, smallXY, smallYZ, smallZX)

        self.stop_ambient_camera_rotation

    def expandSectors(self):

        self.move_camera(phi=80 * DEGREES, theta=20 * DEGREES)

        self.bitruncated = Bitruncated(
            1, color=ORANGE, fill_color=BLUE, fill_opacity=0.7, stroke_width=1.3)
        self.add(self.bitruncated)

        all = VGroup()
        for i in self.mobjects:
            all.add(i)

        self.play(all.scale, 0.5, {"about_point": ORIGIN})

        self.remove(self.cube)

        for i in range(0, 8):
            self.play(self.sectors[i].shift, self.vectors[i])

        self.wait(3)

    def combineSectors1(self):
        self.wait()

        self.play(ApplyMethod(self.sectors[0].shift, -2 * self.vectors[0]),
                  ApplyMethod(self.sectors[1].shift, -2 * self.vectors[1]),
                  ApplyMethod(self.sectors[2].shift, -2 * self.vectors[2]),
                  ApplyMethod(self.sectors[3].shift, -2 * self.vectors[3]),
                  ApplyMethod(self.sectors[4].shift, -2 * self.vectors[4]),
                  ApplyMethod(self.sectors[5].shift, -2 * self.vectors[5]),
                  ApplyMethod(self.sectors[6].shift, -2 * self.vectors[6]),
                  ApplyMethod(self.sectors[7].shift, -2 * self.vectors[7]), run_time=2)
        self.play(FadeOut(self.bitruncated))
        #oldSectors = VGroup()

        for i in range(0, 8):
            # oldSectors.add(self.sectors[i])
            self.remove(self.sectors[i])

        # self.add(oldSectors)

        newSectors = Bitruncated(
            0.5, color=ORANGE, fill_color=BLUE, fill_opacity=0.7, stroke_opacity=1.3)

        self.add(newSectors)

        self.begin_ambient_camera_rotation(0.1)

        self.wait(5)

        self.play(newSectors.scale, 2, {"about_point": ORIGIN})

        self.wait(5)

        self.stop_ambient_camera_rotation

    def combineSectors2(self):

        self.play(UpdateFromAlphaFunc(self.bitruncated,
                                      self.updateOpacity), rate_func=smooth, run_time=2)
        self.wait()

    def updateOpacity(self, object, dt):
        opacity = interpolate(1, 0, dt)
        new_object = Bitruncated(
            0.5, color=ORANGE, fill_color=BLUE, fill_opacity=0.7 * opacity, stroke_width=1.3)
        object.become(new_object)

    def splitCenter(self):

        self.play(ShowCreation(self.replaceSectors[0]),
                  ShowCreation(self.replaceSectors[1]),
                  ShowCreation(self.replaceSectors[2]),
                  ShowCreation(self.replaceSectors[3]),
                  ShowCreation(self.replaceSectors[4]),
                  ShowCreation(self.replaceSectors[5]),
                  ShowCreation(self.replaceSectors[6]),
                  ShowCreation(self.replaceSectors[7]))

        self.play(ApplyMethod(self.replaceSectors[0].shift, -2 * self.vectors[0]),
                  ApplyMethod(
                      self.replaceSectors[1].shift, -2 * self.vectors[1]),
                  ApplyMethod(
                      self.replaceSectors[2].shift, -2 * self.vectors[2]),
                  ApplyMethod(
                      self.replaceSectors[3].shift, -2 * self.vectors[3]),
                  ApplyMethod(
                      self.replaceSectors[4].shift, -2 * self.vectors[4]),
                  ApplyMethod(
                      self.replaceSectors[5].shift, -2 * self.vectors[5]),
                  ApplyMethod(
                      self.replaceSectors[6].shift, -2 * self.vectors[6]),
                  ApplyMethod(self.replaceSectors[7].shift, -2 * self.vectors[7]), run_time=2)

        self.begin_ambient_camera_rotation(0.1)

        for i in range(0, 8):
            self.play(FadeOut(self.replaceSectors[i]))

        self.wait(5)

        self.stop_ambient_camera_rotation()

    def construct(self):

        self.init()

        self.drawFirstCube()

        self.drawSectors()

        self.expandSectors()

        # self.combineSectors1()
        # combineSectors1 results in weird rendering issues

        # self.splitCenter()
        # another possible option

        self.combineSectors2()


class Truncation(ThreeDScene):
    CONFIG = {
        # "VMObject_config": {"stroke-opacity": 0},
        # "camera_config": {"background_color": RED},
    }

    def init(self):
        self.set_camera_orientation(phi=80 * DEGREES, theta=20 * DEGREES)

        # shifted to "center" at (0,0,0)

        # hexagon
        self.hexagon = Polygon(
            np.array([0, 1, -1]),
            np.array([-1, 1, 0]),
            np.array([-1, 0, 1]),
            np.array([0, -1, 1]),
            np.array([1, -1, 0]),
            np.array([1, 0, -1]),
            stroke_width=1.3
        )
        #hexagon.scale(0.95, about_point=hexagon.get_center())
        # hexagon.scale_in_place(0.99)

        # sides

        self.sideXY = Polygon(
            np.array([1, 1, 1]),
            np.array([-1, 1, 1]),
            np.array([-1, 0, 1]),
            np.array([0, -1, 1]),
            np.array([1, -1, 1]),
            stroke_width=1.3
        )
        # sideXY.scale(0.95, about_point=sideXY.get_center())
        # sideXY.scale_in_place(0.99)

        self.sideYZ = Polygon(
            np.array([1, 1, 1]),
            np.array([1, -1, 1]),
            np.array([1, -1, 0]),
            np.array([1, 0, -1]),
            np.array([1, 1, -1]),
            stroke_width=1.3
        )
        # sideYZ.scale(0.95, about_point=sideYZ.get_center())
        # sideYZ.scale_in_place(0.99)

        self.sideZX = Polygon(
            np.array([1, 1, 1]),
            np.array([1, 1, -1]),
            np.array([0, 1, -1]),
            np.array([-1, 1, 0]),
            np.array([-1, 1, 1]),
            stroke_width=1.3
        )
        # sideZX.scale(0.95, about_point=sideZX.get_center())
        # sideZX.scale_in_place(0.99)

        # small

        self.smallXY = Polygon(
            np.array([1, 1, -1]),
            np.array([0, 1, -1]),
            np.array([1, 0, -1]),
            stroke_width=1.3
        )
        # smallXY.scale(0.95, about_point=smallXY.get_center())
        # smallXY.scale_in_place(0.99)

        self.smallYZ = Polygon(
            np.array([-1, 1, 1]),
            np.array([-1, 0, 1]),
            np.array([-1, 1, 0]),
            stroke_width=1.3
        )
        # smallYZ.scale(0.95, about_point=smallYZ.get_center())
        # smallYZ.scale_in_place(0.99)

        self.smallZX = Polygon(
            np.array([1, -1, 1]),
            np.array([1, -1, 0]),
            np.array([0, -1, 1]),
            stroke_width=1.3
        )
        # smallZX.scale(0.95, about_point=smallZX.get_center())
        # smallZX.scale_in_place(0.99)

        self.object = VGroup(hexagon, sideXY, sideYZ,
                             sideZX, smallXY, smallYZ, smallZX)

        self.play(ShowCreation(self.object))

    def threePyramid(self):

        self.pyraXY = VGroup(
            Polygon(np.array([1, 1, -1]),
                    np.array([1, 0, -1]), np.array([1, 1, -2]),
                    stroke_width=1.3),
            Polygon(np.array([1, 1, -1]),
                    np.array([1, 1, -2]), np.array([0, 1, -1]),
                    stroke_width=1.3),
            Polygon(np.array([1, 1, -1]),
                    np.array([0, 1, -1]), np.array([1, 0, -1]),
                    stroke_width=1.3),
            Polygon(np.array([0, 1, -1]),
                    np.array([1, 0, -1]), np.array([1, 1, -2]),
                    stroke_width=1.3)
        )
        # pyraXY.scale(0.95, about_point=pyraXY.get_center())
        # pyraXY.scale_in_place(0.99)

        self.pyraYZ = VGroup(
            Polygon(np.array([-1, 1, 1]),
                    np.array([-1, 1, 0]), np.array([-2, 1, 1]),
                    stroke_width=1.3),
            Polygon(np.array([-1, 1, 1]),
                    np.array([-2, 1, 1]), np.array([-1, 0, 1]),
                    stroke_width=1.3),
            Polygon(np.array([-1, 1, 1]),
                    np.array([-1, 0, 1]), np.array([-1, 1, 0]),
                    stroke_width=1.3),
            Polygon(np.array([-1, 0, 1]),
                    np.array([-1, 1, 0]), np.array([-2, 1, 1]),
                    stroke_width=1.3)
        )
        # pyraYZ.scale(0.95, about_point=pyraYZ.get_center())
        # pyraYZ.scale_in_place(0.99)

        self.pyraZX = VGroup(
            Polygon(np.array([1, -1, 1]),
                    np.array([0, -1, 1]), np.array([1, -1, 0]),
                    stroke_width=1.3),
            Polygon(np.array([1, -1, 1]),
                    np.array([1, -2, 1]), np.array([0, -1, 1]),
                    stroke_width=1.3),
            Polygon(np.array([1, -1, 1]),
                    np.array([1, -1, 0]), np.array([1, -2, 1]),
                    stroke_width=1.3),
            Polygon(np.array([1, -1, 0]),
                    np.array([0, -1, 1]), np.array([1, -2, 1]),
                    stroke_width=1.3)
        )
        # pyraZX.scale(0.95, about_point=pyraZX.get_center())
        # pyraZX.scale_in_place(0.99)

        self.play(ShowCreation(self.pyraXY))
        self.play(ShowCreation(self.pyraYZ))
        self.play(ShowCreation(self.pyraZX))

    def twoDFace(self):
        center = Sphere()
        center.scale(0.1)
        center.set_color(RED)
        center.move_to(np.array([-1, -1, -1]))

        l1 = Line(np.array([-1, -1, -1]), np.array([-1, -1, 1]))
        l2 = Line(np.array([-1, -1, 1]), np.array([0, -1, 1]))

        l3 = Line(np.array([1, 1, 1]), np.array([1, -1, 1]))
        l4 = Line(np.array([1, -1, 1]), np.array([0, -1, 1]))

        self.play(ShowCreation(l1))
        self.play(ShowCreation(l2))
        self.play(ShowCreation(l3))
        self.play(ShowCreation(l4))

        self.move_camera(phi=90 * DEGREES, theta=90 * DEGREES, run_time=1)

    def labelLengths(self):
        self.wait()

    def construct(self):
        self.init()

        self.threePyramid()
