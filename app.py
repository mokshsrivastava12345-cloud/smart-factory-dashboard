import streamlit as st
import pandas as pd
import random
from time import sleep

# Page config
st.set_page_config(page_title="Smart Factory Dashboard", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.metric-card {
    background-color: #1c1f26;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    color: white;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.3);
}
.section {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
}
h1, h2, h3 {
    color: #00d4ff;
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.title("⚙️ Control Panel")
view = st.sidebar.selectbox("Select View", ["Overview", "AI Insights"])
uploaded_file = st.sidebar.file_uploader("📂 Upload CSV", type=["csv"])

st.sidebar.markdown("---")
st.sidebar.write("👤 Moksh Dashboard")
st.sidebar.write("🟢 System Active")

# Load data
user_data = None
if uploaded_file is not None:
    user_data = pd.read_csv(uploaded_file)

# Placeholder
placeholder = st.empty()

while True:
    with placeholder.container():

        # ---------- HEADER ----------
        st.markdown("<h1>🏭 Smart AI Factory Dashboard</h1>", unsafe_allow_html=True)
        st.caption("Real-time Monitoring • Logistics • AI Insights")

        # ---------- KPI SECTION ----------
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("📊 Key Performance Indicators")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Production", f"{random.randint(100,150)} units/hr", "+5%")
        col2.metric("Efficiency", f"{random.randint(85,95)}%", "+2%")
        col3.metric("Downtime", f"{random.randint(5,15)} min", "-1 min")
        col4.metric("Energy", f"{random.randint(400,500)} kWh", "-3%")

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------- MACHINE HEALTH ----------
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("🏭 Machine Health")

        col1, col2, col3 = st.columns(3)

        h1 = random.randint(70, 100)
        h2 = random.randint(60, 95)
        h3 = random.randint(75, 98)

        col1.metric("Machine 1", f"{h1}%")
        col2.metric("Machine 2", f"{h2}%")
        col3.metric("Machine 3", f"{h3}%")

        # Alerts
        if h2 < 70:
            st.error("🚨 Machine 2 Critical Condition!")
        elif h1 < 75:
            st.warning("⚠️ Maintenance Required Soon")
        else:
            st.success("✅ All Machines Healthy")

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------- CHARTS ----------
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("📈 Production vs Energy Trends")

        data = pd.DataFrame({
            "Production": [random.randint(90,150) for _ in range(6)],
            "Energy": [random.randint(400,500) for _ in range(6)]
        })

        st.line_chart(data)
        st.markdown('</div>', unsafe_allow_html=True)

        # ---------- INVENTORY ----------
        st.markdown('<div class="section">', unsafe_allow_html=True)
        st.subheader("📦 Inventory")

        col1, col2 = st.columns(2)
        col1.metric("Raw Material", f"{random.randint(200,500)} units")
        col2.metric("Finished Goods", f"{random.randint(100,300)} units")

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------- AI INSIGHTS ----------
        if view == "AI Insights":
            st.markdown('<div class="section">', unsafe_allow_html=True)
            st.subheader("🤖 AI Logistics Insights")

            if user_data is not None:

                st.dataframe(user_data)

                if "stock_level" in user_data.columns:
                    low_stock = user_data[user_data["stock_level"] < 100]
                    if not low_stock.empty:
                        st.error(f"🚨 Low Stock in {len(low_stock)} records")

                if "truck_status" in user_data.columns:
                    stopped = user_data[user_data["truck_status"] == "Stopped"]
                    if not stopped.empty:
                        st.warning(f"⚠️ {len(stopped)} truck(s) stopped")

                if "speed_kmph" in user_data.columns:
                    avg_speed = user_data["speed_kmph"].mean()
                    st.info(f"🚚 Avg Speed: {avg_speed:.2f} km/h")

                if "stock_level" in user_data.columns:
                    st.line_chart(user_data["stock_level"])

            else:
                st.info("Upload CSV to activate AI insights")

            st.markdown('</div>', unsafe_allow_html=True)

        # ---------- FOOTER ----------
        st.markdown("---")
        st.success("🟢 System Fully Operational")
        st.caption("Smart Factory + AI + Logistics | Demo Project")

    sleep(5)
