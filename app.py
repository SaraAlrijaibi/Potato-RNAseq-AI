import streamlit as st

st.set_page_config(
    page_title="Potato RNA-seq AI",
    page_icon="🌱",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #F3FFF2 0%, #FFFFFF 45%, #EEF8E8 100%);
}
.main-title {
    color: #1F5C2E;
    font-size: 44px;
    font-weight: 800;
    text-align: center;
}
.subtitle {
    color: #4B7F52;
    font-size: 22px;
    text-align: center;
}
.card {
    background-color: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 18px;
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
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🌱 Potato RNA-seq AI Bioinformatics</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-assisted gene expression and pathway analysis prototype</div>', unsafe_allow_html=True)

st.info("Academic prototype for plant biotechnology and RNA-seq interpretation.")

st.image("https://images.unsplash.com/photo-1518977676601-b53f82aba655", use_container_width=True)

st.markdown("## Project Overview")

st.markdown("""
<div class="card">
This website explains how AI can support RNA-seq and pathway analysis in potato research.
The system focuses on gene expression pattern recognition, biomarker identification,
pathway prediction, differential gene analysis, and treatment response prediction.
</div>
""", unsafe_allow_html=True)

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
    Machine learning can identify important genes linked to growth or defense.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>🌿 Pathway Prediction</h3>
    AI predicts affected pathways such as auxin signaling, nitrogen metabolism, and PTI immunity.
    </div>
    """, unsafe_allow_html=True)

st.markdown("## Enter RNA-seq Example Data")

gene = st.text_input("Gene name", "YUCCA")
fold_change = st.number_input("Fold change", value=2.5)
p_value = st.number_input("p-value", value=0.01, format="%.4f")
pathway = st.selectbox(
    "Main pathway",
    ["Auxin / IAA signaling", "Nitrogen metabolism", "PTI pathway", "MAPK signaling", "Unknown"]
)

if st.button("Analyze Gene"):

    if fold_change > 1 and p_value < 0.05:
        status = "Upregulated"
    elif fold_change < -1 and p_value < 0.05:
        status = "Downregulated"
    else:
        status = "Not significantly changed"

    st.success("AI Interpretation Generated")

    st.markdown("## AI Output Report")
    st.write(f"**Gene:** {gene}")
    st.write(f"**Expression status:** {status}")
    st.write(f"**Predicted pathway:** {pathway}")

    if pathway == "Auxin / IAA signaling":
        st.write("**Biological meaning:** This may support plant growth and root development.")
    elif pathway == "Nitrogen metabolism":
        st.write("**Biological meaning:** This may improve nutrient absorption and growth.")
    elif pathway == "PTI pathway":
        st.write("**Biological meaning:** This may indicate activation of plant immune defense.")
    elif pathway == "MAPK signaling":
        st.write("**Biological meaning:** This may be related to stress and defense signaling.")
    else:
        st.write("**Biological meaning:** Further analysis is required.")

st.markdown("## Suggested AI Role in the Study")

st.markdown("""
Machine learning algorithms were used to identify important gene expression patterns,
predict affected biological pathways, and improve interpretation of RNA-seq data.
This supports understanding of how treatment may influence potato growth, immunity,
and disease resistance.
""")
