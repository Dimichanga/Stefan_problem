from classes import Boundary, time_, geometry
from onedimensional import onedimensional_Stefan


left = Boundary()
right = Boundary()
onedimens = geometry()
tim = time_()

left.set_boundary("Left.txt")
onedimens.set_length("Geometry.txt")
onedimensional_Stefan("initial_condition.txt", "coef_therm_cond.txt", "enthalpy.txt", onedimens, left, tim)
