import streamlit as st
import pandas as pd
import time


st.title('Startup Dashboard')
st.header('I am learning Streamlit')
st.subheader('And I am loving it !')
st.write('This is a normal text')
st.markdown("""
### My Favorite movie
- ajju
- kajju
- majju
""")
st.code("""
def foo(input):
    return foo**2
x = foo(2)
""")

st.latex('x^2 +y^2 + 2 = 0')

df = pd.DataFrame({
    'name':['yatin','ankit','Anupam'],
    'marks': [26,27,28],
    'package':[10,12,14]
})

st.dataframe(df)

st.metric('Revenue', 'Rs 3L', '3%')

st.json({
    'name':['yatin','ankit','Anupam'],
    'marks': [26,27,28],
    'package':[10,12,14]
})

st.image('images.jpeg')

# st.video()

st.sidebar.title('Sidebar ka Title')

col1,col2,col3 = st.columns(3)
with col1:
     st.image('images.jpeg')

with col2:
    st.image('images.jpeg')

with col3:
    st.image('images.jpeg')


st.error('login failed')
st.success( 'login successful')
st.info( 'login successful')
st.warning( 'login successful')


bar = st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

email = st.text_input('Enter Email')
number = st.number_input('Enter age')
st.date_input('Enter regis date')

# next login code logic

email = st.text_input('Enter email')
password =  st.text_input('Enter password')
gender = st.selectbox('Select gender',['male', 'female', 'others'])

btn = st.button('login')
# if the button login
if btn:
    if email == 'yatin@gmail.com' and password == '1234':
        st.balloons()
        st.success('Login Successful')
    else:
        st.error('Login Failed')

        import pandas as pd
        import streamlit as st

        file = st.file_uploader('Upload a csv file')

        if file is not None:
            df = pd.read_csv(file)
            st.dataframe(df.describe())
