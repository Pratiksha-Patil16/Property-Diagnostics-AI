import streamlit as st
import os
import re

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

    # Extract text
    inspection_text = extract_text(inspection_path)
    thermal_text = extract_text(thermal_path)

    # Find temperatures between 20.5 and 21.5
    temps = re.findall(r"\d+\.\d+", thermal_text)
    temps = [float(t) for t in temps]

    relevant_temps = [
        t for t in temps
        if 20.5 <= t <= 20.9
    ]

    # Extract images
    inspection_images = extract_images(inspection_path)
    thermal_images = extract_images(thermal_path)

    # Generate DDR
    ddr_report = generate_ddr(
        inspection_text,
        thermal_text
    )

    st.success("DDR Generated Successfully")

    st.markdown("## Generated DDR")
    st.write(ddr_report)

    st.markdown("## coldspot Thermal Readings (20.5°C - 20.9°C)")

    if relevant_temps:

        for t in relevant_temps:
            st.write(f"Temperature: {t}°C")

    else:
        st.write("No temperatures found in range 20.5°C - 20.9°C")

    st.markdown("## Relevant Thermal Images")

    if thermal_images:

        for img in thermal_images[:6]:
            st.image(
                img,
                caption="Supporting Thermal Evidence",
                width=400
            )

    else:
        st.write("Image Not Available")
