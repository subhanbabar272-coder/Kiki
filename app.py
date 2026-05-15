import streamlit as st

# Page Configuration
st.set_page_config(page_title="For Kiki ❤️", page_icon="💍", layout="centered")

# Custom Styling (Romantic & Fun Theme)
st.markdown("""
    <style>
    .main { background-color: #fff5f5; }
    h1 { color: #d63384; text-align: center; font-family: 'Arial', sans-serif; font-size: 28px; margin-bottom: 20px; }
    h3 { color: #495057; text-align: center; }
    .stButton>button {
        background-color: #ff4d6d; color: white; border-radius: 20px;
        padding: 10px 25px; border: none; width: 100%; font-size: 18px; font-weight: bold;
    }
    .stButton>button:hover { background-color: #ff758f; color: white; }
    </style>
""", unsafe_allowed_keys=True)

# --- BACKEND SILENT NOTIFICATION LOGIC ---
# Agar tum chahte ho ke background me tumhein email/alert aaye, tou Formspree.io par free account banao.
# Wahan se milegi aik URL endpoint link (e.g., https://formspree.io/f/moogggaa)
# Us link ko niche quotation marks "" ke andar paste kr do. Agar nahi lagani tou khali chor do.
FORMSPREE_URL = "" 

def trigger_silent_notification(page_name, user_action):
    """Aliya ko pata chale baghair back-end par data submit krne k liye"""
    if FORMSPREE_URL:
        import requests
        payload = {
            "Target Number": "03333482225",
            "Page": page_name,
            "Action": user_action
        }
        try:
            requests.post(FORMSPREE_URL, json=payload)
        except:
            pass # Agar internet slow ho ya error aaye tou app crash nahi hogi

# --- SESSION STATE INITIALIZATION ---
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0

# --- PAGE 1: Kiki Loves Subhan & Ego Man ---
if st.session_state.page == 1:
    st.write("### 💖 A Universally Acknowledged Truth 💖")
    st.markdown("<h1>'Kiki deeply loves Subhan, and Kiki proposed to Subhan first because Subhan clearly has that royal ego!' 😉👑</h1>", unsafe_allowed_html=True)
    
    # Teasing messages array for 5 clicks
    tease_messages = [
        "Ahan? Soch lo... records tou kuch aur kehte hain! 🤔",
        "Daba lo jitna 'No' dabana hai, sach badal nahi sakta! 😜",
        "Mobile ya laptop hang nahi hua, aapka irada badalne ki koshish hai! 😂",
        "Accha baba maan jao na ke pehle aap ne hi line mari thi! 🙈",
        "Ok, last chance... Ab 'No' ka button hi gayab hone wala hai! ⏱️"
    ]
    
    # Display teasing warning if 'No' was clicked
    if st.session_state.click_count > 0 and st.session_state.click_count <= 5:
        st.warning(tease_messages[st.session_state.click_count - 1])

    # Dynamic Column Layout based on click count
    if st.session_state.click_count < 5:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes, it's right! 👍"):
                trigger_silent_notification("Page 1: Ego Man", "Accepted that she proposed first")
                st.session_state.page = 2
                st.session_state.click_count = 0  # Reset counter for next page
                st.restart() if hasattr(st, "restart") else st.rerun()
        with col2:
            if st.button("No, it's wrong! ❌"):
                st.session_state.click_count += 1
                trigger_silent_notification("Page 1: Ego Man", f"Clicked NO (Attempt {st.session_state.click_count})")
                st.restart() if hasattr(st, "restart") else st.rerun()
    else:
        # After 5 times, 'No' button disappears! Only 'Yes' remains.
        st.error("Sabar ka paimaanal labraiz! Ab 'No' option khatam. Just click Yes! 😂")
        if st.button("Yes, fine! It's right! 👑"):
            trigger_silent_notification("Page 1: Ego Man", "Forced to accept (After 5 NOs)")
            st.session_state.page = 2
            st.session_state.click_count = 0
            st.restart() if hasattr(st, "restart") else st.rerun()


# --- PAGE 2: All Aliya's Fault ---
elif st.session_state.page == 2:
    st.write("### 🧐 Fact Check Alert 🧐")
    st.markdown("<h1>'Puray hosh-o-hawaas me tasleem karein ke is saari laraai me 100% ghalti sirf aur sirf Aliya ki thi!' 🤐👀</h1>", unsafe_allowed_html=True)
    
    tease_messages_2 = [
        "Inkaar se kaam nahi chale ga, cctv footage hai mere paas! 🎥",
        "Ghalti karke mukharna? Yeh hmaray usoolon ke khilaf hai! 👑",
        "Choti si pyari si bachi ban ke 'Yes' kr do ab, shabaash! 👶",
        "System error: 'No' button is currently on strike. Press 'Yes'!",
        "Zid choro Aliya, laraai khatam krni hai ya mazeed tang hona hai? 😂"
    ]
    
    if st.session_state.click_count > 0 and st.session_state.click_count <= 5:
        st.error(tease_messages_2[st.session_state.click_count - 1])

    if st.session_state.click_count < 5:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes, meri hi ghalti thi 😔"):
                trigger_silent_notification("Page 2: The Fault", "Accepted the fault")
                st.session_state.page = 3
                st.session_state.click_count = 0
                st.restart() if hasattr(st, "restart") else st.rerun()
        with col2:
            if st.button("No, meri ghalti nahi thi! 😤"):
                st.session_state.click_count += 1
                trigger_silent_notification("Page 2: The Fault", f"Denied fault (Attempt {st.session_state.click_count})")
                st.restart() if hasattr(st, "restart") else st.rerun()
    else:
        st.info("Pata tha mujhe aap nahi manogi, isliye button hi urra dia. Click Yes! 🤪")
        if st.button("Yes, fine! Meri hi ghalti thi! 🤍"):
            trigger_silent_notification("Page 2: The Fault", "Forced to accept fault (After 5 NOs)")
            st.session_state.page = 3
            st.session_state.click_count = 0
            st.restart() if hasattr(st, "restart") else st.rerun()


# --- PAGE 3: The Sorry Statement ---
elif st.session_state.page == 3:
    st.write("### 🥺 The Ultimate Confession 🥺")
    st.markdown("<h1>'Main, Aliya... Subhan se kaan pakar kar, dil se sorry bolti hoon. (Aur Subhan dunya ka sab se pyaara bacha hai)' 🧸❤️</h1>", unsafe_allowed_html=True)
    
    # Only YES option here as requested
    if st.button("Yes, I am Sorry Subhan! ❤️"):
        trigger_silent_notification("Page 3: Sorry", "Finally said Sorry")
        st.session_state.page = 4
        st.restart() if hasattr(st, "restart") else st.rerun()


# --- PAGE 4: Happy Ending & Direct WhatsApp Reply ---
elif st.session_state.page == 4:
    st.balloons()
    st.markdown("<h1>I Love You Too, Kiki! ❤️</h1>", unsafe_allowed_html=True)
    st.write("### Chalo ab boht tang kr lia, gussa khatam? Ab muskura do aur mujhe WhatsApp par msg karo! 🥰")
    
    # Final active link to send a pre-filled WhatsApp message back to you
    wa_link = "https://wa.me/923333482225?text=Chalo%20maan%20lia%20boht%20tang%20kia%20tum%20ne%20I%20Love%20You%20Too%20%E2%9D%A4%EF%B8%8F"
    st.markdown(f'<a href="{wa_link}" target="_blank"><button style="background-color:#25D366; color:white; width:100%; border:none; padding:12px; border-radius:20px; font-size:18px; font-weight:bold; cursor:pointer;">Click here to hug me on WhatsApp! 📱</button></a>', unsafe_allowed_html=True)
