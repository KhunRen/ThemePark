import math
import elements.basics as basics
import primitif.basic as basic
import tools.utility as utility
import tools.modifier as modifier
import bpy
from importlib import reload
reload(basics)

class Horse(basics.BasicElement):
    def create(self):
        horse_body = basic.Cylinder(name="horse_body", coords=(0, 0, 5))
        horse_body.rotate((0, 90, 0))
        horse_body.scale((1, 1, 2))


        kaki_kiri_atas = basic.Cylinder(name="kaki_kiri_atas", coords=(2, 1, 3.5))
        kaki_kiri_atas.scale((0.4, 0.4, 1))
        kaki_kiri_atas.rotate((0, -23, 0))

        kaki_kiri_bawah = basic.Cylinder(
            name="kaki_kiri_bawah", coords=(1.9863, 1.00025, 1.36974))
        kaki_kiri_bawah.scale((0.4, 0.4, 1))
        kaki_kiri_bawah.rotate((0, 23, 0))

        kaki_atas_joint = basic.Sphere(
            name="kaki_atas_joint", coords=(1.5623, 1, 4.51882))
        kaki_atas_joint.scale((0.4, 0.4, 0.4))

        kaki_bawah_joint = basic.Sphere(
            name="kaki_bawah_joint", coords=(2.43635, 1, 2.41469))
        kaki_bawah_joint.scale((0.4, 0.4, 0.4))


        utility.parent_objects(horse_body.object, kaki_atas_joint.object)
        utility.parent_objects(kaki_atas_joint.object, kaki_kiri_atas.object)
        utility.parent_objects(kaki_kiri_atas.object, kaki_bawah_joint.object)
        utility.parent_objects(kaki_bawah_joint.object, kaki_kiri_bawah.object)


        kaki_kanan_atas = basic.Cylinder(name="kaki_kanan_atas", coords=(2, -1, 3.5))
        kaki_kanan_atas.scale((0.4, 0.4, 1))
        kaki_kanan_atas.rotate((0, -23, 0))

        kaki_kanan_bawah = basic.Cylinder(
            name="kaki_kanan_bawah", coords=(1.99283, -1, 1.36475))
        kaki_kanan_bawah.scale((0.4, 0.4, 1))
        kaki_kanan_bawah.rotate((0, 23, 0))

        kaki_kanan_atas_joint = basic.Sphere(
            name="kaki_kanan_atas_joint", coords=(1.5623, -1, 4.51882))
        kaki_kanan_atas_joint.scale((0.4, 0.4, 0.4))

        kaki_kanan_bawah_joint = basic.Sphere(
            name="kaki_kanan_bawah_joint", coords=(2.43635, -1, 2.41469))
        kaki_kanan_bawah_joint.scale((0.4, 0.4, 0.4))

        utility.parent_objects(horse_body.object, kaki_kanan_atas_joint.object)
        utility.parent_objects(kaki_kanan_atas_joint.object, kaki_kanan_atas.object)
        utility.parent_objects(kaki_kanan_atas.object, kaki_kanan_bawah_joint.object)
        utility.parent_objects(kaki_kanan_bawah_joint.object, kaki_kanan_bawah.object)

        kaki_belakang_kiri_atas = basic.Cylinder(
            name="kaki_belakang_kiri_atas", coords=(-1.36425 , 1, 4.00937))
        kaki_belakang_kiri_atas.scale((0.4, 0.4, 0.340045))
        kaki_belakang_kiri_atas.rotate((0, -15.8303, 0))

        kaki_belakang_kiri_bawah = basic.Cylinder(
            name="kaki_belakang_kiri_bawah", coords=(-1.75153 ,0.991739 , 3.12889))
        kaki_belakang_kiri_bawah.scale((0.4, 0.4, 0.436474))
        kaki_belakang_kiri_bawah.rotate((0, 57.0171, 0))

        kaki_belakang_kiri_atas_joint = basic.Sphere(
            name="kaki_belakang_kiri_atas_joint", coords=(-1.50208, 1, 4.4456 ))
        kaki_belakang_kiri_atas_joint.scale((0.4, 0.4, 0.4))

        kaki_belakang_kiri_bawah_joint = basic.Sphere(
            name="kaki_belakang_kiri_bawah_joint", coords=(-1.22382, 1, 3.47683))
        kaki_belakang_kiri_bawah_joint.scale((0.4, 0.4, 0.4))

        kaki_belakang_kiri_foot_joint = basic.Sphere(
            name="kaki_belakang_kiri_foot_joint", coords=(-2.24424, 1.00078 , 2.80205))
        kaki_belakang_kiri_foot_joint.scale((0.35757, 0.35757, 0.35757))

        kaki_belakang_kiri_foot = basic.Cylinder(
            name="kaki_belakang_kiri_foot", coords=(-2.25466 , 1.00078 , 1.4948))
        kaki_belakang_kiri_foot.scale((0.399575, 0.399575, 1.13973))
        kaki_belakang_kiri_foot.rotate((0, 1.26817, 0))

        utility.parent_objects(horse_body.object, kaki_belakang_kiri_atas_joint.object)
        utility.parent_objects(kaki_belakang_kiri_atas_joint.object, kaki_belakang_kiri_atas.object)
        utility.parent_objects(kaki_belakang_kiri_atas.object, kaki_belakang_kiri_bawah_joint.object)
        utility.parent_objects(kaki_belakang_kiri_bawah_joint.object, kaki_belakang_kiri_bawah.object)
        utility.parent_objects(kaki_belakang_kiri_bawah.object, kaki_belakang_kiri_foot_joint.object)
        utility.parent_objects(kaki_belakang_kiri_foot_joint.object, kaki_belakang_kiri_foot.object)

        # right back leg
        kaki_belakang_kanan_atas = basic.Cylinder(
            name="kaki_belakang_kanan_atas", coords=(-1.36425, -1, 4.00937))
        kaki_belakang_kanan_atas.scale((0.4, 0.4, 0.340045))
        kaki_belakang_kanan_atas.rotate((0, -15.8303, 0))

        kaki_belakang_kanan_bawah = basic.Cylinder(
            name="kaki_belakang_kanan_bawah", coords=(-1.75153, -1, 3.12889))
        kaki_belakang_kanan_bawah.scale((0.4, 0.4, 0.436474))
        kaki_belakang_kanan_bawah.rotate((0, 57.0171, 0))

        kaki_belakang_kanan_atas_joint = basic.Sphere(
            name="kaki_belakang_kanan_atas_joint", coords=(-1.50208, -1, 4.4456))
        kaki_belakang_kanan_atas_joint.scale((0.4, 0.4, 0.4))

        kaki_belakang_kanan_bawah_joint = basic.Sphere(
            name="kaki_belakang_kanan_bawah_joint", coords=(-1.22382, -1, 3.47683))
        kaki_belakang_kanan_bawah_joint.scale((0.4, 0.4, 0.4))

        kaki_belakang_kanan_foot_joint = basic.Sphere(
            name="kaki_belakang_kanan_foot_joint", coords=(-2.24424, -1.00078, 2.80205))
        kaki_belakang_kanan_foot_joint.scale((0.35757, 0.35757, 0.35757))

        kaki_belakang_kanan_foot = basic.Cylinder(
            name="kaki_belakang_kanan_foot", coords=(-2.25466, -1.00078, 1.4948))
        kaki_belakang_kanan_foot.scale((0.399575, 0.399575, 1.13973))
        kaki_belakang_kanan_foot.rotate((0, 1.26817, 0))

        utility.parent_objects(horse_body.object, kaki_belakang_kanan_atas_joint.object)
        utility.parent_objects(kaki_belakang_kanan_atas_joint.object, kaki_belakang_kanan_atas.object)
        utility.parent_objects(kaki_belakang_kanan_atas.object, kaki_belakang_kanan_bawah_joint.object)
        utility.parent_objects(kaki_belakang_kanan_bawah_joint.object, kaki_belakang_kanan_bawah.object)
        utility.parent_objects(kaki_belakang_kanan_bawah.object, kaki_belakang_kanan_foot_joint.object)
        utility.parent_objects(kaki_belakang_kanan_foot_joint.object, kaki_belakang_kanan_foot.object)



        leher_joint = basic.Sphere(name="leher_joint", coords=(1.96719, 0, 4.98078))
        leher_joint.scale((0.932572, 0.932572, 0.932572))

        leher = basic.Cylinder(name="leher", coords=(2.6332, 0.004759, 6.12217))
        leher.rotate((0, 31.2115, 0))
        leher.scale((0.740471, 0.781058, 0.664706))

        head_joint = basic.Sphere(name="head_joint", coords=(2.95323, 0, 6.65809))
        head_joint.scale((0.686874, 0.686874, 0.686874))

        utility.parent_objects(horse_body.object, leher_joint.object)
        utility.parent_objects(leher_joint.object, leher.object)
        utility.parent_objects(leher.object, head_joint.object)

        pole = basic.Cylinder(name="pole", coords=(0, 0, 12))
        pole.scale((0.2, 0.2, 7))

        utility.parent_objects(pole.object, horse_body.object)


        head = basic.Cylinder(name="head", coords=(3.9741, 0, 7.2539))
        head.rotate((0, 119.69, 0))
        head.scale((0.662, 0.659, 0.985))

        back_head = basic.Sphere(name="back_head", coords=(3.18571, 0, 7.70773 ))
        back_head.scale((0.652473, 0.652473, 0.652473))

        ear_left = basic.Cone(name="ear_left", coords=(3.37645, 0.450177, 8.41217))
        ear_left.rotate((-25.5272, 0, 0))
        ear_left.scale((0.152111, 0.329727, 0.313585))

        ear_right = basic.Cone(name="ear_right", coords=(3.36372, -0.416596, 8.40108))
        ear_right.rotate((25.5272, 0, 0))
        ear_right.scale((0.152111, 0.329727, 0.313585))

        utility.parent_objects(head_joint.object, head.object)
        utility.parent_objects(head.object, back_head.object)
        utility.parent_objects(head.object, ear_left.object)
        utility.parent_objects(head.object, ear_right.object)

        kaki_kiri_depan = kaki_atas_joint
        kaki_kiri_depan.rename("kaki_kiri")
        kaki_kanan_depan = kaki_kanan_atas_joint
        kaki_kanan_depan.rename("kaki_kanan")
        kaki_kanan_depan.rotate((0, -40, 0))

        butt = basic.Sphere(name="butt", coords=(-1.86139 , 0, 4.99036 ))
        butt.scale((0.952686, 0.952686, 0.952686))

        tail = basic.Cube(name="tail", coords=(-3.23612, 0, 4.70232))
        tail.rotate((0, 44.4576, 0))
        tail.scale((0.44, 0.34, 2.03))

        modifier.subdivision_surface(tail.object, 2)

        utility.parent_objects(horse_body.object, butt.object)
        utility.parent_objects(butt.object, tail.object)

        kaki_kiri_belakang = kaki_belakang_kiri_atas_joint
        kaki_kiri_belakang.rename("kaki_kiri_belakang")
        kaki_kiri_belakang.rotate((0, -18.2023, 0))
        kaki_kanan_belakang = kaki_belakang_kanan_atas_joint
        kaki_kanan_belakang.rename("kaki_kanan_belakang")
        
        self.mainObject = pole.object
        self.allObjects = {
            "body": horse_body.object,
            "kaki_kiri_atas": kaki_atas_joint.object,
            "kaki_kiri_bawah": kaki_bawah_joint.object,
            "kaki_kanan_atas": kaki_kanan_atas_joint.object,
            "kaki_kanan_bawah": kaki_kanan_bawah_joint.object,
            "kaki_belakang_kiri_atas": kaki_belakang_kiri_atas_joint.object,
            "kaki_belakang_kiri_bawah": kaki_belakang_kiri_bawah_joint.object,
            "kaki_belakang_kiri_foot": kaki_belakang_kiri_foot_joint.object,
            "kaki_belakang_kanan_atas": kaki_belakang_kanan_atas_joint.object,
            "kaki_belakang_kanan_bawah": kaki_belakang_kanan_bawah_joint.object,
            "kaki_belakang_kanan_foot": kaki_belakang_kanan_foot_joint.object,
            "leher": leher_joint.object,
            "head": head_joint.object,
        }
            
class Komedi_putar(basics.BasicElement):
    def __init__(self, name, coordinates):
        coordinates = (coordinates[0], coordinates[1], coordinates[2] + 1)
        super().__init__(name, coordinates)
        self.horses = []
        self.plot_horse()
        self.animate()
        
    def create(self):
        upper_base = basic.Cylinder(name="upper_base", coords=(0, 0, 1))
        upper_base.scale((20.2937, 20.2937, 1.07793))
        
        lower_base = basic.Cylinder(name="lower_base", coords=(0, 0, 0.413442))
        lower_base.scale((22.3037, 22.3037, 0.507933))
        
        
        center_pole = basic.Cylinder(name="center_pole", coords=(0, 0, 14.5379))
        center_pole.scale((5, 5, 13.79))
        
        top_part = basic.Cone(name="top_part", coords=(0, 0, 27.9213 ))
        top_part.scale((26.3782, 26.3782, 8.49961))
        
        top_part_holder = basic.Torus(name="top_part_holder", coords=(0, 0, 18.3793))
        top_part_holder.scale((23.6526, 23.6526, 7.92263))
        
        utility.parent_objects(upper_base.object, lower_base.object)
        utility.parent_objects(upper_base.object, center_pole.object)
        utility.parent_objects(upper_base.object, top_part.object)
        utility.parent_objects(upper_base.object, top_part_holder.object)
        
        
        self.mainObject = upper_base.object
        self.allObjects = {
            "upper_base": upper_base.object,
            "lower_base": lower_base.object,
            "center_pole": center_pole.object,
            "top_part": top_part.object,
            "top_part_holder": top_part_holder.object
        }
    def plot_horse(self):
        for i in range(0, 360, 45):
            x = 15 * math.cos(math.radians(i))
            y = 15 * math.sin(math.radians(i))
            height = 14
            if i % 90 == 0:
                height = 17
            horse = Horse("horse", (x, y, height))
            horse.rotate((0, 0, i+90))
            utility.parent_objects(self.allObjects["center_pole"], horse.mainObject)
            self.horses.append(horse)
            
    def animate(self):
        end_frame = bpy.context.scene.frame_end
        for i in range(1, end_frame+1):
            self.allObjects["center_pole"].rotation_euler[2] = math.radians(i/2)
            self.allObjects["center_pole"].keyframe_insert(data_path="rotation_euler", frame=i)
            for horse in self.horses:
                movement = 0.007
                if self.horses.index(horse) % 2 == 0:
                    movement = -0.007
                if i % 100 <= 50:
                    horse.mainObject.location.z += movement
                else:
                    horse.mainObject.location.z -= movement
                
                horse.mainObject.keyframe_insert(data_path="location", frame=i)
        
        
        
        