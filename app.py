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

HEDEF_ZAMAN_GENEL = "2026-06-14 00:00:00"
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
    /* 1. AKADEMİK DOKULU VE PREMIUM ARKA PLAN */
    html, body, [data-testid="stAppViewContainer"], .stApp {
        background-color: #0b1426 !important;
        background-image: 
            radial-gradient(at 0% 0%, rgba(30, 58, 138, 0.3) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(15, 23, 42, 0.8) 0px, transparent 50%),
            radial-gradient(at 50% 0%, rgba(79, 70, 229, 0.15) 0px, transparent 40%),
            radial-gradient(rgba(255, 255, 255, 0.04) 1px, transparent 0) !important;
        background-size: 100% 100%, 100% 100%, 100% 100%, 24px 24px !important;
        background-attachment: fixed !important;
    }
    
    [data-testid="stHeader"], [data-testid="stMainSpaceBlockContainer"] {
        background: transparent !important;
    }

    /* 2. NET YAZI SİSTEMİ */
    h1, h2, h3, h4, h5, h6, p, span, label {
        color: #f8fafc !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif !important;
    }

    /* 3. KURUMSAL SOL MENÜ (SIDEBAR) */
    [data-testid="stSidebar"] {
        background: rgba(11, 20, 38, 0.8) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    }

    /* 4. SEÇKİN ÜNİVERSİTE HAVASI VEREN CAM KARTLAR */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(15, 23, 42, 0.45) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(255, 255, 255, 0.09) !important;
        border-radius: 16px !important;
        padding: 24px !important;
        box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5),
                    inset 0 1px 1px rgba(255, 255, 255, 0.05) !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-4px) !important;
        border-color: rgba(99, 102, 241, 0.4) !important;
        background: rgba(15, 23, 42, 0.55) !important;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.6),
                    0 0 20px rgba(99, 102, 241, 0.1) !important;
    }

    /* 5. SEKMELER (TABS) */
    button[data-baseweb="tab"] {
        color: #94a3b8 !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        padding: 12px 24px !important;
        transition: all 0.2s ease !important;
    }
    button[data-baseweb="tab"]:hover {
        color: #ffffff !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #6366f1 !important;
        border-bottom: 2px solid #6366f1 !important;
    }

    /* 6. DENGELİ AKADEMİK SAFİR BUTONLAR VE KORUNAN YAZILAR */
    div.stButton > button:first-child, .stLinkButton a {
        background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        padding: 10px 22px !important;
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.2) !important;
        transition: all 0.25s ease !important;
    }
    
    div.stButton > button:first-child p, 
    div.stButton > button:first-child span, 
    div.stButton > button:first-child div {
        color: #ffffff !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        display: block !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    
    div.stButton > button:first-child:hover, .stLinkButton a:hover {
        background: linear-gradient(135deg, #2563eb 0%, #60a5fa 100%) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 20px rgba(37, 99, 235, 0.35) !important;
    }

    /* BANNER ALANI */
    .dashboard-banner {
        background: linear-gradient(90deg, rgba(30, 58, 138, 0.25) 0%, rgba(15, 23, 42, 0.4) 100%);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-left: 4px solid #3b82f6;
        padding: 24px;
        border-radius: 12px;
        margin-bottom: 25px;
    }

    /* --- DOĞAL VE DOĞRU ÇÖZÜM: ÇEVİRİ MOTORUNU ENGELLEME VE METİN SIFIRLAMA --- */
    /* Sol üst kontrol butonunun konumunu bozmadan, eklentinin ürettiği metinlerin yüksekliğini ve görünürlüğünü sıfırlıyoruz */
    [data-testid="stSidebarCollapsedControl"] {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    /* İçerideki tüm metin katmanlarını ez ve gizle (Orijinal SVG ikon hariç) */
    [data-testid="stSidebarCollapsedControl"] span,
    [data-testid="stSidebarCollapsedControl"] div,
    font {
        font-size: 0px !important;
        line-height: 0 !important;
        color: transparent !important;
        text-indent: -999px !important;
        visibility: hidden !important;
        display: inline-block !important;
        height: 0px !important;
        width: 0px !important;
    }
    
    /* Lisans Sözleşmesi Akordeon Oku Ayarı */
    summary::marker {
        color: #3b82f6 !important;
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
# 🔒 2. AŞAMA: ŞİFRE KONTROL EKRANI (%100 MOBİL & MASAÜSTÜ ORTALI KESİN SÜRÜM)
# =========================================================================
elif st.session_state["sayfa"] == "sifre_kontrol":
    
    # 🎨 Geliştirilmiş UI/UX Tasarım CSS Yapısı
    st.markdown(
        """
        <style>
            /* 1. Yan Menüyü Giriş Ekranında Tamamen İzole Et */
            [data-testid="stSidebar"], [data-testid="stSidebarCollapseButton"] {
                display: none !important;
            }
            
            /* 2. Arka Plan: Akıcı Derin Galaksi Gradyanı */
            .stApp {
                background: linear-gradient(135deg, #020617 0%, #0f172a 30%, #1e1b4b 70%, #030712 100%) !important;
                background-size: cover !important;
                background-attachment: fixed !important;
            }

            /* 3. ULTRA MODERN CARD MOTORU: Sütunun bizzat kendisini cam karta dönüştürüyoruz */
            div[data-testid="column"]:nth-of-type(2) {
                background: rgba(15, 23, 42, 0.45) !important;
                backdrop-filter: blur(25px) saturate(160%) !important;
                -webkit-backdrop-filter: blur(25px) saturate(160%) !important;
                padding: 40px 35px !important;
                border-radius: 24px !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                box-shadow: 0 4px 30px rgba(0, 0, 0, 0.4),
                            0 30px 60px -15px rgba(0, 0, 0, 0.8),
                            inset 0 1px 1px rgba(255, 255, 255, 0.05) !important;
                animation: popupShow 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            }

            div[data-testid="column"]:nth-of-type(2) > div {
                background: transparent !important;
                box-shadow: none !important;
                border: none !important;
            }

            @keyframes popupShow {
                from { transform: translateY(15px); opacity: 0; }
                to { transform: translateY(0); opacity: 1; }
            }

            /* 🎯 GLOBAL RESMİ MERKEZLEME MOTORU */
            div[data-testid="stImage"] {
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
                margin: 0 auto !important;
                width: 100% !important;
                text-align: center !important;
            }
            
            div[data-testid="stImage"] img {
                width: 65px !important;
                height: 65px !important;
                max-width: 65px !important;
                max-height: 65px !important;
                border-radius: 50% !important;
                object-fit: cover !important;
                filter: drop-shadow(0 6px 14px rgba(99, 102, 241, 0.45)) !important;
                border: 1.5px solid rgba(255, 255, 255, 0.2) !important;
                display: block !important;
                margin: 0 auto !important; /* Tarayıcı tabanlı ortalama garantisi */
            }

            /* 📱 MOBİL İÇİN ÖZEL KİLİTLEME RESPONSIVE MOTORU */
            /* Sütunlar alt alta yığıldığında sola kaçışı engeller, merkeze zorlar */
            @media (max-width: 768px) {
                div[data-testid="column"] {
                    display: flex !important;
                    flex-direction: column !important;
                    align-items: center !important;
                    justify-content: center !important;
                }
                div[data-testid="stImage"] {
                    margin: 0 auto 15px auto !important;
                }
            }

            /* 4. Tipografi ve Başlıklar */
            .cyhn-title {
                color: #ffffff !important;
                font-family: 'Inter', sans-serif;
                font-weight: 900 !important;
                font-size: 1.5rem !important;
                letter-spacing: 0.5px;
                margin-top: 15px;
                margin-bottom: 2px;
                text-align: center;
                background: linear-gradient(135deg, #ffffff 30%, #94a3b8 100%);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
            }
            .cyhn-subtitle {
                color: #64748b !important;
                font-size: 0.8rem !important;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 1px;
                margin-bottom: 25px;
                text-align: center;
            }
            .cyhn-label {
                font-weight: 600 !important;
                color: #94a3b8 !important;
                text-align: left;
                margin-top: 12px;
                margin-bottom: 6px;
                font-size: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 0.5px;
                display: block;
            }

            /* 5. Sözleşme Kutusu (Expander) */
            .stExpander {
                background: rgba(2, 6, 23, 0.4) !important;
                border: 1px solid rgba(255, 255, 255, 0.05) !important;
                border-radius: 12px !important;
                text-align: left;
            }
            .stExpander summary span {
                color: #94a3b8 !important;
                font-weight: 500 !important;
                font-size: 0.8rem !important;
            }
            .stCheckbox label span p {
                color: #cbd5e1 !important;
                font-size: 0.8rem !important;
            }
            
            /* 6. Giriş Alanları (Inputs) */
            .stTextInput input {
                color: #ffffff !important;
                background-color: rgba(2, 6, 23, 0.6) !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                border-radius: 12px !important;
                padding: 10px 14px !important;
                font-size: 0.9rem !important;
            }
            .stTextInput input:focus {
                border-color: #4f46e5 !important;
                box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.25) !important;
            }

            /* 7. Standart Premium Buton Stilleri */
            div.stButton > button:first-child {
                background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%) !important;
                color: #ffffff !important;
                border: none !important;
                border-radius: 12px !important;
                font-weight: 600 !important;
                padding: 10px 0 !important;
                font-size: 0.9rem !important;
                box-shadow: 0 4px 15px rgba(79, 70, 229, 0.2) !important;
            }
            div.stButton > button:first-child:hover {
                background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%) !important;
                transform: translateY(-1px);
                box-shadow: 0 6px 20px rgba(79, 70, 229, 0.35) !important;
            }
            
            /* İkincil Buton Modeli (Şifre İste Butonu) */
            div[data-testid="column"] div[data-testid="column"]:nth-of-type(2) div.stButton > button:first-child,
            div[data-testid="column"] div[data-testid="column"]:nth-of-type(2) a {
                background: rgba(255, 255, 255, 0.03) !important;
                color: #e2e8f0 !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                box-shadow: none !important;
            }

            /* 8. KARTIN İÇİNDEKİ GENİŞ GERİ DÖN BUTONU */
            .back-container-fixed {
                margin-top: 15px;
                width: 100% !important;
            }
            .back-container-fixed button {
                background: linear-gradient(135deg, #4f46e5 0%, #4338ca 100%) !important;
                color: #ffffff !important;
                width: 100% !important;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Üst boşluk ayarı
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    
    # 🎛️ COLS MOTORU: Giriş alanını masaüstünde harika merkezleyen stabil 3'lü yapı
    sol_bosluk, orta_kart_alani, sag_bosluk = st.columns([1.1, 1.3, 1.1])
    
    with orta_kart_alani:
        
        # 🎯 KUSURSUZ COLS + RESPONSIVE GRID DÜZENİ
        sub_sol, sub_merkez, sub_sag = st.columns([1.6, 0.8, 1.6])
        with sub_merkez:
            st.image("mc250.png", use_container_width=True)
        
        # Başlıklar
        st.markdown('<p class="cyhn-title">CYHN MATEMATİK PORTALI</p>', unsafe_allow_html=True)
        st.markdown('<p class="cyhn-subtitle">Ders Notları Doğrulama Sistemi</p>', unsafe_allow_html=True)
        
        # 📜 Sözleşme
        with st.expander("🔐 Lisans ve Kullanım Sözleşmesi", expanded=False):
            st.markdown(
                """
                <p style="color: #ef4444 !important; font-weight: 600; margin-bottom: 4px; font-size: 0.8rem; text-transform: uppercase;">Telif Hakkı Bildirimi:</p>
                <p style="color: #94a3b8 !important; font-size: 0.78rem; line-height: 1.4; text-align: left;">
                Bu portalda sunulan tüm akademik PDF dokümanlarının mülkiyet ve telif hakları doğrudan <b>Muharrem CEYHAN</b>'a aittir.<br><br>
                İçeriklerin izinsiz paylaşılması veya kopyalanması yasal işleme tabidir.
                </p>
                """, 
                unsafe_allow_html=True
            )
            st.markdown("<div style='height: 5px;'></div>", unsafe_allow_html=True)
            onay = st.checkbox("Şartları kabul ediyorum.")
            
        st.markdown("<div style='height: 5px;'></div>", unsafe_allow_html=True)
        
        # Giriş Alanları
        st.markdown('<span class="cyhn-label">👤 Kullanıcı Adı</span>', unsafe_allow_html=True)
        kullanici_adi = st.text_input("Kullanıcı Adı Giriş Paneli", label_visibility="collapsed", placeholder="Kullanıcı adınız...").strip().lower()
        
        st.markdown('<span class="cyhn-label">🔑 Parola</span>', unsafe_allow_html=True)
        sifre = st.text_input("Parola Giriş Paneli", type="password", label_visibility="collapsed", placeholder="••••••••")
        
        st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
        
        # Butonlar Grid Düzeni (Giriş Yap & Şifre İste)
        btn_c1, btn_c2 = st.columns(2)
        with btn_c1:
            if st.button("Giriş Yap", use_container_width=True):
                if not onay:
                    st.error("Lütfen önce şartları onaylayınız!")
                elif kullanici_adi in USERS and USERS[kullanici_adi] == sifre:
                    st.toast(f"Giriş başarılı! Yönlendiriliyorsunuz...", icon="🚀")
                    st.balloons()
                    time.sleep(1.2)
                    st.session_state["aktif_user"] = kullanici_adi
                    st.session_state["sayfa"] = "notlar_arsivi"
                    st.rerun()
                else:
                    st.error("Hatalı kimlik bilgileri!")
                    
        with btn_c2:
            mail_konu = "CYHN%20Portal%20Eri%C5%9Fim%20Talebi"
            mail_icerik = "Merhaba,%0D%0ACYHN%20Matematik%20Portalı%20için%20erişim%20bilgileri%20talep%20ediyorum.%0D%0A%0D%0AAdım%20Soyadım:%20"
            mail_link = f"mailto:matematikegitiminevu@gmail.com?subject={mail_konu}&body={mail_icerik}"
            st.link_button("📩 Şifre İste", mail_link, use_container_width=True)

        st.markdown("<div style='height: 5px;'></div>", unsafe_allow_html=True)

        # ⬅️ ANA MENÜYE DÖNÜŞ BUTONU
        st.markdown('<div class="back-container-fixed">', unsafe_allow_html=True)
        if st.button("← Portal Ana Menüsüne Dön", use_container_width=True, key="back_to_main_final_secured"):
            st.session_state["sayfa"] = "ana_menu"
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
            
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
        st.markdown("💡 *Sanal kütüphane altyapısı ile ders içeriklerine güvenle erişebilirsin.*")
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)
        
        # Yenilenen Minimalist İletişim Kanalları
        st.link_button("📩 İletişim Maili", "mailto:matematikegitiminevu@gmail.com", use_container_width=True)
        
        wp_link = "https://wa.me/905061905437?text=Merhaba,%20CYHN%20Matematik%20Portalı%20üzerinden%20ulaşıyorum."
        st.link_button("📞 WhatsApp İletişim", wp_link, use_container_width=True)

        st.link_button("✨ cyhnAI'a Sor", "https://agent.jotform.com/019c71e214af725e8ca84db422ebe7088bfc", use_container_width=True)

        st.divider()
        if st.button("🔐 Güvenli Çıkış", type="secondary", use_container_width=True):
            st.session_state["aktif_user"] = None
            st.session_state["sayfa"] = "ana_menu"
            st.rerun()
            
    kullanici = st.session_state["aktif_user"].capitalize()
    
    st.markdown(
        f"""
        <div class="dashboard-banner">
            <h2 style='margin:0; padding:0; color:#fff; font-size:1.65rem; font-weight:800; letter-spacing:0.5px;'>
                📚 Akademik PDF Arşivi & Kontrol Paneli
            </h2>
            <p style='margin:8px 0 0 0; padding:0; color:#94a3b8; font-size:0.92rem; line-height:1.5;'>
                Hoş geldin, <b>{kullanici}</b>! Bu kütüphane, akademik yolculuğunda sana rehberlik etmek için özenle optimize edilmiştir. 
                İhtiyacın olan dokümanı ilgili sekmeden seçerek güvenle inceleyebilirsin. Başarılar dilerim.
            </p>
        </div>
        """, 
        unsafe_allow_html=True
    )
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
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        st.subheader("Lineer Cebir Ders Notları")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("### Lineer Cebir 1")
                st.caption("Dönem: Güz | Durum: Hazırlanıyor")
                st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln1")
        with col2:
            with st.container(border=True):
                st.markdown("### Lineer Cebir 2")
                st.caption("Dönem: Bahar | Durum: Aktif")
                if st.button("📝 Ders Notunu Aç", key="lin2", type="primary", use_container_width=True):
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
