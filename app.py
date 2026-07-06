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
BAKIM_MODU = False         # Tüm siteyi kapatmak için True yapın
ARSIV_BAKIM_MODU = True      # Sadece ders arşivini kapatmak için True yapın

HEDEF_ZAMAN_GENEL = "2026-06-24 22:00:00"
HEDEF_ZAMAN_ARSIV = "2026-06-17 00:00:00"

# 📢 POPUP DUYURU AYARI
DUYURU_POPUP_AKTIF = True  # Popup duyuruyu açmak için True, kapatmak için False yapın
# =========================================================================

# --- POPUP (DİYALOG) PENCERESİ FONKSİYONU ---
@st.dialog("📢 CYHN MATEMATİK PORTALI", width="large")
def duyuru_popup():
    st.markdown(
        """
        <p style="color: #cbd5e1; font-size: 1.1rem; font-weight: 600; line-height: 1.6; margin-bottom: 15px;">
        Hoş Geldiniz!
        </p>
        <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.6; text-align: justify;">
        Geleceğin matematik eğitimini, modern dijital araçlar ve yapay zekâ teknolojileriyle buluşturan yeni nesil akademik portala adım attınız. Ders notları arşivine erişmek ve akıllı destek sistemini deneyimlemek için hazırsınız. Sürdürülebilir bir başarı yolculuğu dilerim.
        </p>
        <div style="text-align: right; margin-top: 25px; color: #64748b; font-size: 0.85rem; font-style: italic;">
            Saygılarımla,<br>
            <b style="color: #cbd5e1; font-style: normal; font-size: 0.95rem;">Muharrem CEYHAN</b>
        </div>
        """, 
        unsafe_allow_html=True
    )
    st.markdown("---")
    # Kullanıcı bu butona basınca popup kapanır ve sayfayı yenileyerek içeriği açar
    if st.button("Anladım, Kapat", use_container_width=True):
        st.session_state["duyuru_gosterildi"] = True
        st.rerun()
# =========================================================================  

# --- 🤖 YAPAY ZEKÂ MODEL SEÇİM PENCERESİ ---
@st.dialog("🤖 YAPAY ZEKÂ MERKEZİ", width="middle")
def yapay_zeka_secim_popup():
    st.markdown(
        """
        <p style="color: #cbd5e1; font-size: 1.1rem; font-weight: 600; line-height: 1.6; margin-bottom: 15px; text-align: center;">
        Model Seçimi
        </p>
        <p style="color: #94a3b8; font-size: 0.95rem; line-height: 1.6; text-align: center; margin-bottom: 25px;">
        Platform üzerinde deneyimlemek istediğiniz yapay zekâ modelini seçerek sohbet ekranına geçiş yapabilirsiniz:
        </p>
        """, 
        unsafe_allow_html=True
    )
    
    # Butonları yan yana kusursuz hizalamak için iki eşit sütun
    col1, col2 = st.columns(2)
    
    with col1:
        st.link_button("🚀 cyhnAI Asistan", "https://agent.jotform.com/019c71e214af725e8ca84db422ebe7088bfc", use_container_width=True)
            
    with col2:
        st.link_button("🧠 Gemini Asistan", "https://gemini.google.com", use_container_width=True)
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
    <div style="text-align: center; background-color: #1e293b; padding: 25px 15px; border-radius: 16px; border: 1px solid #334155; box-shadow: 0 10px 25px rgba(0,0,0,0.5); font-family: sans-serif; margin-top: 30px;">
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
    st.components.v1.html(tam_sayfa_html, height=620, scrolling=False)
    st.stop()


#---SAYFA AYARLARI ---
st.set_page_config(
    page_title="CYHN | Matematik Portalı", 
    page_icon="mc.png", 
    layout="wide",
    initial_sidebar_state="collapsed" 
)

# ==========================================
# 🗺️ ÖZEL ÜST ŞERİT BAR TANIMLAMASI
# ==========================================
ust_bar_tasarim = (
    "<link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Mr+De+Haviland&family=Poppins:wght@300;400;500;600&display=swap'>"
    "<style>"
    "#MainMenu {visibility: hidden;}"
    "footer {visibility: hidden;}"
    "header {visibility: hidden;}"
    ".block-container {padding-top: 0rem !important; padding-bottom: 0rem !important;}"
    "@media (max-width: 768px) {"
    "    .custom-bar {flex-direction: column !important; gap: 2px !important; padding: 5px 10px !important;}"
    "    .custom-bar .ayrac {display: none !important;}"
    "    .custom-bar .unvan {margin-top: -5px !important;}"
    "}"
    "</style>"
    "<div class='custom-bar' style='background: linear-gradient(90deg, #111827 0%, #1f2937 100%) !important; padding: 10px 20px; border-radius: 0px 0px 12px 12px; margin-bottom: 25px; text-align: center; box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.4); border-bottom: 2px solid #3b82f6; display: flex; justify-content: center; align-items: center; gap: 15px;'>"
    "    <span style='color: #ffffff !important; font-family: \"Mr De Haviland\", cursive !important; font-size: 3.0rem !important; font-weight: normal !important; text-shadow: 0 0 10px rgba(59, 130, 246, 0.3), 1px 1px 2px rgba(0,0,0,0.8); line-height: 1; letter-spacing: 1px;'>Muharrem Ceyhan</span>"
    "    <span class='ayrac' style='color: #3b82f6 !important; font-size: 1.2rem !important; font-family: \"Poppins\", sans-serif !important; font-weight: bold;'>|</span>"
    "    <span class='unvan' style='color: #9ca3af !important; font-family: \"Poppins\", sans-serif !important; font-size: 0.72rem !important; font-weight: 600 !important; letter-spacing: 3px; text-transform: uppercase;'>Founder & Developer</span>"
    "</div>"
)

st.markdown("".join(ust_bar_tasarim), unsafe_allow_html=True)
# ==========================================


# --- SAYFA ARKA PLANI ---
st.markdown(
    """  
    <style> 
    /* 1. ÇOK BEĞENİLEN AKADEMİK DOKULU VE PREMIUM ARKA PLAN (Tam İstediğin Renk) */
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

    /* 2. OKUNABİLİRLİK AYARLARI */
    h1, h2, h3, h4, h5, h6, p, span, label, .stMarkdown {
        color: #f8fafc !important; /* Soft beyaz */
        text-shadow: none !important; /* Göz tırmalayan gölgeler kaldırıldı */
    }

    /* 3. SOL MENÜ (SIDEBAR) & ZARİF LOGO BOYUTLANDIRMA */
    [data-testid="stSidebar"] {
        background: rgba(11, 19, 43, 0.85) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Sidebardaki logoyu otomatik olarak küçülten ve ortalayan yeni kural */
    [data-testid="stSidebar"] [data-testid="stImage"] img {
        max-width: 65% !important; /* Logoyu sidebar genişliğinin %65'ine çeker */
        height: auto !important;
        margin: 0 auto !important;
        display: block !important;
        border-radius: 8px !important; /* Eğer logo köşeliyse hafif yumuşatır */
    }

    /* 4. SORUNSUZ ÇALIŞAN SADE VE ŞIK MAT CAM KARTLAR */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 14px !important; 
        padding: 22px !important;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    div[data-testid="stVerticalBlockBorderWrapper"]:hover {
        transform: translateY(-3px) !important;
        border-color: rgba(255, 255, 255, 0.2) !important; 
        background: rgba(255, 255, 255, 0.05) !important;
        box-shadow: 0 15px 30px -5px rgba(0, 0, 0, 0.4) !important;
    }

    /* 5. SEKMELER (TABS) - MAT VE DOĞAL GEÇİŞ */
    button[data-baseweb="tab"] {
        color: #94a3b8 !important;
        font-weight: 600 !important;
        background: transparent !important;
        padding: 10px 20px !important;
    }
    button[data-baseweb="tab"]:hover {
        color: #f1f5f9 !important;
    }
    button[data-baseweb="tab"][aria-selected="true"] {
        color: #f1f5f9 !important;
        border-bottom: 2px solid #3b82f6 !important; 
    }

    /* 6. HATA VERMEYEN NET VE GÖZ ALICI AKADEMİK MAVİ BUTONLAR */
    div.stButton > button:first-child, .stLinkButton a {
        background: #1e40af !important; /* Soluk siyah yerine net kurumsal koyu mavi */
        color: #f1f5f9 !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        text-transform: none !important; 
        font-size: 0.9rem !important;
        letter-spacing: 0px;
        padding: 10px 20px !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2) !important; 
        transition: all 0.2s ease !important;
    }
    div.stButton > button:first-child:hover, .stLinkButton a:hover {
        background: #2563eb !important; /* Üzerine gelindiğinde canlanan canlı mavi */
        border-color: #3b82f6 !important;
        transform: translateY(-1px) !important;
        color: white !important;
        box-shadow: 0 6px 15px rgba(37, 99, 235, 0.3) !important;
    }
    
    /* Pasif Butonlar */
    div.stButton > button:disabled {
        background: rgba(255, 255, 255, 0.02) !important;
        color: #475569 !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    /* 7. KULLANICI BANNER ALANI (Sadeleştirilmiş) */
    .dashboard-banner {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 24px;
        border-radius: 14px;
        margin-bottom: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)




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
        st.markdown(
            """
            <h1 style='margin-bottom: 0; padding-bottom: 0; font-size: 2.8rem; color: #FF4B4B; font-weight: bold;'>CYHN</h1>
            <h2 style='margin-top: 0; padding-top: 0; font-size: 2rem; font-weight: normal; color: white;'>Matematik Portalı</h2>
            """, 
            unsafe_allow_html=True
        )
        # --------------------------------------------------------------------
        # ESKİ METİN SİLİNDİ, YERİNE ŞIK SİSTEM BİLGİSİ VE YÖNLENDİRME GELDİ
        # --------------------------------------------------------------------
        st.markdown(
            """
            <div style="background-color: #111a2e; border: 1px solid #1e293b; border-radius: 8px; padding: 15px 20px; margin: 15px 0 20px 0; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
                <p style="margin: 0; font-size: 0.95rem; color: #cbd5e1; line-height: 1.5;">
                    ℹ️ <b>Platform Hakkında:</b> Bu platform, İlköğretim matematik eğitimini modern dijital araçlarla harmanlayan ve yapay zekâ teknolojilerini sınıfa taşıyan yeni nesil bir öğrenme ortamıdır.
                </p>
                <p style="margin: 12px 0 0 0; font-size: 0.95rem; color: white; font-weight: 500; text-align: center; border-top: 1px solid #1e293b; padding-top: 10px;">
                    👇 Lütfen devam etmek için aşağıdan bir işlem seçiniz:
                </p>
            </div>
            """, 
            unsafe_allow_html=True
        )
        # --------------------------------------------------------------------

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
                st.markdown("### ✨ Yapay Zekâ Desteği")
                st.write("Matematik sorularınıza, formüllere ve takıldığınız tüm konularda yapay zeka desteğimiz ile anında çözüm bulun.")
                st.write("") # Küçük bir boşluk
                
                # ESKİ st.link_button YERİNE MERKEZİ POPUP'I TETİKLEYEN NORMAL BUTON:
                if st.button("Yapay Zekayı Başlat", use_container_width=True, key="giris_oncesi_ai_btn"):
                    yapay_zeka_secim_popup()
       

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
                    Developed with 💙 by 🇹🇷 <span style='color: #FF4B4B; font-weight: bold;'>Muharrem CEYHAN</span>
                </p>
                """, 
                unsafe_allow_html=True
            )

        st.markdown("---")

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
        st.markdown('<p class="cyhn-subtitle">Ders Arşivi Erişim Paneli</p>', unsafe_allow_html=True)
        
        # 📜 Sözleşme
        with st.expander("🔐 Lisans ve Kullanım Sözleşmesi", expanded=False):
            st.markdown(
                """
                <p style="color: #ef4444 !important; font-weight: 600; margin-bottom: 4px; font-size: 0.8rem; text-transform: uppercase;">Telif Hakkı Bildirimi:</p>
                <p style="color: #94a3b8 !important; font-size: 0.78rem; line-height: 1.4; text-align: left;">
                Bu platformda paylaşılan tüm ders PDF notlarının telif hakları doğrudan <b>Muharrem CEYHAN</b>'a aittir. <br>
                Tüm hakları saklıdır. <br><br>
                İçeriklerin tamamının veya bir kısmının, yazarın yazılı izni olmaksızın kopyalanması, çoğaltılması, işlenmesi veya herhangi bir dijital/basılı mecrada paylaşılması <b>kesinlikle yasaktır</b>. <br><br>
                Sadece kişisel eğitim amaçlıdır..! <br>
                <span style="color: #94a3b8 !important; font-size: 0.75rem; display: block; margin-top: 6px;">(© 2026)</span>
                </p>
                """, 
                unsafe_allow_html=True
            )
            # 2. Onay Kutusu (Sözleşmenin hemen dışına, görünür yere aldık)
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        onay = st.checkbox("Lisans ve kullanım sözleşmesini okudum, kabul ediyorum.")
            
        st.markdown("<div style='height: 5px;'></div>", unsafe_allow_html=True)
        st.markdown('<span class="cyhn-label">👤 Kullanıcı Adı</span>', unsafe_allow_html=True)
        kullanici_adi = st.text_input("Kullanıcı Adı Giriş Paneli", label_visibility="collapsed", placeholder="Kullanıcı adınız...").strip().lower()
        
        st.markdown('<span class="cyhn-label">🔑 Parola</span>', unsafe_allow_html=True)
        sifre = st.text_input("Parola Giriş Paneli", type="password", label_visibility="collapsed", placeholder="••••••••")
        
        st.markdown("<div style='height: 25px;'></div>", unsafe_allow_html=True)
        
        btn_c1, btn_c2 = st.columns(2)
        with btn_c1:
            if st.button("Giriş Yap", use_container_width=True):
                if not onay:
                    st.error("Lütfen önce şartları onaylayınız!")
                elif kullanici_adi in USERS and USERS[kullanici_adi] == sifre:
                    st.toast(f"🔑 Giriş Başarılı! Hoş geldin {kullanici_adi.capitalize()}.", icon="🎉")
                    st.balloons()
                    time.sleep(1.2)
                    # --- POPUP TETİKLEYİCİ BAYRAĞI ---
                    # Kullanıcı yeni girdi, duyuru henüz gösterilmedi diyoruz
                    st.session_state["duyuru_gosterildi"] = False
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

    # ─── 📢 ADIM 3: POPUP KONTROLÜ (TAM OLARAK BURAYA GELİYOR) ───
    # Eğer kullanıcı giriş yaptıysa ve duyuruyu henüz görmediyse popup'ı aç
    if DUYURU_POPUP_AKTIF and "duyuru_gosterildi" in st.session_state and not st.session_state["duyuru_gosterildi"]:
        duyuru_popup()
        st.stop()  # Popup kapanana kadar sayfanın geri kalanını (bakım modu dahil) yüklemeyi durdurur
    # ───────────────────────────────────────────────────────────
    
    # 🌟 BURADAN: (BAKIM MODU KONTROLÜ)
    if ARSIV_BAKIM_MODU and not gizli_yonetici_izni:
                
        sayaç_arsiv_html = kalan_sure_html_hazirla(HEDEF_ZAMAN_ARSIV)
        tam_sayfa_arsiv_html = f"""
        <div style="text-align: center; background-color: #1e293b; padding: 25px 15px; border-radius: 16px; border: 1px solid #334155; box-shadow: 0 10px 25px rgba(0,0,0,0.5); font-family: sans-serif; margin-top: 30px;">
            <h2 style="color: white !important; margin-bottom: 15px;">🚧 Ders Notları Arşivi Bakımda</h2>
            <p style="font-size: 1.1rem; margin-top: 15px; color: #cbd5e1 !important; text-align: center;">
                Sizlere daha hızlı, güvenli ve performanslı bir deneyim sunabilmek amacıyla <b>CYHN Matematik Portalı</b> genel bir güncelleme çalışmasındadır. 
                Ders notları, PDF dokümanları ve haftalık programlar optimize edilmektedir. Arşivimiz aşağıda belirtilen süre zarfında erişime açılacaktır.
            </p>
            {sayaç_arsiv_html}
            <div style="margin-top: 30px; border-top: 1px solid #334155; padding-top: 15px; text-align: center;">
                <p style="color: #FF4B4B !important; font-weight: bold; font-size: 1.1rem; margin-bottom: 5px;">Muharrem CEYHAN</p>
                <p style="color: #64748b !important; font-size: 0.85rem; letter-spacing: 1px;">CYHN MATEMATİK GELİŞTİRME PLATFORMU</p>
            </div>
        </div>
        """
        st.components.v1.html(tam_sayfa_arsiv_html, height=620, scrolling=False)
        st.stop()
        
    with st.spinner("Matematik Portalı Hazırlanıyor..."):
        import time
        time.sleep(1)
    
    kullanici = st.session_state.get("aktif_user", "Kullanıcı").capitalize()
    
    
    st.title("📚 Matematik Ders Notları ve PDF Arşivi")
    st.markdown(f"**Hoş geldin {kullanici}!** Bu arşiv, akademik yolculuğunda sana rehberlik etmek için özenle hazırlanmıştır. Aşağıdaki sekmeleri kullanarak ders notlarına erişebilirsin. Bir sorun olduğunda aşağı menüde bulunan iletişim kanallarından bana ulaşabilirsin. **Başarılar.**")

    st.markdown("---")

    if st.query_params.get("aksiyon") == "cikis":
        st.session_state["aktif_user"] = None
        st.session_state["sayfa"] = "ana_menu"
        # Parametreyi URL'den temizliyoruz ki sonsuz döngüye girmesin
        st.query_params.clear()
        st.toast("Oturum kapatıldı.", icon="👋")
        time.sleep(1.2)
        st.rerun()


    
    # --- 📢 2. BÖLÜM (YENİ YERİ): CANLI BİLDİRİM VE DUYURU BANDI ---
    st.markdown(
        """
        <div style="
            background: rgba(16, 185, 129, 0.1);
            border-left: 4px solid #10b981;
            padding: 14px 20px;
            border-radius: 10px;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        ">
            <div style="display: flex; align-items: center; gap: 12px;">
                <span style="font-size: 1.3rem;">🚀</span>
                <span style="color: #ffffff !important; font-size: 0.92rem; font-weight: 500; letter-spacing: 0.3px; line-height: 1.5;">
                    <b>Hızlı Başlangıç Rehberi:</b> Akademik ders içeriklerine ilgili sekmelerden doğrudan erişebilir, platforma entegre yapay zekâ modüllerini anında deneyimleyebilirsiniz.
                                </span>
            </div>
            <span style="color: #10b981 !important; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; white-space: nowrap; margin-left: 15px;">BİLGİ</span>
        </div>
        """, 
        unsafe_allow_html=True
    )

    
    # --------------------------
    st.markdown("---")

    # --- 🧭 SEKMELERİN ÜSTÜNE BİRLEŞTİRİCİ BAŞLIK ---
    st.markdown(
    """
    <div style="
        background: rgba(30, 41, 59, 0.7) !important; 
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        padding: 18px 20px; 
        border-radius: 12px; 
        border: 1px solid rgba(255, 255, 255, 0.1); 
        border-left: 5px solid #3b82f6; /* Sol taraftaki şık mavi odak çizgisi */
        text-align: left; /* Metni sola hizalamak çizgiyle daha uyumlu durur */
        margin-bottom: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    ">
        <p style="margin: 0; color: #f1f5f9; font-size: 0.95rem; font-weight: 500; letter-spacing: 0.3px;">
            ℹ️ Ders notlarına, güncel duyurulara ve iletişim kanallarına aşağıdaki menüden ulaşabilirsiniz.
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)

    st.markdown("---")

    
    # Konulara göre sekmeler (Tablar)
    tab0, tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🛠️ Destek & İletişim Kanalları",
        "📢 Güncel Duyurular",
        "🔢 Lineer Cebir Notları", 
        "📈 Analiz Notları", 
        "🌌 Soyut Matematik",
        "📐 Analitik Geometri",
        "💻 Algoritma ve Programlama"
    ])


    with tab0:
        st.subheader("Destek ve İletişim Kanalları")
        destek_col1, destek_col2, destek_col3, destek_col4 = st.columns(4)
        
        with destek_col1:
            with st.container(border=True):
                st.markdown("**Yapay Zekâ Desteği**\n\nGelişmiş Asistan Seçenekleri")
                # Kendi fonksiyonun veya yönlendirmen varsa buton içine bağlayabilirsin
                if st.button("✨ Yapay Zekâya Sor", use_container_width=True, key="destek_ai_btn"):
                    yapay_zeka_secim_popup() # Önceki kodundaki fonksiyon
                    
        with destek_col2:
            with st.container(border=True):
                st.markdown("**WhatsApp İletişim**\n\nAnlık Geri Bildirim")
                # Telefon numaranı buraya entegre edebilirsin
                st.link_button("💬 Canlı Destek Al", "https://wa.me/90XXXXXXXXXX", use_container_width=True)
                
        with destek_col3:
            with st.container(border=True):
                st.markdown("**İletişim Maili**\n\nE-Posta İletişimi")
                mail_link_destek = "mailto:matematikegitiminevu@gmail.com?subject=Portal%20Destek"
                st.link_button("📩 E-Posta Gönder", mail_link_destek, use_container_width=True)
                
        with destek_col4:
            with st.container(border=True):
                st.markdown("**NEVÜ UBYS Ekranı**\n\nNEVÜ UBYS Öğrenci Girişi")
                st.link_button("🦅 UBYS'ye Bağlan", "https://ubys.nevsehir.edu.tr/", use_container_width=True)

    with tab1:
        st.subheader("Güncel Duyurular Bölümü")
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
                

    
    with tab2:
        st.subheader("Lineer Cebir PDF Ders Notları")
        
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.markdown("**Lineer Cebir 1**")
                st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln1")
        with col2:
            with st.container(border=True):
                st.markdown("**Lineer Cebir 2**")
                if st.button("📝 Ders Notunu Aç", key="lin2", type="primary", use_container_width=True):
                    pdf_popup_ac("1nXutG6Fz6JtYFGYDlwohTySE6LwTe4Tg")
                    
    with tab3:
        st.subheader("Analiz PDF Ders Notları")
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
                
    with tab4:
        st.subheader("Soyut Matematik PDF Ders Notu")
        if st.button("📝 Ders Notunu Aç", key="soyut1", use_container_width=True):
            pdf_popup_ac("1pyaZAD35q0kIpXduqdjxpz4ylaFd4B5z")

    with tab5:
        st.subheader("Analitik Geometri PDF Ders Notu")
        st.button("⏳ Henüz Yüklenmedi", disabled=True, use_container_width=True, key="ln5")
        
    with tab6:
        st.subheader("Algoritma ve Programlama PDF Ders Notları")
        st.info("💻 Python ve Algoritmaya Giriş dersi kaynak dökümanları.")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.container(border=True):
                st.markdown("**Algoritmaya Giriş**")
                st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/1H6KmPg5sH42uftgaH5d00RZ8Im3mMMWM/view?usp=sharing", use_container_width=True)
            with st.container(border=True):
                st.markdown("**Python 1. Kısım**")
                st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/1rkvLjPNmilgAbUXSQ-FJNIBu2qnFl-5H/view?usp=sharing", use_container_width=True)
        with col2:
            with st.container(border=True):
                st.markdown("**Python 2. Kısım**")
                st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/1XUhVb5QI3jjRy_UqTGlImGJVKTBxXMEG/view?usp=sharing", use_container_width=True)
            with st.container(border=True):
                st.markdown("**Dosya İşlemleri**")
                st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/11hcdjR33ezlsgeP_8wtdRuX-GQSD_aH1/view?usp=sharing", use_container_width=True)
        with col3:
            with st.container(border=True):
                st.markdown("**Python Notları Toplu**")
                st.link_button("PDF'i Görüntüle", "https://drive.google.com/file/d/1bqum31r_D92EwSldH0IRMMb7MtTqVOMq/view?usp=sharing", use_container_width=True)
            with st.container(border=True):
                st.markdown("**💻 Özel Notlar (M.C.)**")
                if st.button("📝 Ders Notunu Aç", key="alg6", use_container_width=True):
                    pdf_popup_ac("1NCqgJKWM0Xs2M1vp9xnUFYpTGioPhZ8v")
                    
    

    st.markdown("---")
    
   

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # --- 🎯 EN ALT KISIM: SAF HTML & CSS MİNİMAL ÇIKISH BUTONU ---
    # URL Parametresi Dinleyicisi (Arka planda çalışır, buton üretmez)
    if st.query_params.get("aksiyon") == "cikis":
        st.session_state["aktif_user"] = None
        st.session_state["sayfa"] = "ana_menu"
        st.query_params.clear()
        st.toast("Oturum kapatıldı.", icon="👋")
        time.sleep(0.5)
        st.rerun()

    # Ekranın tam ortasında kibar durması için 3 sütun açıyoruz, butonu ortaya koyuyoruz
    bos_sol, buton_orta, bos_sag = st.columns([1.5, 1, 1.5])
    with buton_orta:
        html_bottom_logout = """
        <style>
            .pure-logout-btn {
                background: transparent !important;
                background-color: transparent !important;
                color: #94a3b8 !important;
                border: 1px solid rgba(148, 163, 184, 0.25) !important;
                border-radius: 6px !important;
                font-size: 0.78rem !important;
                padding: 5px 12px !important;
                cursor: pointer;
                width: 100% !important;
                text-align: center;
                transition: all 0.2s ease-in-out !important;
                display: inline-block;
                text-decoration: none !important;
                box-sizing: border-box;
            }
            .pure-logout-btn:hover {
                color: #ef4444 !important;
                background-color: rgba(239, 68, 68, 0.08) !important;
                border-color: rgba(239, 68, 68, 0.4) !important;
            }
        </style>
        <a href="?aksiyon=cikis" target="_self" class="pure-logout-btn">
            🔐 Güvenli Çıkış
        </a>
        """
        st.markdown(html_bottom_logout, unsafe_allow_html=True)
        
    
    # Alt Bilgi
    st.markdown("---")
    st.caption("🚀 CYHN Matematik Geliştirme Platformu © 2026")
