import streamlit as st

#---SAYFA AYARLARI ---
st.set_page_config(
    page_title="CYHN | Matematik Portalı", 
    page_icon="mc.png", 
    layout="wide",
    initial_sidebar_state="expanded" 
)


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
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@400;500&display=swap');
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


# --- DURUM YÖNETİMİ (Session State) ---
if "sayfa" not in st.session_state:
    st.session_state["sayfa"] = "ana_menu" # İlk açılışta ana menü görünsün

# --- FONKSİYONLAR ---
def ana_menuye_don():
    st.session_state["sayfa"] = "ana_menu"
    st.rerun()

# --- 1. AŞAMA: ANA KARŞILAMA MENÜSÜ ---
if st.session_state["sayfa"] == "ana_menu":
    col1, col2, col3 = st.columns([0.5, 3, 0.5])
    
    with col2:
        st.title("CYHN Matematik Portalı")
        st.markdown(
            """
            *“Matematik, evrenin dilidir.”*  
            Bilgiye açılan kapıya hoş geldiniz..! Akademik arşivimize ulaşmak veya yapay zeka asistanımızdan destek almak için lütfen bir işlem seçiniz.
            """
        )
        st.divider()
        

        # İki büyük seçenek butonu
        c1, c2 = st.columns(2)
        
        with c1:
            # Ders Notları Kartı
            with st.container(border=True):
                st.markdown("### 📚 Ders Arşivi")
                st.write("Akademik ders notlarının yanı sıra; haftalık ders programları, güncel sınav takvimleri ve bölüm duyurularına tek tıkla erişin.")
                st.write("") # Küçük bir boşluk
                # type="primary" butonu sitenizin ana rengine (genelde kırmızı/turuncu/mavi) boyar
                if st.button("Arşivi Görüntüle", use_container_width=True):
                    st.session_state["sayfa"] = "sifre_kontrol"
                    st.rerun()
                    
        with c2:
            # cyhnAI Destek Kartı
            with st.container(border=True):
                st.markdown("### ✨ cyhnAI Destek")
                st.write("Matematik sorularınıza, formüllere ve takıldığınız tüm konularda yapay zeka desteğimiz ile anında çözüm bulun.")
                st.write("") # Küçük bir boşluk
                # link_button zaten varsayılan olarak şık durur
                st.link_button("Yapay Zekayı Başlat", "https://agent.jotform.com/019c71e214af725e8ca84db422ebe7088bfc", use_container_width=True)
        
        st.divider()

# Alt Bilgi (Footer) Tasarımı
        c_left, c_right = st.columns(2)
        with c_left:
            st.markdown(
                """
                <p style='text-align: left; color: gray; font-size: 0.8rem;'>
                    🚀 CYHN Matematik Geliştirme Platformu © 2026
                </p>
                """, 
                unsafe_allow_html=True
            )
        with c_right:
            st.markdown(
                """
                <p style='text-align: right; color: gray; font-size: 0.8rem;'>
                    Developed with by <span style='color: #FF4B4B; font-weight: bold;'>CYHN</span>
                </p>
                """, 
                unsafe_allow_html=True
            )

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

                # --- ÖNCE GÖRSEL ÖĞELERİ ÇALIŞTIR ---
                    # Sağ altta küçük bir popup (toast) çıkarır
                    st.toast(f"Hoş geldin {kullanici_adi.capitalize()}! Başarılar dileriz. 🚀")
                    
                    # Görsel bir şölen için balonlar
                    st.balloons() 
                    
                    # Mesajın ve balonların görünmesi için kısa bir bekleme süresi
                    import time
                    time.sleep(2) 
                    
                    # --- EN SON SAYFAYI YENİLE ---
                    st.rerun()
                
                # 3. Kontrol: Hatalı bilgiler
                else:
                    st.error("Kullanıcı adı veya şifre hatalı!")
                    
        with c2:
             if st.button("⬅ Geri Dön"):
                ana_menuye_don()

# --- 3. AŞAMA: DERS NOTLARI VE PDF ARŞİVİ ---
elif st.session_state["sayfa"] == "notlar_arsivi":
    with st.spinner("Matematik Portalı Hazırlanıyor..."):
        import time
        time.sleep(1)
    # Sidebar (Yan Menü)
    with st.sidebar:
            st.title(f"♾️ Hoş Geldin, {st.session_state['aktif_user'].capitalize()}!")
            # --- ÖZEL BUTON TASARIMLARI (CSS) ---
            st.markdown("""
            <style>
            .sidebar-custom-button {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 100%);
                color: white !important;
                padding: 12px 20px;
                border-radius: 12px;
                text-decoration: none;
                font-weight: bold;
                transition: all 0.3s ease;
                border: 1px solid rgba(255,255,255,0.1);
                margin-bottom: 15px;
                width: 100%;
            }
            .sidebar-custom-button:hover {
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                background: linear-gradient(135deg, #1e40af 0%, #2563eb 100%);
                text-decoration: none;
                color: #ffffff !important;
            }
            .ai-button {
                background: linear-gradient(135deg, #059669 0%, #10b981 100%) !important; /* Yapay zeka için yeşil tonu */
            }
            .ai-button:hover {
                background: linear-gradient(135deg, #10b981 0%, #34d399 100%) !important;
            }
            </style>
            
            <!-- İletişim Butonu -->
            <a href="mailto:matematikegitiminevu@gmail.com" class="sidebar-custom-button">
                📩 İletişim Maili
            </a>
            
            <!-- Yapay Zeka Butonu (Aynı Tasarım) -->
            <a href="https://agent.jotform.com/019c71e214af725e8ca84db422ebe7088bfc" target="_blank" class="sidebar-custom-button ai-button">
                ✨ cyhnAI'a Sor
            </a>
            """, unsafe_allow_html=True)

            st.divider()
            if st.button("🔐 Güvenli Çıkış"):
                    st.session_state["aktif_user"] = None
                    ana_menuye_don()
            
    st.title("📚 Matematik Ders Notları ve PDF Arşivi")
    kullanici = st.session_state["aktif_user"].capitalize()
    # --- YENİ EKLENEN MESAJ ---
    st.markdown(f"""
    > **Hoş geldin {kullanici}!** Bu arşiv, akademik yolculuğunuzda size rehberlik etmek için özenle hazırlanmıştır. 
    > Aşağıdaki sekmeleri kullanarak ders notlarına erişebilir, çalışmalarınızı derinleştirebilirsiniz. 
    > *Başarılar dileriz!*
       """)
    # --------------------------
    st.markdown("---")

    # Konulara göre sekmeler (Tablar)
    tab0, tab1, tab2, tab3, tab4 = st.tabs([
        "📢 Güncel Duyurular",
        "💻 Algoritma ve Programlama",
        "🔢 Lineer Cebir PDF Notları", 
        "🎲 Analiz PDF Notları", 
        "📐 Soyut Matematik PDF Notları"
    ])

    with tab0:
        st.subheader("Güncel Duyurular Bölümü")
        st.warning("❗Bu kısımda Matematik Eğitimi Anabilimdalının güncel bilgileri paylaşılmaktadır.")
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.container(border=True):
                st.markdown("**NEVÜ MAFET**")
                st.link_button("Sayfayı Görüntüle", "https://mafet.nevsehir.edu.tr/", use_container_width=True)
        with col2:
            with st.container(border=True):
                st.markdown("**Ders Programı**")
                st.link_button("Programı Görüntüle", "https://dosyalar.nevsehir.edu.tr/6667946ceeefe0f7a69e00d88e9e25d7/matematik-egitimi-2025-2026-bahar-donemi-haftalik-program_final-hali-4.pdf", use_container_width=True)
        with col3:
            with st.container(border=True):
                st.markdown("**Sınav Takvimi**")
                st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln0")

    with tab1:
        st.subheader("Algoritma ve Programlama Ders Notu")
        st.warning("❗Bu bölümdeki dosyalar güncellenmektedir. PDF ler henüz yüklenmemiştir!")
        st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln5")

    with tab2:
        st.subheader("Lineer Cebir Ders Notları")
        st.warning("❗Bu bölümdeki dosyalar güncellenmektedir. PDF ler henüz yüklenmemiştir!")
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("**Lineer Cebir 1**")
                st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln1")
        with col2:
            with st.container(border=True):
                st.markdown("**Lineer Cebir 2**")
                st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/1cizrFK5VLT0LXGsYph1q5IOT7nx4TT_H/view?usp=sharing", use_container_width=True)
    
    with tab3:
        st.subheader("Analiz 1 ve 2 Ders Notları")
        st.warning("❗Bu bölümdeki dosyalar güncellenmektedir. PDF ler henüz yüklenmemiştir!")
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("**Analiz 1**")
                st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln2")
        with col2:
            with st.container(border=True):
                st.markdown("**Analiz 2**")
                st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln3")

    with tab4:
        st.subheader("Soyut Matematik Ders Notu")
        st.warning("❗Bu bölümdeki dosyalar güncellenmektedir. PDF ler henüz yüklenmemiştir!")
        st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln4")

    

    # Alt Bilgi
    st.markdown("---")
    st.caption("🚀 CYHN Matematik Geliştirme Platformu © 2026")
