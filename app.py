import streamlit as st

st.title("광운대학교 퀴즈 앱")

st.subheader("1. 광운대의 마스코트로 옳은 것은?")
answer1 = st.radio("객관식", ["환호", "알로스", "팡이와 우니", "백남이"], key="quiz1")

st.subheader("2. 광운대를 가장 빛내는 교수님 성함을 적으시오.")
st.caption("성함 뒤에 '교수님'을 붙여야 함 (예: 홍길동 교수님)")
answer2 = st.text_input("주관식", key="quiz2")

if st.button("퀴즈 제출"):
    st.subheader("📝 채점 결과")

    if answer1 == "팡이와 우니":
        st.success("1번: 정답입니다!")
    else:
        st.error("1번: 오답입니다.")

    if answer2.strip() == "박규동 교수님":
        st.success("2번: 정답입니다!")
    else:
        st.error("2번: 오답입니다.")