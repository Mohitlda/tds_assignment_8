# assignment *

import streamlit as st


st.title("TDS_Assignment_8 : Check number for Odd/Even")

st.subheader("Write here the number")

x = st.number_input("Enter Number")

result = st.button("click here")
if(result==True):
    frac, whole = math.modf(x)    
    if (frac == 0.0):
        if(x%2==0):
            st.write(f"""{x} *is Even Number*""")
        else:
            st.write(f"""{x} *is Odd Number*""")
    else:
        st.write(f"""{x} is neither even nor odd. It is should be whole number""")

        
        
st.subheader("Made by : 21f1005966")


