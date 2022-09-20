import streamlit as st

import sympy as sp
from sympy.plotting import plot


# set symbols for calculations
x, y = sp.symbols('x y')
sp.init_printing()
gfg_exp = sp.csc(x)

st.latex("Before Differentiation")
st.latex(sp.latex(gfg_exp))
  
# Use sympy.diff() method to differentiate expression
dif = sp.diff(gfg_exp, x)

st.latex("After Differentiation")
st.latex(dif)