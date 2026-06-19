from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

def create_pdf(
        report_text,
        output_path="DDR_Report.pdf"
):

    doc = SimpleDocTemplate(output_path)

    styles = getSampleStyleSheet()

    content = []

    for line in report_text.split("\n"):

        content.append(
            Paragraph(line, styles["BodyText"])
        )

        content.append(
            Spacer(1, 5)
        )

    doc.build(content)

    return output_path