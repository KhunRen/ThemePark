import math
import elements.basics as basics
import primitif.basic as basic
import tools.utility as utility
import tools.modifier as modifier
import tools.objectProperty as objectProperty
import tools.materials as materials
import objs.importer as objimporter
import bpy
from importlib import reload
import random
reload(basics)
reload(materials)
reload(objimporter)


class Ground(basics.BasicElement):
    def __init__(self, name, coordinates, trees=True):
        self.trees = trees
        super().__init__(name, coordinates)
    def create(self):
        ground = basic.Plane("ground", (0, 0, 0))
        ground.scale((7.99189, 7.99189, 7.99189))

        grass = materials.create_material(
            "grass", (0.147344, 0.650002, 0.162019, 1), 0.440945, 0, 0.53937)
        materials.assign_material(ground.object, grass)

        road_1 = basic.Cube("road_1", (0, 0, 0))
        road_1.scale((7.99681, 1, 0.01))

        road_2 = basic.Cube("road_2", (0, 0, 0))
        road_2.scale((7.99681, 1, 0.01))
        road_2.rotate((0, 0, 90))

        road_3 = basic.Sphere("road_3", (0, 0, 0))
        road_3.scale((2.2712, 2.2712, 0.055538))

        road_4 = basic.Torus("road_4", (0, 0, 0))
        road_4.scale((5.4031, 5.4031, 0.06655))

        if self.trees:
            for x in range(-1, 2, 2):
                for y in range(-1, 2, 2):
                    tree_1 = Tree("tree_1", (1.22746*x, -2.14078*y, 0.423311))
                    tree_1.scale((0.056968, 0.056968, 0.427262))

                    tree_2 = Tree("tree_2", (1.77889*x, -1.69017*y, 0.423311))
                    tree_2.scale((0.056968, 0.056968, 0.427262))

                    tree_3 = Tree("tree_3", (2.17137*x, -1.15008*y, 0.423311))
                    tree_3.scale((0.056968, 0.056968, 0.427262))

                    tree_4 = Tree("tree_4", (1.6965*x, -2.38498 * y, 0.423311))
                    tree_4.scale((0.056968, 0.056968, 0.427262))

                    tree_5 = Tree("tree_5", (2.46009*x, -2.07771 * y, 0.423311))
                    tree_5.scale((0.056968, 0.056968, 0.427262))

                    tree_6 = Tree("tree_6", (2.96721 * x, -1.4046*y, 0.423311))
                    tree_6.scale((0.056968, 0.056968, 0.427262))

                    tree_7 = Tree("tree_7", (1.40144*x, -2.88945*y, 0.423311))
                    tree_7.scale((0.056968, 0.056968, 0.427262))

                    tree_8 = Tree("tree_8", (2.3871 * x, -3.00383 * y, 0.423311))
                    tree_8.scale((0.056968, 0.056968, 0.427262))

                    tree_9 = Tree("tree_9", (3.12661*x, -2.44656 * y, 0.423311))
                    tree_9.scale((0.056968, 0.056968, 0.427262))

                    tree_10 = Tree("tree_10", (3.57529*x, -1.78896*y, 0.423311))
                    tree_10.scale((0.056968, 0.056968, 0.427262))

        utility.parent_objects(ground.object, road_1.object)
        utility.parent_objects(ground.object, road_2.object)
        utility.parent_objects(ground.object, road_3.object)
        utility.parent_objects(ground.object, road_4.object)

        self.mainObject = ground.object


class Gate(basics.BasicElement):
    def create(self):
        rainbow = basic.Torus("rainbow", (0, 0, 0))
        rainbow.rotate((0, 90, 0))
        rainbow.scale((7.61594, 5.87594, 2.04594))

        rainbow_mat = materials.textured_material(
            "rainbow", "//textures/rainbow.png", 0, 0.459459, 0.148649)
        materials.assign_material(rainbow.object, rainbow_mat)

        left_cloud_1 = basic.Sphere("left_cloud_1", (0, -7.33836, 0))
        left_cloud_2 = basic.Sphere("left_cloud_2", (0, -6.26629, -0.148516))
        left_cloud_3 = basic.Sphere("left_cloud_3", (0, -5.22081, -0.394327))

        right_cloud_1 = basic.Sphere("right_cloud_1", (0, 7.33836, 0))
        right_cloud_2 = basic.Sphere("right_cloud_2", (0, 6.26629, -0.148516))
        right_cloud_3 = basic.Sphere("right_cloud_3", (0, 5.22081, -0.394327))

        cloud = materials.create_material("cloud", (1, 1, 1, 1), 0, 1, 1)
        materials.assign_material(left_cloud_1.object, cloud)
        materials.assign_material(left_cloud_2.object, cloud)
        materials.assign_material(left_cloud_3.object, cloud)
        materials.assign_material(right_cloud_1.object, cloud)
        materials.assign_material(right_cloud_2.object, cloud)
        materials.assign_material(right_cloud_3.object, cloud)

        boolean_box = basic.Cube("boolean_box", (0, 0, -9.64124))
        boolean_box.scale((9.63088, 9.63088, 9.63088))

        self.mainObject = rainbow.object
        utility.parent_objects(rainbow.object, left_cloud_1.object)
        utility.parent_objects(rainbow.object, left_cloud_2.object)
        utility.parent_objects(rainbow.object, left_cloud_3.object)
        utility.parent_objects(rainbow.object, right_cloud_1.object)
        utility.parent_objects(rainbow.object, right_cloud_2.object)
        utility.parent_objects(rainbow.object, right_cloud_3.object)

        modifier.boolean_difference(rainbow.object, boolean_box.object)
        modifier.boolean_difference(left_cloud_1.object, boolean_box.object)
        modifier.boolean_difference(left_cloud_2.object, boolean_box.object)
        modifier.boolean_difference(left_cloud_3.object, boolean_box.object)
        modifier.boolean_difference(right_cloud_1.object, boolean_box.object)
        modifier.boolean_difference(right_cloud_2.object, boolean_box.object)
        modifier.boolean_difference(right_cloud_3.object, boolean_box.object)

        modifier.apply_all_modifier(rainbow.object)
        modifier.apply_all_modifier(left_cloud_1.object)
        modifier.apply_all_modifier(left_cloud_2.object)
        modifier.apply_all_modifier(left_cloud_3.object)
        modifier.apply_all_modifier(right_cloud_1.object)
        modifier.apply_all_modifier(right_cloud_2.object)
        modifier.apply_all_modifier(right_cloud_3.object)

        objectProperty.shade_smooth(rainbow.object)
        objectProperty.shade_smooth(left_cloud_1.object)
        objectProperty.shade_smooth(left_cloud_2.object)
        objectProperty.shade_smooth(left_cloud_3.object)
        objectProperty.shade_smooth(right_cloud_1.object)
        objectProperty.shade_smooth(right_cloud_2.object)
        objectProperty.shade_smooth(right_cloud_3.object)

        boolean_box.remove()


class Tree(basics.BasicElement):
    def create(self):
        base = basic.Cylinder("base", (0, 0, 0))
        base.scale((0.4, 0.4, 3))
        wood_mat = materials.create_material(
            "wood", (0.5, 0.25, 0, 1), 0, 0.5, 0.5)
        materials.assign_material(base.object, wood_mat)

        objectProperty.shade_smooth(base.object)

        for i in range(0, 10):
            leaf = basic.Sphere(
                "leaf_"+str(i), (random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(1, 3)))
            leaf.scale((random.uniform(1, 2), random.uniform(
                1, 2), random.uniform(1, 2)))
            leaf_mat = materials.create_material(
                "leaf", (0.147344, 0.650002, 0.162019, 1), 0.062992, 0, 0.53937)
            materials.assign_material(leaf.object, leaf_mat)
            utility.parent_objects(base.object, leaf.object)

        self.mainObject = base.object
