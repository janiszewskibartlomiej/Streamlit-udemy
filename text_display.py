import streamlit as st


st.markdown('# Markdown')
st.markdown('## Markdown')
st.markdown('### Markdown')


st.header('Header')
st.subheader('Subheader')
st.text('Text')
st.caption('Caption')


code_snippet = """
def greer(name):
    return f"Hello, {name}!"
"""

st.code(code_snippet, language='python')

st.latex(r'\frac{a}{b}')
st.latex(f"""y = m*x + c""")

my_list = [1, 2, 3]
st.write(my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3}
st.write(my_dict)