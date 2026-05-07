import fitz  # PyMuPDF
import os

PDF_PATH = r"Mephisto Waltz No.1, S.514 (Liszt, Franz).pdf"
OUTPUT_DIR = "mephisto_pages"
DPI = 200  # Higher = clearer image, larger file. 200 is good for sheet music.

os.makedirs(OUTPUT_DIR, exist_ok=True)

doc = fitz.open(PDF_PATH)
print(f"Total pages: {len(doc)}")

for i, page in enumerate(doc):
    mat = fitz.Matrix(DPI / 72, DPI / 72)
    pix = page.get_pixmap(matrix=mat, colorspace=fitz.csGRAY)
    out_path = os.path.join(OUTPUT_DIR, f"page_{i+1:03d}.png")
    pix.save(out_path)
    print(f"Saved: {out_path}")

doc.close()
print("Done.")
