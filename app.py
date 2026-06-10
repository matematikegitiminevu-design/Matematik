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

HEDEF_ZAMAN_GENEL = "2026-06-09 00:00:00"
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
    
    # 🔮 1. ADIM: Sayfa Genişliğini Sıfırlayan ve Arka Planı Ayarlayan CSS
    st.markdown(
        """
        <style>
            /* Streamlit üst bar, sidebar ve alt bilgileri gizle */
            [data-testid="stSidebar"], [data-testid="stSidebarCollapseButton"], 
            [data-testid="stHeader"], footer {
                display: none !important;
            }
            
            /* Sayfa container'ını serbest bırak ve dikey/yatay ortala */
            .main .block-container {
                max-width: 100% !important;
                padding: 0 !important;
                display: flex !important;
                justify-content: center !important;
                align-items: center !important;
                min-height: 100vh !important;
            }

            /* Derin Kozmik Nebula Arka Planı */
            .stApp {
                background: linear-gradient(135deg, #050714 0%, #12092e 35%, #380b3c 70%, #52043d 100%) !important;
                background-size: cover !important;
                background-attachment: fixed !important;
            }

            /* Streamlit elemanlarının arka plan çakışmalarını sıfırla */
            [data-testid="element-container"], [data-testid="stVerticalBlock"],
            [data-testid="stVerticalBlockBorderWrapper"] {
                background: transparent !important;
                background-color: transparent !important;
                box-shadow: none !important;
                border: none !important;
            }
            
            /* BUTON: Pembe-Kırmızı Geçişli Akıcı Tasarım */
            div.stButton > button:first-child {
                background: linear-gradient(90deg, #a855f7 0%, #ec4899 50%, #f43f5e 100%) !important;
                border: none !important;
                border-radius: 12px !important;
                color: white !important;
                font-weight: 600 !important;
                padding: 12px 0 !important;
                box-shadow: 0 10px 20px -5px rgba(236, 72, 153, 0.4) !important;
                transition: all 0.3s ease !important;
            }
            div.stButton > button:first-child:hover {
                transform: translateY(-1px) !important;
                filter: brightness(1.1) !important;
            }

            /* Form Elemanları Şıklaştırma */
            .stTextInput input {
                background-color: rgba(255, 255, 255, 0.05) !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                border-radius: 12px !important;
                color: white !important;
            }
            .stTextInput label p {
                color: rgba(255, 255, 255, 0.7) !important;
                font-size: 0.85rem !important;
            }
            .stExpander {
                background: rgba(0, 0, 0, 0.2) !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                border-radius: 12px !important;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # 🔮 2. ADIM: Görseldeki Birebir Sabit Dikdörtgen Kutu Kılıfı (HTML Başlangıcı)
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; width: 100%; padding: 20px; box-sizing: border-box;">
            <div style="
                background: rgba(22, 18, 38, 0.45) !important;
                backdrop-filter: blur(40px) saturate(210%) !important;
                -webkit-backdrop-filter: blur(40px) saturate(210%) !important;
                border-radius: 24px !important;
                border: 1px solid rgba(255, 255, 255, 0.1) !important;
                padding: 40px 35px !important;
                width: 420px !important;
                max-width: 420px !important;
                box-shadow: 0 40px 100px -10px rgba(0, 0, 0, 0.9) !important;
                box-sizing: border-box !important;
            ">
        """, 
        unsafe_allow_html=True
    )

    # --- KUTUNUN İÇİNDEKİ STREAMLIT ELEMANLARI ---
    
    # Merkez Logo
    st.image("mc250.png", width=90)
    
    # Başlıklar
    st.markdown("<h2 style='text-align: center; color: white; margin-top: 10px; font-weight: 700;'>Welcome back!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: rgba(255,255,255,0.45); font-size: 0.9rem; margin-top: -10px; margin-bottom: 25px;'>Let's get you signed up.</p>", unsafe_allow_html=True)
    
    # Giriş Kutuları
    kullanici_adi = st.text_input("Kullanıcı Adı", placeholder="Kullanıcı adınız...")
    sifre = st.text_input("Parola", type="password", placeholder="••••••••")
    
    st.write("") 
    
    # Yasal Şartlar Paneli
    with st.expander("🔒 Telif Hakkı ve Sözleşme"):
        st.caption("Bu portalda sunulan tüm materyallerin telif hakları Muharrem CEYHAN'a aittir. İzinsiz paylaşılması veya çoğaltılması yasaktır.")
        onay = st.checkbox("Onaylıyorum", key="onay_check")
    
    st.write("")

    # Giriş ve Şifre İsteme Butonları
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("Giriş Yap", use_container_width=True):
            if not onay:
                st.error("Şartları onaylayın!")
            elif kullanici_adi in USERS and USERS[kullanici_adi] == sifre:
                st.session_state["aktif_user"] = kullanici_adi
                st.session_state["sayfa"] = "notlar_arsivi"
                st.rerun()
            else:
                st.error("Hatalı giriş!")
                
    with col_btn2:
        st.link_button("📩 Şifre İste", "mailto:matematikegitiminevu@gmail.com", use_container_width=True)
        
    # Alt Kısımdaki Yatay 3 Logo / Sosyal İkon Alanı
    st.markdown(
        """
                <div style="display: flex; justify-content: center; gap: 18px; margin-top: 30px; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 25px;">
                    <a href="#" style="width: 40px; height: 40px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; text-decoration: none; font-size: 1.1rem; transition: 0.2s;">🍏</a>
                    <a href="#" style="width: 40px; height: 40px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; text-decoration: none; font-size: 1rem; font-weight: bold; transition: 0.2s;">G</a>
                    <a href="#" style="width: 40px; height: 40px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; text-decoration: none; font-size: 1.1rem; font-family: sans-serif; transition: 0.2s;">f</a>
                </div>
            </div>
        </div>
        """, 
        unsafe_allow_html=True
    )

    # Portal Ana Menüye Dönüş (Kutunun dışında, sayfanın en altında bağımsız durur)
    st.write("")
    _, center_col, _ = st.columns([0.3, 0.4, 0.3])
    with center_col:
        st.markdown(
            """
            <style>
                div[data-testid="stBlock"] button {
                    background: transparent !important;
                    color: rgba(255, 255, 255, 0.4) !important;
                    border: none !important;
                    box-shadow: none !important;
                }
                div[data-testid="stBlock"] button:hover { color: white !important; }
            </style>
            """, unsafe_allow_html=True
        )
        if st.button("⬅ Portal Ana Menüsüne Dön", key="back_btn"):
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
