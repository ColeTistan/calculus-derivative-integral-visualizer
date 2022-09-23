import streamlit as st

import sympy as sp
from sympy.plotting import plot


# set constants for sympy and streamlit
options = ('Derivative', 'Integral')

x, y = sp.symbols('x y')
sp.init_printing(use_latex=True)

user_input = st.text_input(
    'Enter expression here... Ex: x**2',
    x**2,
    placeholder=x**2
)

select_box = st.selectbox(
    'Would you like to visualize a derivative or integral?',
    options
)

st.write('You selected:', select_box)

if select_box == 'Derivative':
    # Use sympy.diff() method to differentiate expression
    dif = sp.diff(user_input, x)

    st.latex("Differentiation")
    st.latex(dif)
else:
    inte = sp.integrate(user_input, x)
    st.latex("Integral")
    st.latex(inte)