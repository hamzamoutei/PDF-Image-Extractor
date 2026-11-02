from __future__ import annotations

import argparse
from pathlib import Path

from .extractor import PDFValidationError, extract_images_from_pdf


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pdf-image-extractor",
        description="Extract embedded images from a PDF file.",
    )
    parser.add_argument("pdf", nargs="?", help="Path to the PDF file")
    parser.add_argument(
        "-o", "--output",
        help="Folder where extracted images will be saved",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    pdf_path = args.pdf or input("PDF file path (or 'q' to quit): ").strip()
    if pdf_path.lower() in {"q", "quit", "quitter"}:
        print("Program ended.")
        return 0

    output_dir = args.output or input(
        "Output folder (default: extracted_images): "
    ).strip()
    if not output_dir:
        output_dir = "extracted_images"

    try:
        result = extract_images_from_pdf(pdf_path, output_dir)
    except (PDFValidationError, OSError) as exc:
        print(f"Error: {exc}")
        return 1

    print(f"Done! {result.images_saved} image(s) extracted.")
    print(f"Pages scanned: {result.pages_scanned}")
    print(f"Output folder: {result.output_dir.resolve()}")
    if result.images_saved == 0:
        print("No embedded images were found in this PDF.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
