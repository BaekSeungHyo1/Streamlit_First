import streamlit as st

st.title("퀴즈 앱")

st.subheader("1. 광운대의 마스코트로 옳은 것은?")
answer1 = st.radio("객관식", ["환호", "알로스", "팡이와 우니", "백남이"])
if answer1 == "팡이와 우니":
    st.success("정답입니다!")
else:
    st.error("오답입니다.")

st.subheader("2. 광운대를 가장 빛내는 교수님 성함을 적으시오(성함 뒤에 교수님을 붙여야함 ex: 홍길동 교수님).")
answer2 = st.text_input("주관식")
if answer2:
    st.write(f"정답 : {answer2}")


