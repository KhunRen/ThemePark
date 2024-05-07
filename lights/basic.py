import bpy
import math
import tools.utility as utility

class Basic:
    def __init__(self, name, coords):
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
        
class Light_probe_irradiance_volume(Basic):
    def __init__(self, name, coords, distance=0.1, falloff=0.1, intensity=1, resolution=(4,4,4), clipping_start=0, clipping_end=10, visibility_bias=1, visibility_bleed_bias=0, visibility_blur=0):
        self.distance = distance
        self.falloff = falloff
        self.intensity = intensity
        self.resolution = resolution
        self.clipping_start = clipping_start
        self.clipping_end = clipping_end
        self.visibility_bias = visibility_bias
        self.visibility_bleed_bias = visibility_bleed_bias
        self.visibility_blur = visibility_blur
        super().__init__(name, coords)
    
    def create(self):
        bpy.ops.object.light_probe_irradiance_volume_add(location=self.coords)
        self.object = bpy.context.object
        self.object.data.distance = self.distance
        self.object.data.falloff = self.falloff
        self.object.data.intensity = self.intensity
        self.object.data.resolution = self.resolution
        self.object.data.clipping_start = self.clipping_start
        self.object.data.clipping_end = self.clipping_end
        self.object.data.visibility_bias = self.visibility_bias
        self.object.data.visibility_bleed_bias = self.visibility_bleed_bias
        self.object.data.visibility_blur = self.visibility_blur