import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="cyhnAI | Matematik Arşivi", page_icon="📐", layout="wide")

# --- GİRİŞ SİSTEMİ ---
def giris_kontrol():
    if "giris_yapildi" not in st.session_state:
        st.session_state["giris_yapildi"] = False

    if not st.session_state["giris_yapildi"]:
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.title("🔒 Matematik Paneli")
            sifre = st.text_input("Erişim Şifresi:", type="password")
            if st.button("Sisteme Giriş"):
                if sifre == "mat2026":
                    st.session_state["giris_yapildi"] = True
                    st.rerun()
                else:
                    st.error("Hatalı şifre!")
        return False
    return True

# --- ANA İÇERİK ---
if giris_kontrol():
    # Sidebar (Yan Menü)
    with st.sidebar:
        st.title("📐 Matematik Portalı")
        st.write("Hoş geldiniz!")
        if st.button("Güvenli Çıkış"):
            st.session_state["giris_yapildi"] = False
            st.rerun()

    st.title("📚 Matematik Ders Notları ve PDF Arşivi")
    st.markdown("---")

    # Konulara göre sekmeler (Tablar) oluşturuyoruz
    tab1, tab2, tab3, tab4 = st.tabs([
        "🔢 Lineer Cebir PDF Notları", 
        "🎲 Boş Alan 1", 
        "📐 Boş Alan 2",
        "📝 Boş Alan 3"
    ])

    with tab1:
        st.subheader("Lineer Cebir Ders Notları")
        col1, col2 = st.columns(2)
        with col1:
            st.info("Lineer Cebir 1")
            st.link_button("PDF'i Görüntüle", "BURAYA_DRIVE_LINKI_GELECEK")
        with col2:
            st.info("Lineer Cebir 2")
            st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/1cizrFK5VLT0LXGsYph1q5IOT7nx4TT_H/view?usp=sharing")

    with tab2:
        st.subheader("Boş Alan 1")
        st.write("Bu bölümdeki dosyalar güncellenmektedir.")
        # Liste şeklinde butonlar
        st.link_button("👉 Boş Alan ", "BURAYA_DRIVE_LINKI_GELECEK")
        st.link_button("👉 Boş Alan ", "BURAYA_DRIVE_LINKI_GELECEK")

    with tab3:
        st.subheader("Boş Alan 2")
        st.write("Bu bölümdeki dosyalar güncellenmektedir.")
        st.link_button("👉 Boş Alan", "BURAYA_DRIVE_LINKI_GELECEK")
        st.link_button("👉 Boş Alan", "BURAYA_DRIVE_LINKI_GELECEK")

    with tab4:
        st.subheader("Boş Alan 3")
        st.warning("Bu bölümdeki dosyalar güncellenmektedir.")
        st.link_button("👉 Boş Alan", "BURAYA_DRIVE_LINKI_GELECEK")

    # Alt Bilgi
    st.markdown("---")
    st.caption("M.cyhn Matematik Geliştirme Platformu © 2026")