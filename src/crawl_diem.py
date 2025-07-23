import requests
import time
import csv
import os

os.makedirs("data", exist_ok = True)

CHECKPOINT_FILE = "data/last_index.txt"
CSV_FILE = "data/CrawledInHANOI.csv"

if not os.path.exists(CHECKPOINT_FILE):
    with open(CHECKPOINT_FILE, "w") as f:
        f.write("0")

def read_last_index():
    try:
        with open(CHECKPOINT_FILE, "r") as f:
            return int(f.read().strip())
    except:
        return 0

def save_last_index(index):
    with open(CHECKPOINT_FILE, "w") as f:
        f.write(str(index))

def tracudiem (sbd: str, nam: int = 2025):
    url = "https://s6.tuoitre.vn/api/diem-thi-thpt.htm"
    params = {
        "sbd": sbd,
        "year": nam
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36"
    }
    try:
        res = requests.get(url, params = params, headers = headers, timeout = 10)
        if res.status_code == 200:
            data = res.json()
            diem_thi = data["data"] [0] if data["data"] else {}
            output = {
                "SBD": diem_thi.get("SBD"),
                "TONGDIEM": diem_thi.get("TONGDIEM")
            }

            mon_thi = ["TOAN", "VAN", "NGOAI_NGU", 
                        "SU", "DIA", "GDKT_PL", 
                        "LI", "HOA", "SINH", 
                        "TIN_HOC", "GIAO_DUC_CONG_DAN", "CN_CONG_NGHIEP", 
                        "CN_NONG_NGHIEP", "NGAY_SINH"
                    ]

            for mon in mon_thi:
                diem = diem_thi.get(mon, -1)
                try:
                    diem = float(diem)
                    if diem >= 0: 
                        output[mon] = diem
                except:
                    pass
            return output if output["SBD"] else None
        else: 
            print(f"Lỗi HTTPS: {res.status_code}")
            return None
    except Exception as e:
        print('Không thể đọc dữ liệu', str(e))
        return None

file_CSV_exists = os.path.exists(CSV_FILE)
with open(CSV_FILE, mode = 'a', newline = '', encoding = "utf-8") as fileCrawled:
    fieldnames = [
        "SBD", "TONGDIEM",
        "TOAN", "VAN", "NGOAI_NGU", 
        "SU", "DIA", "GDKT_PL", 
        "LI", "HOA", "SINH", 
        "TIN_HOC", "GIAO_DUC_CONG_DAN", "CN_CONG_NGHIEP", 
        "CN_NONG_NGHIEP", "NGAY_SINH"
        ]
    writer = csv.DictWriter(fileCrawled, fieldnames = fieldnames)
    if not file_CSV_exists:
        writer.writeheader()
    Khong_co_diem = 0
    start_index = read_last_index()
    for i in range(start_index, 1000000):
        sbd = f"01{i:06d}"
        print(f"[Checkpoint {i}] Crawling {sbd}...")
        diem = tracudiem(sbd)
        if diem:
            writer.writerow(diem)
            print("✓", diem)
            Khong_co_diem = 0
        else:
            Khong_co_diem += 1
            print(f"[Checkpoint {i}] ✗ Không có dữ liệu {sbd}")
            if Khong_co_diem >= 300:
                print(f"Đã gặp trên {Khong_co_diem} thí sinh không có điểm")
                break

        save_last_index(i+1)
        time.sleep(0.3)