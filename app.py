import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Potato RNA-seq AI",
    page_icon="🌱",
    layout="wide"
)

# ===== STYLE =====
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #F4FFF1 0%, #FFFFFF 45%, #EEF8E8 100%);
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

.main-title {
    color: #1F5C2E;
    font-size: 46px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 0px;
}

.subtitle {
    color: #4B7F52;
    font-size: 22px;
    text-align: center;
    font-weight: 600;
    margin-top: 5px;
}

.card {
    background-color: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}

.green-card {
    background: linear-gradient(135deg, #E8F5E9, #FFFFFF);
    padding: 22px;
    border-radius: 18px;
    border-left: 6px solid #2E7D32;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.07);
}

.stButton>button {
    background: linear-gradient(90deg, #2E7D32, #7CB342);
    color: white;
    border-radius: 14px;
    height: 52px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #1B5E20, #558B2F);
    color: white;
}

[data-testid="metric-container"] {
    background-color: white;
    border-radius: 16px;
    padding: 16px;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.08);
}

.footer {
    text-align: center;
    color: #1F5C2E;
    font-size: 15px;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ===== HEADER =====
st.markdown('<div class="main-title">🌱 Potato RNA-seq AI Bioinformatics</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">AI-assisted gene expression and pathway analysis prototype</div>',
    unsafe_allow_html=True
)

st.info("Academic prototype for plant biotechnology and RNA-seq interpretation.")

# ===== MESSAGE ABOUT POTATO IMAGE =====
st.warning("Please upload a potato-related image later to improve the website design and visualization.")

# ===== PROJECT OVERVIEW =====
st.markdown("## Project Overview")

st.markdown("""
<div class="green-card">
This website explains how AI can support RNA-seq and pathway analysis in potato research.
The system focuses on gene expression pattern recognition, biomarker identification,
pathway prediction, differential gene analysis, and treatment response prediction.
</div>
""", unsafe_allow_html=True)

# ===== AI ANALYSIS SECTION =====
st.markdown("## AI-Assisted Bioinformatics Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>🧬 Gene Expression</h3>
    AI helps detect genes that are upregulated or downregulated after treatment.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>🔍 Biomarker Identification</h3>
    Machine learning can identify important genes linked to plant growth or defense.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>🌿 Pathway Prediction</h3>
    AI predicts affected pathways such as auxin signaling, nitrogen metabolism, and PTI immunity.
    </div>
    """, unsafe_allow_html=True)

# ===== INPUT SECTION =====
st.markdown("## Enter RNA-seq Example Data")

input_col1, input_col2 = st.columns(2)

with input_col1:
    gene = st.text_input("Gene name", "YUCCA")
    fold_change = st.number_input("Fold change", value=2.5)

with input_col2:
    p_value = st.number_input("p-value", value=0.01, format="%.4f")
    pathway = st.selectbox(
        "Main pathway",
        ["Auxin / IAA signaling", "Nitrogen metabolism", "PTI pathway", "MAPK signaling", "Unknown"]
    )

# ===== ANALYSIS =====
if st.button("Analyze Gene"):

    if fold_change > 1 and p_value < 0.05:
        status = "Upregulated"
        importance = "High"
    elif fold_change < -1 and p_value < 0.05:
        status = "Downregulated"
        importance = "High"
    else:
        status = "Not significantly changed"
        importance = "Low"

    st.success("AI Interpretation Generated")

    st.markdown("## AI Output Report")

    r1, r2, r3 = st.columns(3)

    with r1:
        st.metric("Gene", gene)

    with r2:
        st.metric("Expression Status", status)

    with r3:
        st.metric("AI Importance", importance)

    st.markdown("### Predicted Pathway")
    st.write(pathway)

    st.markdown("### Biological Interpretation")

    if pathway == "Auxin / IAA signaling":
        st.write("This may support plant growth, root development, and improved biomass.")
    elif pathway == "Nitrogen metabolism":
        st.write("This may improve nutrient absorption and plant growth performance.")
    elif pathway == "PTI pathway":
        st.write("This may indicate activation of early plant immune defense.")
    elif pathway == "MAPK signaling":
        st.write("This may be related to stress signaling and defense responses.")
    else:
        st.write("Further bioinformatics validation is required.")

# ===== AI SUMMARY =====
st.markdown("## Suggested AI Role in the Study")

st.markdown("""
<div class="green-card">
Machine learning algorithms can be used to identify important gene expression patterns,
predict affected biological pathways, and improve interpretation of RNA-seq data.
This supports understanding of how treatment may influence potato growth, immunity,
and disease resistance.
</div>
""", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("---")

squ_logo = Image.open("SQU-LOGO.png")

footer_col1, footer_col2, footer_col3 = st.columns([2,1,2])

with footer_col2:
    st.image(squ_logo, width=130)

st.markdown(
    '<div class="footer">Sultan Qaboos University | AI-Assisted Plant Biotechnology Prototype</div>',
    unsafe_allow_html=True
)
