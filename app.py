import streamlit as st
import base64

st.set_page_config(
    page_title="JGAN Designer",
    page_icon="🔥",
    layout="wide"
)

def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = get_base64_image("logo.png")
zap_base64 = get_base64_image("whatsapp.png")

st.markdown("""
<style>
.stApp{
    background: linear-gradient(180deg,#050816,#071126,#0b1736);
    color: white;
}
html, body, [class*="css"]{
    color: white;
    font-family: Arial;
}
img{
    border-radius:20px;
}
.main-title{
    font-size:60px;
    font-weight:900;
    color:white;
}
.sub-title{
    font-size:25px;
    color:#00d9ff;
}
.about-box{
    background: rgba(255,255,255,0.05);
    padding:30px;
    border-radius:20px;
    line-height:2;
    font-size:20px;
}
.section-title{
    font-size:40px;
    font-weight:800;
    margin-top:50px;
    margin-bottom:20px;
    color:#00d9ff;
}
.social-btn{
    display:inline-block;
    background: linear-gradient(90deg,#833ab4,#fd1d1d,#fcb045);
    color:white;
    padding:15px 35px;
    border-radius:15px;
    text-decoration:none;
    font-size:18px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.markdown(f"""
    <div style="text-align:center; margin-top:20px;">
        <img src="data:image/png;base64,{logo_base64}" width="250">
    </div>
    """, unsafe_allow_html=True)

col_left, col_right = st.columns([1,1])

with col_left:

    st.markdown("""
    <div class="main-title">
        JGAN Designer
    </div>

    <div class="sub-title">
        Sports Graphic Designer
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="about-box">

    Me chamo Gabriel Alves, conhecido como JGAN.

    Sou designer esportivo especializado em artes para:
    <br><br>

    • Futebol<br>
    • Vôlei<br>
    • Basquete<br>
    • Matchdays<br>
    • Social Media<br>
    • Posters Esportivos<br>
    • Wallpapers<br>

    Atendendo clientes do Brasil e exterior.

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <a class="social-btn"
       href="https://www.instagram.com/jgan.designer/"
       target="_blank">

       Ver Meu Instagram

    </a>
    """, unsafe_allow_html=True)

with col_right:
    st.image("minhafoto.png", width=450)

st.markdown("""
<div class="section-title">
Meu Portfólio
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image("arte1.png", use_container_width=True)

with col2:
    st.image("arte2.png", use_container_width=True)

st.markdown(f"""
<div style="text-align:center; margin-top:40px;">

    <a href="https://wa.me/558396851338" target="_blank">

        <img src="data:image/png;base64,{zap_base64}"
             width="90">

    </a>

</div>
""", unsafe_allow_html=True)

st.markdown("""
<br><br>

<div style="text-align:center; color:gray;">
© 2026 - JGAN Designer
</div>
""", unsafe_allow_html=True)
