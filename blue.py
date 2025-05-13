import streamlit as st
st.title("Blue, Don't get sick")
st.header("Listen Blue, I got a message for u")
st.subheader("Lu wishes the best for u so be warm n ok, ok?")


st.markdown("""
<style>
    div.stButton > button:first-child {
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 10px 24px;
    }
</style>
""", unsafe_allow_html=True)

if st.button("ok"):
   st.write("ma boy!")
   st.balloons()
