import streamlit as st
import time

# --- 1. SAYFA AYARLARI ---
st.set_page_config(
    page_title="CYHN | Matematik Portalı", 
    page_icon="mc.png", 
    layout="wide",
    initial_sidebar_state="expanded" 
)

# --- 2. DURUM YÖNETİMİ ---
if "ana_sayfa_sekme" not in st.session_state:
    st.session_state["ana_sayfa_sekme"] = "🏠 Ana Sayfa"

if "giris_yapildi" not in st.session_state:
    st.session_state["giris_yapildi"] = False

USERS = {
    "muharrem": "mat2026",
    "ogrenci1": "admin1",
    "ogrenci2": "admin2",
    "ogrenci3": "admin3",
    "ogrenci4": "admin4"
}

# --- 3. TASARIM (CSS) ---
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #1e40af 100%);
        background-attachment: fixed;
    }
    h1, h2, h3, p, span, label {
        color: white !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    /* Üst Menü Butonları */
    div.stButton > button {
        background-color: transparent !important;
        color: white !important;
        border: none !important;
        font-size: 18px !important;
        font-weight: 500 !important;
        transition: all 0.3s ease;
        border-bottom: 2px solid transparent !important;
    }
    div.stButton > button:hover {
        color: #ff4b4b !important;
        border-bottom: 2px solid #ff4b4b !important;
        background-color: rgba(255, 75, 75, 0.05) !important;
    }
    /* İmza Fontu */
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;500&display=swap');
    .signature {
        font-family: 'Dancing Script', cursive;
        font-size: 24px;
        color: #ffffff;
        margin-top: -10px;
    }
</style>
""", unsafe_allow_html=True)

# --- 4. YAN MENÜ (SIDEBAR) ---
st.sidebar.image("mc250.png") 
st.sidebar.markdown("---")
st.sidebar.write("### CYHN Matematik Portalı")
st.sidebar.markdown('<p class="signature">Muharrem Ceyhan</p>', unsafe_allow_html=True)
st.sidebar.markdown("---")

# --- 5. ÜST MENÜ NAVİGASYON ---
m1, m2, m3, m4 = st.columns(4)
with m1:
    if st.button("🏠 Ana Sayfa", use_container_width=True):
        st.session_state["ana_sayfa_sekme"] = "🏠 Ana Sayfa"
        st.rerun()
with m2:
    if st.button("👥 Biz Kimiz", use_container_width=True):
        st.session_state["ana_sayfa_sekme"] = "👥 Biz Kimiz"
        st.rerun()
with m3:
    if st.button("ℹ️ Hakkımızda", use_container_width=True):
        st.session_state["ana_sayfa_sekme"] = "ℹ️ Hakkımızda"
        st.rerun()
with m4:
    if st.button("🔐 Portal Giriş", use_container_width=True):
        st.session_state["ana_sayfa_sekme"] = "🔐 Portal Giriş"
        st.rerun()

st.markdown("---")

# --- 6. SAYFA İÇERİKLERİ ---

# --- SEKME: ANA SAYFA ---
if st.session_state["ana_sayfa_sekme"] == "🏠 Ana Sayfa":
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.title("CYHN Matematik Portalı")
        st.markdown("*“Matematik, evrenin dilidir.”*")
        st.write("Platformumuza hoş geldiniz. Lütfen yapmak istediğiniz işlemi seçiniz:")
        st.divider()

        c1, c2 = st.columns(2)
        with c1:
            st.info("✨ **cyhnAI Destek**")
            st.write("Sorularınıza yapay zeka ile anında çözüm bulun.")
            st.link_button("Yapay Zekayı Başlat", "https://agent.jotform.com/019c71e214af725e8ca84db422ebe7088bfc")
        with c2:
            st.success("📚 **Ders Notları**")
            st.write("Lineer Cebir ve diğer ders notlarına erişin.")
            if st.button("Arşivi Görüntüle"):
                st.session_state["ana_sayfa_sekme"] = "🔐 Portal Giriş"
                st.rerun()

# --- SEKME: BİZ KİMİZ ---
elif st.session_state["ana_sayfa_sekme"] == "👥 Biz Kimiz":
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("mc250.png")
    with col2:
        st.header("Muharrem Ceyhan")
        st.write("""
        İlköğretim Matematik Öğretmenliği öğrencisiyim. Teknolojiyi ve matematiği 
        birleştirerek öğrencilere dijital dünyada rehberlik etmeyi amaçlıyorum.
        """)

# --- SEKME: HAKKIMIZDA ---
elif st.session_state["ana_sayfa_sekme"] == "ℹ️ Hakkımızda":
    st.header("Portal Hakkında")
    st.info("""
    Bu platform, matematik eğitiminde yapay zeka ve dijital materyallerin 
    etkin kullanımını göstermek amacıyla geliştirilmiştir.
    """)

# --- SEKME: PORTAL (GİRİŞ VE ARŞİV) ---
elif st.session_state["ana_sayfa_sekme"] == "🔐 Portal Giriş":
    if not st.session_state["giris_yapildi"]:
        col1, col2, col3 = st.columns([1,2,1])
        with col2:
            st.subheader("🔒 Özel Arşiv Erişimi")
            st.write("Bu alan sadece yetkilendirilmiş kullanıcılara özeldir.")
            
            with st.expander("⚠️ Telif Hakkı ve Kullanım Şartları", expanded=True):
                st.warning("""
                    **Yasal Uyarı:** 
                    Bu platformda paylaşılan tüm ders PDF notlarının telif hakları doğrudan **Muharrem CEYHAN**'a aittir. 
                    Tüm hakları saklıdır. İçeriklerin kopyalanması kesinlikle yasaktır. (© 2026)
                """)
                onay = st.checkbox("Okudum, anladım ve kullanım şartlarını kabul ediyorum.")
            
            st.divider()
            kullanici_adi = st.text_input("Kullanıcı Adı:")
            sifre = st.text_input("Portal Erişim Şifresi:", type="password")
            
            if st.button("Sisteme Giriş", use_container_width=True):
                if not onay:
                    st.error("Lütfen önce kullanım şartlarını onaylayınız!")
                elif kullanici_adi in USERS and USERS[kullanici_adi] == sifre:
                    st.session_state["giris_yapildi"] = True
                    st.session_state["aktif_user"] = kullanici_adi
                    st.rerun()
                else:
                    st.error("Kullanıcı adı veya şifre hatalı!")
    else:
        # ARŞİV İÇERİĞİ
        with st.spinner("Matematik Portalı Hazırlanıyor..."):
            time.sleep(1)

        with st.sidebar:
            st.success(f"Giriş Yapıldı: {st.session_state['aktif_user']}")
            if st.button("🔐 Güvenli Çıkış"):
                st.session_state["giris_yapildi"] = False
                st.rerun()

        st.title("📚 Matematik Ders Notları ve PDF Arşivi")
        st.markdown("> **Hoş geldiniz!** Bu arşiv, akademik yolculuğunuzda size rehberlik etmek için özenle hazırlanmıştır.")
        
        tab0, tab1, tab2, tab3, tab4 = st.tabs([
            "📢 Güncel Duyurular", "🔢 Lineer Cebir", "🎲 Analiz", "📐 Soyut Matematik", "📝 Boş Alan"
        ])

        with tab0:
            st.subheader("Güncel Duyurular")
            st.warning("❗Bu bölümde üniversiteye dair güncel bilgiler paylaşılmaktadır.")
            c1, c2 = st.columns(2)
            with c1:
                st.info("Ders Programı")
                st.link_button("PDF'i Görüntüle", "LİNK_BURAYA")
            with c2:
                st.info("Sınav Takvimi")
                st.link_button("PDF'i Görüntüle", "LİNK_BURAYA")
            
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
