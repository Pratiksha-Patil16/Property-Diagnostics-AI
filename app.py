import streamlit as st
import os

from document_parser import extract_text
from image_extractor import extract_images
from reasoning import generate_ddr

st.set_page_config(
    page_title="Property Diagnostics AI",
    page_icon="🏢",
    layout="wide"
)

st.title("🏢 Property Diagnostics AI")
st.subheader("AI-Powered DDR Report Generator")

st.write(
    "Upload the Inspection Report and Thermal Report to generate a Detailed Diagnostic Report (DDR)."
)

inspection_pdf = st.file_uploader(
    "Upload Inspection Report",
    type=["pdf"]
)

thermal_pdf = st.file_uploader(
    "Upload Thermal Report",
    type=["pdf"]
)

if st.button("Generate DDR"):

    if inspection_pdf is None or thermal_pdf is None:
        st.error("Please upload both PDFs.")
        st.stop()

    os.makedirs("uploads", exist_ok=True)

    inspection_path = os.path.join(
        "uploads",
        inspection_pdf.name
    )

    thermal_path = os.path.join(
        "uploads",
        thermal_pdf.name
    )

    with open(inspection_path, "wb") as f:
        f.write(inspection_pdf.getbuffer())

    with open(thermal_path, "wb") as f:
        f.write(thermal_pdf.getbuffer())

    inspection_text = extract_text(inspection_path)
    thermal_text = extract_text(thermal_path)

    ddr_report = generate_ddr(
        inspection_text,
        thermal_text
    )

    st.success("DDR Generated Successfully")

    st.markdown("## Generated DDR")
    st.write(ddr_report)