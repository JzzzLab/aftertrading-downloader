import urllib.request
import datetime

today = datetime.datetime.today().strftime("%Y/%m/%d")
today = today.replace(today[:4], str(eval(today[:4]) - 1911))

time = datetime.datetime.today().strftime("%H:%M:%S")

#today = '109/05/07'

url = f'https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=csv&d={today}&se=EW&s=0,asc,0'

name = 'SQUOTE_EW_{}_{}.csv'.format(today.replace('/', ''), time.replace(':', ''))

urllib.request.urlretrieve(url, name)

print(f"{today} {time} complete")