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
    # 'Evet' butonunun büyüme miktarı
    buyume_orani = 1.0 + (hayir_sayaci * 0.4)
    
    # 'Hayır' butonu için renkler
    hayir_bg_color = "#E06666" if hayir_sayaci < 7 else "#CD5C5C"
    
    # Büyüyen Evet butonu stili
    evet_style = f"""
        .stButton button[key="evet_button_kucuk"] {{
            font-size: {buyume_orani * 1.5}rem !important;
            padding: {buyume_orani * 0.5}rem {buyume_orani * 1}rem !important;
            background-color: #5CB85C !important;
            color: white !important;
            border-radius: 10px !important;
            border: 2px solid #5CB85C !important;
            transition: all 0.3s ease-in-out;
        }}
    """
    
    # Hayır butonu stili
    hayir_style = f"""
        .stButton button[key="hayir_button"] {{
            font-size: 1.5rem !important;
            padding: 0.5rem 1rem !important;
            background-color: {hayir_bg_color} !important;
            color: white !important;
            border-radius: 10px !important;
            border: 2px solid {hayir_bg_color} !important;
            transition: all 0.3s ease-in-out;
        }}
    """
    
    # Tüm ekranı kaplayan Evet butonu stili
    buyuk_evet_style = """
        .stButton button[key="evet_button_buyuk"] {
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
        }
    """
    return f"<style>{evet_style}{hayir_style}{buyuk_evet_style}</style>"

# Sticker'ların HTML ve CSS'i
def get_sticker_html(url):
    return f"""
    <div style="text-