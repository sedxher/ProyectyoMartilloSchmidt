# R_l : rebote promedio
# d : densidad

import pandas as pd
import numpy as np

# 1-Deere and Miller 1966
def deeremillerusc(R_l, d):
   ucs_reb = 9.97 * np.exp(0.02 * d * R_l)
   return ucs_reb

# 2-Aufmuth 1973
def aufmuthusc(R_l, d):
   ucs_reb = 0.33  * (R_l * d)**(1.35)
   return ucs_reb

# 3-Yasar and Erdogan 2004
def yasarerdoganusc(R_l, d):
   ucs_reb = 0.000004 * (R_l)**(4.29)
   return ucs_reb