# Proyek Prediksi Tingkat Kebugaran

## Deskripsi
Proyek ini bertujuan untuk memprediksi tingkat kebugaran individu berdasarkan berbagai fitur yang terkait dengan kesehatan, seperti usia, BMI, detak jantung, kebiasaan latihan, dan lainnya. Model prediksi ini membantu menilai apakah seseorang termasuk dalam kategori "Pemula", "Menengah", atau "Lanjutan" berdasarkan tingkat kebugaran mereka, memberikan wawasan yang berharga mengenai kesehatan dan kebugaran mereka. Model ini dibangun menggunakan *decision tree classifier*, yang dilatih dengan dataset yang berisi atribut-atribut yang terkait dengan kesehatan dan kebugaran.

## Gambaran Umum Proyek
Tujuan dari proyek ini adalah untuk membuat model prediktif yang dapat mengklasifikasikan tingkat kebugaran individu berdasarkan data input mereka. Proyek ini terdiri dari beberapa tahapan:
1. **Analisis Dataset**: Mengeksplorasi dan memahami dataset, diikuti dengan rekayasa fitur.
2. **Pemodelan**: Melatih model *decision tree* untuk memprediksi tingkat kebugaran.
3. **Evaluasi Model**: Menilai performa model menggunakan berbagai metrik.
4. **Diskusi dan Kesimpulan**: Menganalisis hasil dan memberikan rekomendasi untuk perbaikan.

## Langkah-langkah yang Dilakukan
1. **Pengumpulan Data**: Dataset ini berisi atribut kunci seperti usia, berat badan, tinggi badan, detak jantung maksimum dan rata-rata, kebiasaan latihan, kalori yang terbakar, dan lainnya.
2. **Eksplorasi Data (EDA)**: Melakukan eksplorasi awal pada data untuk memahami hubungan antar fitur dan pengaruhnya terhadap tingkat kebugaran.
3. **Rekayasa Fitur**: Memproses data dan membuat fitur-fitur yang bermakna untuk model.
4. **Pelatihan Model**: Mengimplementasikan dan melatih model *decision tree* pada data yang telah diproses.
5. **Evaluasi**: Menguji akurasi dan performa model, menggunakan metrik seperti akurasi dan matriks kebingungannya.
6. **Kesimpulan**: Membahas hasil yang diperoleh, termasuk performa model dan area untuk perbaikan lebih lanjut.

## Struktur Proyek
- **data**: Berisi dataset mentah dan dataset yang telah dibersihkan untuk pelatihan.
- **notebooks**: Jupyter notebook untuk EDA, pemrosesan data, dan pelatihan model.
- **models**: Berisi model yang telah dilatih dan daftar fitur.
- **app.py**: Aplikasi Streamlit untuk memprediksi tingkat kebugaran berdasarkan input pengguna.

## Persyaratan
- Python 3.x
- Libraries: pandas, scikit-learn, streamlit, joblib, matplotlib, seaborn

## Cara Menjalankan
1. Clone repository ini.
2. Instal dependensi yang diperlukan:
    ```bash
    pip install -r requirements.txt
    ```
3. Jalankan aplikasi Streamlit:
    ```bash
    streamlit run app.py
    ```

