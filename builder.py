import primitif.basic as basic
import tools.utility as utility
import tools.objectProperty as objectProperty
import tools.modifier as modifier
import elements.komediputar as komediputar
import elements.ombakbanyu_atas as ombakatas
from importlib import reload

reload(basic)
reload(utility)
reload(objectProperty)
reload(modifier)
reload(komediputar)
reload(ombakatas)
utility.clear_scene()

# komedi = komediputar.Komedi_putar("komedi", (0, 0, 0))
ombak = ombakatas.OmbakBanyu_Atas("ombakatas", (0,0,0))
# komedi.rotate((0, 90, 0))
# komedi.translate((0, 0, 10))

# kuda = komediputar.Horse("kuda", (0, 0, 0))
# kuda.translate((0, 10, 12))
# bench = komediputar.Bench("bench", (0, 0, 0))