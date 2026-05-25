import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- UTILS IMPORTS ---------------- #

from utils.lead_generator import (
    calculate_score,
    generate_recommendations
)

from utils.market_analyzer import (
    get_markets,
    get_regions
)

from utils.pitch_generator import (
    generate_pitch
)

from utils.email_sender import (
    generate_bulk_email
)

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Marketing Agent",
    page_icon="🤖",
    layout="wide"
)

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🤖 AI Marketing Agent")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Lead Insights",
        "Market Opportunities",
        "AI Pitch Generator",
        "Bulk Email Automation"
    ]
)

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📂 Upload Lead Dataset",
    type=["csv", "xlsx"]
)

# ---------------- MAIN APP ---------------- #

if uploaded_file.name.endswith(".csv"):

    df = pd.read_csv(uploaded_file)

elif uploaded_file.name.endswith(".xlsx"):

    df = pd.read_excel(uploaded_file)

    # ---------------- LEAD SCORING ---------------- #

    df["Lead_Score"] = df.apply(
        calculate_score,
        axis=1
    )

    # ---------------- DASHBOARD ---------------- #

    if menu == "Dashboard":

        st.title("📊 AI Marketing Dashboard")

        st.success("Dataset Uploaded Successfully!")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total Leads",
            len(df)
        )

        col2.metric(
            "High Interest Leads",
            len(df[df["Interest_Level"] == "High"])
        )

        col3.metric(
            "Healthcare Companies",
            len(df[df["Industry"] == "Healthcare"])
        )

        col4.metric(
            "Defense Companies",
            len(df[df["Industry"] == "Defense"])
        )

        st.write("")

        st.subheader("📋 Lead Dataset")

        st.dataframe(df)

        # ---------------- EXPORT REPORT FEATURE ---------------- #

        st.subheader("📥 Export Business Report")

        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇️ Download Lead Report",
            data=csv,
            file_name="AI_Marketing_Report.csv",
            mime="text/csv"
        )

        # ---------------- VISUALIZATIONS ---------------- #

        st.subheader("📊 Business Analytics Visualization")

        chart_col1, chart_col2 = st.columns(2)

        # Industry Distribution Chart

        industry_count = df["Industry"].value_counts()

        fig1 = px.bar(
            x=industry_count.index,
            y=industry_count.values,
            labels={
                "x": "Industry",
                "y": "Count"
            },
            title="Industry Distribution"
        )

        chart_col1.plotly_chart(
            fig1,
            use_container_width=True
        )

        # Interest Level Pie Chart

        interest_count = df["Interest_Level"].value_counts()

        fig2 = px.pie(
            names=interest_count.index,
            values=interest_count.values,
            title="Interest Level Distribution"
        )

        chart_col2.plotly_chart(
            fig2,
            use_container_width=True
        )

        # Lead Score Chart

        st.subheader("🏆 Top Lead Score Analysis")

        top_scores = df.sort_values(
            by="Lead_Score",
            ascending=False
        ).head(10)

        fig3 = px.bar(
            top_scores,
            x="Company",
            y="Lead_Score",
            color="Industry",
            title="Top Lead Scores"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    # ---------------- LEAD INSIGHTS ---------------- #

    elif menu == "Lead Insights":

        st.title("🎯 Lead Insights & Target Customers")

        top_leads = df.sort_values(
            by="Lead_Score",
            ascending=False
        )

        st.subheader("🏆 Top Potential Customers")

        st.dataframe(top_leads)

        st.subheader("📈 AI Lead Recommendations")

        for index, row in top_leads.head(5).iterrows():

            recommendation = generate_recommendations()

            st.info(
                f"""
                {row['Name']} from {row['Company']}
                is a high-priority lead in the
                {row['Industry']} sector.

                AI Insight:
                {recommendation}
                """
            )

    # ---------------- MARKET OPPORTUNITIES ---------------- #

    elif menu == "Market Opportunities":

        st.title("🌍 New Market Opportunities")

        st.success("AI Market Analysis Completed")

        st.subheader("📌 Recommended Business Markets")

        markets = get_markets()

        for market in markets:
            st.write(f"✅ {market}")

        st.subheader("📍 Suggested Expansion Regions")

        regions = get_regions()

        for region in regions:
            st.write(f"📌 {region}")

    # ---------------- AI PITCH GENERATOR ---------------- #

    elif menu == "AI Pitch Generator":

        st.title("✉️ AI Customized Pitch Generator")

        customer = st.selectbox(
            "Select Customer",
            df["Company"]
        )

        selected_row = df[
            df["Company"] == customer
        ].iloc[0]

        if st.button("Generate AI Pitch"):

            pitch = generate_pitch(selected_row)

            st.success(
                "AI Pitch Generated Successfully!"
            )

            st.text_area(
                "Generated Proposal",
                pitch,
                height=350
            )

    # ---------------- BULK EMAIL AUTOMATION ---------------- #

    elif menu == "Bulk Email Automation":

        st.title("📧 Bulk Email Automation")

        st.subheader(
            "📨 Generate Personalized Outreach Emails"
        )

        if st.button("Start AI Email Campaign"):

            st.success(
                "AI Bulk Outreach Started Successfully!"
            )

            for index, row in df.head(10).iterrows():

                email = generate_bulk_email(row)

                st.info(email)

            st.balloons()

else:

    st.warning(
        "Please upload a CSV dataset to continue."
    )