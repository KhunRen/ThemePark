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
    bpy.context.object.modifiers["Subdivision"].render_levels = level
    
def wireframe(obj, size, offset=0, replace_original=True):
    utility.select_object(obj)
    bpy.ops.object.modifier_add(type='WIREFRAME')
    bpy.context.object.modifiers["Wireframe"].thickness = size
    bpy.context.object.modifiers["Wireframe"].offset = offset
    bpy.context.object.modifiers["Wireframe"].use_replace = replace_original

def weld(obj, distance):
    utility.select_object(obj)
    bpy.ops.object.modifier_add(type='WELD')
    bpy.context.object.modifiers["Weld"].merge_threshold = distance
    
def displace(obj, strength, midlevel):
    utility.select_object(obj)
    bpy.ops.object.modifier_add(type='DISPLACE')
    bpy.context.object.modifiers["Displace"].strength = strength
    bpy.context.object.modifiers["Displace"].mid_level = midlevel
    
def cast(obj, factor):
    utility.select_object(obj)
    bpy.ops.object.modifier_add(type='CAST')
    bpy.context.object.modifiers["Cast"].factor = factor
    
def apply_all_modifier(obj):
    utility.select_object(obj)
    bpy.ops.object.convert(target='MESH')

def boolean_difference(obj, target):
    utility.select_object(obj)
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
    bpy.context.object.modifiers["Boolean"].object = target