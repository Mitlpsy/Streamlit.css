import streamlit as st
import base64

st.title("4 collum")

# Add CSS style
st.markdown("""
    <style>
        .card {
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 10px;
            width: 200px; /* ปรับความกว้างของการ์ดให้เท่ากันทุกคอลัม */
            text-align: center;
        }

        .img {
            width: 50%;
            height: auto;
            border-radius: 50;
        }

        .card img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100px;
            height: 100px;
        }
        
        .custom-column {
            width: 25%;
            padding: 10px;
            box-sizing: border-box;
        }
    </style>
""", unsafe_allow_html=True)

# Create 4 columns
col1, col2, col3, col4 = st.columns(4)

# Add content to each column

with col1:
    st.image("1.png",width=200)
    with open("C:/Users/Legion/Downloads/75a1d8e3ee6058c578a2b33b0da968e9.svg", "rb") as file:
        svg_content = file.read()
        encoded_svg = base64.b64encode(svg_content).decode()
    st.markdown(f"""
    <div class="card">
        <h1>1</h1>
        <p>ข้อความ</p>
        <img height="50" width="100" src="data:image/svg+xml;base64,{encoded_svg}">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.image("2.png",width=200)
    with open("C:/Users/Legion/Downloads/75a1d8e3ee6058c578a2b33b0da968e9.svg", "rb") as file:
        svg_content = file.read()
        encoded_svg = base64.b64encode(svg_content).decode()
    st.markdown(f"""
    <div class="card">
        <h1>2</h1>
        <p>ข้อความ</p>
        <img height="50" width="100" src="data:image/svg+xml;base64,{encoded_svg}">
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.image("3.png",width=200)
    with open("C:/Users/Legion/Downloads/75a1d8e3ee6058c578a2b33b0da968e9.svg", "rb") as file:
        svg_content = file.read()
        encoded_svg = base64.b64encode(svg_content).decode()
    st.markdown(f"""
    <div class="card">
        <h1>3</h1>
        <p>ข้อความ</p>
       <img height="50" width="100" src="data:image/svg+xml;base64,{encoded_svg}">
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.image("4.png",width=200)
    with open("C:/Users/Legion/Downloads/75a1d8e3ee6058c578a2b33b0da968e9.svg", "rb") as file:
        svg_content = file.read()
        encoded_svg = base64.b64encode(svg_content).decode()
    st.markdown(f"""
    <div class="card">
        <h1 style="text-align: right;">4</h1>
        <p style="text-align: left;"> ข้อความ</p>
        <img height="50" width="100" src="data:image/svg+xml;base64,{encoded_svg}">
    </div>
    """, unsafe_allow_html=True)
