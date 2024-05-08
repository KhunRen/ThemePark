import bpy
import tools.utility as utility
import math


def clear_alpha(obj):
    utility.select_object(obj)
    objects = bpy.context.selected_objects

    # Iterate through the objects
    for obj in objects:
        # Check if the object has a material
        if obj.data.materials:
            # Iterate through the materials of the object
            for material in obj.data.materials:
                # Check if the material has a node tree
                if material.node_tree:
                    # Get the node tree of the material
                    node_tree = material.node_tree
                    nodes = node_tree.nodes

                    # Iterate through the nodes in the node tree
                    for node in nodes:
                        # Check if the node is a Principled BSDF
                        if node.type == 'BSDF_PRINCIPLED':
                            # Find the alpha socket and disconnect the image texture
                            if 'Alpha' in node.inputs:
                                input_alpha = node.inputs['Alpha']
                                if input_alpha.is_linked:
                                    links = node_tree.links
                                    for link in links:
                                        if link.to_socket == input_alpha:
                                            links.remove(link)
                                input_alpha.default_value = 1.0


class OBJ:
    def __init__(self, filename, clear_alpha=False):
        self.objects = None
        self.filename = filename
        self.clear_alpha = clear_alpha
        self.import_file()

    def import_file(self):
        utility.deselect_all()
        bpy.ops.import_scene.obj(filepath=self.filename)
        self.objects = bpy.context.selected_objects
        if self.clear_alpha:
            clear_alpha(self.objects)

    def translate(self, coordinates):
        for obj in self.objects:
            obj.location = coordinates

    def scale(self, size):
        for obj in self.objects:
            obj.scale = size

    def rotate(self, angle):
        for obj in self.objects:
            obj.rotation_euler = (math.radians(angle[0]), math.radians(
                angle[1]), math.radians(angle[2]))
