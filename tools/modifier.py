import bpy
import tools.utility as utility


def add_bevel(obj, size):
    utility.select_object(obj)
    bpy.ops.object.modifier_add(type='BEVEL')
    bpy.context.object.modifiers["Bevel"].width = size


def boolean_difference(obj, target):
    utility.select_object(obj)
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
    bpy.context.object.modifiers["Boolean"].object = target

def subdivision_surface(obj, level):
    utility.select_object(obj)
    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subdivision"].levels = level