import fitz
import os

def extract_images(pdf_path, output_folder):

    os.makedirs(output_folder, exist_ok=True)

    pdf = fitz.open(pdf_path)

    image_paths = []

    for page_index in range(len(pdf)):

        page = pdf[page_index]

        images = page.get_images()

        for img_index, img in enumerate(images):

            xref = img[0]

            base_image = pdf.extract_image(xref)

            image_bytes = base_image["image"]

            image_path = (
                f"{output_folder}/"
                f"page_{page_index}_{img_index}.png"
            )

            with open(image_path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(image_path)

    return image_paths