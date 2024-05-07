import primitif.basic as basic
import tools.utility as utility
import tools.objectProperty as objectProperty
import tools.modifier as modifier
import elements.korakora as korakora
from importlib import reload

reload(basic)
reload(utility)
reload(objectProperty)
reload(modifier)
reload(korakora)

utility.clear_scene()

korakora = korakora.Kora_Kora(name="korakora")