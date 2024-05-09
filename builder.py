import primitif.basic as basic
import tools.utility as utility
import tools.render as render
import tools.objectProperty as objectProperty
import tools.modifier as modifier
import elements.komediputar as komediputar
import elements.etc as etc
import objs.importer as objimporter
import elements.ombakbanyu as ombakbanyu
import lights.basic as lightbasic
import os
from importlib import reload

reload(basic)
reload(utility)
reload(objectProperty)
reload(modifier)
reload(komediputar)
reload(lightbasic)
reload(render)
reload(objimporter)
reload(etc)
reload(ombakbanyu)

utility.clear_scene()
utility.clear_materials()
utility.delete_light_cache()


komedi = komediputar.Komedi_putar("komedi", (0, 0, 0))
komedi.scale((1.04592,1.04592,0.026723))
komedi.translate((0, 0, 0.049222))

ground = etc.Ground("ground", (0, 0, 0))

gate = etc.Gate("gate", (7.92662, 0, 0))
gate.scale((1.66563,1.28508,0.447452))

ombak_banyu = ombakbanyu.OmbakBanyu("Ombak Banyu", (0,-5.33983,-1.44876 ))
ombak_banyu.scale((0.988065,0.988065,0.033877))

render.hide_hdri("//HDRs/satara_night_2k.hdr")
render.set_viewport_shading_material(True, True, 0, 1, 1, 0)
render.eevee_sampling(64, 16, False)
render.eevee_ambient_occlusion()
render.eevee_bloom()
render.eevee_screen_space_reflections()
render.color_management("sRGB", "Filmic", "Medium High Contrast")

irradiance = lightbasic.Irradiance_Volume("irradiance", (0, 0, 0.65),4.8,0,1,(6,6,6),0.01,10)
irradiance.scale((1.5,1.5,1.5))
utility.bake_indirect_lighting()

