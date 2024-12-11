import streamlit as st

# Data gejala yang dapat dipilih oleh pengguna
symptoms_data = {
    'P001': 'P001 : Nyeri dada',
    'P002': 'P002 : Bahu kiri terasa tidak enak',
    'P003': 'P003 : Keringat dingin',
    'P004': 'P004 : Sesak nafas',
    'P005': 'P005 : Gangguan pencernaan',
    'P006': 'P006 : Mual',
    'P007': 'P007 : Detak jantung tidak teratur',
    'P008': 'P008 : Pusing',
    'P009': 'P009 : Kaki bengkak',
    'P010': 'P010 : Jantung berdebar-debar',
    'P011': 'P011 : Mudah lelah',
    'P012': 'P012 : Nyeri di daerah dada tengah',
    'P013': 'P013 : Mudah berkeringat',
    'P014': 'P014 : Dada mengeluarkan',
    'P015': 'P015 : Pembengkakan pada jantung',
    'P016': 'P016 : Kelainan fungsi jantung',
    'P017': 'P017 : Pendarahan dari hidung',
    'P018': 'P018 : Wajah kemerah-merahan',
    'P019': 'P019 : Batuk',
    'P020': 'P020 : Sakit perut',
    'P021': 'P021 : Detak jantung cepat',
    'P022': 'P022 : Nyeri di daerah lengan kiri',
    'P023': 'P023 : Punggung terasa tidak enak',
    'P024': 'P024 : Sakit Kepala'
}

# Data diagnosis berdasarkan aturan yang ada
diagnosis_data = {
    'R01': 'Penyakit Jantung Koroner',
    'R02': 'Penyakit Otot Jantung (Kardiomiopati)',
    'R03': 'Penyakit Jantung Iskemik',
    'R04': 'Gagal Jantung',
    'R05': 'Penyakit Jantung Hipertensi',
    'R06': 'Penyakit Katup Jantung',
    'R07': 'Kardiomegali atau Hipertrofi'
}

# Aturan gejala yang digunakan untuk mendiagnosis penyakit
rule_data = {
    'R01': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P023', 'P024'],
    'R02': ['P004', 'P007', 'P008', 'P009', 'P010', 'P011'],
    'R03': ['P012', 'P013', 'P014', 'P022'],
    'R04': ['P004', 'P015', 'P016'],
    'R05': ['P008', 'P011', 'P008', 'P017', 'P018'],
    'R06': ['P001', 'P004', 'P009', 'P010', 'P011', 'P019'],
    'R07': ['P001', 'P007', 'P020', 'P021']
}

# Fungsi untuk melakukan diagnosis berdasarkan gejala yang dipilih
def diagnose_heart_disease(selected_symptoms):
    # Memeriksa setiap aturan dan mencocokkan gejala dengan diagnosis yang sesuai
    for rule, symptoms in rule_data.items():
        if all(symptom in selected_symptoms for symptom in symptoms):  # jika semua gejala cocok
            return diagnosis_data[rule]  # kembalikan diagnosis yang sesuai
    return "Tidak ada diagnosis yang sesuai"  # jika tidak ada aturan yang cocok

# Fungsi untuk halaman Beranda aplikasi
def home_page():
    st.title("Selamat datang di Sistem Pakar Deteksi Penyakit Jantung")
    st.write("Aplikasi ini membantu mendiagnosa penyakit jantung berdasarkan gejala-gejala yang dialami.")
    st.image("logo.png", width=800)  # Menampilkan logo aplikasi

# Fungsi untuk Sistem Pakar Jantung
def heart_disease_system():
    st.title("Sistem Pakar Deteksi Awal Penyakit Jantung")
    st.write("Silakan pilih gejala-gejala yang Anda alami dari daftar berikut:")

    # Menampilkan gambar tabel keputusan dengan ukuran lebih kecil
    st.image("tabelkeputusan.png", caption="Tabel Keputusan Penyakit Jantung", width=400)

    # Inisialisasi status checkbox di session_state jika belum ada
    if 'selected_symptoms' not in st.session_state:
        st.session_state.selected_symptoms = []  # Menyimpan gejala yang dipilih di session_state

    # Checkbox untuk memilih gejala
    for symptom, label in symptoms_data.items():
        if symptom in st.session_state.selected_symptoms:
            checked = True  # Jika gejala sudah dipilih, centang checkbox
        else:
            checked = False  # Jika gejala belum dipilih, biarkan tidak dicentang

        if st.checkbox(label, value=checked, key=symptom):
            if symptom not in st.session_state.selected_symptoms:
                st.session_state.selected_symptoms.append(symptom)  # Menambahkan gejala yang dipilih
        else:
            if symptom in st.session_state.selected_symptoms:
                st.session_state.selected_symptoms.remove(symptom)  # Menghapus gejala yang tidak dipilih

    # Tombol diagnosis
    if st.button("Diagnosa"):
        if st.session_state.selected_symptoms:
            result = diagnose_heart_disease(st.session_state.selected_symptoms)  # Memanggil fungsi diagnosis
            st.success(f"Hasil diagnosis: {result}")  # Menampilkan hasil diagnosis
        else:
            st.warning("Silakan pilih minimal satu gejala sebelum melanjutkan.")  # Peringatan jika tidak ada gejala yang dipilih

    # Fitur reset
    if st.button("Reset"): 
        # Menghapus status checkbox dengan cara lebih sederhana
        st.session_state.selected_symptoms.clear()
        
        # Menampilkan pesan reset
        st.success("Semua gejala telah direset!")

# Fungsi untuk halaman Tentang Aplikasi
def about_page():
    st.title("Tentang Aplikasi")
    st.write("""
        Aplikasi ini dikembangkan untuk membantu deteksi dini penyakit jantung berdasarkan gejala-gejala yang muncul pada pasien. 
        Sistem ini menggunakan basis data gejala dan diagnosis yang telah ditentukan sebelumnya. 
        Aplikasi ini cocok digunakan untuk memberikan indikasi awal mengenai penyakit jantung.
    """)
    st.write("""
        Aplikasi ini menggunakan pendekatan **forward** dalam proses diagnosa. Pengguna memilih gejala-gejala yang mereka alami, 
        dan sistem akan mendiagnosis kemungkinan penyakit jantung berdasarkan gejala yang dipilih. 
        Dengan kata lain, aplikasi ini mengalir maju dari pemilihan gejala menuju diagnosis, tanpa memerlukan penelusuran kembali atau pengujian terhadap gejala yang tidak dipilih.
    """)
    st.write("""
        **Cara Kerja Aplikasi**:
        
        1. **Pemilihan Gejala**: Pengguna akan melihat daftar gejala yang umum terjadi pada penyakit jantung. Pengguna dapat memilih gejala-gejala yang mereka alami melalui checkbox.
        2. **Proses Diagnosa**: Setelah memilih gejala, pengguna menekan tombol "Diagnosa". Sistem akan memproses gejala yang dipilih dan membandingkannya dengan aturan yang telah ditentukan dalam basis data aplikasi.
        3. **Hasil Diagnosis**: Berdasarkan gejala yang dipilih, aplikasi akan memberikan diagnosis penyakit jantung yang sesuai. Jika tidak ada kecocokan, aplikasi akan memberikan hasil "Tidak ada diagnosis yang sesuai".
        4. **Fitur Reset**: Pengguna dapat mengklik tombol "Reset" untuk menghapus pilihan gejala yang telah dipilih, dan memulai kembali proses diagnosis dari awal.
    """)

# Main navigation with page selection
# Pilihan menu halaman yang dapat dipilih di sidebar
page = st.sidebar.selectbox("Pilih menu:", ["Beranda", "Sistem Pakar Jantung", "Tentang Aplikasi"])

# Menampilkan halaman berdasarkan pilihan
if page == "Beranda":
    home_page()  # Menampilkan halaman beranda
elif page == "Sistem Pakar Jantung":
    heart_disease_system()  # Menampilkan sistem pakar untuk diagnosa penyakit jantung
elif page == "Tentang Aplikasi":
    about_page()  # Menampilkan halaman tentang aplikasi
