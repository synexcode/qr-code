import streamlit as st
import qrcode
from io import BytesIO

# --- Configuration ---
st.set_page_config(page_title="Secure QR Generator", page_icon="🔐", layout="centered")

# ✅ Replace this with your actual Synexcode logo URL
LOGO_URL = "SynexCode.png"

# Custom CSS Styling
st.markdown("""
    <style>
        body {
            background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
        }
        .main {
            background: rgba(255, 255, 255, 0.8);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            max-width: 450px;
            margin: auto;
        }
        input, textarea {
            border-radius: 10px !important;
            border: 1px solid #0077b6 !important;
        }
        .stButton {
        display: flex;
        justify-content: center;
    }
    .stButton>button {
        background: linear-gradient(90deg, #0077b6, #00b4d8);
        color: white;
        border-radius: 10px;
            width: 100%;
        padding: 10px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- Authentication --- 
USERNAME = "admin@synexcode.com"
PASSWORD = "SynexCode@0811"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# ✅ Authentication Page
if not st.session_state["authenticated"]:
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.image(LOGO_URL, width=200)  # ✅ Logo Here
    st.title("🔐 Secure Access")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("❌ Invalid Credentials")
    st.markdown('</div>', unsafe_allow_html=True)

# ✅ Main App Page
else:
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.image(LOGO_URL, width=200)  # ✅ Logo Here
    st.markdown("<h2 style='text-align:center;color:#0077b6;'>✨ Stylish QR Generator</h2>", unsafe_allow_html=True)

    name = st.text_input("📝 Enter File Name")
    url = st.text_input("🔗 Enter URL")

    if st.button("Generate QR Code"):
        if url and name:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            img_buffer = BytesIO()
            img.save(img_buffer, format="PNG")
            img_buffer.seek(0)

            st.success(f"✅ QR Ready for {name}")
            st.image(img_buffer, caption="QR Preview", use_column_width=True)

            st.download_button("⬇ Download QR Code", img_buffer, f"{name}.png", mime="image/png")

        else:
            st.warning("⚠️ Please enter both fields")

    if st.button("Logout"):
        st.session_state["authenticated"] = False
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
