import primitif.basic as basic
import tools.utility as utility
import tools.render as render
import tools.objectProperty as objectProperty
import tools.modifier as modifier
import elements.komediputar as komediputar
import elements.ombakbanyu_bawah as ombakbanyubawah
import elements.ombakbanyu_atas as ombakatas
import elements.ombakbanyu as ombakbanyu
import lights.basic as lightbasic
import os
from importlib import reload

reload(basic)
reload(utility)
reload(objectProperty)
reload(modifier)
reload(komediputar)
reload(ombakbanyu)

utility.clear_scene()

# komedi = ombakbanyubawah.Ombak_banyu("ombakbawah", (0, 0, 0))
# komedi = komediputar.Komedi_putar("komedi", (0, 0, 0))
reload(ombakatas)
ombak_banyu = ombakbanyu.OmbakBanyu("Ombak Banyu", (0,0,0))

# komedi = komediputar.Komedi_putar("komedi", (0, 0, 0))
# ombak = ombakatas.OmbakBanyu_Atas("ombakatas", (0,0,0))
# komedi.rotate((0, 90, 0))
# komedi.translate((0, 0, 10))

# kuda = komediputar.Horse("kuda", (0, 0, 0))
# kuda.translate((0, 10, 12))
# bench = komediputar.Bench("bench", (0, 0, 0))
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
