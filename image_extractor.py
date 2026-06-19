import fitz
import os
import re

def extract_images(
    pdf_path,
    output_folder="extracted_images"
):

    os.makedirs(output_folder, exist_ok=True)

    pdf = fitz.open(pdf_path)

    image_paths = []

    for page_index in range(len(pdf)):

        page = pdf[page_index]

        page_text = page.get_text()

        temps = re.findall(r"\d+\.\d+", page_text)

        temps = [float(t) for t in temps]

        relevant_page = any(
            20.5 <= temp <= 20.9
            for temp in temps
        )

        if relevant_page:

            images = page.get_images()

            for img_index, img in enumerate(images):

                xref = img[0]

                base_image = pdf.extract_image(xref)

                image_bytes = base_image["image"]

                image_path = os.path.join(
                    output_folder,
                    f"page_{page_index}_{img_index}.png"
                )

                with open(image_path, "wb") as f:
                    f.write(image_bytes)

                image_paths.append(image_path)

    return image_paths
