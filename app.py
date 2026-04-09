import streamlit as st
import random
import pandas as pd
from time import sleep

# Page config
st.set_page_config(page_title="Smart Factory Dashboard", layout="wide")

# ✅ Sidebar OUTSIDE loop (fixes error)
st.sidebar.title("⚙️ Control Panel")
view = st.sidebar.selectbox(
    "Select View",
    ["Overview", "Detailed"],
    key="view_select"
)

st.sidebar.markdown("---")
st.sidebar.write("👤 Dashboard Lead")
st.sidebar.write("📡 System: Active")

# Placeholder for live updates
placeholder = st.empty()

while True:
    with placeholder.container():

        # Title
        st.title("🏭 Smart AI Factory Dashboard")
        st.markdown("Real-time monitoring | AI Predictions | Industry 4.0")

        # KPI Section
        st.subheader("📊 Key Performance Indicators")
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Production", f"{random.randint(100,150)} units/hr", "+5%")
        col2.metric("Efficiency", f"{random.randint(85,95)}%", "+2%")
        col3.metric("Downtime", f"{random.randint(5,15)} min", "-1 min")
        col4.metric("Energy Usage", f"{random.randint(400,500)} kWh", "-3%")

        st.markdown("---")

        # Machine Health
        st.subheader("🏭 Machine Health Monitoring")
        col1, col2, col3 = st.columns(3)

        with col1:
            health1 = random.randint(70, 100)
            st.metric("Machine 1", f"{health1}%")

        with col2:
            health2 = random.randint(60, 95)
            st.metric("Machine 2", f"{health2}%")

        with col3:
            health3 = random.randint(75, 98)
            st.metric("Machine 3", f"{health3}%")

        st.markdown("---")

        # AI Decision Engine
        st.subheader("🤖 AI Decision Engine")

        if health2 < 70:
            st.error("🚨 AI Action: Reduce load on Machine 2")
        elif health1 < 75:
            st.warning("⚠️ AI Action: Schedule maintenance")
        else:
            st.success("✅ AI: System operating optimally")

        st.markdown("---")

        # Charts
        st.subheader("📊 Production & Energy Trends")

        data = pd.DataFrame({
            "Production": [random.randint(90,150) for _ in range(6)],
            "Energy": [random.randint(400,500) for _ in range(6)]
        })

        st.line_chart(data)

        st.markdown("---")

        # Inventory
        st.subheader("📦 Inventory Status")
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Raw Material", f"{random.randint(200,500)} units")

        with col2:
            st.metric("Finished Goods", f"{random.randint(100,300)} units")

        st.markdown("---")

        # Integration Flow
        st.subheader("🔄 System Integration Flow")
        st.info("Sensors → Data Collection → AI Model → Dashboard → Decision Making")

        st.markdown("---")

        # Footer
        st.success("✅ System Status: Fully Operational")
        st.caption("Smart Factory System | Hackathon Demo Project")

    sleep(5)