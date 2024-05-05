import math
import bpy
import tools.utility as utility

class BasicElement:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.mainObject = None
        self.allObjects = None

        self.create()
        self.mainObject.name = name
        self.translate(coordinates)
        
    def create(self):
        pass
    
    def translate(self, coordinates):
        self.coordinates = coordinates
        self.mainObject.location = coordinates
        
    def rotate(self, angle):
        self.mainObject.rotation_euler = (math.radians(
            angle[0]), math.radians(angle[1]), math.radians(angle[2]))
        
    def scale(self, size):
        self.mainObject.scale = size
        
    def mirror(self, axis):
        utility.select_object(self.mainObject)
        bpy.ops.object.modifier_add(type='MIRROR')
        bpy.context.object.modifiers["Mirror"].use_axis[0] = axis[0]
        bpy.context.object.modifiers["Mirror"].use_axis[1] = axis[1]
        bpy.context.object.modifiers["Mirror"].use_axis[2] = axis[2]
        