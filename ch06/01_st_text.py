import streamlit as st

# 타이틀 적용 예시
st.title('(KPC) 입문자를 위한 Chatgpt 및 API 활용 서비스 제작 실무')

# Header 적용
st.header('1. [Day1] vscode 환경에서 chatGPT 기본 API 사용해보기')
st.markdown('---')

st.header('2. [Day2] Streamlit으로 웹앱 만들기')
st.markdown('---')


# Subheader 적용
st.subheader(' 가. Text 실습')

# 코드 표시
sample_code = '''
def function():
    for idx in ['a', 'b', 'c']
        print(f'{idx}')
'''
st.code(sample_code, language="python")
# 캡션 적용
st.caption('코드 블럭 표시를 위해서 code()를 사용하면 복사하기 기능 지원됩니다.')

# 일반 text
st.text('일반적인 텍스트를 입력해 보았습니다.')

# 마크다운 문법 지원
body= 'streamlit은 **마크다운(md) 문법을 지원**합니다. :+1:'
st.markdown(body, unsafe_allow_html=False, help=None)

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')

multi = '''If you end a line with two spaces,  
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

# 선 그리기
st.markdown('---')

st.markdown(":green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다.")

# LaTex 수식 지원
st.latex(r'\sqrt{x^2+y^2}=1')