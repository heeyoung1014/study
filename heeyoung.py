import streamlit as st
import pandas as pd

# 제목 만들기
st.title('자기소개')

# 인사 버튼 만들기
if st.button('안녕하세요!'):
    st.write('반가워요 :)')
else:
    st.write('안녕하세요를 눌러주세요.')
    
# 소제목 만들기
st.markdown('## 1. 기본 정보')
    
# 기본 정보 버튼으로 만들기
info = st.radio('알고 싶은 정보를 눌러주세요.', ('이름', '성별', '나이', '지역', '전공'))

if info == '이름':
    st.write('박희영이라고 합니다. 잘 부탁드립니다.🙃')
elif info == '성별':
    st.write('저는 여자입니다.👀')
elif info == '나이':
    st.write('27살 입니다.')
elif info == '지역':
    st.write('저는 경상남도 양산에 살고 있습니다.🏡')
else:
    st.write('저는 지질환경과학을 전공했습니다.🌋')
    
# 소제목 만들기
st.markdown('## 2. 좋아하는 영화 장르')

# 기본 정보 버튼으로 만들기
movie = st.radio('제가 좋아하는 영화 장르는 무엇일까요?', ('로맨스', '공포', '스릴러', '액션', 'SF'))

if movie == '로맨스':
    st.write('로맨스는 딱히 엄청 좋아하지 않습니다 ㅎㅎ')
elif movie == '공포':
    st.write('깜짝놀래키는 귀신은 싫어합니다.')
elif movie == '스릴러':
    st.write('정답! 저는 범죄, 스릴러 영화를 제일 좋아합니다.')
elif movie == '액션':
    st.write('정답! 액션 영화도 너무 좋아합니다.')
else:
    st.write('SF영화도 좋아해요!')
    

# 소제목 만들기
st.markdown('## 3. 재밌게 본 영화 추천')

col1, col2, col3 = st.columns(3)

with col1:
    st.image('https://movie-phinf.pstatic.net/20130206_29/13601146693401seof_JPEG/movie_image.jpg') 
    st.text('신세계')
    
with col2:
    st.image('https://movie-phinf.pstatic.net/20170512_76/1494564316131VmHQY_JPEG/movie_image.jpg')
    st.text('겟 아웃')
    
with col3:
    st.image('https://movie-phinf.pstatic.net/20170915_299/1505458505658vbKcN_JPEG/movie_image.jpg')
    st.text('범죄도시')
    
col4, col5, col6 = st.columns(3)

with col4:
    st.image('https://movie-phinf.pstatic.net/20200310_91/1583805533463Yqyui_JPEG/movie_image.jpg')
    st.text('분노의질주')
    
with col5:
    st.image('https://movie-phinf.pstatic.net/20160217_153/1455686083975zjajH_JPEG/movie_image.jpg')
    st.text('주토피아')

with col6:
    st.image('https://movie-phinf.pstatic.net/20181114_127/15421634814664mCUO_JPEG/movie_image.jpg')
    st.text('트와일라잇')
    

# 소제목 만들기
st.markdown('## 4. 내 기준 재미없었던 영화')

cola, colb = st.columns(2)

with cola:
    st.image('https://movie-phinf.pstatic.net/20220607_129/16545872892918GA4h_JPEG/movie_image.jpg')
    st.text('헤어질 결심')

with colb:
    st.image('https://movie-phinf.pstatic.net/20171222_257/15139181561647cwWN_JPEG/movie_image.jpg')
    st.text('다운 사이징')
    
# 소제목 만들기
st.markdown('## 5. 노래 추천')

st.text('디오 - Im gonna love you')
st.audio('study/do.mp3')

st.text('릴러말즈 - trip')
st.audio('study/trip.mp3')