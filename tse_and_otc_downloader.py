import urllib.request
import datetime

otc_url = 'https://www.tpex.org.tw/web/stock/aftertrading/otc_quotes_no1430/stk_wn1430_result.php?l=zh-tw&o=csv&d={}&se=EW&s=0,asc,0'
tse_url = 'https://www.twse.com.tw/exchangeReport/MI_INDEX?response=csv&date={}&type=ALLBUT0999'
otc_name = 'SQUOTE_EW_{}.csv'
tse_name = 'MI_INDEX_{}.csv'

#2020/01/01
today_ac = datetime.datetime.today().strftime("%Y/%m/%d")
#109/01/01
today_tw = today_ac.replace(today_ac[:4], str(eval(today_ac[:4]) - 1911))
#14:30:00
time = datetime.datetime.today().strftime("%H:%M:%S")

def naming(name, date):
    return name.format(date.replace('/', ''))

#download tse: 上市股票每日收盤行情(全部(不含權證、牛熊證))
urllib.request.urlretrieve(tse_url.format(today_ac.replace('/', '')), naming(tse_name, today_ac))
#download otc: 上櫃股票每日收盤行情(不含定價) 所有證券(不含權證、牛熊證)
urllib.request.urlretrieve(otc_url.format(today_tw), naming(otc_name, today_tw))

print(f"{today_ac} {time} complete")
