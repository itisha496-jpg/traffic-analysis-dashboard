import streamlit as st
import plotly.express as px
import json

st.set_page_config(page_title="Traffic Analysis Dashboard", layout="wide", page_icon="🚦")

with open('/content/output.json', 'r') as f:
    data = json.load(f)

st.title("🚦 Indian Roads Traffic Analysis Dashboard")
st.markdown("---")

# Summary Cards - Fixed
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 🚗 Total Vehicles")
    st.markdown(f"## **{data['summary']['total_vehicles']}**")
with col2:
    st.markdown("### 🚨 Total Violations")
    st.markdown(f"## **{data['summary']['total_violations']}**")
with col3:
    st.markdown("### 🔀 Total Junctions")
    st.markdown(f"## **{data['summary']['total_junctions']}**")

st.markdown("---")

col4, col5 = st.columns(2)

with col4:
    st.subheader("🚨 Violations Breakdown")
    violations = data["violations"]
    viol_names = ["Helmet Less", "Wrong Side", "Signal Jump", "Mobile Use", "Triple Riding"]
    viol_counts = [
        len(violations["helmet_less"]),
        len(violations["wrong_side"]),
        len(violations["signal_jumping"]),
        len(violations["mobile_use"]),
        len(violations["triple_riding"])
    ]
    fig1 = px.bar(x=viol_names, y=viol_counts, color=viol_names,
                  title="Violations by Type",
                  labels={"x": "Violation Type", "y": "Count"})
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    st.subheader("🚗 Vehicle Distribution")
    veh = data["vehicles"]
    fig2 = px.pie(
        names=["Two Wheeler", "LMV", "HMV", "Others"],
        values=[veh["two_wheeler"], veh["LMV"], veh["HMV"], veh["others"]],
        title="Vehicle Category Distribution"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

st.subheader("📈 Vehicle Density Over Time")
density = data["vehicle_density"]
timestamps = [d["timestamp"] for d in density[::5]]
counts = [d["count"] for d in density[::5]]
fig3 = px.line(x=timestamps, y=counts, title="Vehicles Per Frame Over Time",
               labels={"x": "Timestamp", "y": "Vehicle Count"})
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

col6, col7 = st.columns(2)

with col6:
    st.subheader("🚨 Violations Event Log")
    for vtype, events in violations.items():
        for e in events:
            st.markdown(f"🔴 **{vtype.replace('_', ' ').title()}** — `{e['timestamp']}`")

with col7:
    st.subheader("🔀 Junction Log")
    for j in data["junctions"]:
        st.markdown(f"🟢 **{j['type']}** — `{j['timestamp']}`")
