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

class RotateThing(basics.BasicElement):
    def __init__(self, name, coordinates):
        super().__init__(name, coordinates)

    
    def create(self):
        Cutter1 = basic.Cylinder(name="Cutter1", coords=(0, 0, 100))
        Cutter1.scale((50, 50, 15)) 
        red_dull = materials.create_material("red dull",(0.610496,0.078187,0.05448,1),0,1,0.311)
        materials.assign_material(Cutter1.object, red_dull)
            
        self.mainObject = Cutter1.object
        self.allObjects = {
            "Cutter1" : Cutter1,
        }
        # Cutter1 = bpy.context.object
    
        yangNaikTurun = basic.Cylinder(name="yangNaikTurun", coords=(0, 0, 100))
        yangNaikTurun.scale((40, 40, 15)) 
        yangNaikTurun = bpy.context.object

        modifier.boolean_difference(Cutter1.object, yangNaikTurun)

        bpy.data.objects.remove(yangNaikTurun, do_unlink=True)

        # kursi1 = bpy.context.object
        for i in range(0, 360, 20):
            x = 60 * math.cos(math.radians(i))
            y = 60 * math.sin(math.radians(i))
            kursi1 = Chair("chair",(x, y, 90))
            kursi1.rotate((0,0,i+90))
            # kursi2 = Chair("chair2",(17, -59, 90))
            utility.parent_objects(Cutter1.object, kursi1.mainObject)
        
        

class Hysteria(basics.BasicElement):
    def __init__(self, name, coordinates):
        coordinates = (coordinates[0], coordinates[1], coordinates[2] + 1)
        super().__init__(name, coordinates)
        self.RotateThing = []
        self.glued()
        self.animate()

    def create(self):
        center_pole = basic.Cylinder(name="center_pole", coords=(0, 0, 100))
        center_pole.scale((22, 22, 100))  

        red_dull = materials.create_material("red dull",(0.610496,0.078187,0.05448,1),0,1,0.311)
        materials.assign_material(center_pole.object, red_dull)
            
        atap = basic.Cube(name="atap", coords=(0,0,200))
        atap.scale((40,40,10))
        atap.rotate((0,0,-45))

        blue_plastic = materials.create_material("blue plastic",(0.048171,0.250158,0.313989,1),0,1,0)
        materials.assign_material(atap.object, blue_plastic)

        penyangga1 = basic.Cylinder(name="penyangga1", coords=(-25, 0, 100))
        penyangga1.scale((6, 6, 100))      
        
        penyangga2 = basic.Cylinder(name="penyangga2", coords=(25, 0, 100))
        penyangga2.scale((6, 6, 100))    

        penyangga3 = basic.Cylinder(name="penyangga3", coords=(0, -25, 100))
        penyangga3.scale((6, 6, 100))    

        penyangga4 = basic.Cylinder(name="penyangga4", coords=(0, 25, 100))
        penyangga4.scale((6, 6, 100))   
        neon = materials.create_material("neon",(0.8,0.8,0.8,1),0,0.5,0.5,(1,0.290841,0.75787,1),7)
        materials.assign_material(penyangga1.object, neon)
        materials.assign_material(penyangga2.object, neon)
        materials.assign_material(penyangga3.object, neon)
        materials.assign_material(penyangga4.object, neon)

        utility.parent_objects(center_pole.object, atap.object)
        utility.parent_objects(center_pole.object, penyangga1.object)
        utility.parent_objects(center_pole.object, penyangga2.object)
        utility.parent_objects(center_pole.object, penyangga3.object)
        utility.parent_objects(center_pole.object, penyangga4.object)

        self.mainObject = center_pole.object
        self.allObjects = {
            "atap" : atap.object,
            "penyangga1" : penyangga1.object,
            "penyangga2" : penyangga2.object,
            "penyangga3" : penyangga3.object,
            "penyangga4" : penyangga4.object,
            "center_pole" : center_pole.object
        }

    def glued(self):
        rotateThing = RotateThing("RotateThing", coordinates=(0,0,15))
        utility.parent_objects(self.allObjects["center_pole"], rotateThing.mainObject)
        self.RotateThing.append(rotateThing)
        self.allObjects["RotateThing"] = rotateThing.mainObject #ini biar allObj nya kebawa
        

    def animate(self):
        end_frame = bpy.context.scene.frame_end
        for i in range(1, end_frame):
            self.allObjects["RotateThing"].rotation_euler[2] = math.radians(i*3)
            self.allObjects["RotateThing"].keyframe_insert(data_path="rotation_euler", frame=i)

            for kursi1 in self.RotateThing:
                if i % end_frame <= 20 or (i % end_frame >60 and i % end_frame <= 100) or (i % end_frame >140 and i % end_frame <= 180) or (i % end_frame >220 and i % end_frame <= 260) or (i % end_frame >300 and i % end_frame <= 340) or (i % end_frame >380 and i % end_frame <= 420) or (i % end_frame >460 and i % end_frame <= 500):
                    movement = 0.2 
                else:
                    movement = -0.2 
                    
                kursi1.mainObject.location.z += movement
                kursi1.mainObject.keyframe_insert(data_path="location", frame=i)

class Chair(basics.BasicElement):
    def create(self):
        seat = basic.Cube(name="tempat_duduk", coords=(0, -51, 0))
        seat.scale((8, 6, 2))
        
        atasKursi = basic.Cube(name="atas_kursi", coords=(0, -51, 10))
        atasKursi.scale((8, -2, 12))
        
        pengamanKanan = basic.Cube(name="pengaman_kanan", coords=(6.0389,-57.232,11.098))
        pengamanKanan.scale((-0.757, -0.557, 12.000))
        pengamanKanan.rotate((-27.858, -0.86724, -0.20174))
        
        pengamanKiri = basic.Cube(name="pengaman_kiri", coords=(-6.0905, -57.56, 10.15))
        pengamanKiri.scale((-0.757, -0.557, 12.000))
        pengamanKiri.rotate((-26.928, -0.92175, -0.13101))

        pengamanBawah = basic.Cube(name="pengaman_Bawah", coords=(0.040151, -61, 2.8849))
        pengamanBawah.scale((-0.757, -0.557, 6.202))
        pengamanBawah.rotate((-76.986, 87.504, -77.137))

        utility.parent_objects(seat.object, atasKursi.object)
        utility.parent_objects(atasKursi.object, pengamanKanan.object)
        utility.parent_objects(atasKursi.object, pengamanKiri.object)
        utility.parent_objects(atasKursi.object, pengamanBawah.object)

        blue_plastic = materials.create_material("blue plastic",(0.048171,0.250158,0.313989,1),0,1,0)
        materials.assign_material(atasKursi.object, blue_plastic)
        materials.assign_material(pengamanKiri.object, blue_plastic)
        materials.assign_material(pengamanKanan.object, blue_plastic)
        materials.assign_material(pengamanBawah.object, blue_plastic)

        atasKursi.translate((0, -4, 0))
        

        self.mainObject = seat.object
        self.allObjects = {
            "atas_kursi" : atasKursi.object,
            "pengaman_kanan" : pengamanKanan.object,
            "pengaman_kiri" : pengamanKiri.object,
            "pengaman_bawah" : pengamanBawah.object,
        }