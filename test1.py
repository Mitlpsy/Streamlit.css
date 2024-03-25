import streamlit as st
import base64

st.set_page_config(layout="wide") # เซตติง page wide mode

st.title("4 collum")
with open("test/style1.css","r", encoding="utf-8") as file:
    css = file.read()
 
# Decorate css
st.markdown(f"""
        <style>
            {css}
        </style>
""", unsafe_allow_html=True)


# Create 4 columns
col1, col2, col3, col4 = st.columns(4)


# Add content to each column
with col1:
    st.image("1.png", width=200)
    with open("C:/Users/Legion/Downloads/75a1d8e3ee6058c578a2b33b0da968e9.svg", "rb") as file:
        svg_content = file.read()
        encoded_svg = base64.b64encode(svg_content).decode()
    st.markdown(f"""
    <div class="card">
        <p style="margin-top: 80px; text-align: right;">สมาชิกทั้งหมด</p>
        <h1 style="margin-bottom: 5px;">1ล้าน</h1>  
        <img height="60" width="200" src="data:image/svg+xml;base64,{encoded_svg}">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("2.png", width=200)
    with open("C:/Users/Legion/Downloads/75a1d8e3ee6058c578a2b33b0da968e9.svg", "rb") as file:
        svg_content = file.read()
        encoded_svg = base64.b64encode(svg_content).decode()
    st.markdown(f"""
    <div class="card">
        <p style="margin-top: 80px;">ค้างชำระและหมดสัญญา</p>
        <h1 style="margin-bottom: 5px;">4000ล้าน</h1>
        <img height="60" width="100" src="data:image/svg+xml;base64,{encoded_svg}">
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.image("3.png", width=200)
    with open("C:/Users/Legion/Downloads/75a1d8e3ee6058c578a2b33b0da968e9.svg", "rb") as file:
        svg_content = file.read()
        encoded_svg = base64.b64encode(svg_content).decode()
    st.markdown(f"""
    <div class="card">
        <p  style="magin-top: 10px;">ค้างชำระ3งวดขึ้นไป</p>
        <h1 style="margin-bottom: 5px;">3000ล้าน</h1>
       <img height="60" width="100" src="data:image/svg+xml;base64,{encoded_svg}">
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.image("4.png", width=200)
    with open("C:/Users/Legion/Downloads/75a1d8e3ee6058c578a2b33b0da968e9.svg", "rb") as file:
        svg_content = file.read()
        encoded_svg = base64.b64encode(svg_content).decode()
    st.markdown(f"""
    <div class="card">
        <p style="margin-top: 10px;">หมดสัญญาระหว่างปี</p>
        <h1 style="margin-bottom: 5px;">4000ล้าน</h1>
        <img height="60" width="100" src="data:image/svg+xml;base64,{encoded_svg}">
    </div>
    """, unsafe_allow_html=True)
