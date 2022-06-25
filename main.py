import os
from fpdf import FPDF

Bänder = os.listdir("Mangas")
for band in Bänder:
    Dir = f'Mangas/{band}'
    for Band in os.listdir(Dir):
        pdf = FPDF()
        images = []
        print(f"start: {f'Mangas/{band}'}")
        if os.path.isdir(f'Mangas/{band}'):
            for DATA in os.listdir(f"Mangas/{band}/{Band}"):
                if os.path.isdir(f"Mangas/{band}/{Band}/" + DATA):
                    F_DIR = os.listdir(f"Mangas/{band}/{Band}/" + DATA)
                else:
                    F_DIR = os.listdir(f"Mangas/{band}/{Band}")
                for img in F_DIR:
                    file = f"Mangas/{band}/{Band}/{DATA}/{img}"
                    if file.endswith(".png"):
                        images.append(file)
            print(f'Images Collect: {images}')
            for data in images:
                pdf.add_page()
                pdf.image(data, 0, 0,  210, 297)
            pdf.output(f"Mangas/{band}/{band}-{Band}.pdf", "F")
            print(f'{band}-{Band} saved in: {f"Mangas/{band}/{band}-{Band}.pdf"}')