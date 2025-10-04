# Simple Math Formulas Website ✨

Website interaktif berbasis Streamlit untuk menghitung rumus-rumus matematika sederhana seperti luas dan keliling segitiga, dengan potensi pengembangan untuk rumus lain. Repository ini berisi kode Python untuk aplikasi web. **Penggunaan proyek ini memerlukan izin terlebih dahulu dari pencipta**. 📝

---

## Fitur 📋

- ✅ Hitung luas segitiga
- ✅ Hitung keliling segitiga
- ✅ Tampilan interaktif dengan input pengguna
- ⏳ (Fitur tambahan seperti luas persegi, lingkaran, dll. akan dikembangkan)

---

## Prasyarat 🛠️

- Python 3.7 atau lebih baru
- [Streamlit](https://streamlit.io/) (`pip install streamlit`)
- [NumPy](https://numpy.org/) (`pip install numpy`) untuk perhitungan numerik
- Web browser (Chrome, Firefox, dll.)

---

## Instalasi 🚀

### 1. Clone Repository

```bash
git clone https://github.com/username/simple-math-formulas.git
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
streamlit run app.py
```

- Buka [http://localhost:8501](http://localhost:8501) di browser.

---

## Struktur Folder 📂

```
simple-math-formulas/
├── app.py              # File utama Streamlit untuk aplikasi
├── requirements.txt    # Daftar dependensi Python
├── data/               # (Opsional) Direktori untuk data tambahan
├── utils/              # (Opsional) Fungsi bantu untuk perhitungan
├── README.md           # Panduan ini
```

---

## Cara Penggunaan 🖱️

1. **Buka Website**: Jalankan aplikasi dan akses di browser.
2. **Masukkan Data**: Isi nilai seperti panjang sisi segitiga di form yang disediakan.
3. **Hitung**: Klik tombol "Hitung" untuk melihat hasil luas atau keliling.
4. **Eksplorasi**: Tambahkan input baru untuk mengembangkan rumus lain.

---

## Pengembangan Tambahan 🌱

Proyek ini dirancang untuk dikembangkan lebih lanjut. Berikut ide dan langkah untuk menambahkan fitur:

- **Rumus Baru**: Tambahkan perhitungan seperti luas persegi (`luas = sisi * sisi`) atau luas lingkaran (`luas = π * r²`).
- **Visualisasi**: Gunakan library seperti `matplotlib` untuk menampilkan grafik.
- **Input Validasi**: Tambahkan pengecekan input untuk memastikan nilai positif.
- Edit `app.py` untuk menambahkan fungsi baru, lalu perbarui `requirements.txt` jika ada dependensi baru.

Contoh tambahan di `app.py`:

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
- **Perhitungan**: NumPy (opsional)
- **Visualisasi**: (Opsional, tambahkan matplotlib jika diperlukan)

---

## Kontribusi 🤝

Penggunaan untuk tujuan pribadi atau publik membutuhkan izin dari pencipta. Untuk kontribusi:

1. Fork repository.
2. Buat branch:

```bash
git checkout -b fitur-baru
```

3. Commit perubahan:

```bash
git commit -m "Tambah fitur baru"
```

4. Push branch:

```bash
git push origin fitur-baru
```

5. Buat Pull Request setelah mendapatkan izin.

---

## Lisensi 📜

[MIT License](LICENSE)  
**Harus izin terlebih dahulu jika ingin menggunakan untuk publik.**

---
