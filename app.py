import streamlit as st


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

with st.container():
    st.subheader("Hi i am meekhum :wave:")
    st.title("a stupid prick")
    st.write("I am wasting my time doing this and i dont know why i am doing this but it is kinda fun")
    st.write("[Cute video of miku >](https://youtube.com/shorts/lTGmxLbg7Xo?si=IuiKk5FRRgJZls6c)")
    st.write("[Cute video of horse girl >](https://www.youtube.com/shorts/l74lS0jHnxo)")

with st.container():
    a=st.text_input('Give your name')
    if a.strip():  
        st.write(f"What are you doing, {a}? How is mom?")
        b=st.text_input()
        if b.strip():
            st.write(f"So {b}. Then what about dad?")
            c=st.text_input()