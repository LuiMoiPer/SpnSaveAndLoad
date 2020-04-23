#! python3

from spn.io.Graphics import plot_spn
from spn.io.Text import to_JSON
from spn.algorithms.Marginalization import marginalize
from spn.structure.leaves.parametric.Parametric import Categorical
from spn.structure.Base import Sum, Product
from spn.structure.Base import assign_ids, rebuild_scopes_bottom_up

spn = 0.4 * (Categorical(p=[0.2, 0.8], scope=0) *
             (0.3 * (Categorical(p=[0.3, 0.7], scope=1) *
                     Categorical(p=[0.4, 0.6], scope=2))
            + 0.7 * (Categorical(p=[0.5, 0.5], scope=1) *
                     Categorical(p=[0.6, 0.4], scope=2)))) \
    + 0.6 * (Categorical(p=[0.2, 0.8], scope=0) *
             Categorical(p=[0.3, 0.7], scope=1) *
             Categorical(p=[0.4, 0.6], scope=2))
spn = marginalize(spn, [1,2])
print(to_JSON(spn) + "\n\n\n")
plot_spn(spn, 'spn1.png')

spn2 = Product(children=[Categorical(p=[0.5, 0.5], scope=0), Categorical(p=[0.2, 0.8], scope=2)])
print(to_JSON(spn2))
assign_ids(spn2)
rebuild_scopes_bottom_up(spn2)
plot_spn(spn2, 'basicspn.png')
print(to_JSON(spn2))

def getSpn1():
    spn = 0.4 * (Categorical(p=[0.2, 0.8], scope=0) *
             (0.3 * (Categorical(p=[0.3, 0.7], scope=1) *
                     Categorical(p=[0.4, 0.6], scope=2))
            + 0.7 * (Categorical(p=[0.5, 0.5], scope=1) *
                     Categorical(p=[0.6, 0.4], scope=2)))) \
    + 0.6 * (Categorical(p=[0.2, 0.8], scope=0) *
             Categorical(p=[0.3, 0.7], scope=1) *
             Categorical(p=[0.4, 0.6], scope=2))
    return spn

def getSpn2():
    spn2 = Product(children=[Categorical(p=[0.5, 0.5], scope=0), Categorical(p=[0.2, 0.8], scope=2)])
    assign_ids(spn2)
    rebuild_scopes_bottom_up(spn2)
    return spn2

if __name__ == "__main__":
    pass