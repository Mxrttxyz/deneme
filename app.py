import streamlit as st

# Sayfa ayarları
st.set_page_config(page_title="Özür Dilerim", layout="wide")

# Session state'i başlat
if 'hayir_sayaci' not in st.session_state:
    st.session_state.hayir_sayaci = 0
if 'stage' not in st.session_state:
    st.session_state.stage = 1

# Butonların HTML ve CSS'i
def get_button_style(size):
    if size >= 5: # 4 kere basıldıktan sonra büyüyen buton için
        return f"""
        <style>
            .stButton button {{
                font-size: 5rem !important;
                padding: 3rem 5rem !important;
                background-color: #ff69b4;
                color: white;
                border-radius: 20px;
                border: 2px solid #ff69b4;
                width: 100%;
                height: 100vh;
                position: fixed;
                top: 0;
                left: 0;
            }}
        </style>
        """
    else: # Normal boyut
        font_size = f"{2 + size * 0.5}rem"
        padding_size = f"{0.5 + size * 0.2}rem"
        return f"""
        <style>
            .stButton button {{
                font-size: {font_size};
                padding: {padding_size} 1rem;
                background-color: #ff69b4;
                color: white;
                border-radius: 10px;
                border: 2px solid #ff69b4;
            }}
        </style>
        """

# Sticker'ların HTML ve CSS'i
def get_sticker_html(url, size="300px"):
    return f"""
    <div style="text-align: center; margin: 2rem 0;">
        <img src="{url}" alt="sticker" width="{size}">
    </div>
    """

# --- Uygulama Aşamaları ---

# AŞAMA 1: Özür dileme ve 'Evet/Hayır' butonları
if st.session_state.stage == 1:
    
    st.markdown("<h1 style='text-align: center; font-size: 3rem; color: #ff69b4;'>Seni üzdüğüm için özür dilerim ❤️</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-size: 2.5rem; color: #333;'>Beni affeder misin?</h2>", unsafe_allow_html=True)
    
    # İlk ekrandaki sticker (başını sallayan)
    st.markdown(get_sticker_html("https://media.giphy.com/media/QvTz5Y1K4b30l67m5C/giphy.gif"), unsafe_allow_html=True)

    st.markdown(get_button_style(st.session_state.hayir_sayaci), unsafe_allow_html=True)
    
    # Butonları yerleştirme
    if st.session_state.hayir_sayaci < 4:
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            if st.button("Evet", key="evet_button_kucuk"):
                st.session_state.stage = 2
                st.experimental_rerun()
        with col3:
            if st.button("Hayır", key="hayir_button"):
                st.session_state.hayir_sayaci += 1
                st.experimental_rerun()
    else:
        # Hayır'a 4 kere basıldığında 'Evet' butonu tüm ekranı kaplasın
        st.markdown(get_button_style(5), unsafe_allow_html=True)
        if st.button("Evet", key="evet_button_buyuk"):
            st.session_state.stage = 2
            st.experimental_rerun()

# AŞAMA 2: Affedildiğini gösteren ekran
elif st.session_state.stage == 2:
    st.markdown("<h1 style='text-align: center; font-size: 3rem; color: #ff69b4;'>Evet diyeceğini biliyordummm!</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-size: 2.5rem; color: #333;'>Teşekkür Ederimm ❤️</h2>", unsafe_allow_html=True)
    
    # İkinci ekrandaki sticker (sarılma)
    st.markdown(get_sticker_html("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZtMTdxeGZzOGN2dG1tbmFpaXJsczEwaXJ0bW93c3Y5Z3h3ajd4ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/jY5xK2D6s0uF9lWzVl/giphy.gif"), unsafe_allow_html=True)