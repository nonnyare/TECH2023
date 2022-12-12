import streamlit as st
# st.write("You got gift Number 3")
# streamlit_app.py
# streamlit_app.py

# import streamlit as st
# st.write("Here goes your normal Streamlit app...")
# st.button("Click me")

import streamlit as st

st.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
.medium-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">Enter The Secret Password 👇</p>', unsafe_allow_html=True)

# Store the initial value of widgets in session state
# if "visibility" not in st.session_state:
#     st.session_state.visibility = "visible"
#     st.session_state.disabled = False

# col1, col2 = st.columns(2)

# with col1:
#     # st.checkbox("Disable text input widget", key="disabled")
#     # st.radio(
#     #     "Set text input label visibility 👉",
#     #     key="visibility",
#     #     options=["visible", "hidden", "collapsed"],
#     # )
#     st.text_input(
#         "Placeholder for the other text input widget",
#         "This is a placeholder",
#         key="placeholder",
    # )
# with col2:
text_input = st.text_input(
    "🎄🦌🎁🎉🎊🥳",)
#     label_visibility=st.session_state.visibility,
#     disabled=st.session_state.disabled,
#     placeholder=st.session_state.placeholder,
# )
if len(text_input) >= 1:
    if text_input == '2023':
        # st.write("You got a gift NO.01")
        st.markdown(
            '<p class="medium-font-font">You got a gift <strong style="color:blue">NUMBER 02</strong> from lovely Santa</p>'
            , unsafe_allow_html=True)
        st.image("santa.gif")
    if text_input != '2023':
        st.write("🙄 You are not TECHNOLOGY DEPARTMENT !!!")
        st.write("Try again ?")
    
elif len(text_input) <= 1:
    st.write(" ")