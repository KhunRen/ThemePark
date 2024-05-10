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
    def __init__(self, name, coordinates, trees=True, lamp=True):
        self.trees = trees
        self.lamp = lamp
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
        
        if self.lamp:
            for i in range(0, 360, 15):
                
                
                if (i>240 and i<300) or (i<210 and i >150) or (i>60 and i<120) or (i>=0 and i<30) or i == 345:
                    continue
                
                x = 2.2*math.cos(math.radians(i))
                y = 2.2*math.sin(math.radians(i))
                
                lamp = Lamp("lamp", (x, y, 0.202866))
                lamp.scale((0.007388,0.007388,0.203439))
                lamp.rotate((0,0,i))
                
                
                
            for i in range(0, 360, 10):
            
            
                if (i>=0 and i<20) or i == 350 or (i>250 and i<290)  or (i>70 and i<110) or (i>160 and i<200):
                    continue
                
                x = 4.2*math.cos(math.radians(i))
                y = 4.2*math.sin(math.radians(i))
                
                lamp = Lamp("lamp", (x, y, 0.202866))
                lamp.scale((0.007388,0.007388,0.203439))
                lamp.rotate((0,0,i))
                
                
                
            for i in range(0, 360, 15):
            
            
                if (i>=0 and i<20) or i == 350 or (i>250 and i<290)  or (i>70 and i<110) or (i>160 and i<200) or i == 355:
                    continue
                
                x = 6.5*math.cos(math.radians(i))
                y = 6.5*math.sin(math.radians(i))
                
                lamp = Lamp("lamp", (x, y, 0.202866))
                lamp.scale((0.007388,0.007388,0.203439))
                lamp.rotate((0,0,i))
            
            
            

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


class Lamp_light(basics.BasicElement):
    def create(self):
        
        light_source = basic.Cube("light_source", (0, 0, 0.56831))
        light_source.scale((0.295675,0.295675,0.349758))
        
        light_frame = basic.Cube("light_frame", (0, 0, 0.56831))
        light_frame.scale((0.328026,0.328026,0.388026))
        modifier.wireframe(light_frame.object, 0.281)
        
        top_ornament = basic.Cylinder("top_ornament", (0, 0, 1.10849))
        top_ornament.scale((0.322972,0.322972,0.084643))
        
        top = basic.Cube("top", (0, 0, 1.00673))
        top.scale((0.404273,0.404273,0.03454))
        
        utility.parent_objects(light_source.object, light_frame.object)
        utility.parent_objects(light_source.object, top_ornament.object)
        utility.parent_objects(light_source.object, top.object)
        
        light = materials.create_material("light", (1, 1, 1, 1), 0, 1, 1,(1.0,0.594364,0.128672,1),9)
        materials.assign_material(light_source.object, light)
        
        metal = materials.create_material("metal", (0.178859,0.178859,0.178859,1),1,1,0)
        materials.assign_material(light_frame.object, metal)
        materials.assign_material(top_ornament.object, metal)
        materials.assign_material(top.object, metal)
        
        
        self.mainObject = light_source.object
class Lamp(basics.BasicElement):
    def create(self):
        base = basic.Cylinder("base", (0, 0, 0))
        base.scale((0.114994,0.114994,3.16668))
        
        base_side = basic.Cylinder("base_side", (0, 0, 2.05019))
        base_side.rotate((90, 0, 0))
        base_side.scale((0.114994,0.114994,1.33668))
        
        base_side_left = basic.Cylinder("base_side_left", (0, 1.21485, 2.18677))
        base_side_left.scale((0.114994,0.114994,0.266678))
        
        base_side_right = basic.Cylinder("base_side_right", (0, -1.21485, 2.18677))
        base_side_right.scale((0.114994,0.114994,0.266678))
        
        light_center = Lamp_light("light_center", (0, 0, 3.56831))
        
        light_left = Lamp_light("light_left", (0, 1.21485, 2.76831))
        light_right = Lamp_light("light_right", (0, -1.21485, 2.76831))
        
        
        utility.parent_objects(base.object, base_side.object)
        utility.parent_objects(base.object, base_side_left.object)
        utility.parent_objects(base.object, base_side_right.object)
        utility.parent_objects(base.object, light_center.mainObject)
        utility.parent_objects(base.object, light_left.mainObject)
        utility.parent_objects(base.object, light_right.mainObject)
        
        metal = materials.create_material("metal", (0.178859,0.178859,0.178859,1),1,1,0)
        materials.assign_material(base.object, metal)
        materials.assign_material(base_side.object, metal)
        materials.assign_material(base_side_left.object, metal)
        materials.assign_material(base_side_right.object, metal)
        
        
        self.mainObject = base.object
        