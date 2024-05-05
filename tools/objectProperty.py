import bpy
import tools.utility as utility


def add_colour(obj, colour):
    utility.select_object(obj)
    material = bpy.data.materials.new('material')
    material.diffuse_color = (
        abs(colour[0]), abs(colour[1]), abs(colour[2]), 1)
    bpy.context.object.data.materials.append(material)


    
def shade_smooth(obj):
    utility.select_object(obj)
    bpy.ops.object.shade_smooth()
    
def shade_auto_smooth(obj, angle=30):
    utility.select_object(obj)
    bpy.context.object.data.use_auto_smooth = True
    bpy.context.object.data.auto_smooth_angle = angle
    