import streamlit as st

# Sayfa ayarları
st.set_page_config(page_title="Özür Dilerim", layout="wide")

# Session state'i başlat
if 'hayir_sayaci' not in st.session_state:
    st.session_state.hayir_sayaci = 0
if 'stage' not in st.session_state:
    st.session_state.stage = 1

# "Hayır" butonunun değişen yazıları
hayir_yazilari = [
    "Hayır",
    "Emin misin?",
    "Gerçekten emin misin??",
    "Tam olarak emin olduğunu söyleyebilir misin?",
    "Bir daha düşün lütfen!",
    "Gerçekten çok özülürüm...",
    "Çok ama çok özülürüm...",
    "Peki tamam, artık sormayacağım...",
]

# Butonların HTML ve CSS'i
def get_button_style(hayir_sayaci):
    buyume_orani = 1.0 + (hayir_sayaci * 0.4)
    hayir_bg_color = "#E06666" if hayir_sayaci < 7 else "#CD5C5C"

    # CSS stillerini tek bir dize olarak tanımla
    style_str = f"""
    <style>
    .stButton button[key="evet_button_kucuk"] {{
        font-size: {buyume_orani * 1.5}rem !important;
        padding: {buyume_orani * 0.5}rem {buyume_orani * 1}rem !important;
        background-color: #5CB85C !important;
        color: white !important;
        border-radius: 10px !important;
        border: 2px solid #5CB85C !important;
        transition: all 0.3s ease-in-out;
    }}
    .stButton button[key="hayir_button"] {{
        font-size: 1.5rem !important;
        padding: 0.5rem 1rem !important;
        background-color: {hayir_bg_color} !important;
        color: white !important;
        border-radius: 10px !important;
        border: 2px solid {hayir_bg_color} !important;
        transition: all 0.3s ease-in-out;
    }}
    .stButton button[key="evet_button_buyuk"] {{
        font-size: 10rem !important;
        padding: 5rem 10rem !important;
        background-color: #5CB85C !important;
        color: white !important;
        border-radius: 20px !important;
        border: 2px solid #5CB85C !important;
        position: fixed !important;
        top: 50% !important;
        left: 50% !important;
        transform: translate(-50%, -50%) !important;
        width: 100vw !important;
        height: 100vh !important;
        z-index: 9999 !important;
    }}
    </style>
    """
    return style_str

# Sticker'ların HTML ve CSS'i
def get_sticker_html(url):
    return f"""
    <div style="text-align: center; margin: 2rem 0;">
        <img src="{url}" alt="sticker" width="300px">
    </div>
    """

# --- Uygulama Aşamaları ---

# AŞAMA 1: Özür dileme ve 'Evet/Hayır' butonları
if st.session_state.stage == 1:
    
    st.markdown("<h1 style='text-align: center; font-size: 3rem; color: #E06666;'>Seni Üzdüğüm İçin Özür Dilerim. Barışalım Mı?</h1>", unsafe_allow_html=True)
    
    st.markdown(get_button_style(st.session_state.hayir_sayaci), unsafe_allow_html=True)

    # Butonlar
    col1, col2, col3 = st.columns([1,1.5,1])
    
    with col1:
        if st.session_state.hayir_sayaci < 7: