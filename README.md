# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya jaya

## 📌 Business Understanding
Perusahaan Jaya jaya bergerak di bidang teknologi pendidikan, dengan fokus pada pengembangan platform e-learning untuk meningkatkan kualitas pembelajaran digital. Namun, perusahaan menghadapi tantangan dalam mempertahankan tenaga kerja mereka, terutama di divisi Research & Development (R&D), Sales, dan Human Resources (HR).

## 🚨 Permasalahan Bisnis
- Tingkat attrition yang tinggi di beberapa departemen, terutama R&D, Sales, dan HR.
- Gaji rendah diduga menjadi salah satu faktor utama karyawan meninggalkan perusahaan.
- Jam kerja lembur yang tinggi berkorelasi dengan tingkat keluar karyawan.
- Kepuasan kerja yang bervariasi antar departemen, dengan HR memiliki jumlah karyawan yang sangat sedikit dibandingkan kebutuhan perusahaan.

## 📍 Cakupan Proyek
- Menganalisis faktor-faktor yang memengaruhi tingkat attrition karyawan.
- Menyusun dashboard interaktif untuk memberikan insight tentang tren attrition, pengaruh gaji, jam kerja lembur, dan kepuasan kerja.
- Memberikan rekomendasi strategis berdasarkan data untuk meningkatkan retensi karyawan.

## 📂 Persiapan
### Sumber Data
* https://www.ibm.com/communities/analytics/watson-analytics-blog/watson-analytics-use-case-for-hr-retaining-valuable-employees/


### Setup Environment
1️⃣ **Buat dan Aktifkan Virtual Environment**<br>
   **Windows:**<br>
   `uv venv .venv`<br>
   `.venv\Scripts\activate`<br>
* source `.venv/bin/activate`<br>
2️⃣ **Install Dependensi yang Dibutuhkan**<br>
   `uv pip install pandas matplotlib seaborn scikit-learn joblib`<br>
3️⃣ **Generate requirements.txt**<br>
    `uv pip freeze > requirements.txt`
## 📊 Business Dashboard
Dashboard ini dirancang untuk memberikan insight mendalam mengenai tren attrition karyawan di perusahaan Edutech.

### Komponen Utama dalam Dashboard
* link Access Dashboard => https://public.tableau.com/views/employeedata_17396347287900/DashboardEmployee?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link 
1. **Attrition & Salary Trends** – Menganalisis hubungan antara pendapatan bulanan dan tingkat keluar karyawan.
2. **Over Time vs Attrition** – Menunjukkan dampak jam kerja lembur terhadap attrition.
3. **Job Satisfaction** – Memetakan tingkat kepuasan kerja di setiap departemen.
4. **Attrition Overview** – Mengidentifikasi departemen dengan tingkat keluar tertinggi.

## 📌 Conclusion
- Departemen R&D memiliki tingkat attrition tertinggi, menunjukkan adanya masalah dalam lingkungan kerja atau kebijakan perusahaan.
- Karyawan dengan gaji rendah lebih rentan keluar, sehingga perusahaan perlu mempertimbangkan kebijakan kenaikan gaji atau insentif tambahan.
- Lembur yang tinggi berkorelasi dengan tingkat keluar karyawan, menandakan perlunya kebijakan work-life balance yang lebih baik.
- Jumlah staf HR sangat sedikit dibandingkan kebutuhan perusahaan, yang dapat berdampak pada rendahnya kepuasan kerja dan efisiensi dalam menangani karyawan.

## 🚀 Rekomendasi Action Items
- Tinjau ulang kebijakan gaji dan kompensasi untuk meningkatkan retensi karyawan.
- Kurangi jam kerja lembur dan berikan kebijakan fleksibilitas waktu kerja.
- Evaluasi lingkungan kerja di departemen R&D melalui survei karyawan dan wawancara exit interview.
- Tambahkan tenaga kerja di divisi HR agar dapat menangani kebutuhan karyawan dengan lebih efektif.