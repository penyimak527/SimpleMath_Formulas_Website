# Simple Math Formulas Website ✨

Website interaktif berbasis Streamlit untuk menghitung rumus-rumus matematika sederhana seperti luas dan keliling segitiga, serta rumus lainnya. Repository ini berisi kode Python untuk aplikasi web. **Penggunaan proyek ini memerlukan izin terlebih dahulu dari pencipta**. 📝

---

## Fitur 📋

- ✅ Hitung luas dan keliling segitiga (`segita.py`)
- ✅ Hitung luas lingkaran tahunan (`bungatunggal`)
- ⏳ (Fitur tambahan akan dikembangkan)

---

## Persyarat 🛠️

- Python 3.7 atau lebih baru
- Streamlit (`pip install streamlit`)
- Web browser (Chrome, Firefox, dll.)

---

## Instalasi 🚀

### 1. Clone Repository

```bash
https://github.com/penyimak527/SimpleMath_Formulas_Website.git
```

### 2. Masuk ke Direktori

```bash
cd simple-math-formulas
```

### 3. Instal Dependensi

```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi

- Jalankan Streamlit:

```bash
streamlit run streamlit
```

- Buka http://localhost:8501 di browser.

---

## Struktur Folder 📂

```
simple-math-formulas/
├── streamlit            # File utama untuk menjalankan aplikasi
├── config.toml          # Konfigurasi Streamlit
├── pages/               # Halaman tambahan untuk rumus
├── dashboard.py         # (Opsional) Dashboard utama
├── Profilefile          # (Opsional) File profil atau info tambahan
├── requirements.txt     # Daftar dependensi Python
├── README.md            # Panduan ini
```

---

## Cara Penggunaan 🖱️

1. **Buka Website**: Jalankan aplikasi dan akses di browser.
2. **Pilih Rumus**: Navigasi ke halaman seperti `segita`, `bungatunggaltahunan`.
3. **Masukkan Data**: Isi nilai seperti panjang sisi atau jari-jari.
4. **Hitung**: Klik tombol "Hitung" untuk melihat hasil.

---

## Pengembangan Tambahan 🌱

Proyek ini dapat dikembangkan lebih lanjut. Ide:

- Tambahkan rumus baru (misalnya luas persegi) di file baru di folder `pages/`.
- Tingkatkan UI dengan tema kustom di `config.toml`.
- Tambahkan validasi input di setiap halaman.

Contoh tambahan di `pages/persegi.py`:

```python
import streamlit as st

st.title("Rumus Persegi")
sisi = st.number_input("Masukkan panjang sisi", min_value=0.0)
luas = sisi * sisi
st.write(f"Luas persegi: {luas}")
```

---

## Teknologi 💻

- **Frontend**: Streamlit
- **Backend**: Python

---

## Lisensi 📜

MIT License\
**Harus izin terlebih dahulu jika ingin menggunakan untuk publik.**


