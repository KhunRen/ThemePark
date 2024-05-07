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
        
        self.allObjects={
            "tiang_ke_frame":tiang_ke_frame
        }
        
        
class Frame(basics.BasicElement):
    def create(self):
        plane = basic.Plane(name="plane", coords=(0, 0, 0))
        plane.scale((30, 50, 1))
        
        pole = basic.Cylinder(name="pole", coords=(0, 0, 60))
        # lock rotation of x and z by 90
        
        pole.rotate((90, 90, 90))
        
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
        utility.parent_objects(pole.object, kora.allObjects['tiang_ke_frame'].object)
        
        self.allObjects = {
            "pole": pole.object,
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
        
        
        
        
class Kora_Kora(basics.BasicElement):
    def __init__(self, name, coordinates = (0, 0, 0)):
        coordinates = (coordinates[0], coordinates[1], coordinates[2] + 1.5)
        super().__init__(name, coordinates)
        self.animate()
        
    def create(self):
        kora2 = Frame("kora2", (0, 0, 0))
        kora3 = Tangga("kora3", (0, 0, 0))
        
        self.allObjects = {
            "pole": kora2.allObjects["pole"],
        }

    def animate(self):
        end_frame = bpy.context.scene.frame_end
        rotation_direction = 1  # Arah rotasi awal adalah positif
        
        for i in range(1, end_frame+1):
            # Mengonversi derajat ke radian
            rotation_angle = math.radians(i * 2 * rotation_direction)
            
            # Membatasi rotasi dalam rentang 0 sampai 2*pi (360 derajat)
            rotation_angle %= 2 * math.pi
            
            # Mengubah arah rotasi jika mencapai batas tertentu
            if rotation_angle >= math.radians(333):
                rotation_direction = -1
            elif rotation_angle <= math.radians(27):
                rotation_direction = 1
            
            self.allObjects["pole"].rotation_euler[1] = rotation_angle
            self.allObjects["pole"].keyframe_insert(data_path="rotation_euler", frame=i)