
# PDF Image Extractor

Ein Python-Projekt zum Extrahieren von Bildern aus PDF-Dateien.

## Funktionen

- PDF-Dateien öffnen und analysieren.
- Alle Seiten einer PDF-Datei durchsuchen.
- Eingebettete Bilder extrahieren.
- Bilder einzeln speichern.
- Automatische Erstellung des Ausgabeordners.
- Anzeige der Anzahl extrahierter Bilder.
- Automatisierte Unit-Tests mit unittest.

## Voraussetzungen

- Python 3.9 oder höher
- pip

## Installation

Installiere die benötigte Bibliothek:

```bash
python -m pip install -r requirements.txt
```

## Verwendung

Starte das Programm:

```bash
python -m pdf_image_extractor
```

Gib anschließend den Pfad zur PDF-Datei ein.

Danach gib den Namen des Ausgabeordners ein.

### Alternative: Direkter Start

```bash
python -m pdf_image_extractor "beispiel.pdf" -o "bilder"
```

## Beispiel

Nach der Extraktion können die Dateien so aussehen:

```text
bilder/
├── page_1_image_1.png
├── page_1_image_2.jpeg
└── page_2_image_1.png
```

## Unit-Tests

Das Projekt verwendet das integrierte Python-Modul unittest.

Tests starten:

```bash
python -m unittest discover -s tests -v
```

## Projektstruktur

```text
pdf_image_extractor/
├── src/
│   └── pdf_image_extractor/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       └── extractor.py
├── tests/
│   └── test_extractor.py
├── README.md
├── requirements.txt
├── pyproject.toml
└── LICENSE
```

## Verwendete Technologien

- Python
- PyMuPDF
- unittest

## Hinweis

Das Programm extrahiert eingebettete Rasterbilder aus PDF-Dateien. Vektorgrafiken werden nicht automatisch als Bilder gespeichert.

## Lizenz

MIT License
