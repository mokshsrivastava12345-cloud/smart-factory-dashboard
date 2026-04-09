import streamlit as st
import random
import pandas as pd
import numpy as np
from time import sleep

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="Smart Factory Dashboard", layout="wide")

# -------------------------
# Sidebar Controls
# -------------------------
st.sidebar.title("⚙️ Control Panel")
view = st.sidebar.selectbox("Select View", ["Overview", "Detailed"])
show_ai = st.sidebar.checkbox("Show AI Insights", value=True)

# File Upload using session_state
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None

uploaded_file = st.sidebar.file_uploader("📂 Upload CSV for AI Analysis", type=["csv"])
if uploaded_file:
    st.session_state.uploaded_file = uploaded_file

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
        # Generate Machine Health Randomly
        # -------------------------
        health1 = random.randint(70, 100)
        health2 = random.randint(60, 95)
        health3 = random.randint(75, 98)

        # -------------------------
        # Top Alert Banner
        # -------------------------
        alert_message = ""
        if health1 < 75:
            alert_message = "🚨 Machine 1 needs maintenance!"
        elif health2 < 70:
            alert_message = "🚨 Machine 2 overload detected!"
        elif health3 < 75:
            alert_message = "🚨 Machine 3 requires attention!"

        if alert_message:
            st.markdown(
                f"<div style='background-color:#ff4b4b; color:white; padding:15px; border-radius:5px; text-align:center; font-size:18px; font-weight:bold;'>{alert_message}</div>",
                unsafe_allow_html=True
            )

        # -------------------------
        # Title
        # -------------------------
        st.markdown("<h1 style='text-align:center; color:#1f77b4;'>🏭 Smart AI Factory Dashboard</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; font-size:16px;'>Real-time monitoring | AI Predictions | Industry 4.0</p>", unsafe_allow_html=True)
        st.markdown("---")

        # -------------------------
        # Tabs
        # -------------------------
        tab1, tab2, tab3 = st.tabs(["Overview", "Machine Health", "AI Insights"])

        # -------------------------
        # Tab 1: Overview
        # -------------------------
        with tab1:
            st.subheader("📊 Key Performance Indicators")
            col1, col2, col3, col4 = st.columns(4)

            prod = random.randint(100,150)
            eff = random.randint(85,95)
            downtime = random.randint(5,15)
            energy = random.randint(400,500)

            col1.metric("Production", f"{prod} units/hr", "+5%")
            col2.metric("Efficiency", f"{eff}%", "+2%")
            col3.metric("Downtime", f"{downtime} min", "-1 min")
            col4.metric("Energy Usage", f"{energy} kWh", "-3%")

            st.markdown("---")

            # Production & Energy Trends - Streamlit chart
            st.subheader("📈 Production & Energy Trends")
            data = pd.DataFrame({
                "Production": [random.randint(90,150) for _ in range(6)],
                "Energy": [random.randint(400,500) for _ in range(6)]
            })
            st.line_chart(data)

            st.markdown("---")

            # Inventory
            st.subheader("📦 Inventory Status")
            col1, col2 = st.columns(2)
            col1.metric("Raw Material", f"{random.randint(200,500)} units")
            col2.metric("Finished Goods", f"{random.randint(100,300)} units")

        # -------------------------
        # Tab 2: Machine Health
        # -------------------------
        with tab2:
            st.subheader("🏭 Machine Health Monitoring")
            col1, col2, col3 = st.columns(3)
            col1.metric("Machine 1", f"{health1}%", delta="Good" if health1>80 else "Check", delta_color="normal")
            col2.metric("Machine 2", f"{health2}%", delta="Good" if health2>70 else "Warning", delta_color="inverse")
            col3.metric("Machine 3", f"{health3}%", delta="Good" if health3>75 else "Check", delta_color="inverse")

            st.markdown("---")
            st.subheader("🤖 AI Decision Engine")
            if health2 < 70:
                st.error("🚨 Reduce load on Machine 2")
            elif health1 < 75:
                st.warning("⚠️ Schedule maintenance")
            else:
                st.success("✅ System operating optimally")

        # -------------------------
        # Tab 3: AI Insights
        # -------------------------
        with tab3:
            if show_ai:
                st.subheader("🤖 AI Insights from Uploaded Data")
                if user_data is not None:
                    if "Value" in user_data.columns:
                        st.line_chart(user_data["Value"])
                        next_val = user_data["Value"].mean()
                        st.info(f"📈 Predicted next Value: {next_val:.2f}")
                    else:
                        st.warning("⚠️ Uploaded CSV missing 'Value' column")
                else:
                    st.info("Upload a CSV in the sidebar to see AI insights")
            else:
                st.info("AI Insights disabled via sidebar toggle")

        # -------------------------
        # Footer
        # -------------------------
        st.markdown("---")
        st.success("✅ System Status: Fully Operational")
        st.caption("Smart Factory System | Hackathon Demo Project")

    sleep(5)
