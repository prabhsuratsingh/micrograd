from micrograd.layer import Layer
from micrograd.mlp import MLP
from micrograd.neuron import Neuron
from micrograd.value import Value
from micrograd.visualize import draw_dot


# x1 = Value(2.0, label='x1')
# x2 = Value(0.0, label='x2')
# w1 = Value(-3.0, label='w1')
# w2 = Value(1.0, label='w2')
# b = Value(6.8813735870195432, label='b')

# x1w1 = x1 * w1; x1w1.label = "x1w1"
# x2w2 = x2 * w2; x2w2.label = "x2w2"
# x1w1x2w2 = x1w1 + x2w2; x1w1x2w2.label = "x1w1 + x2w2"

# n = x1w1x2w2 + b; n.label = "n"


# # o = n.tanh()

# e = (2*n).exp()
# o = (e-1)/(e+1)
# o.label = 'o'


# o.backward()
# dot = draw_dot(o)
# dot.render("graph", view=True)

x = [2.0, 3.0, -1.0]
n = MLP(3, [4, 4, 1])
print(len(n.parameters()))

xs = [
    [2.0, 3.0, -1.0],
    [3.0, -1.0, 0.5],
    [0.5, 1.0, 1.0],
    [1.0, 1.0, -1.0],
]

ys = [1.0, -1.0, -1.0, 1.0]

for k in range(20):
    ypred = [n(x) for x in xs]

    loss = sum((yout - ygt)**2 for ygt, yout in zip(ys, ypred))

    for p in n.parameters():
        p.grad = 0.0
    loss.backward()

    for p in n.parameters():
        p.data += -0.05 * p.grad

    print(f"Step: {k} | Loss: {loss.data}")

print("Prediction")
print(ypred)
# dot = draw_dot(loss)
# dot.render("graph", view=True)