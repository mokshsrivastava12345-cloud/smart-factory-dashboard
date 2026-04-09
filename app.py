import streamlit as st
import random
import pandas as pd
from time import sleep

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="Smart Factory Dashboard", layout="wide")

# -------------------------
# Sidebar Controls
# -------------------------
st.sidebar.title("⚙️ Control Panel")
view = st.sidebar.selectbox(
    "Select View",
    ["Overview", "Detailed"],
    key="view_select"
)

# -------------------------
# File Upload using session_state
# -------------------------
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

uploaded_file = st.sidebar.file_uploader("📂 Upload CSV for AI Analysis", type=["csv"])
if uploaded_file is not None:
    st.session_state.uploaded_file = uploaded_file

# Load uploaded data
if st.session_state.uploaded_file:
    user_data = pd.read_csv(st.session_state.uploaded_file)
    st.sidebar.success("File uploaded successfully!")
else:
    user_data = None

st.sidebar.markdown("---")
st.sidebar.write("👤 Dashboard Lead")
st.sidebar.write("📡 System: Active")

# -------------------------
# Placeholder for live updates
# -------------------------
placeholder = st.empty()

while True:
    with placeholder.container():

        # -------------------------
        # Title & Intro
        # -------------------------
        st.title("🏭 Smart AI Factory Dashboard")
        st.markdown("Real-time monitoring | AI Predictions | Industry 4.0")

        # -------------------------
        # KPI Section
        # -------------------------
        st.subheader("📊 Key Performance Indicators")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Production", f"{random.randint(100,150)} units/hr", "+5%")
        col2.metric("Efficiency", f"{random.randint(85,95)}%", "+2%")
        col3.metric("Downtime", f"{random.randint(5,15)} min", "-1 min")
        col4.metric("Energy Usage", f"{random.randint(400,500)} kWh", "-3%")

        st.markdown("---")

        # -------------------------
        # Machine Health
        # -------------------------
        st.subheader("🏭 Machine Health Monitoring")
        col1, col2, col3 = st.columns(3)
        health1 = random.randint(70, 100)
        health2 = random.randint(60, 95)
        health3 = random.randint(75, 98)
        col1.metric("Machine 1", f"{health1}%")
        col2.metric("Machine 2", f"{health2}%")
        col3.metric("Machine 3", f"{health3}%")

        st.markdown("---")

        # -------------------------
        # AI Decision Engine
        # -------------------------
        st.subheader("🤖 AI Decision Engine")
        if health2 < 70:
            st.error("🚨 AI Action: Reduce load on Machine 2")
        elif health1 < 75:
            st.warning("⚠️ AI Action: Schedule maintenance")
        else:
            st.success("✅ AI: System operating optimally")

        st.markdown("---")

        # -------------------------
        # Production & Energy Charts
        # -------------------------
        st.subheader("📊 Production & Energy Trends")
        data = pd.DataFrame({
            "Production": [random.randint(90,150) for _ in range(6)],
            "Energy": [random.randint(400,500) for _ in range(6)]
        })
        st.line_chart(data)

        st.markdown("---")

        # -------------------------
        # Inventory Status
        # -------------------------
        st.subheader("📦 Inventory Status")
        col1, col2 = st.columns(2)
        col1.metric("Raw Material", f"{random.randint(200,500)} units")
        col2.metric("Finished Goods", f"{random.randint(100,300)} units")

        st.markdown("---")

        # -------------------------
        # System Integration Flow
        # -------------------------
        st.subheader("🔄 System Integration Flow")
        st.info("Sensors → Data Collection → AI Model → Dashboard → Decision Making")

        st.markdown("---")

        # -------------------------
        # AI Insights from Uploaded Data
        # -------------------------
        st.subheader("🤖 AI Insights from Uploaded Data")
        if user_data is not None:
            if "Value" in user_data.columns:
                next_val = user_data["Value"].mean()
                st.info(f"📈 Predicted next Value: {next_val:.2f}")
            else:
                st.warning("⚠️ Uploaded CSV missing 'Value' column")
        else:
            st.info("Upload a CSV in the sidebar to see AI insights")

        st.markdown("---")

        # -------------------------
        # Footer
        # -------------------------
        st.success("✅ System Status: Fully Operational")
        st.caption("Smart Factory System | Hackathon Demo Project")

    sleep(5)  # Refresh every 5 seconds
