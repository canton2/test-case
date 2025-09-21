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
