import streamlit as st


#---SAYFA AYARLARI ---
st.set_page_config(
    page_title="CYHN | Matematik Portalı", 
    page_icon="mc.png", 
    layout="wide",
    initial_sidebar_state="expanded" 
)

USERS = {
    "muharrem": "mat2026",
    "ogrenci1": "admin1",
    "ogrenci2": "admin2",
    "ogrenci3": "admin3",
    "ogrenci4": "admin4"
    
}
    
# --- LOGOYU YAN MENÜYE EKLEME ---
st.sidebar.image("mc250.png") 

# İsteğe bağlı: Logonun altına ince bir ayırıcı çizgi ve başlık ekleyebilirsiniz
st.sidebar.markdown("---")
st.sidebar.write("### CYHN Matematik Portalı")
# İmza tarzı, ince yazı tasarımı
st.sidebar.markdown(
    """
    <meta name="google-site-verification" content="O9e2wXECkBmV8edl91Ov0QPjWT9qakF70z9H3fGBgVI" />
    <style>
    
    .signature {
        font-family: 'Dancing Script', cursive;
        font-size: 24px;
        font-weight: 400;
        color: #555555;
        margin-top: -10px;
    }
    </style>
    <p class="signature">Muharrem Ceyhan</p>
    """, 
    unsafe_allow_html=True
)
st.sidebar.markdown("---")


# --- SAYFA ARKA PLANI ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #1e40af 100%);
        background-attachment: fixed;
    }
    
    /* Yazıların daha okunaklı olması için beyaz gölge ekleyelim */
    h1, h2, h3, p {
        color: white !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)


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
        st.title("CYHN Matematik Portalı")
        st.markdown("*“Matematik, evrenin dilidir.”*")
        st.write("Platformumuza hoş geldiniz. Lütfen yapmak istediğiniz işlemi seçiniz:")
        st.divider()

        # İki büyük seçenek butonu
        c1, c2 = st.columns(2)
        
        with c1:
            st.info("✨ **cyhnAI Destek**")
            st.write("Sorularınıza yapay zeka ile anında çözüm bulun.")
            # Yapay zeka sitene doğrudan yönlendirme butonu
            st.link_button("Yapay Zekayı Başlat", "https://agent.jotform.com/019c71e214af725e8ca84db422ebe7088bfc")

        with c2:
            st.success("📚 **Ders Notları**")
            st.write("Lineer Cebir ve diğer ders notlarına erişin.")
            if st.button("Arşivi Görüntüle"):
                st.session_state["sayfa"] = "sifre_kontrol"
                st.rerun()
        
        st.divider()
        st.caption("CYHN Matematik Geliştirme Platformu © 2026")

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
                Bu platformda paylaşılan tüm ders PDF notlarının telif hakları doğrudan **Muharrem CEYHAN**'a aittir. 
    Tüm hakları saklıdır.    
    İçeriklerin tamamının veya bir kısmının, yazarın yazılı izni olmaksızın kopyalanması, çoğaltılması, işlenmesi veya herhangi bir dijital/basılı mecrada paylaşılması **kesinlikle yasaktır**. (© 2026)
    Sadece kişisel eğitim amaçlıdır..!
            """)
            # Onay kutucuğu
            onay = st.checkbox("Okudum, anladım ve kullanım şartlarını kabul ediyorum.")
        
        st.divider()
        
        # --- KULLANICI ADI VE ŞİFRE GİRİŞİ ---
        kullanici_adi = st.text_input("Kullanıcı Adı:")
        sifre = st.text_input("Portal Erişim Şifresi:", type="password")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Sisteme Giriş"):
                # 1. Kontrol: Onay kutusu
                if not onay:
                    st.error("Lütfen önce kullanım şartlarını onaylayınız!")
                
                # 2. Kontrol: Kullanıcı adı ve Şifre eşleşmesi
                elif kullanici_adi in USERS and USERS[kullanici_adi] == sifre:
                    st.session_state["sayfa"] = "notlar_arsivi"
                    st.session_state["aktif_user"] = kullanici_adi # Kimin girdiğini hafızaya alalım
                    st.rerun()
                
                # 3. Kontrol: Hatalı bilgiler
                else:
                    st.error("Kullanıcı adı veya şifre hatalı!")
                    
        with c2:
             if st.button("⬅ Geri Dön"):
                ana_menuye_don()

# --- 3. AŞAMA: DERS NOTLARI VE PDF ARŞİVİ ---
elif st.session_state["sayfa"] == "notlar_arsivi":
    # Sidebar (Yan Menü)
    with st.sidebar:
        st.title("♾️ Matematik Portalı")
        st.write("Hoş geldiniz!")
        st.divider()
        st.success("✨ Yapay Zeka Desteği")
        st.link_button("cyhnAI'a Sor", "https://agent.jotform.com/019c71e214af725e8ca84db422ebe7088bfc")
        st.divider()
        if st.button("🔐 Güvenli Çıkış"):
            ana_menuye_don()
            
    st.title("📚 Matematik Ders Notları ve PDF Arşivi")
    # --- YENİ EKLENEN MESAJ ---
    st.markdown("""
    > **Hoş geldiniz!** Bu arşiv, akademik yolculuğunuzda size rehberlik etmek için özenle hazırlanmıştır. 
    > Aşağıdaki sekmeleri kullanarak ders notlarına erişebilir, çalışmalarınızı derinleştirebilirsiniz. 
    > *Başarılar dileriz!*
    """)
    # --------------------------
    st.markdown("---")

    # Konulara göre sekmeler (Tablar)
    tab1, tab2, tab3, tab4 = st.tabs([
        "🔢 Lineer Cebir PDF Notları", 
        "🎲 Analiz PDF Notları", 
        "📐 Soyut Matematik PDF Notları",
        "📝 Boş Alan 3"
    ])

    with tab1:
        st.subheader("Lineer Cebir Ders Notları")
        st.warning("❗Bu bölümdeki dosyalar güncellenmektedir. PDF ler henüz yüklenmemiştir!")
        col1, col2 = st.columns(2)
        with col1:
            st.info("Lineer Cebir 1")
            st.link_button("PDF'i Görüntüle", "BURAYA_DRIVE_LINKI_GELECEK")
        with col2:
            st.info("Lineer Cebir 2")
            st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/1cizrFK5VLT0LXGsYph1q5IOT7nx4TT_H/view?usp=sharing")

    with tab2:
        st.subheader("Analiz 1 ve 2 Ders Notları")
        st.warning("❗Bu bölümdeki dosyalar güncellenmektedir. PDF ler henüz yüklenmemiştir!")
        col1, col2 = st.columns(2)
        with col1:
            st.info("Analiz 1")
            st.link_button("PDF'i Görüntüle", "BURAYA_DRIVE_LINKI_GELECEK")
        with col2:
            st.info("Analiz 2")
            st.link_button("PDF'i Görüntüle", "BURAYA_DRIVE_LINKI_GELECEK")

    with tab3:
        st.subheader("Soyut Matematik Ders Notu")
        st.warning("❗Bu bölümdeki dosyalar güncellenmektedir. PDF ler henüz yüklenmemiştir!")
        st.link_button("PDF'i Görüntüle ", "BURAYA_DRIVE_LINKI_GELECEK")

    with tab4:
        st.subheader("Boş Alan 3")
        st.warning("❗Bu bölümdeki dosyalar güncellenmektedir. PDF ler henüz yüklenmemiştir!")
        st.link_button("👉 Boş Alan", "BURAYA_DRIVE_LINKI_GELECEK")

    # Alt Bilgi
    st.markdown("---")
    st.caption("CYHN Matematik Geliştirme Platformu © 2026")
