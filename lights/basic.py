import bpy
import math
import tools.utility as utility

class Basic:
    def __init__(self):
        self.light = None
        self.create()
    def create(self):
        pass
    def translate(self, location):
        utility.select_object(self.light)
        self.light.location = location
    def rotate(self, rotation):
        utility.select_object(self.light)
        self.light.rotate(rotation)
    def scale(self, scale):
        utility.select_object(self.light)
        self.light.scale = scale
    
class Point(Basic):
    def __init__(self, name, location, color=(1,1,1), power=10,diffuse=0,specular=1,volume=1,radius=0):
        self.name = name
        self.location = location
        self.color = color
        self.power = power
        self.diffuse = diffuse
        self.specular = specular
        self.volume = volume
        self.radius = radius
        self.create()
    def create(self):
        bpy.ops.object.light_add(type='POINT', radius=self.radius, align='WORLD', location=self.location)
        self.light = bpy.context.object
        self.light.data.color = self.color
        self.light.data.energy = self.power
        self.light.data.diffuse_factor = self.diffuse
        self.light.data.specular_factor = self.specular
        self.light.data.volume_factor = self.volume
        self.light.data.shadow_soft_size = self.radius
        self.light.data.falloff_type = 'INVERSE_SQUARE'
        self.light.data.use_shadow = True
        self.light.data.use_contact_shadow = True
        
class Sun(Basic):
    def __init__(self, name, location, color=(1,1,1), strength=10, diffuse=0,specular=1,volume=1,angle=0.526):
        self.name = name
        self.location = location
        self.color = color
        self.strength = strength
        self.diffuse = diffuse
        self.specular = specular
        self.volume = volume
        self.angle = angle
        self.create()
    def create(self):
        bpy.ops.object.light_add(type='SUN', align='WORLD', location=self.location)
        self.light = bpy.context.object
        self.light.data.color = self.color
        self.light.data.energy = self.strength
        self.light.data.diffuse_factor = self.diffuse
        self.light.data.specular_factor = self.specular
        self.light.data.volume_factor = self.volume
        self.light.data.angle = self.angle
        self.light.data.use_shadow = True
        self.light.data.use_contact_shadow = True
        
class Spot(Basic):
    def __init__(self, name, location, color=(1,1,1), power=10,diffuse=0,specular=1,volume=1,radius=0,shape_size=45,shape_blend=0.150):
        self.name = name
        self.location = location
        self.color = color
        self.power = power
        self.diffuse = diffuse
        self.specular = specular
        self.volume = volume
        self.radius = radius
        self.shape_size = math.radians(shape_size)
        self.shape_blend = shape_blend
        self.create()
    
    def create(self):
        bpy.ops.object.light_add(type='SPOT', radius=self.radius, align='WORLD', location=self.location)
        self.light = bpy.context.object
        self.light.data.color = self.color
        self.light.data.energy = self.power
        self.light.data.diffuse_factor = self.diffuse
        self.light.data.specular_factor = self.specular
        self.light.data.volume_factor = self.volume
        self.light.data.shadow_soft_size = self.radius
        self.light.data.spot_size = self.shape_size
        self.light.data.spot_blend = self.shape_blend
        self.light.data.falloff_type = 'INVERSE_SQUARE'
        self.light.data.use_shadow = True
        self.light.data.use_contact_shadow = True
        self.light.data.use_custom_distance = True
        self.light.data.distance = 10
        
class Area(Basic):
    def __init__(self, name, location, color=(1,1,1), power=10,diffuse=1,specular=1,volume=1,shape="SQUARE",size=1,size_tuple=(1,1)):
        self.name = name
        self.location = location
        self.color = color
        self.power = power
        self.diffuse = diffuse
        self.specular = specular
        self.volume = volume
        self.shape = shape
        self.size = size
        if shape == "RECTANGLE" or shape == "ELLIPSE":
            self.size = size_tuple
        self.create()
    def create(self):
        bpy.ops.object.light_add(type='AREA', align='WORLD', location=self.location)
        self.light = bpy.context.object
        self.light.data.color = self.color
        self.light.data.energy = self.power
        self.light.data.diffuse_factor = self.diffuse
        self.light.data.specular_factor = self.specular
        self.light.data.volume_factor = self.volume
        self.light.data.shape = self.shape
        self.light.data.size = self.size
        self.light.data.use_shadow = True
        self.light.data.use_contact_shadow = True
        
class Reflection_cubemap(Basic):
    def __init__(self, name, location, radius=2.5,falloff=0.2,intensity=1,clipping_start=0.8,clipping_end=40):
        self.name = name
        self.location = location
        self.radius = radius
        self.falloff = falloff
        self.intensity = intensity
        self.clipping_start = clipping_start
        self.clipping_end = clipping_end
        self.create()
    def create(self):
        bpy.ops.object.lightprobe_add(type="CUBEMAP", align='WORLD', location=self.location)
        self.light = bpy.context.object
        self.light.data.influence_distance = self.radius
        self.light.data.falloff = self.falloff
        self.light.data.intensity = self.intensity
        self.light.data.clip_start = self.clipping_start
        self.light.data.clip_end = self.clipping_end
        
class Reflection_plane(Basic):
    def __init__(self, name, location, distance=0.1,falloff=0.500,clipping_offset=0.001):
        self.name = name
        self.location = location
        self.distance = distance
        self.falloff = falloff
        self.clipping_offset = clipping_offset
        self.create()
    def create(self):
        bpy.ops.object.lightprobe_add(type='PLANAR', align='WORLD', location=self.location)
        self.light = bpy.context.object
        self.light.data.influence_distance = self.distance
        self.light.data.falloff = self.falloff
        self.light.data.clip_start = self.clipping_offset

class Irradiance_Volume(Basic):
    def __init__(self, name,location, distance=0.3,falloff=1,intensity=1,resolution=(4,4,4),clipping_start=0.01,clipping_end=10):
        self.name = name
        self.location = location
        self.distance = distance
        self.falloff = falloff
        self.intensity = intensity
        self.resolution = resolution
        self.clipping_start = clipping_start
        self.clipping_end = clipping_end
        self.create()
    def create(self):
        bpy.ops.object.lightprobe_add(type='GRID', align='WORLD', location=self.location)
        self.light = bpy.context.object
        self.light.data.influence_distance = self.distance
        self.light.data.falloff = self.falloff
        self.light.data.intensity = self.intensity
        self.light.data.grid_resolution_x = self.resolution[0]
        self.light.data.grid_resolution_y = self.resolution[1]
        self.light.data.grid_resolution_z = self.resolution[2]
        self.light.data.clip_start = self.clipping_start
        self.light.data.clip_end = self.clipping_end