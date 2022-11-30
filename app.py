# assignment *

import streamlit as st


st.title("Check number for Odd/Even")

st.subheader("Write here the number")

x = st.number_input("Enter Number")

result = st.button("click here")
if(result==True):
    if(x%2==0):
        st.write(f"""{x} *is Even Number*""")
    else:
        st.write(f"""{x} *is Odd Number*""")
        
        
        
st.subheader("21f1005966")


