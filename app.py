import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="M.cyhn | Matematik Portalı", page_icon="📐", layout="wide")

# --- DURUM YÖNETİMİ (Session State) ---
if "sayfa" not in st.session_state:
    st.session_state["sayfa"] = "ana_menu" # İlk açılışta ana menü görünsün

# --- FONKSİYONLAR ---
def ana_menuye_don():
    st.session_state["sayfa"] = "ana_menu"
    st.rerun()

# --- 1. AŞAMA: ANA KARŞILAMA MENÜSÜ ---
if st.session_state["sayfa"] == "ana_menu":
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        st.title("📐 cyhn Matematik Portalı")
        st.markdown("*“Matematik, evrenin dilidir.”*")
        st.write("Platformumuza hoş geldiniz. Lütfen yapmak istediğiniz işlemi seçiniz:")
        st.divider()

        # İki büyük seçenek butonu
        c1, c2 = st.columns(2)
        
        with c1:
            st.info("🤖 **cyhnAI Destek**")
            st.write("Sorularınıza yapay zeka ile anında çözüm bulun.")
            # Yapay zeka sitene doğrudan yönlendirme butonu
            st.link_button("Yapay Zekayı Başlat", "https://SENIN_AI_SITENIN_LINKI.com")

        with c2:
            st.success("📚 **Ders Notları**")
            st.write("Lineer Cebir ve diğer ders notlarına erişin.")
            if st.button("Arşivi Görüntüle"):
                st.session_state["sayfa"] = "sifre_kontrol"
                st.rerun()
        
        st.divider()
        st.caption("M.cyhn Matematik Geliştirme Platformu © 2026")

# --- 2. AŞAMA: ŞİFRE KONTROL EKRANI ---
elif st.session_state["sayfa"] == "sifre_kontrol":
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.subheader("🔒 Özel Arşiv Erişimi")
        st.write("Bu alan sadece yetkilendirilmiş kullanıcılara özeldir.")
        
        # --- TELİF HAKKI UYARISI ---
        # expanded=True yaparak kutunun otomatik açık gelmesini sağladık
        with st.expander("⚠️ Telif Hakkı ve Kullanım Şartları", expanded=True):
            st.warning("""
                **Yasal Uyarı:** 
                Bu platformda paylaşılan tüm ders notları ve materyaller **M.cyhn** telif hakları kapsamındadır. 
                İçeriklerin izinsiz olarak kopyalanması, çoğaltılması veya başka platformlarda 
                paylaşılması yasal sorumluluk doğurabilir. 
                Sadece kişisel eğitim amaçlı kullanım içindir.
            """)
            # Onay kutucuğu
            onay = st.checkbox("Okudum, anladım ve kullanım şartlarını kabul ediyorum.")
        
        st.divider()
        
        sifre = st.text_input("Lütfen Erişim Şifresini Giriniz:", type="password")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Sisteme Giriş"):
                # ÖNCE ONAY KUTUSUNA BAKIYORUZ:
                if not onay:
                    st.error("Lütfen önce kullanım şartlarını onaylayınız!")
                # SONRA ŞİFREYE BAKIYORUZ:
                elif sifre == "mat2026":
                    st.session_state["sayfa"] = "notlar_arsivi"
                    st.rerun()
                else:
                    st.error("Hatalı şifre!")
        with c2:
            if st.button("⬅ Geri Dön"):
                ana_menuye_don()

# --- 3. AŞAMA: DERS NOTLARI VE PDF ARŞİVİ ---
elif st.session_state["sayfa"] == "notlar_arsivi":
    # Sidebar (Yan Menü)
    with st.sidebar:
        st.title("📐 Matematik Portalı")
        st.write("Hoş geldiniz!")
        st.divider()
        st.success("🤖 Yapay Zeka Desteği")
        st.link_button("cyhnAI Zekasına Sor", "https://SENIN_AI_SITENIN_LINKI.com")
        st.divider()
        if st.button("Güvenli Çıkış"):
            ana_menuye_don()

    st.title("📚 Matematik Ders Notları ve PDF Arşivi")
    st.markdown("---")

    # Konulara göre sekmeler (Tablar)
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
        st.link_button("👉 Boş Alan ", "BURAYA_DRIVE_LINKI_GELECEK")

    with tab3:
        st.subheader("Boş Alan 2")
        st.write("Bu bölümdeki dosyalar güncellenmektedir.")
        st.link_button("👉 Boş Alan", "BURAYA_DRIVE_LINKI_GELECEK")

    with tab4:
        st.subheader("Boş Alan 3")
        st.warning("Bu bölümdeki dosyalar güncellenmektedir.")
        st.link_button("👉 Boş Alan", "BURAYA_DRIVE_LINKI_GELECEK")

    # Alt Bilgi
    st.markdown("---")
    st.caption("M.cyhn Matematik Geliştirme Platformu © 2026")
