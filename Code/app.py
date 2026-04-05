import streamlit as st

# Page config
st.set_page_config(page_title="Aishwarya Operations course", page_icon="🚀", layout="wide")

# Custom CSS for UI
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
    }
    .sub {
        text-align: center;
        font-size: 18px;
        color: green;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">🚀 Aishwarya Operations website</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">"Unlock Your Learning Journey"</div>', unsafe_allow_html=True)

st.divider()

# Form
with st.form("registration_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email")

    with col2:
        phone = st.text_input("Phone Number")
        role = st.selectbox("Your Role", ["Student", "Fresher", "Working Professional"])

    submitted = st.form_submit_button("Register Now 🚀")

# On Submit
if submitted:
    if name and email:
        st.success(f"🎉 Welcome {name}! You are now part of Aishwarya’s Operations Journey 🚀")

        st.balloons()

        st.markdown("## 🔓 You just unlocked exciting projects!")

        st.info("🔥 Congratulations! You now have access to real Sre projects and learning paths.")

        st.markdown("### 🚀 Recommended Learning Videos")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.video("https://youtu.be/7mB8RVbnpTo?si=CFF21hTqu40zV7vz")

        with col2:
            st.video("https://youtu.be/JKwSfa6Av9A?si=AyjEtXsEMaKUps3e")

        with col3:
            st.video("https://youtu.be/cToslh2KfV0?si=aN-0_rukyplyFQPm")

        st.markdown("### 💡 What’s Next?")
        st.write("""
        - Start with Linux basics  
        - Learn Docker & Kubernetes  
        - Practice real-time troubleshooting  
        - Build your own projects  
        """)

    else:
        st.error("⚠️ Please fill all required fields")