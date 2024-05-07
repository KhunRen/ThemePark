import math
import elements.basics as basics
import primitif.basic as basic
import tools.utility as utility
import tools.modifier as modifier
import tools.objectProperty as objectProperty
import tools.materials as materials
import bpy
from importlib import reload
import random
reload(basics)
reload(materials)

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
        modifier.wireframe(pole.object, 0.08,0,False)

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
        modifier.weld(tail.object, 0.552)

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
        
class Bench(basics.BasicElement):
    def create(self):
        pole = basic.Cylinder(name="pole", coords=(0, 0, 12))
        pole.scale((0.2, 0.2, 7))
        modifier.wireframe(pole.object, 0.08,0,False)
        self.mainObject = pole.object
        
        back_chair_top = basic.Cube(name="back_chair_top", coords=(-3.01355, 0, 4.09991))
        back_chair_top.rotate((0,-17.8158,0))
        back_chair_top.scale((0.14659,2.29195,0.879661))
        
        back_chart_bottom = basic.Cube(name="back_chair_bottom", coords=(-2.04148 , 0, 3.17498 ))
        back_chart_bottom.rotate((0, 90,0))
        back_chart_bottom.scale((0.14659,2.29195,0.879661))
        
        front_chair_top = basic.Cube(name="front_chair_top", coords=(2.05936,0,4.09991))
        front_chair_top.rotate((0,-17.8158,0))
        front_chair_top.scale((0.14659,2.29195,0.879661))
        
        front_chair_bottom = basic.Cube(name="front_chair_bottom", coords=(3.03143,0,3.17498))
        front_chair_bottom.rotate((0,90,0))
        front_chair_bottom.scale((0.14659,2.29195,0.879661))
        
        left_front_wheel = basic.Cube(name="left_front_wheel", coords=(2.65948, 2.39578 , 1.75656))
        left_front_wheel.scale((1.9568,0.241142,2.14919))
        modifier.subdivision_surface(left_front_wheel.object, 2)
        
        left_back_wheel = basic.Cube(name="left_back_wheel", coords=(-2.19804,2.39578,1.75656 ))
        left_back_wheel.scale((1.9568,0.241142,2.14919))
        modifier.subdivision_surface(left_back_wheel.object, 2)
        
        right_front_wheel = basic.Cube(name="right_front_wheel", coords=(2.65948 , -2.39456, 1.75656))
        right_front_wheel.scale((1.9568,0.241142,2.14919))
        modifier.subdivision_surface(right_front_wheel.object, 2)
        
        right_back_wheel = basic.Cube(name="right_back_wheel", coords=(-2.19804,-2.36187,1.75656))
        right_back_wheel.scale((1.9568,0.241142,2.14919))
        modifier.subdivision_surface(right_back_wheel.object, 2)
        
        modifier.apply_all_modifier(left_front_wheel.object)
        modifier.apply_all_modifier(left_back_wheel.object)
        modifier.apply_all_modifier(right_front_wheel.object)
        modifier.apply_all_modifier(right_back_wheel.object)
        

        base = basic.Cube(name="base", coords=(0.629296,0.042405,1.10786))
        base.scale((4.61913,2.31373,0.255156))
        
        pole_holder = basic.Cube(name="pole_holder", coords=(0,0,3.14642))
        pole_holder.scale((0.326266,0.326266,1.88622))
        
        right_door = basic.Cube(name="right_door", coords=(0,-2.07894,1.94006))
        right_door.scale((2.23383,0.256342,1.26739))
        
        left_door = basic.Cube(name="left_door", coords=(0,2.10664,1.94006 ))
        left_door.scale((2.22383,0.256342,1.26739))
        
        back_board = basic.Cube(name="back_board", coords=(-3.62773,0.055628,3.03618))
        back_board.scale((0.400066,2.32863,1.87668))
        
        front_bottom_board = basic.Cube(name="front_bottom_board", coords=(2.85704 ,0.055628,2.16409))
        front_bottom_board.scale((0.699731,2.32863,1.05057))
        
        back_bottom_board = basic.Cube(name="back_bottom_board", coords=(-2.15277 ,0.055628 ,2.16409))
        back_bottom_board.scale((0.699731,2.32863,1.05057))
        
        front_right_monkey = basic.Suzanne(name="front_right_monkey", coords=(2.62468,-2.60427,1.76302  ))
        back_right_monkey = basic.Suzanne(name="back_right_monkey", coords=(-2.25274,-2.60427,1.76302))
        
        front_left_monkey = basic.Suzanne(name="front_left_monkey", coords=(2.62468,2.62928,1.76302 ))
        front_left_monkey.rotate((0,0,180))
        
        back_left_monkey = basic.Suzanne(name="back_left_monkey", coords=(-2.24102 ,2.62928,1.76302))
        back_left_monkey.rotate((0,0,180))
        
        utility.parent_objects(pole.object, base.object)
        utility.parent_objects(base.object, back_chair_top.object)
        utility.parent_objects(base.object, back_chart_bottom.object)
        utility.parent_objects(base.object, front_chair_top.object)
        utility.parent_objects(base.object, front_chair_bottom.object)
        utility.parent_objects(base.object, left_front_wheel.object)
        utility.parent_objects(base.object, left_back_wheel.object)
        utility.parent_objects(base.object, right_front_wheel.object)
        utility.parent_objects(base.object, right_back_wheel.object)
        utility.parent_objects(base.object, pole_holder.object)
        utility.parent_objects(base.object, right_door.object)
        utility.parent_objects(base.object, left_door.object)
        utility.parent_objects(base.object, back_board.object)
        utility.parent_objects(base.object, front_bottom_board.object)
        utility.parent_objects(base.object, back_bottom_board.object)
        utility.parent_objects(base.object, front_right_monkey.object)
        utility.parent_objects(base.object, back_right_monkey.object)
        utility.parent_objects(base.object, front_left_monkey.object)
        utility.parent_objects(base.object, back_left_monkey.object)
        
        
        self.allObjects = {
            "back_chair_top": back_chair_top.object,
            "back_chart_bottom": back_chart_bottom.object,
            "front_chair_top": front_chair_top.object,
            "front_chair_bottom": front_chair_bottom.object,
            "left_front_wheel": left_front_wheel.object,
            "left_back_wheel": left_back_wheel.object,
            "right_front_wheel": right_front_wheel.object,
            "right_back_wheel": right_back_wheel.object,
            "base": base.object,
            "pole_holder": pole_holder.object,
            "right_door": right_door.object,
            "left_door": left_door.object,
            "back_board": back_board.object,
            "front_bottom_board": front_bottom_board.object,
            "back_bottom_board": back_bottom_board.object,
            "front_right_monkey": front_right_monkey.object,
            "back_right_monkey": back_right_monkey.object,
            "front_left_monkey": front_left_monkey.object,
            "back_left_monkey": back_left_monkey.object
        }
        
class Komedi_putar(basics.BasicElement):
    def __init__(self, name, coordinates):
        coordinates = (coordinates[0], coordinates[1], coordinates[2] + 1.5)
        super().__init__(name, coordinates)
        self.horses = []
        self.plot_horse()
        self.animate()
        
    def create(self):
        base = basic.Cylinder(name="base", coords=(0, 0, -0.5))
        base.scale((31.1973, 31.1973, 0.79709))
        modifier.subdivision_surface(base.object, 3)
        
        upper_base = basic.Cylinder(name="upper_base", coords=(0, 0, 1))
        upper_base.scale((20.2937, 20.2937, 1.07793))
        
        lower_base = basic.Cylinder(name="lower_base", coords=(0, 0, 0.413442))
        lower_base.scale((22.3037, 22.3037, 0.507933))
        
        
        center_pole = basic.Cylinder(name="center_pole", coords=(0, 0, 14.5379))
        center_pole.scale((5, 5, 13.79))
        
        top_part = basic.Cone(name="top_part", coords=(0, 0, 35.9213 ))
        top_part.scale((26.3782, 26.3782, 8.64961))
        modifier.wireframe(top_part.object, 0.024, 1, False)
        
        top_part_holder = basic.Torus(name="top_part_holder", coords=(0, 0, 19.3793))
        top_part_holder.scale((23.6526, 23.6526, 7.92263))
        
        top_banner = basic.Torus(name="top_banner", coords=(0, 0, 27.1721 ))
        top_banner.scale((23.8237,23.8237,23.8237))
        
        top_wire = basic.Cylinder(name="top_wire", coords=(0, 0, 22.1694 ))
        top_wire.scale((29.0064, 29.0064, 2.09852))
        modifier.wireframe(top_wire.object, 0.02)
        modifier.subdivision_surface(top_wire.object, 1)
        
        fence = basic.Cylinder(name="fence", coords=(0, 0, 1.15))
        fence.scale((27.3717,27.3717,1.47164))
        modifier.wireframe(fence.object, 0.02)
        
        top_closer = basic.Cylinder(name="top_closer", coords=(0, 0, 23.7899))
        top_closer.scale((20.2084, 20.2084, 1.22842))
        
        pole_decors = []
        
        for i in range(0, 3):
            pole_decor = basic.Cylinder(name=f"pole_decor{i}", coords=(0, 0, 20.0281- (7*i)))
            pole_decor.scale((6.50674, 6.50674, 2.75145))
            modifier.wireframe(pole_decor.object, 0.051,0,False)
            utility.parent_objects(center_pole.object, pole_decor.object)
            
            pole_decors.append(pole_decor)
        
        top_ornament = basic.Cylinder(name="top_ornament", coords=(0, 0, 25.1319))
        top_ornament.scale((23.8683,23.8683,8.4359))
        modifier.wireframe(top_ornament.object, 0.02)
        modifier.subdivision_surface(top_ornament.object, 1)
        modifier.displace(top_ornament.object, 1, 0.959)
        modifier.cast(top_ornament.object,-0.86)
        
        utility.parent_objects(base.object,top_ornament.object)
        utility.parent_objects(base.object, upper_base.object)
        utility.parent_objects(base.object, lower_base.object)
        utility.parent_objects(base.object, center_pole.object)
        utility.parent_objects(base.object, top_part.object)
        utility.parent_objects(base.object, top_part_holder.object)
        utility.parent_objects(base.object, top_banner.object)
        utility.parent_objects(base.object, top_wire.object)
        utility.parent_objects(base.object, fence.object)
        utility.parent_objects(base.object, top_closer.object)
        
        # ================== materials
        
        blue_plastic = materials.create_material("blue plastic",(0.048171,0.250158,0.313989,1),0,1,0)
        materials.assign_material(top_part.object, blue_plastic)
        materials.assign_material(top_part_holder.object, blue_plastic)
        materials.assign_material(top_closer.object, blue_plastic)
        materials.assign_material(top_ornament.object, blue_plastic)
        materials.assign_material(fence.object, blue_plastic)
        
        red_dull = materials.create_material("red dull",(0.610496,0.078187,0.05448,1),0,1,0.311)
        materials.assign_material(top_banner.object, red_dull)
        materials.assign_material(lower_base.object, red_dull)
        materials.assign_material(base.object, red_dull)
        for pole_decor in pole_decors:
            materials.assign_material(pole_decor.object, red_dull)
        
        gold = materials.create_material("gold",(0.98225,1,0.701102,1),1,1,0.135,(0.991101,0.952603,0.32074,1),0.100)
        materials.assign_material(top_wire.object, gold)
        
        cream_matte = materials.create_material("cream matte",(0.846873,0.571124,0.274677,1),0,0.486,0.5)
        materials.assign_material(upper_base.object, cream_matte)
        
        mirror_matte = materials.create_material("mirror matte",(0.8,0.8,0.8,1),0.676,1,0)
        materials.assign_material(center_pole.object, mirror_matte)
        
        # ================== materials
        
        self.mainObject = base.object
        self.allObjects = {
            "upper_base": upper_base.object,
            "lower_base": lower_base.object,
            "center_pole": center_pole.object,
            "top_part": top_part.object,
            "top_part_holder": top_part_holder.object,
            "top_banner": top_banner.object,
            "top_wire": top_wire.object,
            "fence": fence.object
        }
    def plot_horse(self):
        for i in range(0, 360, 45):
            x = 15 * math.cos(math.radians(i))
            y = 15 * math.sin(math.radians(i))
            height = 16
            if i % 90 == 0:
                height = 19
            
            random_num = random.randint(0, 1)
            horse = None
            # horse = Horse("horse", (x, y, height))
            
            if random_num == 1:
                horse = Bench("bench", (x, y, height))
            else:
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
        
        
        
        