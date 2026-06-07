import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo
import time

#---KULLANICI İSİMLERİ VE ŞİFRELERİ ---
USERS = {
    "muharrem": "mat2026",
    "mustafa": "bekmezcioğlu2026",
    "ahmed": "ahmedbedenli50",
    "ibrahim": "akkutlu26",
    "serap": "serapnom26",
    "mehmet": "guver51",
    "nisa": "nisatürk38",
    "irem": "iremyıldızoğlu26",
    "deniz": "denizekici26",
    "rumeysa": "rumeysa38",
    "gülsüm": "keve26",
    "seyit": "seyitcantör26",
    "hicran": "hicranünal26",
    "duygu": "duyguongeli26",
    "admin3": "adminşifre3",
    "admin3": "adminşifre3"
    
}


# =========================================================================
# 🛠️ BAKIM MODU AYARLARI
# =========================================================================
BAKIM_MODU = False           # Tüm siteyi kapatmak için True yapın
ARSIV_BAKIM_MODU = True     # Sadece ders arşivini kapatmak için True yapın

HEDEF_ZAMAN_GENEL = "2026-06-07 10:00:00"
HEDEF_ZAMAN_ARSIV = "2026-06-08 00:00:00"
# =========================================================================

# 🔐 GİZLI URL PARAMETRESİ KONTROLÜ (Adres çubuğunda ?mod=admin araması yapar)
gizli_yonetici_izni = str(st.query_params.get("mod")).lower() == "admin"


# --- SÜRE HESAPLAMA MOTORU (HTML Şablonu İçin) ---
def kalan_sure_html_hazirla(hedef_zaman_str):
    tr_saat_dilimi = ZoneInfo("Europe/Istanbul")
    simdi = datetime.now(tr_saat_dilimi)
    hedef = datetime.strptime(hedef_zaman_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=tr_saat_dilimi)
    kalan_sure = hedef - simdi
    
    if kalan_sure.total_seconds() > 0:
        gun = kalan_sure.days
        saat, artan = divmod(kalan_sure.seconds, 3600)
        dakika, _ = divmod(artan, 60)
        return f"""
        <div style="display: flex; justify-content: center; gap: 15px; margin-top: 25px; margin-bottom: 10px;">
            <div style="background: #ef4444; padding: 12px 20px; border-radius: 10px; min-width: 70px; text-align: center;">
                <span style="font-size: 1.8rem; font-weight: bold; display: block; color: white !important;">{gun}</span>
                <span style="font-size: 0.8rem; color: #fee2e2 !important; text-transform: uppercase; font-family: sans-serif;">Gün</span>
            </div>
            <div style="background: #3b82f6; padding: 12px 20px; border-radius: 10px; min-width: 70px; text-align: center;">
                <span style="font-size: 1.8rem; font-weight: bold; display: block; color: white !important;">{saat}</span>
                <span style="font-size: 0.8rem; color: #dbeafe !important; text-transform: uppercase; font-family: sans-serif;">Saat</span>
            </div>
            <div style="background: #10b981; padding: 12px 20px; border-radius: 10px; min-width: 70px; text-align: center;">
                <span style="font-size: 1.8rem; font-weight: bold; display: block; color: white !important;">{dakika}</span>
                <span style="font-size: 0.8rem; color: #d1fae5 !important; text-transform: uppercase; font-family: sans-serif;">Dk</span>
            </div>
        </div>
        """
    else:
        return """
        <p style="color: #10b981 !important; font-weight: bold; font-size: 1.2rem; margin-top: 25px; text-align: center; font-family: sans-serif;">
            🔄 Çalışmalar tamamlandı, sistem çok kısa süre içinde aktif olacaktır.
        </p>
        """


# =========================================================================
# 🛑 1. EN BAŞTAKİ KONTROL: SİTE GENEL BAKIM MODU
# =========================================================================
if BAKIM_MODU and not gizli_yonetici_izni:
    st.set_page_config(page_title="CYHN | Website Bakım Çalışması", page_icon="🔧", layout="centered")
    
    sayaç_html = kalan_sure_html_hazirla(HEDEF_ZAMAN_GENEL)
    tam_sayfa_html = f"""
    <div style="text-align: center; background-color: #1e293b; padding: 40px; border-radius: 16px; border: 1px solid #334155; box-shadow: 0 10px 25px rgba(0,0,0,0.5); font-family: sans-serif; margin-top: 30px;">
        <h2 style="color: white !important; margin-bottom: 15px;">🚧 Sistem Genel Bakım Çalışması</h2>
        <p style="font-size: 1.1rem; margin-top: 15px; color: #cbd5e1 !important; text-align: center;">
            Sizlere daha hızlı, güvenli ve performanslı bir deneyim sunabilmek amacıyla <b>CYHN Matematik Portalı</b> genel bir güncelleme çalışmasındadır.
        </p>
        {sayaç_html}
        <p style="color: #94a3b8 !important; font-size: 0.9rem; margin-top: 25px; text-align: center;">
            Sistem genelinde altyapı, veritabanı ve ders notları optimizasyonları yapılmaktadır. Anlayışınız için teşekkür ederiz.
        </p>
        <div style="margin-top: 30px; border-top: 1px solid #334155; padding-top: 15px; text-align: center;">
            <p style="color: #FF4B4B !important; font-weight: bold; font-size: 1.1rem; margin-bottom: 5px;">Muharrem CEYHAN</p>
            <p style="color: #64748b !important; font-size: 0.85rem; letter-spacing: 1px;">CYHN MATEMATİK GELİŞTİRME PLATFORMU</p>
        </div>
    </div>
    """
    st.components.v1.html(tam_sayfa_html, height=520, scrolling=False)
    st.stop()


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
    
    /* Yazıların daha okunaklı olması için gölge */
    h1, h2, h3, p, span, label {
        color: white !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.4);
    }

    /* 🛠️ GİRİŞ KUTULARINI MAT VE BELİRGİN YAPMA 🛠️ */
    .stTextInput input {
        background-color: #1e293b !important; /* Şeffaflığı bitiren mat koyu gri/mavi tonu */
        color: white !important;               /* İçindeki yazı rengi beyaz */
        border: 1px solid #334155 !important;  /* Kutunun etrafına ince şık bir çerçeve */
        border-radius: 8px !important;         /* Kenarları hafif yumuşat */
    }

    /* Kutunun içine tıklandığında (Focus modunda) çerçevenin parlaması için */
    .stTextInput input:focus {
        border-color: #FF4B4B !important;      /* Tıklanınca senin ana rengin olan kırmızı yansın */
        box-shadow: 0 0 0 1px #FF4B4B !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# --- LOGOYU YAN MENÜYE EKLEME ---
st.sidebar.image("mc250.png") 

# Logonun altına ince bir ayırıcı çizgi ve başlık 
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

# --- POPUP İÇİNDE GÜVENLİ PDF GÖSTERME MOTORU ---
@st.dialog("📄 CYHN Portal | Ders Notu Önizleme", width="large")
def pdf_popup_ac(drive_id):
    # Drive ID'sini alıp indirme/yazdırma araçlarını gizleyen 'preview' linkine dönüştürüyoruz
    embed_link = f"https://drive.google.com/file/d/{drive_id}/preview?hl=tr"
    
    kullanici = st.session_state.get("aktif_user", "Bilinmeyen Kullanıcı").upper()
    su_an = datetime.now().strftime("%d.%m.%Y")

    # Gelişmiş Güvenlik, Filigran ve Tıklama Kalkanı CSS'i
    st.markdown(f"""
    <style>
    .popup-konteyner {{
        position: relative;
        width: 100%;
        height: 650px;
    }}
    
    /* Pop-out (Drive'da Aç) butonunu kilitleyen görünmez kalkan */
    .drive-tıklama-kalkani {{
        position: absolute;
        top: 0;
        right: 0;
        width: 120px;       /* Butonun olduğu alanı genişçe kaplar */
        height: 60px;       /* Üst bar yüksekliği kadar yer kaplar */
        background-color: rgba(0, 0, 0, 0); /* Tamamen şeffaf / görünmez */
        z-index: 99999;     /* En üst katmanda durur */
        cursor: default;    /* Üzerine gelince tıklama işareti çıkmaz */
    }}
    
    .popup-filigran {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) rotate(-25deg);
        font-size: 1.8rem;
        color: rgba(239, 68, 68, 0.15) !important; /* %15 şeffaf kırmızı */
        font-weight: bold;
        text-align: center;
        z-index: 9998;     /* Filigran kalkanın bir tık altında kalabilir */
        pointer-events: none;
        white-space: nowrap;
        font-family: sans-serif;
    }}
    </style>
    
    <div class="popup-konteyner">
        <div class="drive-tıklama-kalkani"></div>
        
        <div class="popup-filigran">KULLANICI: {kullanici}<br>CYHN PORTAL LİSANSLI DÖKÜMAN<br>{su_an}</div>
    </div>
    """, unsafe_allow_html=True)

    # Iframe ile Drive PDF'ini popup içine gömüyoruz
    st.components.v1.html(
        f'<iframe src="{embed_link}#toolbar=0&navpanes=0" width="100%" height="640" style="border:none; border-radius:8px;"></iframe>',
        height=650
    )
    

# --- 1. AŞAMA: ANA KARŞILAMA MENÜSÜ ---
if st.session_state["sayfa"] == "ana_menu":
    col1, col2, col3 = st.columns([0.5, 3, 0.5])
    
    with col2:
        st.title("CYHN Matematik Portalı")
        st.markdown(
            """
            *“Matematik, evrenin dilidir.”*  
            Bilgiye açılan kapıya hoş geldiniz..! Akademik ders notları arşivimize ulaşmak veya yapay zeka asistanımızdan destek almak için lütfen bir işlem seçiniz.
            """
        )
        st.divider()
        

        # İki büyük seçenek butonu
        c1, c2 = st.columns(2)
        
        with c1:
            # Ders Notları Kartı
            with st.container(border=True):
                st.markdown("### 📚 Ders Notları Arşivi")
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
                    Developed with by 🇹🇷 <span style='color: #FF4B4B; font-weight: bold;'>CYHN</span>
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
    İçeriklerin tamamının veya bir kısmının, yazarın yazılı izni olmaksızın kopyalanması, çoğaltılması, işlenmesi veya herhangi bir dijital/basılı mecrada paylaşılması **kesinlikle yasaktır**.
    Sadece kişisel eğitim amaçlıdır..!
    (© 2026)
            """)
            # Onay kutucuğu
            onay = st.checkbox("Okudum, anladım ve kullanım şartlarını kabul ediyorum.")
        
        st.divider()
        
        # --- KULLANICI ADI VE ŞİFRE GİRİŞİ ---
        kullanici_adi = st.text_input("Kullanıcı Adı:")
        sifre = st.text_input("Portal Erişim Şifresi:", type="password")
        
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("🔒 Güvenli Giriş", use_container_width=True):
                # 1. Kontrol: Onay kutusu
                if not onay:
                    st.error("Lütfen önce kullanım şartlarını onaylayınız!")
                
                # 2. Kontrol: Kullanıcı adı ve Şifre eşleşmesi (YENİ VE DÜZELTİLEN KISIM BURASI)
                elif kullanici_adi in USERS and USERS[kullanici_adi] == sifre:
                    # Başarılı giriş popup mesajı (Ekranın sağ altında görünür)
                    st.toast(f"🔑 Giriş Başarılı! Hoş geldin {kullanici_adi.capitalize()}.🚀", icon="🎉")
                    # Havai fişek/balon efekti
                    st.balloons() 
                    
                    # Kullanıcı mesajı görsün diye 2 saniye bekletiyoruz
                    import time
                    time.sleep(2) 
                    
                    # Bilgileri kaydedip sayfayı yönlendiriyoruz
                    st.session_state["aktif_user"] = kullanici_adi 
                    st.session_state["sayfa"] = "notlar_arsivi"    
                    st.rerun()
                
                # 3. Kontrol: Hatalı bilgiler
                else:
                    st.error("Kullanıcı adı veya şifre hatalı!")

        with c2:
            mail_konu = "CYHN%20Portal%20Eri%C5%9Fim%20Talebi"
            mail_icerik = "Merhaba,%0D%0ACYHN%20Matematik%20Portalı%20için%20kullanıcı%20adı%20ve%20şifre%20talep%20ediyorum.%0D%0A%0D%0AAdım%20Soyadım:%20"
            mail_link = f"mailto:matematikegitiminevu@gmail.com?subject={mail_konu}&body={mail_icerik}"
             
            # Şifre Al butonu
            st.link_button("📩 Şifre İste", mail_link, use_container_width=True)
        
        with c3:
             if st.button("⬅ Ana Menüye Dön", use_container_width=True):
                ana_menuye_don()

# --- 3. AŞAMA: DERS NOTLARI VE PDF ARŞİVİ ---
elif st.session_state["sayfa"] == "notlar_arsivi":
    # 🌟 BURADAN: (BAKIM MODU KONTROLÜ)
    if ARSIV_BAKIM_MODU and not gizli_yonetici_izni:
        with st.sidebar:
            if st.button("⬅ Ana Menüye Dön / Çıkış"):
                st.session_state["aktif_user"] = None
                ana_menuye_don()
                
        sayaç_arsiv_html = kalan_sure_html_hazirla(HEDEF_ZAMAN_ARSIV)
        tam_sayfa_arsiv_html = f"""
        <div style="text-align: center; background-color: #1e293b; padding: 40px; border-radius: 16px; border: 1px solid #334155; box-shadow: 0 10px 25px rgba(0,0,0,0.5); font-family: sans-serif; margin-top: 30px;">
            <h2 style="color: white !important; margin-bottom: 15px;">🚧 Ders Notları Arşivi Bakımda</h2>
            <p style="font-size: 1.1rem; margin-top: 15px; color: #cbd5e1 !important; text-align: center;">
                Ders notları, PDF dokümanları ve haftalık programlar optimize edilmektedir. Arşivimiz kısa süre sonra erişime açılacaktır.
            </p>
            {sayaç_arsiv_html}
            <div style="margin-top: 30px; border-top: 1px solid #334155; padding-top: 15px; text-align: center;">
                <p style="color: #FF4B4B !important; font-weight: bold; font-size: 1.1rem; margin-bottom: 5px;">Muharrem CEYHAN</p>
                <p style="color: #64748b !important; font-size: 0.85rem; letter-spacing: 1px;">CYHN MATEMATİK GELİŞTİRME PLATFORMU</p>
            </div>
        </div>
        """
        st.components.v1.html(tam_sayfa_arsiv_html, height=450, scrolling=False)
        st.stop()
        
    with st.spinner("Matematik Portalı Hazırlanıyor..."):
        import time
        time.sleep(1)
    # Sidebar (Yan Menü)
    with st.sidebar:
            st.title(f"♾️ Hoş Geldin, {st.session_state['aktif_user'].capitalize()}!")
            st.markdown("💡 *Bir sorun mu var? Aşağıdaki kanallardan bize hızlıca ulaşabilir veya yapay zeka asistanımıza danışabilirsin.*")
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
                text-decoration: none !important;
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
                text-decoration: none !important;
                color: #ffffff !important;
            }
            .ai-button {
                text-decoration: none !important;
            }
            .ai-button:hover {
                text-decoration: none !important;
            }
                /* WhatsApp için marka rengi gradyanı */
            .wp-button {
                text-decoration: none !important;
            }
            .wp-button:hover {
                text-decoration: none !important;
            }
            </style>
            
            <!-- İletişim Butonu -->
            <a href="mailto:matematikegitiminevu@gmail.com" class="sidebar-custom-button">
                📩 İletişim Maili
            </a>
            <a href="https://wa.me/905061905437?text=Merhaba,%20CYHN%20Matematik%20Portalı%20üzerinden%20ulaşıyorum.%20Bir%20konu%20hakkında%20bilgi%20almak%20istiyorum.%0D%0AKonu:%20" target="_blank" class="sidebar-custom-button wp-button">
                📞 WhatsApp İletişim
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
    > **Hoş geldin {kullanici}!** Bu arşiv, akademik yolculuğunda sana rehberlik etmek için özenle hazırlanmıştır. 
    > Aşağıdaki sekmeleri kullanarak ders notlarına erişebilir, çalışmalarını derinleştirebilirsin. 
    > Bir sorun olduğunda yan menüde bulunan iletişim kanallarından bana ulaşabilirsin. **Başarılar.**
       """)
    # --------------------------
    st.markdown("---")


    # Konulara göre sekmeler (Tablar)
    tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📢 Güncel Duyurular",
        "💻 Algoritma ve Programlama",
        "🔢 Lineer Cebir PDF Notları", 
        "🎲 Analiz PDF Notları", 
        "📐 Soyut Matematik PDF Notları",
        "📖 Türk Dili 2 Videoları"
    ])

    with tab0:
        st.subheader("Güncel Duyurular Bölümü")
        st.warning("❗Bu kısımda Matematik Eğitimi Anabilimdalının güncel bilgileri paylaşılmaktadır.")
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.container(border=True):
                st.markdown("**NEVÜ MAFET**")
                st.link_button("🌐 MAFET Resmî Web Sitesi", "https://mafet.nevsehir.edu.tr/", use_container_width=True)
        with col2:
            with st.container(border=True):
                st.markdown("**Ders Programı**")
                st.link_button("📅 Haftalık Ders Programı (PDF)", "https://dosyalar.nevsehir.edu.tr/6667946ceeefe0f7a69e00d88e9e25d7/matematik-egitimi-2025-2026-bahar-donemi-haftalik-program_final-hali-4.pdf", use_container_width=True)
        with col3:
            with st.container(border=True):
                st.markdown("**Sınav Takvimi**")
                st.link_button("📝 Dönem İçi Sınav Takvimi (PDF)", "https://dosyalar.nevsehir.edu.tr/27b9857ff2d7c3247d597c4ca999de35/matematik-egitimi-2025-2026-bahar-donemi-final-programi.pdf", use_container_width=True)

    with tab1:
        st.subheader("Algoritma ve Programlama Ders Notu")
        st.warning("❗Algoritma dersinde kullanılmış olan notlar aşağıdadır.")
        
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        
        with col1:
            with st.container(border=True):
                st.markdown("**Algoritmaya Giriş**")
                if st.button("👁️ Notu Aç", key="alg1", use_container_width=True):
                    pdf_popup_ac("1Dz9nJXinGmgUajJH4Ljov7sSpMQv89Pn")
                    
        with col2:
            with st.container(border=True):
                st.markdown("**Python 1.kısım**")
                if st.button("👁️ Notu Aç", key="alg2", use_container_width=True):
                    pdf_popup_ac("1eQdLmcqXiTYdhQ-n53IJbj6DFgrlvpl5")
                    
        with col3:
            with st.container(border=True):
                st.markdown("**Python 2.kısım**")
                if st.button("👁️ Notu Aç", key="alg3", use_container_width=True):
                    pdf_popup_ac("1WUxVwNK4uvNj8k23yeZtfWEVyOwMQH9o")
                    
        with col4:
            with st.container(border=True):
                st.markdown("**Dosya İşlemleri**")
                if st.button("👁️ Notu Aç", key="alg4", use_container_width=True):
                    pdf_popup_ac("1JLnAzmiXzytjKCUzUheIFzhPcj8gODml")
                    
        with col5:
            with st.container(border=True):
                st.markdown("**Python Notları Toplu**")
                if st.button("👁️ Notu Aç", key="alg5", use_container_width=True):
                    pdf_popup_ac("1pv5oPwe81IOMzNBb12q-GaQVL-VEnD7y")
                    
        with col6:
            with st.container(border=True):
                st.markdown("**💻 Özel Notlar (M.C.)**")
                if st.button("👁️ Notu Aç", key="alg6", use_container_width=True):
                    pdf_popup_ac("1OUdyrIEHGOgsj-ltJBPb4u6KxPuWLjNF")
    with tab2:
        st.subheader("Lineer Cebir Ders Notları")
        st.warning("❗Website bakımı nedeniyle bu bölümdeki dosyalar güncellenmektedir. Lineer Cebir 1 PDF dosyası henüz yüklenmemiştir!")
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("**Lineer Cebir 1**")
                st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln1")
        with col2:
            with st.container(border=True):
                st.markdown("**Lineer Cebir 2**")
                if st.button("👁️ Notu Aç", key="lin2", use_container_width=True):
                    pdf_popup_ac("1yk5VmfUbipnQR8IK6gWVHW9LMibP-zVR")
    with tab3:
        st.subheader("Analiz 1 ve 2 Ders Notları")
        st.warning("❗Website bakımı nedeniyle bu bölümdeki dosyalar güncellenmektedir. Analiz 1 PDF dosyası henüz yüklenmemiştir!")
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("**Analiz 1**")
                st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln2")
        with col2:
            with st.container(border=True):
                st.markdown("**Analiz 2**")
                if st.button("👁️ Notu Aç", key="anlz2", use_container_width=True):
                    pdf_popup_ac("1_v-11l519_-I8VD759O0-0Vwo6oasGHB")
    with tab4:
        st.subheader("Soyut Matematik Ders Notu")
        st.warning("❗Soyut matematik dersinde kullanılmış olan notlar aşağıdadır.")
        if st.button("👁️ Notu Aç", key="soyut1", use_container_width=True):
            pdf_popup_ac("1AFXcBbNphoZDs41NjH-ofDbkePWk3emL")
            
    with tab5:
        st.subheader("Türk Dili 2 Videoları")
        st.warning("❗Türk Dili 2 dersine ait UBYS sisteminde de yüklü olan videolara aşağıdaki bağlantıdan tıklayarak ulaşabilirsiniz.")
        st.link_button("Videoları Görüntüle", "https://bulut.nevsehir.edu.tr/index.php/s/eMP56Ty6dfeCdFc", use_container_width=True)
    

    # Alt Bilgi
    st.markdown("---")
    st.caption("🚀 CYHN Matematik Geliştirme Platformu © 2026")
