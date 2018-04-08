from sympy import solve
from sympy.abc import x
from math import log10

import numpy as np
import matplotlib.pyplot as plt

Vb = 0
Va = 25
Cb = 0.1
Ca = 0.1
ka = 6.66810 ** -4
kw = 10 ** -14

l = []

Vb_list = np.linspace(0, 2*Va, 51)

while Vb <= 2 * Va:
	
	Vt = Vb + Va
	B = Vb*Cb/Vt
	A = Va*Ca/Vt
	l.append(list(map(lambda x: -log10(x), [complex(sol).real for sol in solve(x**3 + (x**2)*(B + ka) + x*(ka*(B-A)-kw)-kw*ka, x) if complex(sol).real > 0]))[0])
	
	Vb += 1

ph_list = np.array(l)

plt.plot(Vb_list, ph_list)
plt.show()
