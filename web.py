# app.py
import streamlit as st

st.set_page_config(page_title="Welcome", layout="centered")

# ---- CSS styling to mimic your mobile mockup ----
st.markdown(
    """
    <style>
    /* center narrow "phone" frame */
    .phone {
        width: 360px;
        margin: 30px auto;
        border-radius: 28px;
        box-shadow: 0 8px 30px rgba(0,0,0,0.7);
        border: 6px solid #0b0b0b;
        background: white;
        overflow: hidden;
        font-family: "Helvetica", Arial, sans-serif;
    }
    /* top camera notch + header */
    .topbar {
        background: #dcdcdc;
        padding: 16px 10px;
        text-align: center;
        font-weight: 800;
        font-size: 20px;
    }
    .content {
        padding: 18px 20px 30px 20px;
    }
    .logo-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 8px;
    }
    .logo {
        font-size: 26px;
        font-weight: 700;
        font-style: italic;
    }
    .icons { font-size: 22px; opacity: 0.9; }

    /* pill toggle */
    .pill {
        display:flex;
        border: 3px solid #000;
        border-radius: 40px;
        overflow: hidden;
        width: 280px;
        margin: 18px auto;
        box-sizing: border-box;
    }
    .pill button {
        flex:1;
        padding: 10px 0;
        border: none;
        background: #fff;
        cursor: pointer;
        font-weight: 600;
    }
    .pill .active {
        background: #dcdcdc;
    }

    /* rounded input box area */
    .form-round {
        background: #e6e6e6;
        border-radius: 40px;
        padding: 18px;
        border: 3px solid #000;
        margin-bottom: 18px;
    }
    .field-label { font-weight: 800; margin-bottom: 8px; }
    .input-box {
        border: 3px solid #000;
        padding: 12px;
        border-radius: 4px;
        background: #fff;
    }

    /* black login button */
    .login-btn {
        background: #0b0b0b;
        color: #fff;
        text-align: center;
        padding: 12px;
        border-radius: 6px;
        font-size: 22px;
        margin: 8px 0 4px 0;
        font-weight: 600;
    }
    .or-text { text-align:center; margin:6px 0; font-size:18px; }
    .google-btn {
        border: 3px solid #000;
        padding: 10px;
        border-radius: 6px;
        font-size: 20px;
        text-align:center;
        font-weight:600;
        background: #fff;
    }

    /* small mobile top camera circle just for look */
    .camera {
        width:14px;height:14px;border-radius:50%;background:#111;
        position: relative; left:50%; transform: translateX(-50%); top:6px;
    }

    /* streamlit special adjustments */
    .stButton>button { padding: 0.6rem 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---- phone container ----
st.markdown('<div class="phone">', unsafe_allow_html=True)

# top camera + header
st.markdown('<div class="camera"></div>', unsafe_allow_html=True)
st.markdown('<div class="topbar">WELCOME!!</div>', unsafe_allow_html=True)

# content area
st.markdown('<div class="content">', unsafe_allow_html=True)

# logo row with home icon and burger icon
st.markdown(
    """
    <div class="logo-row">
      <div class="icons">🏠</div>
      <div class="logo">Logo</div>
      <div class="icons">☰</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# pill toggle: sign in / sign up
# We'll use a radio for logic and render the pill look with HTML/CSS
mode = st.radio("", ("sign in", "sign up"), index=0, horizontal=True)
# Render pill HTML to match the selected state
pill_html = f"""
<div class="pill">
  <button class="{ 'active' if mode=='sign in' else ''}">sign in</button>
  <button class="{ 'active' if mode=='sign up' else ''}">sign up</button>
</div>
"""
st.markdown(pill_html, unsafe_allow_html=True)

# form container (rounded)
st.markdown('<div class="form-round">', unsafe_allow_html=True)

st.markdown('<div class="field-label">Email</div>', unsafe_allow_html=True)
email = st.text_input("", placeholder="email address or user name", key="email")
# simulate the boxed look under the label with markdown wrapper
st.markdown('<div style="height:8px"></div>', unsafe_allow_html=True)

st.markdown('<div class="field-label">Password</div>', unsafe_allow_html=True)
password = st.text_input("", placeholder="enter your password", type="password", key="password")

st.markdown('</div>', unsafe_allow_html=True)  # close form-round

# Login button area
if st.button("Login"):
    st.success(f"Attempting to {mode} with {email or 'no email entered'}")
    # Replace above with real auth logic as needed

st.markdown('<div class="or-text">or</div>', unsafe_allow_html=True)

# Continue with Google (non-functional placeholder)
if st.button("continue with google"):
    st.info("Google sign-in clicked (placeholder)")

st.markdown('</div>', unsafe_allow_html=True)  # close content
st.markdown('</div>', unsafe_allow_html=True)  # close phone