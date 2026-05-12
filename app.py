import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Potato Auxin Gene AI",
    page_icon="🌱",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #F4FFF1 0%, #FFFFFF 50%, #EEF8E8 100%);
}
.main-title {
    color: #1F5C2E;
    font-size: 44px;
    font-weight: 800;
    text-align: center;
}
.subtitle {
    color: #4B7F52;
    font-size: 21px;
    text-align: center;
    font-weight: 600;
}
.card {
    background-color: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
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
[data-testid="metric-container"] {
    background-color: white;
    border-radius: 16px;
    padding: 16px;
    box-shadow: 0px 6px 16px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# ===== SQU LOGO TOP =====
try:
    logo = Image.open("SQU-LOGO.png")
    c1, c2, c3 = st.columns([2,1,2])
    with c2:
        st.image(logo, width=140)
except:
    pass

st.markdown('<div class="main-title">🌱 AI Analysis of Auxin-Related Genes in Potato</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">ZNC-induced IPA-dependent IAA biosynthesis pathway prediction</div>', unsafe_allow_html=True)

st.info("This academic prototype predicts whether ZNC activates auxin biosynthesis based on RNA-seq/qRT-PCR gene expression patterns.")

st.markdown("## Enter Gene Expression Fold Change")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Upregulated Auxin Genes")
    yuca3 = st.number_input("StYUCCA3 fold change", value=2.5)
    yuca4 = st.number_input("StYUCCA4 fold change", value=2.2)
    yuca10 = st.number_input("StYUCCA10 fold change", value=2.8)
    tir1 = st.number_input("StTIR1 fold change", value=1.8)
    arf9 = st.number_input("StARF9 fold change", value=1.7)
    saur = st.number_input("SAUR genes fold change", value=2.0)

with col2:
    st.subheader("Downregulated IAA-Conjugation Gene")
    gh36 = st.number_input("GH3.6-like fold change", value=-1.8)

    st.subheader("Optional Physiological Result")
    iaa_increase = st.number_input("Free IAA increase (%)", value=30.0)
    concentration = st.selectbox("ZNC concentration", ["1 ng/ml", "5 ng/ml", "10 ng/ml", "100 ng/ml"])

if st.button("Analyze Auxin Pathway"):

    upregulated_genes = 0

    for gene_value in [yuca3, yuca4, yuca10, tir1, arf9, saur]:
        if gene_value > 1:
            upregulated_genes += 1

    gh3_downregulated = gh36 < -1
    iaa_high = 18 <= iaa_increase <= 45

    score = 0

    if upregulated_genes >= 4:
        score += 40

    if gh3_downregulated:
        score += 30

    if iaa_high:
        score += 20

    if concentration in ["1 ng/ml", "5 ng/ml", "10 ng/ml"]:
        score += 10

    if score >= 80:
        situation = "Strong activation of IPA-dependent IAA biosynthesis"
        interpretation = "ZNC strongly activates auxin biosynthesis and signaling. This supports increased free IAA content, enhanced cell elongation, root development, and tuber bulking."

    elif score >= 50:
        situation = "Moderate activation of auxin pathway"
        interpretation = "The gene expression pattern suggests partial activation of auxin-related growth pathways, but not all markers show a strong response."

    else:
        situation = "Weak or unclear auxin activation"
        interpretation = "The current gene expression pattern does not strongly support ZNC-induced auxin pathway activation. Further RNA-seq/qRT-PCR validation is needed."

    st.success("AI Gene Interpretation Generated")

    st.markdown("## AI Output Report")

    r1, r2, r3 = st.columns(3)

    with r1:
        st.metric("Upregulated Auxin Genes", f"{upregulated_genes}/6")

    with r2:
        st.metric("GH3.6 Status", "Downregulated" if gh3_downregulated else "Not downregulated")

    with r3:
        st.metric("AI Confidence Score", f"{score}%")

    st.markdown("### Predicted Biological Situation")
    st.write(situation)

    st.markdown("### Biological Interpretation")
    st.write(interpretation)

    st.markdown("### Pathway Conclusion")
    if score >= 80:
        st.write("✅ ZNC likely promotes potato growth through activation of IPA-dependent IAA biosynthesis.")
    elif score >= 50:
        st.write("⚠️ ZNC may activate auxin signaling, but the evidence is moderate.")
    else:
        st.write("❌ Auxin pathway activation is not clearly supported by the entered data.")

st.markdown("---")
st.markdown("Sultan Qaboos University | AI-Assisted Plant Biotechnology Prototype")
