
import unittest
import tempfile
from pathlib import Path

from pdf_image_extractor.extractor import (
    extract_images_from_pdf,
    PDFValidationError
)


class TestPDFExtractor(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_pdf_not_found(self):
        pdf = self.folder / "missing.pdf"

        with self.assertRaises(PDFValidationError):
            extract_images_from_pdf(
                pdf,
                self.folder / "output"
            )

    def test_wrong_file_extension(self):
        file = self.folder / "document.txt"
        file.write_text("Hello World")

        with self.assertRaises(PDFValidationError):
            extract_images_from_pdf(
                file,
                self.folder / "output"
            )

    def test_output_folder_created(self):
        output = self.folder / "images"

        output.mkdir(parents=True, exist_ok=True)

        self.assertTrue(output.exists())
        self.assertTrue(output.is_dir())


if __name__ == "__main__":
    unittest.main(verbosity=2)
