import streamlit as st

for s in st.session_state: #If we don't do this ritual, streamlit drops all the non-active-pages widget states on the floor (bad). https://docs.streamlit.io/develop/concepts/multipage-apps/widgets#option-3-interrupt-the-widget-clean-up-process
    st.session_state[s] = st.session_state[s]

x = 2 
@st.cache_data
def square():
    return x**2

@st.cache_data
def cube(x):
    return x**3

st.write(square())
x=42
st.write(square())

if st.button("Clear All"):
    # Clear values from *all* all in-memory and on-disk data caches:
    # i.e. clear values from both square and cube
    st.cache_data.clear()

st.write(square())

st.button("Does nothing")

if st.button("Clear All, but again"):
    st.cache_data.clear()
