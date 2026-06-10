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
BAKIM_MODU = True          # Tüm siteyi kapatmak için True yapın
ARSIV_BAKIM_MODU = False     # Sadece ders arşivini kapatmak için True yapın

HEDEF_ZAMAN_GENEL = "2026-06-12 00:00:00"
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
    initial_sidebar_state="collapsed" 
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

# --- POPUP İÇİNDE GÜVENLİ PDF GÖSTERME MOTORU ---
@st.dialog("📄 CYHN Portal | Ders Notu Önizleme", width="large")
def pdf_popup_ac(drive_id):
    # Drive ID'sini alıp indirme/yazdırma araçlarını gizleyen 'preview' linkine dönüştürüyoruz
    embed_link = f"https://drive.google.com/file/d/{drive_id}/preview?hl=tr"
    
    kullanici = st.session_state.get("aktif_user", "Bilinmeyen Kullanıcı").upper()
    su_an = datetime.now().strftime("%d.%m.%Y")

    # 1. Filigranı Görüntüleme Alanından Çıkarıp Başlığın Altına "Alt Yazı" Olarak Ekliyoruz
    st.caption(f"🛡️ Telif Hakkı: MUHARREM CEYHAN | Bu döküman {kullanici} adına kişiselleştirilmiştir. • {su_an}")
    # 2. Görüntülenen alanın içindeki filigranı tamamen sildik, sadece kalkan ve PDF kaldı
    tam_html = f"""
    <div style="position: relative; width: 100%; height: 650px; overflow: hidden; border-radius: 8px; background-color: #1e1e1e;">
        
        <div style="
            position: absolute;
            top: 0;
            right: 0;
            width: 150px;
            height: 55px;
            background-color: rgba(0, 0, 0, 0);
            z-index: 99999;
            cursor: default;
        "></div>
        
        <iframe src="{embed_link}#toolbar=0&navpanes=0" 
                width="100%" 
                height="100%" 
                style="border: none;" 
                allow="autoplay">
        </iframe>
        
    </div>
    """

    # Hepsini tek seferde Streamlit bileşeni olarak ekrana basıyoruz
    st.components.v1.html(tam_html, height=660)
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

# =========================================================================
# 🔒 2. AŞAMA: ŞİFRE KONTROL EKRANI (TEMİZ VE SADE POPUP / MODAL KONSEPTİ)
# =========================================================================
elif st.session_state["sayfa"] == "sifre_kontrol":
    
    # 🎨 Geliştirilmiş Popup Efekti ve CSS
    st.markdown(
        """
        <style>
            /* 1. Sol menüyü (Sidebar) giriş ekranında tamamen gizle */
            [data-testid="stSidebar"], [data-testid="stSidebarCollapseButton"] {
                display: none !important;
            }
            
            /* 2. Arka Plan: Derin ve modern akıcı kuantum gradyanı */
            .stApp {
                background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 40%, #2e1065 70%, #064e3b 100%) !important;
                background-size: cover !important;
                background-attachment: fixed !important;
            }
            
            /* Streamlit'in kendi katman gölgelerini tamamen nötrle */
            [data-testid="element-container"], 
            [data-testid="stVerticalBlockBorderWrapper"], 
            [data-testid="stVerticalBlock"] {
                background-color: transparent !important;
                box-shadow: none !important;
                border: none !important;
            }

            /* 3. POPUP KART: Ekranda Yüzen Pencere (Modal) Efekti */
            .cyhn-popup-card {
                background: rgba(23, 23, 37, 0.6) !important; /* Popup içi tok ve odaklı bir koyulukta */
                backdrop-filter: blur(20px) saturate(140%) !important;
                -webkit-backdrop-filter: blur(20px) saturate(140%) !important;
                max-width: 440px;
                margin: 70px auto !important; /* Yukarıdan dengeli popup boşluğu */
                padding: 40px 35px !important;
                border-radius: 20px !important; /* Yumuşak popup oval köşeleri */
                border: 1px solid rgba(255, 255, 255, 0.12) !important;
                /* Güçlü popup gölgesi ile derinlik hissi */
                box-shadow: 0 30px 60px -15px rgba(0, 0, 0, 0.7), 0 0 50px rgba(129, 140, 248, 0.05) !important;
                text-align: center;
                animation: popupShow 0.4s ease-out; /* Açılışta hafif büyüme efekti */
            }

            /* Popup Açılış Animasyonu */
            @keyframes popupShow {
                from { transform: scale(0.96); opacity: 0; }
                to { transform: scale(1); opacity: 1; }
            }

            /* 4. Tipografi ve Kusursuz Okunurluk */
            .cyhn-title {
                color: #ffffff !important;
                font-family: 'Inter', 'Segoe UI', sans-serif;
                font-weight: 800 !important;
                font-size: 1.45rem !important;
                letter-spacing: 0.5px;
                margin-top: 15px;
                margin-bottom: 2px;
                background: linear-gradient(to right, #ffffff, #e2e8f0);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .cyhn-subtitle {
                color: #94a3b8 !important;
                font-size: 0.85rem !important;
                font-weight: 500;
                margin-bottom: 25px;
            }
            .cyhn-label {
                font-weight: 600 !important;
                color: #cbd5e1 !important;
                text-align: left;
                margin-top: 5px;
                margin-bottom: 8px;
                font-size: 0.85rem;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                display: block;
            }

            /* 5. Şartlar Kutusu (Expander) Yeniden Yorumlandı */
            .stExpander {
                background: rgba(15, 23, 42, 0.7) !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                border-radius: 10px !important;
                text-align: left;
            }
            .stExpander summary span {
                color: #ffffff !important;
                font-weight: 600 !important;
                font-size: 0.85rem !important;
            }
            .stExpander p {
                color: #cbd5e1 !important;
            }
            
            /* Checkbox metni */
            .stCheckbox label span p {
                color: #cbd5e1 !important;
                font-size: 0.85rem !important;
            }
            
            /* 6. Giriş Kutuları (Inputs) */
            .stTextInput input {
                color: #ffffff !important;
                background-color: rgba(15, 23, 42, 0.5) !important;
                border: 1px solid rgba(255, 255, 255, 0.15) !important;
                border-radius: 10px !important;
                padding: 11px 14px !important;
            }
            .stTextInput input:focus {
                border-color: #818cf8 !important;
                box-shadow: 0 0 0 2px rgba(129, 140, 248, 0.25) !important;
            }

            /* 7. Butonlar */
            div.stButton > button:first-child {
                background: linear-gradient(135deg, #4f46e5 0%, #3730a3 100%) !important;
                color: #ffffff !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                border-radius: 10px !important;
                font-weight: 600 !important;
                padding: 10px 0 !important;
                transition: all 0.3s ease !important;
                box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3) !important;
            }
            div.stButton > button:first-child:hover {
                background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
                transform: translateY(-1px);
                box-shadow: 0 6px 20px rgba(79, 70, 229, 0.4) !important;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Dengeli üst boşluk
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    # 🏛️ HTML ile Popup Kartı Başlatıyoruz
    st.markdown('<div class="cyhn-popup-card">', unsafe_allow_html=True)
    
    # Logo Tasarımı (Hafif parıltılı)
    st.markdown('<div style="display: flex; justify-content: center; filter: drop-shadow(0 0 15px rgba(255,255,255,0.1));">', unsafe_allow_html=True)
    st.image("mc250.png", width=95)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Başlıklar
    st.markdown('<p class="cyhn-title">CYHN MATEMATİK PORTALI</p>', unsafe_allow_html=True)
    st.markdown('<p class="cyhn-subtitle">Özel Ders Notları Arşivi Doğrulama</p>', unsafe_allow_html=True)
    
    # 📜 Yasal Uyarı ve Şartlar
    with st.expander("🔒 Telif Hakkı ve Kullanım Şartları", expanded=True):
        st.markdown(
            """
            <p style="color: #fca5a5 !important; font-weight: bold; margin-bottom: 6px; font-size: 0.85rem;">Yasal Uyarı:</p>
            <p style="color: #cbd5e1 !important; font-size: 0.82rem; line-height: 1.5; font-weight: normal !important; text-align: left;">
            Bu platformda paylaşılan tüm ders PDF notlarının telif hakları doğrudan <b>Muharrem CEYHAN</b>'a aittir. <br>
            Tüm hakları saklıdır. <br><br>
            İçeriklerin tamamının veya bir kısmının, yazarın yazılı izni olmaksızın kopyalanması, çoğaltılması, işlenmesi veya herhangi bir dijital/basılı mecrada paylaşılması <b>kesinlikle yasaktır</b>. <br><br>
            Sadece kişisel eğitim amaçlıdır..! <br>
            <span style="color: #94a3b8 !important; font-size: 0.75rem; display: block; margin-top: 6px;">(© 2026)</span>
            </p>
            """, 
            unsafe_allow_html=True
        )
        onay = st.checkbox("Okudum, şartları kabul ediyorum.")
        
    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    
    # 👤 Kullanıcı Adı Girişi
    st.markdown('<span class="cyhn-label">Kullanıcı Adı</span>', unsafe_allow_html=True)
    kullanici_adi = st.text_input("Kullanıcı Adı Giriş Paneli", label_visibility="collapsed", placeholder="Kullanıcı adınız...").strip().lower()
    
    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
    
    # 🔑 Parola Girişi
    st.markdown('<span class="cyhn-label">Parola</span>', unsafe_allow_html=True)
    sifre = st.text_input("Parola Giriş Paneli", type="password", label_visibility="collapsed", placeholder="Şifrenizi yazınız...")
    
    st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
    
    # 🖲️ Butonlar (Modern Grid Düzeni)
    btn_c1, btn_c2 = st.columns(2)
    with btn_c1:
        if st.button("Giriş Yap", use_container_width=True):
            if not onay:
                st.error("Lütfen önce şartları onaylayınız!")
            elif kullanici_adi in USERS and USERS[kullanici_adi] == sifre:
                st.toast(f"🔑 Giriş Başarılı! Hoş geldin {kullanici_adi.capitalize()}.", icon="🎉")
                st.balloons()
                import time
                time.sleep(1.5)
                st.session_state["aktif_user"] = kullanici_adi
                st.session_state["sayfa"] = "notlar_arsivi"
                st.rerun()
            else:
                st.error("Kullanıcı adı veya şifre hatalı!")
                
    with btn_c2:
        mail_konu = "CYHN%20Portal%20Eri%C5%9Fim%20Talebi"
        mail_icerik = "Merhaba,%0D%0ACYHN%20Matematik%20Portalı%20için%20kullanıcı%20adı%20ve%20şifre%20talep%20ediyorum.%0D%0A%0D%0AAdım%20Soyadım:%20"
        mail_link = f"mailto:matematikegitiminevu@gmail.com?subject={mail_konu}&body={mail_icerik}"
        st.link_button("📩 Şifre İste", mail_link, use_container_width=True)
    
    # Popup Kartı Kapatıyoruz
    st.markdown('</div>', unsafe_allow_html=True)

    # ⬅️ PORTAL ANA MENÜSÜNE DÖNÜŞ (Popup dışında kalan transparan buton)
    _, ana_btn_col, _ = st.columns([0.3, 0.4, 0.3])
    with ana_btn_col:
        if st.button("⬅ Portal Ana Menüsüne Dön", use_container_width=True):
            st.session_state["sayfa"] = "ana_menu"
            st.rerun()
            
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
                    st.session_state["sayfa"] = "ana_menu"
                    st.rerun()
            
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
        "🔢 Lineer Cebir PDF Notları", 
        "🎲 Analiz PDF Notları", 
        "📐 Soyut Matematik PDF Notları",
        "💻 Algoritma ve Programlama",
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
                st.markdown("**Bütünleme Sınav Takvimi**")
                st.link_button("📝 Bütünleme Sınav Takvimi (PDF)", "https://dosyalar.nevsehir.edu.tr/78816a5e3b323ca077fa388d5a7bbcdc/matematik-egitimi-2025-2026-bahar-donemi-butunleme-programi-1.pdf", use_container_width=True)
        with col3:
            with st.container(border=True):
                st.markdown("**Ders Programı**")
                st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln3")
        

    with tab1:
        st.subheader("Lineer Cebir Ders Notları")
        st.warning("❗Lineer Cebir 1 PDF dosyası henüz yüklenmemiştir!")
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("**Lineer Cebir 1**")
                st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln1")
        with col2:
            with st.container(border=True):
                st.markdown("**Lineer Cebir 2**")
                if st.button("📝 Ders Notunu Aç", key="lin2", use_container_width=True):
                    pdf_popup_ac("1nXutG6Fz6JtYFGYDlwohTySE6LwTe4Tg")
                    
    with tab2:
        st.subheader("Analiz Dersi Ders Notları")
        st.warning("❗Analiz 1 PDF dosyası henüz yüklenmemiştir!")
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.container(border=True):
                st.markdown("**Analiz 1**")
                st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln2")
        with col2:
            with st.container(border=True):
                st.markdown("**Analiz 2**")
                if st.button("📝 Ders Notunu Aç", key="anlz2", use_container_width=True):
                    pdf_popup_ac("1qnqJBPsZLYCtTIN1X-XCP6mEph7OHhAJ")
        with col3:
            with st.container(border=True):
                st.markdown("**Analiz 3**")
                st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln4")
                
    with tab3:
        st.subheader("Soyut Matematik Ders Notu")
        st.warning("❗Soyut matematik dersinde kullanılmış olan notlar aşağıdadır.")
        if st.button("📝 Ders Notunu Aç", key="soyut1", use_container_width=True):
            pdf_popup_ac("1pyaZAD35q0kIpXduqdjxpz4ylaFd4B5z")

    with tab4:
        st.subheader("Algoritma ve Programlama Ders Notu")
        st.warning("❗Algoritma dersinde kullanılmış olan notlar aşağıdadır.")
        
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        
        with col1:
            with st.container(border=True):
                st.markdown("**Algoritmaya Giriş**")
                st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/1H6KmPg5sH42uftgaH5d00RZ8Im3mMMWM/view?usp=sharing", use_container_width=True)
                    
        with col2:
            with st.container(border=True):
                st.markdown("**Python 1.kısım**")
                st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/1rkvLjPNmilgAbUXSQ-FJNIBu2qnFl-5H/view?usp=sharing", use_container_width=True)
                    
        with col3:
            with st.container(border=True):
                st.markdown("**Python 2.kısım**")
                st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/1XUhVb5QI3jjRy_UqTGlImGJVKTBxXMEG/view?usp=sharing", use_container_width=True)
                    
        with col4:
            with st.container(border=True):
                st.markdown("**Dosya İşlemleri**")
                st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/11hcdjR33ezlsgeP_8wtdRuX-GQSD_aH1/view?usp=sharing", use_container_width=True)
                    
        with col5:
            with st.container(border=True):
                st.markdown("**Python Notları Toplu**")
                st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/1bqum31r_D92EwSldH0IRMMb7MtTqVOMq/view?usp=sharing", use_container_width=True)
                    
        with col6:
            with st.container(border=True):
                st.markdown("**💻 Özel Notlar (M.C.)**")
                if st.button("📝 Ders Notunu Aç", key="alg6", use_container_width=True):
                    pdf_popup_ac("1NCqgJKWM0Xs2M1vp9xnUFYpTGioPhZ8v")
                    
    with tab5:
        st.subheader("Türk Dili 2 Videoları")
        st.warning("❗Türk Dili 2 dersine ait UBYS sisteminde de yüklü olan videolara aşağıdaki bağlantıdan tıklayarak ulaşabilirsiniz.")
        st.link_button("Videoları Görüntüle", "https://bulut.nevsehir.edu.tr/index.php/s/eMP56Ty6dfeCdFc", use_container_width=True)
    

    # Alt Bilgi
    st.markdown("---")
    st.caption("🚀 CYHN Matematik Geliştirme Platformu © 2026")
