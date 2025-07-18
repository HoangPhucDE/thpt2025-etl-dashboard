import requests
import time
import csv

def tracudiem (sbd: str, nam: int = 2025):
    url = "https://s6.tuoitre.vn/api/diem-thi-thpt.htm"
    params = {
        "sbd": sbd,
        "year": nam
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36"
    }
    res = requests.get(url, params = params, headers = headers)
    if res.status_code == 200:
        try:
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
                        "CN_NONG_NGHIEP", "NGAY_SINH"]
            for mon in mon_thi:
                diem = diem_thi.get(mon, -1)
                try:
                    diem = float(diem)
                    if diem >= 0: 
                        output[mon] = diem
                except:
                    pass
            return output
        except Exception as e:
            print('Không thể đọc dữ liệu'), str(e)
            return None
    else: 
        print(f"Lỗi HTTPS: {res.status_code}")
        return None

with open("data/crawledAtHaNoi.csv", mode = 'w', newline = '', encoding = "utf-8") as fileCrawled:
    fieldnames = [
        "SBD", "TONGDIEM",
        "TOAN", "VAN", "NGOAI_NGU", 
        "SU", "DIA", "GDKT_PL", 
        "LI", "HOA", "SINH", 
        "TIN_HOC", "GIAO_DUC_CONG_DAN", "CN_CONG_NGHIEP", 
        "CN_NONG_NGHIEP", "NGAY_SINH"
        ]
        write = csv.DictWriter(fileCrawled, fieldnames = fieldnames)
        write.writeheader()

for i in range(0, 1000000):
    sbd = f"01{i:06d}"
    print(f"Crawling {sbd}...")
    diem = tracudiem(sbd)
    if diem:
        write.writerow(diem)
        print("✓", diem)
    else:
        print(f"✗ Không có dữ liệu {sbd}")
    time.sleep(0.3)
