import streamlit as st
import base64

# Sayfa ayarları
st.set_page_config(page_title="Özür Dilerim", layout="wide")

# Session state'i başlat
if 'button_size' not in st.session_state:
    st.session_state.button_size = 1
if 'stage' not in st.session_state:
    st.session_state.stage = 1

# Butonların HTML ve CSS'i
def get_button_html(text, button_id, size=1):
    font_size = f"{2.5 + size * 0.2}rem"  # Her basışta yazı tipi boyutu büyür
    padding_size = f"{0.5 + size * 0.1}rem" # Her basışta padding boyutu büyür
    
    css_style = f"""
    <style>
        .stButton button#{button_id} {{
            font-size: {font_size};
            padding: {padding_size} 1rem;
            color: #fff;
            background-color: #4CAF50;
            border: 2px solid #4CAF50;
            border-radius: 10px;
            cursor: pointer;
            transition: all 0.3s ease;
        }}
    </style>
    """
    
    return css_style + f'<button id="{button_id}">{text}</button>'

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
    
    # Uyumlu ilk sticker
    st.markdown(get_sticker_html("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZtMTdxeGZzOGN2dG1tbmFpaXJsczEwaXJ0bW93c3Y5Z3h3ajd4ZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/jY5xK2D6s0uF9lWzVl/giphy.gif"), unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pass
    
    with col2:
        # Evet butonu büyüyen buton
        if st.button("Evet", key="evet_button"):
            st.session_state.stage = 2
            st.experimental_rerun()
            
        st.markdown(f'<style>.stButton button {{font-size: {2.5 + st.session_state.button_size * 0.2}rem; padding: {0.5 + st.session_state.button_size * 0.1}rem 1rem;}}</style>', unsafe_allow_html=True)
    
    with col3:
        # Hayır butonu
        if st.button("Hayır", key="hayir_button"):
            st.session_state.button_size += 1
            st.experimental_rerun()

# AŞAMA 2: Affedildiğini gösteren ekran
elif st.session_state.stage == 2:
    st.markdown("<h1 style='text-align: center; font-size: 3rem; color: #ff69b4;'>Beni affedeceğini biliyordum!</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; font-size: 2.5rem; color: #333;'>Seni çok seviyorum ❤️</h2>", unsafe_allow_html=True)
    
    # Öpücük sticker'ı
    st.markdown(get_sticker_html("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzM5OTYyOHRraXBwN2F0M241aXZsdGhkajZtb3Nkd3k3eTB1aWRkZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/z5B1g3tF48p4b1Vb5b/giphy.gif"), unsafe_allow_html=True)