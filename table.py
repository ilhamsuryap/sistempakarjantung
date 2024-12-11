from PIL import Image, ImageDraw, ImageFont

# Ukuran gambar
image_width, image_height = 800, 1300
cell_width, cell_height = 100, 40
header_height = 60

# Warna
background_color = "white"
line_color = "black"
header_color = "#add8e6"  # Warna biru muda


# Data untuk tabel
symptoms = [
    "P001", "P002", "P003", "P004", "P005", "P006", "P007", "P008",
    "P009", "P010", "P011", "P012", "P013", "P014", "P015", "P016",
    "P017", "P018", "P019", "P020", "P021", "P022", "P023", "P024"
]
diagnoses = ["R01", "R02", "R03", "R04", "R05", "R06", "R07"]

# Aturan gejala untuk setiap rule
rule_mapping = {
    "R01": ["P001", "P002", "P003", "P004", "P005", "P006", "P007", "P022", "P023"],
    "R02": ["P004", "P008", "P009", "P010", "P011", "P007"],
    "R03": ["P012", "P013", "P014", "P022", "P024"],
    "R04": ["P004", "P015", "P016"],
    "R05": ["P024", "P017", "P008", "P018", "P011"],
    "R06": ["P011", "P010", "P004", "P019", "P009"],
    "R07": ["P020", "P007", "P021", "P022"]
}

# Buat gambar kosong
img = Image.new("RGB", (image_width, image_height), background_color)
draw = ImageDraw.Draw(img)

# Font untuk teks
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
font = ImageFont.truetype(font_path, 18)

# Header
draw.rectangle([(0, 0), (image_width, header_height)], fill=header_color, outline=line_color)
draw.text((10, 15), "Tabel Keputusan Penyakit Jantung", fill=line_color, font=font)

# Header kolom
for i, diagnosis in enumerate(diagnoses):
    x0 = (i + 1) * cell_width
    draw.rectangle([(x0, header_height), (x0 + cell_width, header_height + cell_height)], fill=header_color, outline=line_color)
    draw.text((x0 + 10, header_height + 10), diagnosis, fill=line_color, font=font)

# Baris gejala dan data
for i, symptom in enumerate(symptoms):
    y0 = header_height + (i + 1) * cell_height
    # Gejala kolom
    draw.rectangle([(0, y0), (cell_width, y0 + cell_height)], fill=header_color, outline=line_color)
    draw.text((10, y0 + 10), symptom, fill=line_color, font=font)
    # Data rule
    for j, diagnosis in enumerate(diagnoses):
        x0 = (j + 1) * cell_width
        draw.rectangle([(x0, y0), (x0 + cell_width, y0 + cell_height)], outline=line_color)
        if symptom in rule_mapping[diagnosis]:
            draw.text((x0 + 35, y0 + 10), "X", fill=line_color, font=font)

# Simpan gambar
image_path = "D:\KULIAH\SEMESTER 3\SISTEM CERDAS\pertemuan 15\praktikum\tabel_keputusan_jansstung.png"
img.save(image_path)
image_path
