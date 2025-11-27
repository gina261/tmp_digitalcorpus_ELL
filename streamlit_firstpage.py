import streamlit as st
from streamlit_app.styles.utils import inject_css, inject_css_bundle
import time
from streamlit_app.utils.spellchecker_func import *
import nltk

# NLTK 데이터 다운로드 (punkt_tab 및 punkt)
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


# ============== 페이지 설정 ==============
st.set_page_config(page_title="Spelling Bot", page_icon="👾", layout="wide")

# 공통 CSS
inject_css("streamlit_app/styles/base.css")

# ============== Session State ==============
# session_state 초기화
if 'page' not in st.session_state:
    st.session_state.page = 'landing'   #'chat_page'
if "messages" not in st.session_state:
    st.session_state.messages = []  # [{"role":"user"/"assistant", "content": "..."}]

# ============== 처음 진입 화면 ==============
def show_landing_page():    
    # 헤더
    # st.markdown("""<br>""", unsafe_allow_html=True)
    st.markdown("""
    <div class="spacing"></div>
    <div class="centered-image">
        <img src="https://i.ibb.co/1G078b6S/y-vengers.png">
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="landing-wrap">
        <div class="landing">
            <br>
            <h1>안녕하세요, Spelling Bot입니다.</h1>
            <h1>영어 문장을 입력하면 오타를 교정해드립니다.</h1>
            <br>
            <h6>NLTK와 SpellChecker를 활용하여 빠르고 정확하게 교정합니다.</h6>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # CSS 스타일 적용
    inject_css("streamlit_app/styles/landing.css")

    # 입력 처리
    first_text = st.chat_input("교정할 영어 문장을 입력해주세요.")
    if first_text:
        st.session_state.messages.append({"role": "user", "content": first_text})
        # 봇 응답 생성
        answer = generate_spelling_response(first_text)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.session_state.page = "chat_page"
        st.rerun()
        
        
# ============== CHAT 대화 화면 ==============
def show_chat():
    assistant_avatar = "streamlit_app/img/y-vengers.png"
    user_avatar = "streamlit_app/img/y-vengers.png"

    # CSS 스타일 적용
    inject_css("streamlit_app/styles/chat.css")
    
    # 1. 기존 대화 렌더링
    for message in st.session_state.messages:
        # role에 따라 아바타 설정
        avatar = user_avatar if message["role"] == "user" else assistant_avatar
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"], unsafe_allow_html=True)

    # 2. 새로운 입력 처리
    prompt = st.chat_input("교정할 영어 문장을 입력해주세요.")
    if prompt:
        # 사용자 메시지 추가 및 렌더링
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=user_avatar):
            st.write(prompt)
        
        # 봇 응답 생성 및 렌더링
        with st.chat_message("assistant", avatar=assistant_avatar):
            with st.spinner("분석 중..."):
                # 약간의 딜레이(UX 효과)
                time.sleep(0.5) 
                response_text = generate_spelling_response(prompt)
                st.markdown(response_text)
                
        # 세션에 봇 응답 추가
        st.session_state.messages.append({"role": "assistant", "content": response_text})
    
    

# ============== Router ==============
if st.session_state.page == 'landing' and len(st.session_state.messages) == 0:
    show_landing_page()
else:
    # 채팅 페이지로 고정
    show_chat()