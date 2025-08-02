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
    "Peki tamam, artık sormayacağım...", # 8. basış için
    "Peki tamam, artık sormayacağım...", # 9. basış için
]

# Butonların HTML ve CSS'i
def get_button_style(hayir_sayaci):
    # 'Evet' butonunun büyüme miktarı
    buyume_orani = 1.0 + (hayir_sayaci * 0.4)
    
    # 'Hayır' butonu için renkler
    hayir_bg_color = "#E06666" if hayir_sayaci < 5 else "#CD5C5C"
    
    # Büyüyen Evet butonu stili
    evet_style = f"""
        .stButton button[key="evet_button_kucuk"] {{
            font-size: {buyume_orani * 1.5}rem;
            padding: {buyume_orani * 0.5}rem {buyume_orani * 1}rem;
            background-color: #5CB85C;
            color: white;
            border-radius: 10px;
            border: 2px solid #5CB85C;
            transition: all 0.5s ease-in-out;
        }}
    """
    
    # Hayır butonu stili
    hayir_style = f"""
        .stButton button[key="hayir_button"] {{
            font-size: 1.5rem;
            padding: 0.5rem 1rem;
            background-color: {hayir_bg_color};
            color: white;
            border-radius: 10px;
            border: 2px solid {hayir_bg_color};
            transition: all 0.5s ease-in-out;
        }}
    """
    
    # Tüm ekranı kaplayan Evet butonu stili
    buyuk_evet_style = """
        .stButton button[key="evet_button_buyuk"] {
            font-size: 10rem;
            padding: 5rem 10rem;
            background-color: #5CB85C;
            color: white;
            border-radius: 20px;
            border: 2px solid #5CB85C;
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 100vw;
            height: 100vh;
            z-index: 9999;
        }
    """
    return f"<style>{evet_style}{hayir_style}{buyuk_evet_style}</style>"

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
        if st.session_state.hayir_sayaci < 8:
            if st.button("Evet", key="evet_button_kucuk"):
                st.session_state.stage = 2
                st.experimental_rerun()
    
    with col3:
        if st.session_state.hayir_sayaci < 9:
            hayir_metni = hayir_yazilari[st.session_state.hayir_sayaci]
            if st.button(hayir_metni, key="hayir_button"):
                st.session_state.hayir_sayaci += 1
                st.experimental_rerun()
    
    # Tüm ekranı kaplayan Evet butonu
    if st.session_state.hayir_sayaci >= 8:
        if st.button("Evet", key="evet_button_buyuk"):
            st.session_state.stage = 2
            st.experimental_rerun()
    
    # Sticker
    st.markdown(get_sticker_html("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3dpeGd0bjlsMXZ6eW9naDJrMG03MmowbmxnMjZzbGdsNnZld29zZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/uP63dDtykQz3S9iT1q/giphy.gif"), unsafe_allow_html=True)

# AŞAMA 2: Affedildiğini gösteren ekran
elif st.session_state.stage == 2:
    st.markdown("<h1 style='text-align: center; font-size: 3rem; color: #E06666;'>Evet diyeceğini biliyordummm!</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-size: 2.5rem; color: #E06666;'>Teşekkür Ederimm ❤️</h2>", unsafe_allow_html=True)
    
    # Aşk dolu sarılma sticker'ı
    st.markdown(get_sticker_html("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZtMTdxeGZzOGN2dG1tbmFpaXJsczEwaXJ0bW93c3Y5Z3h3ajd4ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/jY5xK2D6s0uF9lWzVl/giphy.gif"), unsafe_allow_html=True)