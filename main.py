from micrograd.value import Value
from micrograd.visualize import draw_dot


a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = Value(10.0, label='c')

e = a*b; e.label='e'
d = e+ c; d.label='d'
f = Value(-2.0, label='f')
L = d * f; L.label='L'


dot = draw_dot(L)
dot.render("graph", view=True)