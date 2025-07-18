import requests

def tracudiem (sbd: str, nam: int = 2025):
    url = "https://s6.tuoitre.vn/api/diem-thi-thpt.htm"

    # sbd = "01016799"

    params = {
        "sbd": sbd,
        "year": nam
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36"
    }

    res = requests.get(url, params = params, headers = headers)

    if res.status_code  == 200
        try:
            data = res.json()
            diem_thi = data["data"] [0] if data["data"] else {}
            
            output = {
                "SBD: ": diem_thi.get("SBD"),
                "TONGDIEM": diem_thi.get("TONGDIEM")
            }

            mon_thi = ["TOAN", "VAN", "NGOAI_NGU", "SU", "DIA", "GDKT_PL", "LI", "HOA", "SINH", "TIN_HOC", "GIAO_DUC_CONG_DAN", "CN_CONG_NGHIEP", "CN_NONG_NGHIEP", "NGAY_SINH"]

            for mon in mon_thi:
                diem = diem_thi.get(mon, -1)
                if diem >= 0: 
                    output[mon] = diem
                
            print(output)
            return output
        except:
            print('Không thể đọc dữ liệu'), str(e)

tracudiem("01016799")