import streamlit as st
import sympy as sp

from sympy.plotting import plot


def get_figure(user_input, expr):
    """
    Retrieves matplotlib figure

    Args:
        user_input (String): input by user
        expr (String): expression being evaluated

    Returns:
        Plot: return Plot object
    """
    sp_plot = plot(user_input, expr, (x, -1, 1))
    return sp_plot._backend.fig


if __name__ == '__main__':

    # set constants for sympy and streamlit
    options = ('Derivative', 'Integral')

    x = sp.symbols('x')
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

    if select_box == 'Derivative':
        # Use sympy.diff() method to differentiate expression
        dif = sp.diff(user_input, x)
        st.latex("Differentiation")
        st.latex(dif)
        st.pyplot(get_figure(user_input, dif))
    else:
        # use sympy.integrate to get the integral of the expression
        inte = sp.integrate(user_input, x)
        st.latex("Integral")
        st.latex(inte)
        st.pyplot(get_figure(user_input, inte))