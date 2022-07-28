import urllib.request
import datetime
data_type = "rain" # "temp" "rain"
now = datetime.datetime.now()
tag = f"{str(now.hour).zfill(2)}{str(now.minute).zfill(2)[0]}"
now = now - datetime.timedelta(minutes=(now.minute % 5))

dates = []
for delta_time in range(0,15,5):
    now = now - datetime.timedelta(minutes=5)
    date = f"{now.year}{str(now.month).zfill(2)}{str(now.day).zfill(2)}{str(now.hour).zfill(2)}{str(now.minute).zfill(2)}"
    dates += [date]

if data_type == "temp":
    link1 = "https://www.weather.go.kr/img/aws/aws_mtv_"
    link2 = "_460_A0_CENSN_"
    link3 = "_M.png"

elif data_type == "rain":
    link1 = "https://www.weather.go.kr/img/aws/aws_mrh_"
    link2 = "_460_A0_CENSN_"
    link3 = "_M.png"

for date in dates:
    try:
        link = f"{link1}{date}{link2}{tag}{link3}"
        urllib.request.urlretrieve(link, f"./image/aws_{data_type}.png")
        print(link)
        break
    except:
        pass