import bpy
import random
import string
import copy
from mathutils import Matrix

def object_copy(object):
    temp = object.copy()
    temp.data = object.data
    bpy.context.collection.objects.link(temp)
    return temp


def set_viewport_shading(mode):
    for area in bpy.context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.shading.type = mode
                    break
            break
        


def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def clear_materials():
    for m in bpy.data.materials:
        bpy.data.materials.remove(m)

def select_object(obj, deselect_other=False):
    if deselect_other:
        deselect_all()
    if isinstance(obj, list):
        for o in obj:
            o.select_set(True)
    else:
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
    
def deselect_all():
    bpy.ops.object.select_all(action='DESELECT')
    
    
    
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def parent_objects(parent_obj, child_obj):
    deselect_all()
    select_object(child_obj)
    select_object(parent_obj)
    act = bpy.context.active_object
    for o in bpy.context.selected_objects:
        if o == act:
            continue
        mat_world = o.matrix_world.copy()
        o.parent_type = 'OBJECT'
        o.parent = act
        o.matrix_parent_inverse = act.matrix_world.inverted() @ o.matrix_world
        o.matrix_world = mat_world

def bake_indirect_lighting():
    bpy.ops.scene.light_cache_bake()
def delete_light_cache():
    try:
        bpy.ops.scene.light_cache_free()
    except:
        pass