import streamlit as st

# "Say hello"というキャプションのボタンを作成する
if st.button('Say hello'):
    # ボタンが押されればこちらが表示される
    st.write('Why hello there')
else:
    # ボタンが押されなければこちらが表示される
    st.write('Goodbye')

import numpy as np
import altair as alt
import pandas as pd


# ランダムなデータを挿入したデータフレームを生成する(3次元の点×200点)
df_random = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
# Altairでチャートを生成する
c = alt.Chart(df_random).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# 生成したチャートを表示
st.write('Chart:', c)

from datetime import time, datetime

st.header('st.slider')

# Example 1
st.subheader('Slider')
age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2
st.subheader('Range slider')
values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0)
)
st.write('Values:', values)

# Example 3
st.subheader('Range time slider')
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45))
)
st.write("You're scheduled for:", appointment)

# Example 4
st.subheader('Datetime slider')
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm"
)
st.write("Start time:", start_time)


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green')
)

st.write(
    'Your favorite color is <span style="color:{}">{}</span>'.format(option.lower(), option),
     unsafe_allow_html=True
)
