import math
import elements.basics as basics
import primitif.basic as basic
import tools.utility as utility
import tools.modifier as modifier
import tools.objectProperty as objectProperty
import bpy
from importlib import reload
import random
reload(basics)

class Boat(basics.BasicElement):
    def create(self):
        depan1 = basic.Cone(name="depan", coords=(0, 30, 23))
        depan1.rotate((-50, 0, 0))
        depan1.scale((3.6, 3.3, 6.7))
        
        depan2 = basic.Sphere(name="depan2", coords=(0, 21.6383, 17.296))
        depan2.scale((6.2, 5, 5))
        
        belakang1 = basic.Cone(name="belakang1", coords=(0, -30, 23))
        belakang1.rotate((50, 0, 0))
        belakang1.scale((3.6, 3.3, 6.7))
        
        belakang2 = basic.Sphere(name="belakang2", coords=(0, -21.6383, 17.296))
        belakang2.scale((6.2, 5, 5))
        
        tengah = basic.Sphere(name="tengah", coords=(0, 0, 16))
        tengah.scale((14.7, 24.7499, 7.89263))
        
        tengah_bool = basic.Sphere(name="tengah_bool", coords=(0, 0, 18))
        tengah_bool.scale((13.7, 23.7499, 6.89263))

        
        modifier.boolean_difference(tengah.object, tengah_bool.object)
        modifier.apply_all_modifier(tengah.object)
        tengah_bool.remove()
        
        utility.parent_objects(tengah.object, depan1.object)
        utility.parent_objects(tengah.object, depan2.object)
        utility.parent_objects(tengah.object, belakang1.object)
        utility.parent_objects(tengah.object, belakang2.object)
        
        tiang_ke_frame = basic.Cylinder(name="tiang_ke_frame", coords=(0, 0, 35))
        tiang_ke_frame.scale((0.7, 0.7, 25))
        
        tiang_kiri1 = basic.Cylinder(name="tiang_kiri1", coords=(-7.5, -8.5, 37))
        tiang_kiri1.rotate((-20, 0, 0))
        tiang_kiri1.scale((0.7, 0.7, 25))
        
        tiang_kiri2 = basic.Cylinder(name="tiang_kiri2", coords=(-7.5, 8.5, 37))
        tiang_kiri2.rotate((20, 0, 0))
        tiang_kiri2.scale((0.7, 0.7, 25))
        
        tiang_kanan1 = basic.Cylinder(name="tiang_kanan1", coords=(7.5, -8.5, 37))
        tiang_kanan1.rotate((-20, 0, 0))
        tiang_kanan1.scale((0.7, 0.7, 25))
        
        tiang_kanan2 = basic.Cylinder(name="tiang_kanan2", coords=(7.5, 8.5, 37))
        tiang_kanan2.rotate((20, 0, 0))
        tiang_kanan2.scale((0.7, 0.7, 25))
        
        tiang_tengah_belakang = basic.Cylinder(name="tiang_tengah_belakang", coords=(0, -15, 41))
        tiang_tengah_belakang.rotate((-37, 0, 0))
        tiang_tengah_belakang.scale((0.7, 0.7, 24.5))
        
        tiang_tengah_depan = basic.Cylinder(name="tiang_tengah_depan", coords=(0, 15, 41))
        tiang_tengah_depan.rotate((37, 0, 0))
        tiang_tengah_depan.scale((0.7, 0.7, 24.5))
        
        utility.parent_objects(tiang_ke_frame.object, tengah.object)
        utility.parent_objects(tiang_ke_frame.object, tiang_kiri1.object)
        utility.parent_objects(tiang_ke_frame.object, tiang_kiri2.object)
        utility.parent_objects(tiang_ke_frame.object, tiang_kanan1.object)
        utility.parent_objects(tiang_ke_frame.object, tiang_kanan2.object)
        utility.parent_objects(tiang_ke_frame.object, tiang_tengah_belakang.object)
        utility.parent_objects(tiang_ke_frame.object, tiang_tengah_depan.object)
        
        self.mainObject = tengah
        self.allObjects={
            "tiang_ke_frame":tiang_ke_frame,
            "depan1": depan1.object,
            "depan2": depan2.object,
            "belakang1": belakang1.object,
            "belakang2": belakang2.object,
            "tengah": tengah.object,
            "tengah_bool": tengah_bool.object,
            "tiang_kiri1": tiang_kiri1.object,
            "tiang_kiri2": tiang_kiri2.object,
            "tiang_kanan1": tiang_kanan1.object,
            "tiang_kanan2": tiang_kanan2.object,
            "tiang_tengah_belakang": tiang_tengah_belakang.object,
            "tiang_tengah_depan": tiang_tengah_depan.object,
        }
        
        
class Frame(basics.BasicElement):
    def create(self):
        plane = basic.Plane(name="plane", coords=(0, 0, 0))
        plane.scale((30, 50, 1))
        
        pole = basic.Cylinder(name="pole", coords=(0, 0, 60))
        # lock rotation of x and z by 90
        
        pole.rotate((90, 0, 90))
        
        pole.scale((1.3, 1.3, 19.8))
        # modifier.wireframe(pole.object, 0.08,0,False)
        
        frame_kanan1 = basic.Cylinder(name="frame_kanan1", coords=(17.2, -11.6, 29.5))
        frame_kanan1.rotate((-20, 0, 0))
        frame_kanan1.scale((0.7, 0.7, 32.11))
        
        frame_kanan2 = basic.Cylinder(name="frame_kanan2", coords=(17.2, 11.6, 29.5))
        frame_kanan2.rotate((20, 0, 0))
        frame_kanan2.scale((0.7, 0.7, 32.11))
        
        frame_kiri1 = basic.Cylinder(name="frame_kiri1", coords=(-17.2, -11.6, 29.5))
        frame_kiri1.rotate((-20, 0, 0))
        frame_kiri1.scale((0.7, 0.7, 32.11))
        
        frame_kiri2 = basic.Cylinder(name="frame_kiri2", coords=(-17.2, 11.6, 29.5))
        frame_kiri2.rotate((20, 0, 0))
        frame_kiri2.scale((0.7, 0.7, 32.11))
        
        kora = Boat("kora", (0, 0, 0))
        
        # # utility.parent_objects( Tangga,pole.object)
        utility.parent_objects(pole.object, kora.allObjects['tiang_ke_frame'].object)
        
        self.mainObject = pole
        self.allObjects = {
            "pole": pole.object,
            "plane": plane.object,
            "frame_kanan1": frame_kanan1.object,
            "frame_kanan2": frame_kanan2.object,
            "frame_kiri1": frame_kiri1.object,
            "frame_kiri2": frame_kiri2.object,
            "boat": kora
        }
        
        
        
class Tangga(basics.BasicElement):
    def create(self):
        tangga1 = basic.Cube(name="tangga1", coords=(18, 0, 8))
        tangga1.scale((2, 10, 8))
        
        tangga2 = basic.Cube(name="tangga2", coords=(22, 0, 6))
        tangga2.scale((2, 10, 6))
        
        tangga3 = basic.Cube(name="tangga3", coords=(26, 0, 4))
        tangga3.scale((2, 10, 4))
        
        tangga4 = basic.Cube(name="tangga4", coords=(30, 0, 2))
        tangga4.scale((2, 10, 2))
        
        self.mainObject = tangga1
        self.allObjects = {
            "tangga1": tangga1.object,
            "tangga2": tangga2.object,
            "tangga3": tangga3.object,
            "tangga4": tangga4.object,
        }
        
        
        
        
class Kora_Kora(basics.BasicElement):
    def __init__(self, name, coordinates = (0, 0, 0)):
        coordinates = (coordinates[0], coordinates[1], coordinates[2] + 1.5)
        super().__init__(name, coordinates)
        self.animate()
        
    def create(self):
        frame = Frame("frame", (0, 0, 0))
        tangga = Tangga("tangga", (0, 0, 0))
        
        utility.parent_objects(frame.allObjects["plane"], tangga.allObjects["tangga1"])
        utility.parent_objects(frame.allObjects["plane"], tangga.allObjects["tangga2"])
        utility.parent_objects(frame.allObjects["plane"], tangga.allObjects["tangga3"])
        utility.parent_objects(frame.allObjects["plane"], tangga.allObjects["tangga4"])
        
        utility.parent_objects(frame.allObjects["plane"], frame.allObjects["frame_kanan1"])
        utility.parent_objects(frame.allObjects["plane"], frame.allObjects["frame_kanan2"])
        utility.parent_objects(frame.allObjects["plane"], frame.allObjects["frame_kiri1"])
        utility.parent_objects(frame.allObjects["plane"], frame.allObjects["frame_kiri2"])
        
        utility.parent_objects(frame.allObjects["plane"], frame.allObjects["pole"])
        
        
        
        
        self.mainObject = frame.allObjects["plane"]
        self.allObjects = {
            "pole": frame.allObjects["pole"],
        }

    def animate(self):
        
        end_frame = bpy.context.scene.frame_end
        mode="maju"
        rotation=0
        
        for i in range(1, end_frame+1):
            if rotation >= 70:
                mode="mundur"
            elif rotation <= -70:
                mode="maju"
                
            if mode=="maju":
                rotation+=1
            else:
                rotation-=1
            
            self.allObjects["pole"].rotation_euler = (math.radians(0), 
                                                      math.radians(0), 
                                                      math.radians(rotation))
            self.allObjects["pole"].keyframe_insert(data_path="rotation_euler", frame=i)