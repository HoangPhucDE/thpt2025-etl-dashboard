# thpt2025-etl-dashboard
ETL pipeline to crawl, clean, analyze, and visualize the Vietnam National High School Exam scores (THPT 2025). Includes dashboard and insights by region, subject, and exam group.

# 📊 THPT 2025 ETL Dashboard

Dự án thu thập, xử lý và trực quan hóa dữ liệu điểm thi THPT Quốc gia năm 2025 từ Bộ Giáo dục và Đào tạo Việt Nam.  
Dự án được triển khai theo mô hình **ETL pipeline hoàn chỉnh**, từ crawling dữ liệu đến xây dựng dashboard phân tích.

---

## 🎯 Mục tiêu dự án

- Thu thập dữ liệu điểm thi từ website Bộ GD&ĐT
- Làm sạch và chuẩn hóa dữ liệu
- Phân tích phổ điểm, điểm trung bình, top tỉnh/thành, khối thi
- Hiển thị dữ liệu trực quan bằng **Streamlit Dashboard**

---

## 🏗️ Kiến trúc pipeline

[Crawl dữ liệu] 
      ↓
[Làm sạch & chuẩn hóa] 
      ↓
[Lưu trữ (CSV / SQLite)] 
      ↓
[Phân tích & thống kê] 
      ↓
[Dashboard trực quan (Streamlit)]

---

## ⚙️ Công nghệ sử dụng

| Giai đoạn         | Công cụ / Thư viện                             |
|------------------|-------------------------------------------------|
| Crawl dữ liệu     | `requests`, `BeautifulSoup`, `selenium`        |
| Xử lý dữ liệu     | `pandas`, `re`, `unicodedata`                  |
| Lưu trữ           | `CSV`, `SQLite`     |
| Trực quan hóa     | `Streamlit`, `matplotlib`, `seaborn`, `plotly` |
| Quản lý dự án     | `Git`, `GitHub`                                |

---

📁 Cấu trúc thư mục

thpt2025-etl-dashboard/
│
├── data/                 # Dữ liệu thô và dữ liệu đã xử lý (CSV)
│
├── src/                  # Mã nguồn chính cho ETL pipeline
│   ├── crawl_diem.py         # Thu thập dữ liệu
│   ├── clean_dulieu.py       # Làm sạch và chuẩn hóa
│   ├── analyze.py            # Phân tích dữ liệu
│   └── utils.py              # Các hàm hỗ trợ
│
├── dashboard/            # Ứng dụng dashboard Streamlit
│   └── dashboard.py
│
├── docs/                 # Hình ảnh, tài liệu mô tả, kết quả
│
├── main.py               # Chạy toàn bộ pipeline ETL
├── requirements.txt      # Danh sách thư viện cần cài đặt
├── .gitignore
└── README.md

git clone https://github.com/<your-username>/thpt2025-etl-dashboard.git
cd thpt2025-etl-dashboard
