import streamlit as st

st.title("Simple Calculator") 

st.markdown("This is a simple calculator app built with Streamlit.")

c1,c2 = st.columns(2)
fnum = c1.number_input("First Number", value=0)
snum = c2.number_input("Second Number", value=0)
options = ["addition", "subtraction", "multiplication", "division"]
choice = st.radio("Select Operation", options)

button = st.button("calculate")

result =0
if button:
    if choice == "addition":
        result = fnum + snum
    elif choice == "subtraction":
        result = fnum - snum
    elif choice == "multiplication":
        result = fnum * snum
    elif choice == "division":
        result = fnum/snum 
       
st.warning((f"result is : {result}"))