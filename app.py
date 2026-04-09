import streamlit as st
import pandas as pd
import random
import time
from time import sleep

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Smart Factory Dashboard", layout="wide")

# ---------- SESSION STATE ----------
if "prev_data" not in st.session_state:
    st.session_state.prev_data = {"prod":120,"eff":90,"down":10,"energy":450}

if "upload_time" not in st.session_state:
    st.session_state.upload_time = None

# ---------- AI ----------
def predict_demand(stock):
    return "🚨 Low Stock Risk" if stock < 100 else "✅ Stock Safe"

def best_route():
    return "🗺️ Route: A → C → D"

def predict_delay(speed):
    return "🚨 High Delay" if speed < 10 else "✅ Low Delay"

# ---------- DELTA ----------
def get_delta(current, previous):
    if previous == 0:
        return "0%"
    return f"{((current-previous)/previous)*100:+.1f}%"

# ---------- UI ----------
st.markdown("""
<style>
.stApp { background-color: #0e1117; }
.header {
    padding: 20px;
    border-radius: 12px;
    background: linear-gradient(90deg, #00d4ff, #007cf0);
    color: white;
    text-align: center;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 12px;
    margin-top: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.title("⚙️ Control Panel")
view = st.sidebar.radio("Select Section", ["Overview", "AI Insights"])
uploaded_file = st.sidebar.file_uploader("📂 Upload CSV", type=["csv"])

st.sidebar.markdown("---")
st.sidebar.write("👤 Dashboard Lead")
st.sidebar.write("🟢 System Active")

# ---------- LOAD DATA ----------
user_data = None

if uploaded_file is not None:
    user_data = pd.read_csv(uploaded_file)

    # store upload time
    if st.session_state.upload_time is None:
        st.session_state.upload_time = time.time()

# ---------- MODE LOGIC ----------
use_csv = False

if st.session_state.upload_time is not None:
    elapsed = time.time() - st.session_state.upload_time

    if elapsed <= 10:
        use_csv = True
    else:
        use_csv = False
        st.session_state.upload_time = None  # reset

# ---------- MAIN LOOP ----------
placeholder = st.empty()

while True:
    with placeholder.container():

        # HEADER
        st.markdown("""
        <div class="header">
            <h1>🏭 Smart AI Factory Dashboard</h1>
            <p>Sense → THINK → Act</p>
        </div>
        """, unsafe_allow_html=True)

        # MODE INDICATOR
        if use_csv:
            st.info("📂 Real Data Mode (10 sec)")
        else:
            st.success("🔄 Simulation Mode")

        # ---------- KPI ----------
        st.markdown('<div class="card">', unsafe_allow_html=True)

        if use_csv and user_data is not None:
            prod = int(user_data["outflow"].mean())
            eff = int((user_data["inflow"].sum()/user_data["outflow"].sum())*100)
            down = int((user_data["truck_status"]=="Stopped").sum())
            energy = int(user_data["speed_kmph"].mean()*5)
        else:
            prod = random.randint(100,150)
            eff = random.randint(85,95)
            down = random.randint(5,15)
            energy = random.randint(400,500)

        prev = st.session_state.prev_data

        c1,c2,c3,c4 = st.columns(4)
        c1.metric("Production", prod, get_delta(prod, prev["prod"]))
        c2.metric("Efficiency", f"{eff}%", get_delta(eff, prev["eff"]))
        c3.metric("Downtime", down, get_delta(down, prev["down"]))
        c4.metric("Energy", energy, get_delta(energy, prev["energy"]))

        st.session_state.prev_data = {"prod":prod,"eff":eff,"down":down,"energy":energy}

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------- MACHINE ----------
        st.markdown('<div class="card">', unsafe_allow_html=True)

        if use_csv and user_data is not None:
            h1 = int(user_data["speed_kmph"].iloc[0]*2)
            h2 = int(user_data["speed_kmph"].iloc[1]*2)
            h3 = int(user_data["speed_kmph"].iloc[2]*2)
        else:
            h1 = random.randint(70,100)
            h2 = random.randint(60,95)
            h3 = random.randint(75,98)

        m1,m2,m3 = st.columns(3)
        m1.metric("Machine 1", f"{h1}%")
        m2.metric("Machine 2", f"{h2}%")
        m3.metric("Machine 3", f"{h3}%")

        # ALERT
        popup = False
        msg = ""

        if h2 < 70:
            popup = True
            msg = "🚨 Machine 2 Critical!"
        elif h1 < 75:
            popup = True
            msg = "⚠️ Maintenance Required"

        if popup:
            st.error(msg)
        else:
            st.success("✅ All machines healthy")

        if popup:
            st.markdown(f"""
            <div style="
                position: fixed;
                top: 25%;
                left: 30%;
                width: 40%;
                background: red;
                color: white;
                padding: 20px;
                border-radius: 10px;
                text-align:center;
                font-size:20px;
                z-index:9999;">
                {msg}
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------- CHART ----------
        st.markdown('<div class="card">', unsafe_allow_html=True)

        if use_csv and user_data is not None:
            st.line_chart(user_data[["stock_level","speed_kmph"]])
        else:
            chart = pd.DataFrame({
                "Production":[random.randint(90,150) for _ in range(6)],
                "Energy":[random.randint(400,500) for _ in range(6)]
            })
            st.line_chart(chart)

        st.markdown('</div>', unsafe_allow_html=True)

        # ---------- AI ----------
        if view == "AI Insights":
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.subheader("🧠 THINK Layer")

            if use_csv and user_data is not None:
                st.dataframe(user_data)
                st.info(predict_demand(user_data["stock_level"].mean()))
                st.success(best_route())

                delay = predict_delay(user_data["speed_kmph"].mean())
                if "High" in delay:
                    st.error(delay)
                else:
                    st.success(delay)
            else:
                st.warning("Simulation Mode - Upload CSV")

            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("---")
        st.success("🟢 System Running")

    sleep(5)
