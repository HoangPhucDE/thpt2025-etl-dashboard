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

    print('Status code: ', res.status_code)
    print("Kết quả: ", res.text)

tracudiem("01016799")