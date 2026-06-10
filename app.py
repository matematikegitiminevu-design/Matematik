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
# 🔒 2. AŞAMA: ŞİFRE KONTROL EKRANI (KESİN ÇÖZÜM - SIFIR HATA + BİREBİR TASARIM)
# =========================================================================
elif st.session_state["sayfa"] == "sifre_kontrol":
    
    # 🔮 1. ADIM: Streamlit Alanını Temizleyen ve Çakışmaları Önleyen İzole CSS
    st.markdown(
        """
        <style>
            /* Streamlit varsayılan üst bar, sidebar ve alt bilgileri tamamen kapat */
            [data-testid="stSidebar"], [data-testid="stSidebarCollapseButton"], 
            [data-testid="stHeader"], footer {
                display: none !important;
            }
            
            /* Sayfa container sınırlarını sıfırla */
            .main .block-container {
                max-width: 100% !important;
                padding: 0px !important;
            }
            
            /* ARKA PLAN: Görseldeki pembe-mor dokulu kozmik nebula atmosferi */
            .stApp {
                background: linear-gradient(135deg, #2b0833 0%, #630b4f 40%, #1a083a 80%, #0b051c 100%) !important;
                background-size: cover !important;
                background-attachment: fixed !important;
                min-height: 100vh !important;
                display: flex !important;
                align-items: center !important;
                justify-content: center !important;
            }

            /* Streamlit'in görünmez container arka planlarını şeffaflaştır */
            [data-testid="element-container"], [data-testid="stVerticalBlock"], 
            [data-testid="stVerticalBlockBorderWrapper"] {
                background-color: transparent !important;
                box-shadow: none !important;
                border: none !important;
            }
            
            /* Hata mesajı paneli tasarımı */
            .cyhn-error-box {
                background-color: rgba(220, 38, 38, 0.25);
                color: #fca5a5;
                border: 1px solid rgba(220, 38, 38, 0.4);
                border-radius: 12px;
                width: 380px;
                padding: 12px;
                margin: 15px auto 0 auto;
                text-align: center;
                font-size: 0.85rem;
                font-family: sans-serif;
            }
        </style>
        """, 
        unsafe_allow_html=True
    )

    # Arka planda hata yönetimi için değişken kontrolü
    hata_mesaji = ""

    # 🔮 2. ADIM: Form Girdilerini İşleyen Güvenli Python Motoru
    params = st.query_params
    
    # Ana menüye dönüş kontrolü
    if "back_to_menu" in params:
        st.session_state["sayfa"] = "ana_menu"
        st.query_params.clear()
        st.rerun()
        
    # Giriş yap kontrolü
    if "form_submitted" in params:
        html_user = params.get("html_username", "").strip().lower()
        html_pass = params.get("html_password", "")
        
        # Kullanıcı Adı ve Şifre Doğrulama
        if html_user in USERS and USERS[html_user] == html_pass:
            st.toast("🔑 Giriş Başarılı!", icon="🎉")
            st.balloons()
            st.session_state["aktif_user"] = html_user
            st.session_state["sayfa"] = "notlar_arsivi"
            st.query_params.clear()
            st.rerun()
        else:
            hata_mesaji = "Kullanıcı adı veya şifre hatalı. Lütfen tekrar deneyin!"

    # 🔮 3. ADIM: image_72785e.png Görselindeki Arayüzün Birebir HTML Yapısı
    st.markdown(
        """
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; width: 100vw; min-height: 100vh; font-family: 'Inter', system-ui, -apple-system, sans-serif; box-sizing: border-box;">
            
            <div style="
                background: rgba(30, 24, 38, 0.65);
                backdrop-filter: blur(30px) saturate(180%);
                -webkit-backdrop-filter: blur(30px) saturate(180%);
                width: 380px;
                padding: 40px 30px 50px 30px;
                border-radius: 28px;
                border: 1px solid rgba(255, 255, 255, 0.08);
                box-shadow: 0 30px 70px rgba(0, 0, 0, 0.7);
                box-sizing: border-box;
                position: relative;
            ">
                
                <h2 style="color: #ffffff; text-align: center; margin: 0 0 6px 0; font-size: 1.6rem; font-weight: 600; letter-spacing: -0.5px; background: none; -webkit-text-fill-color: initial;">Welcome back!</h2>
                <p style="color: rgba(255, 255, 255, 0.5); text-align: center; margin: 0 0 30px 0; font-size: 0.88rem;">Let's get you signed up.</p>
                
                <form method="get" action="/" style="display: flex; flex-direction: column;">
                    <input type="hidden" name="form_submitted" value="true">
                    
                    <div style="display: flex; gap: 12px; margin-bottom: 14px;">
                        <input type="text" name="html_firstname" placeholder="First Name" required style="
                            width: 50%;
                            background: rgba(255, 255, 255, 0.03);
                            border: 1px solid rgba(255, 255, 255, 0.15);
                            border-radius: 12px;
                            padding: 12px 14px;
                            color: #ffffff;
                            font-size: 0.9rem;
                            outline: none;
                            box-sizing: border-box;
                        ">
                        <input type="text" name="html_lastname" placeholder="Last Name" required style="
                            width: 50%;
                            background: rgba(255, 255, 255, 0.03);
                            border: 1px solid rgba(255, 255, 255, 0.15);
                            border-radius: 12px;
                            padding: 12px 14px;
                            color: #ffffff;
                            font-size: 0.9rem;
                            outline: none;
                            box-sizing: border-box;
                        ">
                    </div>
                    
                    <input type="text" name="html_username" placeholder="Kullanıcı Adı" required style="
                        background: rgba(255, 255, 255, 0.03);
                        border: 1px solid rgba(255, 255, 255, 0.15);
                        border-radius: 12px;
                        padding: 13px 14px;
                        color: #ffffff;
                        font-size: 0.9rem;
                        margin-bottom: 14px;
                        outline: none;
                        width: 100%;
                        box-sizing: border-box;
                    ">
                    
                    <div style="position: relative; margin-bottom: 14px; width: 100%; box-sizing: border-box;">
                        <input type="password" name="html_password" placeholder="Password" required style="
                            width: 100%;
                            background: rgba(255, 255, 255, 0.03);
                            border: 1px solid rgba(255, 255, 255, 0.15);
                            border-radius: 12px;
                            padding: 13px 14px;
                            color: #ffffff;
                            font-size: 0.9rem;
                            outline: none;
                            box-sizing: border-box;
                        ">
                        <span style="position: absolute; right: 15px; top: 50%; transform: translateY(-50%); color: rgba(255,255,255,0.3); font-size: 0.9rem; cursor: pointer;">👁</span>
                    </div>
                    
                    <select style="
                        background: rgba(30, 24, 38, 0.95);
                        border: 1px solid rgba(255, 255, 255, 0.15);
                        border-radius: 12px;
                        padding: 13px 14px;
                        color: rgba(255, 255, 255, 0.7);
                        font-size: 0.9rem;
                        margin-bottom: 20px;
                        outline: none;
                        cursor: pointer;
                        width: 100%;
                        box-sizing: border-box;
                    ">
                        <option>Turkey (CYHN Portal)</option>
                        <option>United States</option>
                    </select>
                    
                    <div style="display: flex; align-items: flex-start; gap: 10px; margin-bottom: 25px; padding: 0 4px;">
                        <input type="checkbox" id="legal_agree" name="html_agree" value="yes" required style="margin-top: 2px; accent-color: #ec4899; cursor: pointer; width: 15px; height: 15px;">
                        <label for="legal_agree" style="color: rgba(255,255,255,0.5); font-size: 0.72rem; line-height: 1.4; cursor: pointer; user-select: none;">
                            Telif haklarını kabul ediyorum, dökümanları izinsiz paylaşmayacağım. <a href="#" style="color: #38bdf8; text-decoration: none;">Sözleşme Detayları</a>
                        </label>
                    </div>
                    
                    <button type="submit" style="
                        background: linear-gradient(90deg, #7c3aed 0%, #e11d48 100%);
                        color: #ffffff;
                        border: none;
                        border-radius: 12px;
                        padding: 14px 0;
                        font-size: 1rem;
                        font-weight: 600;
                        cursor: pointer;
                        transition: opacity 0.2s;
                        width: 100%;
                        box-sizing: border-box;
                    " onmouseover="this.style.opacity='0.9';" onmouseout="this.style.opacity='1';">
                        Sign Up / Giriş Yap
                    </button>
                </form>
                
                <div style="
                    position: absolute;
                    bottom: -22px;
                    left: 50%;
                    transform: translateX(-50%);
                    display: flex;
                    gap: 14px;
                    z-index: 999;
                ">
                    <a href="#" style="width: 44px; height: 44px; background: #14121e; border: 1px solid rgba(255,255,255,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 20px rgba(0,0,0,0.5); text-decoration: none;">
                        <img src="https://img.icons8.com/ios-filled/50/ffffff/mac-os.png" width="18"/>
                    </a>
                    <a href="mailto:matematikegitiminevu@gmail.com" style="width: 44px; height: 44px; background: #14121e; border: 1px solid rgba(255,255,255,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 20px rgba(0,0,0,0.5); text-decoration: none;">
                        <img src="https://img.icons8.com/color/48/000000/google-logo.png" width="18"/>
                    </a>
                    <a href="#" style="width: 44px; height: 44px; background: #14121e; border: 1px solid rgba(255,255,255,0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 20px rgba(0,0,0,0.5); text-decoration: none;">
                        <img src="https://img.icons8.com/ios-filled/50/1877f2/facebook-new.png" width="20"/>
                    </a>
                </div>
                
            </div>

            <form method="get" action="/" style="margin-top: 50px;">
                <input type="hidden" name="back_to_menu" value="true">
                <button type="submit" style="
                    background: transparent;
                    color: rgba(255, 255, 255, 0.4);
                    border: none;
                    cursor: pointer;
                    font-size: 0.9rem;
                    transition: color 0.2s;
                " onmouseover="this.style.color='#ffffff';" onmouseout="this.style.color='rgba(255, 255, 255, 0.4)';">
                    育 Portal Ana Menüsüne Dön
                </button>
            </form>

        </div>
        """, 
        unsafe_allow_html=True
    )

    # 🔮 4. ADIM: Hata Oluştuysa Kartın Altında Güvenli Biçimde Göster
    if hata_mesaji:
        st.markdown(f'<div class="cyhn-error-box">⚠️ {hata_mesaji}</div>', unsafe_allow_html=True)
            
            
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
