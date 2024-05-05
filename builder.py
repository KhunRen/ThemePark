import primitif.basic as basic
import tools.utility as utility
import tools.objectProperty as objectProperty
import tools.modifier as modifier
from importlib import reload

reload(basic)
reload(utility)
reload(objectProperty)
reload(modifier)

utility.clear_scene()
