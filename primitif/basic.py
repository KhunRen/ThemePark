import bpy
import math
import tools.utility as utility


class Basic:
    def __init__(self, name=utility.random_string(5), coords=(0, 0, 0)):
        self.coords = coords
        self.object = None

        self.create()
        self.rename(name)

    def create(self):
        pass

    def translate(self, coords):
        self.coords = coords
        self.object.location = coords

    def rotate(self, angle):
        self.object.rotation_euler = (math.radians(
            angle[0]), math.radians(angle[1]), math.radians(angle[2]))

    def scale(self, size):
        self.object.scale = size

    def mirror(self, axis):
        utility.select_object(self.object)
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_axis[0] = axis[0]
        bpy.context.object.modifiers["Mirror"].use_axis[1] = axis[1]
        bpy.context.object.modifiers["Mirror"].use_axis[2] = axis[2]

    def rename(self, name):
        self.object.name = name


class Cube(Basic):
    def create(self):
        bpy.ops.mesh.primitive_cube_add(location=self.coords)
        self.object = bpy.context.object


class Sphere(Basic):
    def create(self):
        bpy.ops.mesh.primitive_uv_sphere_add(location=self.coords)
        self.object = bpy.context.object


class Cylinder(Basic):
    def create(self):
        bpy.ops.mesh.primitive_cylinder_add(location=self.coords)
        self.object = bpy.context.object


class Cone(Basic):
    def create(self):
        bpy.ops.mesh.primitive_cone_add(location=self.coords)
        self.object = bpy.context.object


class Torus(Basic):
    def create(self):
        bpy.ops.mesh.primitive_torus_add(location=self.coords)
        self.object = bpy.context.object


class Plane(Basic):
    def create(self):
        bpy.ops.mesh.primitive_plane_add(location=self.coords)
        self.object = bpy.context.object

class Suzanne(Basic):
    def create(self):
        bpy.ops.mesh.primitive_monkey_add(location=self.coords)
        self.object = bpy.context.object