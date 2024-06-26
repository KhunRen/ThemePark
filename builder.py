import primitif.basic as basic
import tools.utility as utility
import tools.render as render
import tools.objectProperty as objectProperty
import tools.modifier as modifier
import elements.komediputar as komediputar
import elements.etc as etc
import elements.hysteria as Hysteria
import objs.importer as objimporter
import elements.ombakbanyu as ombakbanyu
import lights.basic as lightbasic
import os
import elements.korakora as korakora
from importlib import reload

reload(basic)
reload(utility)
reload(objectProperty)
reload(modifier)
reload(komediputar)
reload(Hysteria)
reload(lightbasic)
reload(render)
reload(objimporter)
reload(etc)
reload(ombakbanyu)
reload(korakora)


def build():

    utility.clear_scene()
    utility.clear_materials()
    utility.delete_light_cache()

    print("making ground")
    ground = etc.Ground("ground", (0, 0, 0))

    hysteria = Hysteria.Hysteria("Hysteria", (-5.29048, 0, 0.44713))
    hysteria.scale((0.320664, 0.320664, 1.45756))

    print("making komedi")
    komedi = komediputar.Komedi_putar("komedi", (0, 0, 0))
    komedi.scale((1.04592, 1.04592, 0.026723))
    komedi.translate((0, 0, 0.049222))

    print("making gate")
    gate = etc.Gate("gate", (7.92662, 0, 0))
    gate.scale((1.66563, 1.28508, 0.447452))

    print("making ombak banyu")
    ombak_banyu = ombakbanyu.OmbakBanyu("Ombak Banyu", (0, -5.33983, -1.44876))
    ombak_banyu.scale((0.988065, 0.988065, 0.033877))

    print("making korakora")
    korakora_obj = korakora.Kora_Kora("korakora", (0, 7.13349, -1.507104))
    korakora_obj.rotate((0, 0, -90))
    korakora_obj.scale((0.870099, 1.45017, 0.029003))

    render.hide_hdri("//HDRs/satara_night_2k.hdr")
    render.set_viewport_shading_material(True, True, 0, 1, 1, 0)
    render.eevee_sampling(64, 16, False)
    render.eevee_ambient_occlusion()
    render.eevee_bloom()
    render.eevee_screen_space_reflections()
    render.color_management("sRGB", "Filmic", "Medium High Contrast")

    print("making light")
    irradiance = lightbasic.Irradiance_Volume(
        "irradiance", (0, 0, 0.65), 4.8, 0, 1, (6, 6, 6), 0.01, 10)
    irradiance.scale((1.5, 1.5, 1.5))

    irradiance = lightbasic.Irradiance_Volume(
        "irradiance2", (-5.32997, 0, 1.56803), 4.8, 0, 1, (3, 3, 3), 0.01, 10)
    irradiance.scale((1.5, 1.5, 1.5))
    
    irradiance = lightbasic.Irradiance_Volume(
        "irradiance2", (-0.029212 , -5.45144 , 1.08465 ), 4.8, 0, 1, (3, 3, 3), 0.01, 10)
    irradiance.scale((1.5, 1.5, 1.5))
    
    

    print("baking")
    utility.bake_indirect_lighting()

    print("done!")
