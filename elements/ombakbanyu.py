import math
import elements.basics as basics
import primitif.basic as basic
import tools.utility as utility
import tools.modifier as modifier
import tools.objectProperty as objectProperty
import bpy
from importlib import reload
import random

reload(basics)


class OmbakBanyu(basics.BasicElement):
    def __init__(self, name, coordinates):
        coordinates = (coordinates[0], coordinates[1], coordinates[2] + 1.5)
        super().__init__(name, coordinates)
        self.animate()

    def create(self):
        top_cone = basic.Cone(name="top_cone", coords=(0, 0, 36.8413))
        top_cone.scale((30, 30, 5.28961))
        modifier.wireframe(top_cone.object, 0.024, 1, False)

        seat = basic.Torus(name="seat", coords=(0, 0, 19.7393))
        seat.scale((23.6526, 23.6526, 2.09852))

        back_rest = basic.Cylinder(name="back_rest", coords=(0, 0, 22.1694))
        back_rest.scale((29.0064, 29.0064, 2.09852))
        modifier.wireframe(back_rest.object, 0.107)
        modifier.subdivision_surface(back_rest.object, 6)

        top_fence = basic.Cylinder(name="top_fence", coords=(0, 0, 27.85))
        top_fence.scale((29.0064, 29.0064, 3.58164))
        modifier.wireframe(top_fence.object, 0.02)

        base = basic.Cone(name="base", coords=(0, 0, -0.5))
        base.scale((35, 35, 1.2))
        modifier.wireframe(base.object, 0.01, 1, False)

        ring_decor_1 = basic.Torus(name="ring_decor_1", coords=(0, 0, -0.3))
        ring_decor_1.scale((10, 10, 3))

        ring_decor_2 = basic.Torus(name="ring_decor_2", coords=(0, 0, 3))
        ring_decor_2.scale((5, 5, 3))

        center_pole = basic.Cylinder(name="center_pole", coords=(0, 0, 12))
        center_pole.scale((1.6, 1.6, 12.4))

        lower_decor = basic.Cylinder(name="lower_decor", coords=(0, 0, 2))
        lower_decor.scale((2.5, 2.5, 3.4))

        center_pole_2 = basic.Cone(name="center_pole_2", coords=(0, 0, 17))
        center_pole_2.scale((1.5, 1.5, 19))

        diagonal_pole_1 = basic.Cylinder(name="diagonal_pole_1", coords=(4, 4, 12.3))
        diagonal_pole_1.scale((0.8, 0.8, 15))
        diagonal_pole_1.rotate((0, -19, 45))

        diagonal_pole_2 = basic.Cylinder(name="diagonal_pole_2", coords=(-4, 4, 12.3))
        diagonal_pole_2.scale((0.8, 0.8, 15))
        diagonal_pole_2.rotate((19, 0, 45))

        diagonal_pole_3 = basic.Cylinder(name="diagonal_pole_3", coords=(-4, -4, 12.3))
        diagonal_pole_3.scale((0.8, 0.8, 15))
        diagonal_pole_3.rotate((0, 19, 45))

        diagonal_pole_4 = basic.Cylinder(name="diagonal_pole_4", coords=(4, -4, 12.3))
        diagonal_pole_4.scale((0.8, 0.8, 15))
        diagonal_pole_4.rotate((-19, 0, 45))

        cantilever_pole_1 = basic.Cylinder(
            name="cantilever_pole_1", coords=(2.5, 2.5, 13.3)
        )
        cantilever_pole_1.scale((0.4, 0.4, 3))
        cantilever_pole_1.rotate((45, 90, 90))

        cantilever_pole_2 = basic.Cylinder(
            name="cantilever_pole_2", coords=(-2.5, 2.5, 13.3)
        )
        cantilever_pole_2.scale((0.4, 0.4, 3))
        cantilever_pole_2.rotate((90, 45, 45))

        cantilever_pole_3 = basic.Cylinder(
            name="cantilever_pole_3", coords=(-2.5, -2.5, 13.3)
        )
        cantilever_pole_3.scale((0.4, 0.4, 3))
        cantilever_pole_3.rotate((45, 90, 90))

        cantilever_pole_4 = basic.Cylinder(
            name="cantilever_pole_4", coords=(2.5, -2.5, 13.3)
        )
        cantilever_pole_4.scale((0.4, 0.4, 3))
        cantilever_pole_4.rotate((90, 45, 45))

        top_sphere_1 = basic.Sphere(name="top_sphere_1", coords=(0, 0, 26.1))
        top_sphere_1.scale((2.5, 2.5, 2.5))

        top_sphere_2 = basic.Sphere(name="top_sphere_2", coords=(0, 0, 31.5))
        top_sphere_2.scale((1, 1, 1))

        top_sphere_3 = basic.Sphere(name="top_sphere_3", coords=(0, 0, 35.5))
        top_sphere_3.scale((0.5, 0.5, 0.5))

        fence = basic.Cylinder(name="fence", coords=(0, 0, -0.02))
        fence.scale((32.9, 32.9, 1.7))
        modifier.wireframe(fence.object, 0.02)

        utility.parent_objects(seat.object, back_rest.object)
        utility.parent_objects(seat.object, top_fence.object)
        utility.parent_objects(seat.object, top_cone.object)
        utility.parent_objects(base.object, center_pole.object)
        utility.parent_objects(base.object, center_pole_2.object)
        utility.parent_objects(base.object, lower_decor.object)
        utility.parent_objects(base.object, ring_decor_1.object)
        utility.parent_objects(base.object, ring_decor_2.object)
        utility.parent_objects(base.object, center_pole_2.object)
        utility.parent_objects(base.object, diagonal_pole_1.object)
        utility.parent_objects(base.object, diagonal_pole_2.object)
        utility.parent_objects(base.object, diagonal_pole_3.object)
        utility.parent_objects(base.object, diagonal_pole_4.object)
        utility.parent_objects(base.object, top_sphere_1.object)
        utility.parent_objects(base.object, top_sphere_2.object)
        utility.parent_objects(base.object, top_sphere_3.object)
        utility.parent_objects(base.object, fence.object)

        self.mainObject = base.object
        self.topObjects = {
            "top_cone": top_cone.object,
            "seat": seat.object,
            "back_rest": back_rest.object,
            "top_fence": top_fence.object,
        }
        self.bottomObjects = {
            "center_pole": center_pole.object,
            "center_pole_2": center_pole_2.object,
            "lower_decor": lower_decor.object,
            "ring_decor_1": ring_decor_1.object,
            "ring_decor_2": ring_decor_2.object,
            "center_pole_2": center_pole_2.object,
            "diagonal_pole_1": diagonal_pole_1.object,
            "diagonal_pole_2": diagonal_pole_2.object,
            "diagonal_pole_3": diagonal_pole_3.object,
            "diagonal_pole_4": diagonal_pole_4.object,
            "top_sphere_1": top_sphere_1.object,
            "top_sphere_2": top_sphere_2.object,
            "top_sphere_3": top_sphere_3.object,
            "fence": fence.object,
        }

        seat.scale((27.6526, 27.6526, 2.09852))
        seat.translate((0,0,16))

    def animate(self):
        # Mendapatkan jumlah frame pada animasi
        total_frames = 500

        # Pembagian frame menjadi 2 bagian
        for i in range(1, total_frames + 1):
            # Rotasi terhadap sumbu Y
            if i <= total_frames / 2:
                # Bagian 1 (frame 1 - 250)
                self.topObjects["seat"].rotation_euler[1] = math.radians(
                    -7.08689 * (i / (total_frames / 2))
                )
            else:
                # Bagian 2 (frame 251 - 500)
                self.topObjects["seat"].rotation_euler[1] = math.radians(
                    -7.08689 * (1 - (i - total_frames / 2) / (total_frames / 2))
                )

            # Rotasi terhadap sumbu Z
            self.topObjects["seat"].rotation_euler[2] = math.radians(20 * i)

            # Menyisipkan keyframe untuk rotasi objek "seat"
            self.topObjects["seat"].keyframe_insert(data_path="rotation_euler", frame=i)
