import primitif.basic as basic
import tools.utility as utility
import tools.render as render
import tools.objectProperty as objectProperty
import tools.modifier as modifier
import elements.komediputar as komediputar
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

folder_path = os.path.realpath(__file__)
folder_path = folder_path.replace("builder.py", "")

utility.clear_scene()
utility.clear_materials()
render.set_HDRI("//HDRs/satara_night_2k.hdr")
render.set_viewport_shading_material(True,True,0,1,1,0)
render.eevee_sampling(64, 16, False)
render.eevee_ambient_occlusion()
render.eevee_bloom()
render.eevee_screen_space_reflections()
render.color_management("sRGB","Filmic","Medium High Contrast")

komedi = komediputar.Komedi_putar("komedi", (0, 0, 0))
# komedi.rotate((0, 90, 0))
# komedi.translate((0, 0, 10))
komedi.scale((1.04592,1.04592,0.026723))
komedi.translate((0, 0, 0.049222))

# lightbasic.Light_probe_irradiance_volume("light_probe_irradiance_volume", (0, 0, 0), distance=0.1, falloff=0.1, intensity=1, resolution=(4,4,4), clipping_start=0, clipping_end=10, visibility_bias=1, visibility_bleed_bias=0, visibility_blur=0)

# kuda = komediputar.Horse("kuda", (0, 0, 0))
# kuda.translate((0, 10, 12))
# bench = komediputar.Bench("bench", (0, 0, 0))