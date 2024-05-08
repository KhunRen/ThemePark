import primitif.basic as basic
import tools.utility as utility
import tools.render as render
import tools.objectProperty as objectProperty
import tools.modifier as modifier
import lights.basic as lightbasic
import objs.importer as objimporter
from importlib import reload

reload(basic)
reload(utility)
reload(objectProperty)
reload(modifier)
reload(lightbasic)
reload(render)
reload(objimporter)

utility.clear_scene()
utility.clear_materials()
utility.delete_light_cache()

render.hide_hdri("//HDRs/satara_night_2k.hdr")
render.set_viewport_shading_material(True, True, 0, 1, 1, 0)
render.eevee_sampling(64, 16, False)
render.eevee_ambient_occlusion()
render.eevee_bloom()
render.eevee_screen_space_reflections()
render.color_management("sRGB", "Filmic", "Medium High Contrast")
