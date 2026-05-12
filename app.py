import streamlit as st
from PIL import Image

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Molecular Analysis AI",
    page_icon="🧬",
    layout="wide"
)

# ---------------- SQU LOGO AT TOP ----------------
logo = Image.open("SQU-LOGO.png")

col1, col2, col3 = st.columns([1,2,1])

with col2:
    st.image(logo, width=180)

# ---------------- TITLE ----------------
st.markdown(
    """
    <h1 style='text-align: center; color: #2E7D32;'>
    AI-Assisted Molecular Analysis
    </h1>
    """,
    unsafe_allow_html=True
)

st.info("This is an academic prototype for RNA-seq and bioinformatics analysis.")

# ---------------- INTRODUCTION ----------------
st.markdown("## Overview")

st.write("""
This workflow explains how RNA-seq, bioinformatics, and artificial intelligence (AI)
can be used together to study important molecular pathways in plants.
""")

# ---------------- WORKFLOW ----------------
st.markdown("## Molecular Workflow")

workflow = """
1. RNA Extraction  
→ Collect plant leaves and extract total RNA.

2. RNA Sequencing (RNA-seq)  
→ Sequence RNA to study gene expression.

3. Bioinformatics Analysis  
→ Perform genome alignment and pathway analysis.

4. AI-Assisted Analysis  
→ Use machine learning to identify:
   - Gene expression patterns
   - Important biomarkers
   - Affected pathways
   - Similar gene clusters

5. qRT-PCR Validation  
→ Confirm important genes experimentally.
"""

st.markdown(workflow)

# ---------------- TARGET PATHWAYS ----------------
st.markdown("## Important Molecular Pathways")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("Auxin / IAA Pathway")

with col2:
    st.success("Nitrogen Metabolism")

with col3:
    st.success("PTI Immunity Pathway")

# ---------------- OUTCOME ----------------
st.markdown("## Final Outcome")

st.write("""
Combining RNA-seq, AI, and bioinformatics helps researchers better understand
plant molecular mechanisms and identify important biological pathways.
""")

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Developed for academic and educational purposes.")
