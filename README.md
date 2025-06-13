# CareerCompass

CareerCompass adalah sistem yang dirancang untuk membantu pencari kerja menemukan pekerjaan yang sesuai dengan keterampilan dan pengalaman mereka. Proyek ini terdiri dari tiga bagian utama:

- **Frontend**: Antarmuka pengguna yang dibangun dengan React.
- **Backend**: API yang dibangun dengan Node.js dan Express.
- **Machine Learning**: Model yang digunakan untuk memberikan rekomendasi pekerjaan berdasarkan CV pengguna.

## Struktur Proyek
CareerCompass/
  │ ├── frontend/
  │ ├── backend/
  │ └── machine_learning/


## Persyaratan

Sebelum memulai, pastikan Anda memiliki:
- [Node.js](https://nodejs.org/) dan npm (package manager untuk Node.js)
- [Python](https://www.python.org/downloads/) untuk bagian machine learning
- [pip](https://pip.pypa.io/en/stable/) untuk mengelola paket Python

## Instalasi

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan aplikasi:

### 1. Clone Repository

Buka terminal dan jalankan perintah berikut untuk meng-clone repository ini:

```bash
git clone https://github.com/SitiNurbayanah/CareerCompass.git
```

2. Instalasi Frontend
Masuk ke direktori frontend dan instal dependensi:

```bash
cd frontend
npm install
```

3. Instalasi Backend
Masuk ke direktori backend dan instal dependensi:

```bash
cd ../backend
npm install
```

4. Instalasi Machine Learning
Masuk ke direktori machine_learning dan instal dependensi:

```bash
cd ../machine_learning
pip install -r requirements.txt
```

### 2. Menjalankan Aplikasi

1. Menjalankan Backend
Kembali ke direktori backend dan jalankan server:

```bash
cd ../backend
node server.js
```

2. Menjalankan Frontend
Kembali ke direktori frontend dan jalankan aplikasi:

```bash
cd ../frontend
npm start
```

3. Menjalankan Preprocessing dan Modeling Machine Learning
Jalankan model machine learning sesuai dengan instruksi yang ada di dalam direktori machine_learning.

4. Menjalankan API Machine Learning
Masuk ke direktori ML_Deployment.

```bash
cd ../../ML_Deployment
python app.py
```

---
Dibuat dengan ❤️ oleh Tim CC25-CF288
