import streamlit as st
import time
st.title('Streamlit 超入門')

st.write('Dsiplay Image')

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns=['lat','lon']
# )

# if st.checkbox('show Image'):
#     img = Image.open('/Users/shimadagaku/myblogapp/pyhonWebApp/skuawk_sozai_13.jpeg')
#     st.image(img, caption = 'cat',use_column_width= True)
# st.table(df)
# st.map(df)

# option = st.selectbox(
#     'あなた好きな数字を教えてください',
#     list(range(1,11))
# )

'staet!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'



left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右からむ')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

#'あなたの好きな数字は、', option ,'です。'

#text = st.text_input('あなたの趣味を教えてください')
#'あなたの趣味は、', text ,'です。'


#condition = st.slider('あなたの今の調子は?',0,100,50)
#'コンディション：',condition 