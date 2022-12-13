import streamlit as st

st.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
.medium-font {
    font-size:23px !important;
}
</style>
""", unsafe_allow_html=True)
st.markdown('<p class="big-font">Enter The Secret Password 👇</p>', unsafe_allow_html=True)

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
            '<p class="medium-font-font"><strong style="color:orange">CONGRATS !!! </strong></p>'
            , unsafe_allow_html=True)
        st.markdown(
            '<p class="medium-font-font"> You got <strong style="color:orange"> THE SPECIAL GIFT </strong> from lovely Santa...</p>'
            , unsafe_allow_html=True)
        st.write('I hope you will get the greatest gift, Good luck !')
        st.image("fireworks.gif")
        st.image("santa.gif")
    if text_input != '2023':
        st.markdown(
            '<p class="medium-font-font"><strong style="color:red">INCORRECT !!!!!</strong></p>'
            , unsafe_allow_html=True)
        st.write("🙄 You are not in TECHNOLOGY DEPARTMENT !!!")
        st.write("Try again ?")
    
elif len(text_input) <= 1:
    st.write(" ")