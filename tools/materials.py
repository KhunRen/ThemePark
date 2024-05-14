import bpy
import tools.utility as utility


def create_material(name, color, metalic=0, specular=0, roughness=0, emmision_color=(0, 0, 0, 1), emmision_strength=0):
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    else:
        # principled bsdf
        mat = bpy.data.materials.new(name=name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        principled = nodes.get('Principled BSDF')
        principled.inputs['Base Color'].default_value = color
        principled.inputs['Metallic'].default_value = metalic
        principled.inputs['Specular'].default_value = specular
        principled.inputs['Roughness'].default_value = roughness
        principled.inputs['Emission'].default_value = emmision_color
        principled.inputs['Emission Strength'].default_value = emmision_strength
        return mat


def textured_material(name, texture_src, metalic=0, specular=0, roughness=0, emmision_color=(0, 0, 0, 1), emmision_strength=0):
    if name in bpy.data.materials:
        return bpy.data.materials[name]
    else:
        mat = bpy.data.materials.new(name=name)
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        principled = nodes.get('Principled BSDF')
        principled.inputs['Metallic'].default_value = metalic
        principled.inputs['Specular'].default_value = specular
        principled.inputs['Roughness'].default_value = roughness
        principled.inputs['Emission'].default_value = emmision_color
        principled.inputs['Emission Strength'].default_value = emmision_strength

        texture = nodes.new('ShaderNodeTexImage')
        texture.image = bpy.data.images.load(texture_src)
        mat.node_tree.links.new(
            texture.outputs['Color'], principled.inputs['Base Color'])
        return mat


def assign_material(obj, mat):
    if obj.data.materials:
        obj.data.materials[0] = mat
    else:
        obj.data.materials.append(mat)


def assign_material_by_name(obj, name):
    if name in bpy.data.materials:
        mat = bpy.data.materials[name]
    else:
        raise ValueError("Material not found")
    assign_material(obj, mat)
