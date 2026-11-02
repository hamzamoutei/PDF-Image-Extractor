from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import fitz  # PyMuPDF


@dataclass
class ExtractionResult:
    """Summary returned after extracting images from a PDF."""

    pdf_path: Path
    output_dir: Path
    images_saved: int
    pages_scanned: int


class PDFValidationError(ValueError):
    """Raised when the input PDF path is invalid or unreadable."""


def extract_images_from_pdf(
    pdf_path: str | Path,
    output_folder: str | Path,
) -> ExtractionResult:
    """
    Extract embedded raster images from a PDF and save them to output_folder.

    Each saved image is named page_<page>_image_<number>.<extension>.
    Images are extracted as stored in the PDF; vector drawings and scanned
    page backgrounds are not converted into separate images.
    """
    pdf_path = Path(pdf_path).expanduser()
    output_dir = Path(output_folder).expanduser()

    if not pdf_path.exists():
        raise PDFValidationError(f"PDF file does not exist: {pdf_path}")
    if not pdf_path.is_file():
        raise PDFValidationError(f"PDF path is not a file: {pdf_path}")
    if pdf_path.suffix.lower() != ".pdf":
        raise PDFValidationError("The input file must have a .pdf extension.")

    try:
        document = fitz.open(pdf_path)
    except (fitz.FileDataError, RuntimeError) as exc:
        raise PDFValidationError(f"Could not open this PDF: {exc}") from exc

    saved = 0
    pages = len(document)
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        for page_number, page in enumerate(document, start=1):
            images = page.get_images(full=True)

            for image_number, image_info in enumerate(images, start=1):
                xref = image_info[0]
                image_data = document.extract_image(xref)

                if not image_data or not image_data.get("image"):
                    continue

                extension = image_data.get("ext", "bin")
                image_bytes = image_data["image"]
                output_path = (
                    output_dir
                    / f"page_{page_number}_image_{image_number}.{extension}"
                )
                output_path.write_bytes(image_bytes)
                saved += 1
    finally:
        document.close()

    return ExtractionResult(
        pdf_path=pdf_path,
        output_dir=output_dir,
        images_saved=saved,
        pages_scanned=pages,
    )
