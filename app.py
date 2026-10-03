import streamlit as st

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================
st.set_page_config(
    page_title="NeuroFocus AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=None
)
# ==========================================================
# SESSION STATE
# ==========================================================

if "page" not in st.session_state:
    st.session_state.page = "home"

# ==========================================================
# CUSTOM CSS
# ==========================================================


st.markdown("""
<style>

/* ===============================================
GENERAL
=============================================== */

#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

.stApp{
    background:#07131F;
}

/* ===============================================
TEXT
=============================================== */

html,body,p,span,label,div,h1,h2,h3,h4,h5,h6{
    color:white !important;
}

/* ===============================================
HEADINGS
=============================================== */

.main-title{
    text-align:center;
    font-size:60px;
    font-weight:bold;
    color:#00D4FF !important;
}

.subtitle{
    text-align:center;
    font-size:22px;
    color:#DCE7F5 !important;
}

.description{
    text-align:center;
    color:#BFC9D8 !important;
}

/* ===============================================
CARDS
=============================================== */

.card{

    background:#111C2D;

    border-radius:18px;

    padding:20px;

    border:1px solid #00D4FF;

    box-shadow:0px 0px 20px rgba(0,212,255,.18);

}

/* ===============================================
BUTTONS
=============================================== */

.stButton>button{

    width:100%;

    height:55px;

    border-radius:12px;

    background:#00D4FF;

    color:black;

    font-weight:bold;

    font-size:18px;

    border:none;

}

.stButton>button:hover{

    background:#33E2FF;

    color:black;

}

/* ===============================================
DOWNLOAD BUTTON
=============================================== */

[data-testid="stDownloadButton"] button{

    background:#00D4FF;

    color:black;

    font-weight:bold;

}

/* ===============================================
METRICS
=============================================== */

[data-testid="stMetric"]{

    background:#111C2D;

    border-radius:15px;

    border:1px solid #00D4FF;

    padding:15px;

}

[data-testid="stMetricLabel"]{

    color:white !important;

}

[data-testid="stMetricValue"]{

    color:#00D4FF !important;

    font-size:30px;

    font-weight:bold;

}

/* ===============================================
FILE UPLOADER
=============================================== */

[data-testid="stFileUploader"]{

    background:#111C2D !important;

    border:2px dashed #00D4FF !important;

    border-radius:15px;

    padding:20px;

}

[data-testid="stFileUploader"] *{

    color:black !important;

}

/* ===============================================
TABLE
=============================================== */

table{

    color:white !important;

    background:#111C2D !important;

}

th{

    background:#00D4FF !important;

    color:black !important;

}

td{

    background:#111C2D !important;

    color:white !important;

}

/* ===============================================
ALERTS
=============================================== */

.stAlert{

    color:white !important;

}

/* ===============================================
SIDEBAR
=============================================== */

section[data-testid="stSidebar"]{

    background:#111C2D;

}

/* ===============================================
FOOTER
=============================================== */

.footer{

    color:#BFC9D8 !important;

    text-align:center;

}
/* Toolbar background */
[data-testid="stElementToolbar"] {
    background: #111C2D !important;
    border-radius: 10px !important;
}

/* Toolbar buttons */
[data-testid="stElementToolbar"] button {
    background: #111C2D !important;
    color: white !important;
}

/* SVG icons (download, expand, etc.) */
[data-testid="stElementToolbar"] svg {
    fill: white !important;
    color: white !important;
    stroke: white !important;
}

/* Hover effect */
[data-testid="stElementToolbar"] button:hover {
    background: #00D4FF !important;
}

[data-testid="stElementToolbar"] button:hover svg {
    fill: black !important;
    stroke: black !important;
}
</style>
""", unsafe_allow_html=True)
# ==========================================================
# HOME PAGE
# ==========================================================

def home_page():

    st.markdown(
        "<div class='main-title'>🧠 NeuroFocus AI</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>Single-Channel EEG Attention Monitoring System</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='description'>Powered by Deep Learning (1D Convolutional Neural Network)</div>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    st.markdown("---")

    st.subheader("📖 About NeuroFocus AI")

    st.write("""
NeuroFocus AI is an intelligent EEG attention monitoring system developed using a
Single-Channel EEG signal and a Deep Learning based 1D CNN model.

The system analyzes EEG recordings, predicts attention every second,
computes average attention every 10 seconds,
and generates visual analytics including graphs,
timeline reports, AI summaries and downloadable PDF reports.
""")

    st.write("")
    st.markdown("---")

    st.subheader("✨ Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
<div class="card">

### 📂 CSV Analysis

Upload raw EEG CSV recordings.

Automatic preprocessing.

250-sample window generation.

</div>
""", unsafe_allow_html=True)

    with c2:
        st.markdown("""
<div class="card">

### 🧠 CNN Prediction

Uses trained AttentionCNN.

Threshold = 0.35

Predicts Attention every second.

</div>
""", unsafe_allow_html=True)

    with c3:
        st.markdown("""
<div class="card">

### 📊 Visual Report

Attention Graph

Pie Chart

Timeline

PDF Report

</div>
""", unsafe_allow_html=True)

    st.write("")
    st.markdown("---")

    st.subheader("🚀 Start Analysis")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("📂 Upload EEG CSV"):

            st.session_state.page = "upload"

            st.rerun()

    with col2:

        st.button(
            "📡 Live EEG (Coming Soon)",
            disabled=True
        )

    st.write("")
    st.write("")

    st.markdown(
        """
<div class='footer'>

Developed as a <b>B.Tech Mini Project</b><br><br>

Department of CSE (Data Science)<br>

Geethanjali College of Engineering and Technology

</div>
""",
        unsafe_allow_html=True
    )


# ==========================================================
# PAGE ROUTER
# ==========================================================

if st.session_state.page == "home":

    home_page()

elif st.session_state.page == "upload":

    st.info("Upload Page (Coming in Part 2)")
# ==========================================================
# PAGE 2
# Upload Page + Processing Pipeline
# Paste this below Page 1 in app.py
# ==========================================================

import pandas as pd
import numpy as np
import torch
import torch.nn as nn
import time

MODEL_PATH = "attention_cnn.pth"
THRESHOLD = 0.35

class AttentionCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv1d(1,16,kernel_size=5,padding=2),
            nn.BatchNorm1d(16),
            nn.ReLU(),
            nn.MaxPool1d(2),
            nn.Conv1d(16,32,kernel_size=5,padding=2),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.MaxPool1d(2),
            nn.Conv1d(32,64,kernel_size=3,padding=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(1)
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Dropout(0.5),
            nn.Linear(64,1)
        )

    def forward(self,x):
        x=self.features(x)
        return self.classifier(x)

@st.cache_resource
def load_model():
    model=AttentionCNN()
    model.load_state_dict(torch.load(MODEL_PATH,map_location="cpu"))
    model.eval()
    return model

def normalize_signal(signal):
    signal=np.asarray(signal,dtype=np.float32)
    return (signal-signal.mean())/(signal.std()+1e-8)

def create_windows(signal,window=250):
    out=[]
    for i in range(0,len(signal)-window+1,window):
        out.append(signal[i:i+window])
    out=np.array(out).reshape(-1,1,250)
    return out

def upload_page():

    st.title("📂 Upload EEG CSV")

    uploaded=st.file_uploader(
        "Select EEG CSV",
        type=["csv"]
    )

    if uploaded is None:
        st.info("Please upload a CSV containing an FP1 column.")
        return

    df=pd.read_csv(uploaded)

    if "FP1" not in df.columns:
        st.error("CSV must contain a column named FP1.")
        return

    signal=df["FP1"].values

    samples=len(signal)
    duration=samples/250

    st.success("CSV Loaded Successfully")

    c1,c2,c3=st.columns(3)
    c1.metric("Samples",samples)
    c2.metric("Duration",f"{duration:.1f} sec")
    c3.metric("Windows",samples//250)

    if st.button("🧠 Analyze EEG"):

        progress=st.progress(0)
        status=st.empty()

        status.info("Loading AttentionCNN...")
        model=load_model()
        progress.progress(15)

        status.info("Normalizing EEG...")
        signal=normalize_signal(signal)
        progress.progress(35)

        status.info("Creating Windows...")
        windows=create_windows(signal)
        X=torch.tensor(windows,dtype=torch.float32)
        progress.progress(55)

        status.info("Running CNN...")
        with torch.no_grad():
            logits=model(X)
            probs=torch.sigmoid(logits).cpu().numpy().flatten()
        progress.progress(75)

        attention_percent=probs*100

        ten_second_average=[]
        timeline=[]

        for i in range(0,len(attention_percent),10):
            block=attention_percent[i:i+10]
            avg=float(np.mean(block))
            start=i
            end=min(i+10,len(attention_percent))
            ten_second_average.append(avg)
            timeline.append({
                "Time":f"{start}-{end} sec",
                "Attention":round(avg,2)
            })

        st.session_state.probabilities=probs
        st.session_state.attention_percent=attention_percent
        st.session_state.ten_second_average=ten_second_average
        st.session_state.timeline=timeline
        st.session_state.average_attention=float(np.mean(attention_percent))
        st.session_state.highest_attention=float(np.max(attention_percent))
        st.session_state.lowest_attention=float(np.min(attention_percent))
        st.session_state.attentive_seconds=int(np.sum(probs>=THRESHOLD))
        st.session_state.inattentive_seconds=int(np.sum(probs<THRESHOLD))
        st.session_state.total_windows=len(probs)
        st.session_state.duration=duration
        st.session_state.threshold=THRESHOLD

        progress.progress(100)
        status.success("Analysis Complete!")

        time.sleep(1)

        st.session_state.page="summary"
        st.rerun()

if st.session_state.page=="upload":
    upload_page()

# ==========================================================
# PAGE 3 - EEG ANALYSIS REPORT
# Paste below Page 2
# ==========================================================

import pandas as pd

def summary_page():

    st.title("🧠 EEG Analysis Report")
    st.success("EEG Analysis Completed Successfully")

    avg = st.session_state.average_attention
    high = st.session_state.highest_attention
    low = st.session_state.lowest_attention
    duration = st.session_state.duration
    threshold = st.session_state.threshold
    probs = st.session_state.probabilities

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Average Attention",f"{avg:.2f}%")
    c2.metric("Highest",f"{high:.2f}%")
    c3.metric("Lowest",f"{low:.2f}%")
    c4.metric("Duration",f"{duration:.1f} sec")

    st.divider()

    left,right=st.columns([1,1])

    with left:
        st.subheader("Model Information")
        st.info(f"""
Model : AttentionCNN

Framework : PyTorch

Threshold : {threshold}

Input : (1,1,250)

Predictions : {len(probs)}
""")

    with right:
        st.subheader("Session Statistics")

        attentive = st.session_state.attentive_seconds
        inattentive = st.session_state.inattentive_seconds

        stats = pd.DataFrame({
            "Metric":[
                "Attentive Seconds",
                "Inattentive Seconds",
                "Total Predictions"
            ],
            "Value":[
                attentive,
                inattentive,
                len(probs)
            ]
        })

        st.dataframe(stats,use_container_width=True)

    st.divider()

    st.subheader("AI Interpretation")

    if avg >= 85:
        st.success(
            "Excellent attention detected throughout most of the recording."
        )
    elif avg >= 70:
        st.warning(
            "Good attention with a few moderate attention drops."
        )
    else:
        st.error(
            "Multiple attention drops detected during the session."
        )

    st.subheader("Recommendation")

    st.write(
        """
• Continue regular study sessions.

• Take short breaks every 30–45 minutes.

• Review the dashboard to identify low-attention intervals.
"""
    )

    col1,col2,col3 = st.columns(3)

    with col1:
        if st.button("📊 View Dashboard"):
            st.session_state.page="dashboard"
            st.rerun()

    with col2:
        if st.button("🏠 Home"):
            st.session_state.page="home"
            st.rerun()

    with col3:
        if st.button("🔄 Analyze Another File"):
            st.session_state.page="upload"
            st.rerun()

if st.session_state.page=="summary":
    summary_page()


# ==========================================================
# PAGE 4 - DASHBOARD
# Paste below Page 3
# ==========================================================

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def dashboard_page():

    st.title("📊 NeuroFocus AI Dashboard")

    avg = st.session_state.average_attention
    high = st.session_state.highest_attention
    low = st.session_state.lowest_attention
    timeline = st.session_state.timeline
    ten_avg = st.session_state.ten_second_average

    c1,c2,c3,c4 = st.columns(4)
    c1.metric("Average",f"{avg:.2f}%")
    c2.metric("Highest",f"{high:.2f}%")
    c3.metric("Lowest",f"{low:.2f}%")
    c4.metric("Windows",st.session_state.total_windows)

    st.divider()

    # ---------------- Line Graph ----------------
    st.subheader("Attention Trend (10 Second Average)")

    x = np.arange(1,len(ten_avg)+1)*10

    fig,ax = plt.subplots(figsize=(10,4))
    ax.plot(x,ten_avg,marker="o",linewidth=2)
    ax.fill_between(x,ten_avg,alpha=0.25)
    ax.set_xlabel("Time (Seconds)")
    ax.set_ylabel("Attention (%)")
    ax.set_ylim(0,100)
    ax.grid(True)

    lowest_idx = int(np.argmin(ten_avg))
    ax.scatter([x[lowest_idx]],[ten_avg[lowest_idx]],s=120)
    ax.annotate("Lowest",
                (x[lowest_idx],ten_avg[lowest_idx]))

    st.pyplot(fig)

    st.divider()

    # ---------------- Scatter Plot ----------------

    st.subheader("Attention Variation Over Time")

    # Time points for every 10-second interval
    scatter_time = np.arange(1, len(ten_avg) + 1) * 10

    fig_scatter, ax_scatter = plt.subplots(figsize=(10, 4))

    # Scatter points
    ax_scatter.scatter(
        scatter_time,
        ten_avg,
        s=100
    )   

    # Connect points so rise/fall is easy to understand
    ax_scatter.plot(
        scatter_time,
        ten_avg,
        linewidth=1.5,
        alpha=0.6
    )

    # Add percentage above each point
    for time_point, attention in zip(scatter_time, ten_avg):
        ax_scatter.annotate(
            f"{attention:.1f}%",
            (time_point, attention),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center"
        )

    ax_scatter.set_xlabel("Time (Seconds)")
    ax_scatter.set_ylabel("Attention (%)")
    ax_scatter.set_title("10-Second Attention Variation")

    ax_scatter.set_ylim(0, 100)

    ax_scatter.grid(
        True,
        linestyle="--",
        alpha=0.4
    )

    st.pyplot(fig_scatter)

    st.divider()
    left,right = st.columns(2)

    # ---------------- Pie ----------------
    with left:

        st.subheader("Attentive vs Inattentive")

        fig2,ax2 = plt.subplots(figsize=(5,5))

        ax2.pie(
            [
                st.session_state.attentive_seconds,
                st.session_state.inattentive_seconds
            ],
            labels=["Attentive","Inattentive"],
            autopct="%1.1f%%",
            startangle=90
        )

        ax2.axis("equal")

        st.pyplot(fig2)

    # ---------------- Bar ----------------
    with right:

        st.subheader("Average Attention")

        fig3,ax3 = plt.subplots(figsize=(6,5))

        labels=[f"{i*10}-{(i+1)*10}"
                for i in range(len(ten_avg))]

        ax3.bar(labels,ten_avg)

        ax3.set_ylim(0,100)

        ax3.set_ylabel("Attention %")

        ax3.set_xlabel("Time (sec)")

        plt.xticks(rotation=45)

        st.pyplot(fig3)

    st.divider()

    # ---------------- Timeline ----------------
    st.subheader("Timeline")

    rows=[]

    for row in timeline:

        value=row["Attention"]

        if value>=80:
            status="🟢 High"
        elif value>=60:
            status="🟡 Moderate"
        else:
            status="🔴 Low"

        rows.append({
            "Time":row["Time"],
            "Attention (%)":round(value,2),
            "Status":status
        })

    timeline_df=pd.DataFrame(rows)

    st.dataframe(
        timeline_df,
        use_container_width=True
    )

    st.divider()

    st.subheader("AI Summary")

    if avg>=85:
        st.success(
            "Overall attention remained excellent. Only minor fluctuations were observed."
        )
    elif avg>=65:
        st.warning(
            "Attention remained good with a few moderate drops."
        )
    else:
        st.error(
            "Frequent attention drops were detected during the session."
        )

    col1,col2=st.columns(2)

    with col1:
        if st.button("📄 Download Report"):
            st.session_state.page="report"
            st.rerun()

    with col2:
        if st.button("🏠 Home"):
            st.session_state.page="home"
            st.rerun()


if st.session_state.page=="dashboard":
    dashboard_page()


# ==========================================================
# PAGE 5 - REPORTS & EXPORTS
# Paste below Page 4
# ==========================================================

import io
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf():

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>NeuroFocus AI</b>",styles["Title"]))
    story.append(Paragraph("EEG Attention Analysis Report",styles["Heading1"]))
    story.append(Spacer(1,12))

    story.append(Paragraph(f"Average Attention : {st.session_state.average_attention:.2f}%",styles["BodyText"]))
    story.append(Paragraph(f"Highest Attention : {st.session_state.highest_attention:.2f}%",styles["BodyText"]))
    story.append(Paragraph(f"Lowest Attention : {st.session_state.lowest_attention:.2f}%",styles["BodyText"]))
    story.append(Paragraph(f"Duration : {st.session_state.duration:.1f} sec",styles["BodyText"]))
    story.append(Paragraph(f"Threshold : {st.session_state.threshold}",styles["BodyText"]))
    story.append(Spacer(1,12))

    avg = st.session_state.average_attention

    if avg >= 85:
        summary = "Overall attention level is Excellent. Stable concentration was observed."
    elif avg >= 70:
        summary = "Overall attention level is Good with a few moderate drops."
    else:
        summary = "Multiple attention drops were detected during the recording."

    story.append(Paragraph("<b>AI Summary</b>",styles["Heading2"]))
    story.append(Paragraph(summary,styles["BodyText"]))
    story.append(Spacer(1,18))

    story.append(Paragraph("<b>Developed as a B.Tech Mini Project</b>",styles["BodyText"]))
    story.append(Paragraph("Department of CSE (Data Science)",styles["BodyText"]))
    story.append(Paragraph("Geethanjali College of Engineering and Technology",styles["BodyText"]))

    doc.build(story)

    pdf = buffer.getvalue()
    buffer.close()
    return pdf


def report_page():

    st.title("📄 Download Report")

    st.success("Your EEG analysis has been completed successfully.")

    timeline_df = pd.DataFrame(st.session_state.timeline)

    csv_data = timeline_df.to_csv(index=False).encode("utf-8")

    pdf_data = generate_pdf()

    c1, c2 = st.columns(2)

    with c1:
        st.download_button(
            "📄 Download PDF Report",
            pdf_data,
            file_name="NeuroFocus_AI_Report.pdf",
            mime="application/pdf"
        )

    with c2:
        st.download_button(
            "📊 Download Timeline CSV",
            csv_data,
            file_name="Attention_Timeline.csv",
            mime="text/csv"
        )

    st.divider()

    st.subheader("Quick Summary")

    st.write(f"Average Attention : **{st.session_state.average_attention:.2f}%**")
    st.write(f"Highest Attention : **{st.session_state.highest_attention:.2f}%**")
    st.write(f"Lowest Attention : **{st.session_state.lowest_attention:.2f}%**")
    st.write(f"Total Predictions : **{st.session_state.total_windows}**")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔄 Analyze Another CSV"):
            st.session_state.page = "upload"
            st.rerun()

    with col2:
        if st.button("🏠 Home"):
            st.session_state.page = "home"
            st.rerun()

    st.markdown("---")
    st.markdown(
        """
        <center>
        <b>NeuroFocus AI</b><br>
        Developed as a <b>B.Tech Mini Project</b><br>
        Department of CSE (Data Science)<br>
        Geethanjali College of Engineering and Technology
        </center>
        """,
        unsafe_allow_html=True
    )


if st.session_state.page == "report":
    report_page()


