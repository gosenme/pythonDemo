import datetime

import pymysql
import tushare as ts

ts.set_token("77ec7f5f2064250c1971b29355b5d8d65047f62e40c14dd8be068ed2")
pro = ts.pro_api()
start_dt = '20170101'
time_temp = datetime.datetime.now() - datetime.timedelta(days=1)
end_dt = time_temp.strftime('%Y%m%d')
db = pymysql.connect(host='127.0.0.1', user='root', passwd='1q2w3e4r', db='stock', charset='utf8')
cursor = db.cursor()
stock_pool = ['002841.SZ']
total = len(stock_pool)
for i in range(len(stock_pool)):
    try:
        df = pro.daily(ts_code=stock_pool[i], start_date=start_dt, end_date=end_dt)
        print('Seq:' + str(i + 1) + ' of ' + str(total) + ' Code:' + str(stock_pool[i]))
        c_len = df.shape[0]
    except Exception as aa:
        print(aa)
        print('No DATA Code' + str(i))
        continue
    for j in range(c_len):
        resu0 = list(df.ix[c_len - 1 - j])
        resu = []
        for k in range(len(resu0)):
            if str(resu0[k]) == 'nan':
                resu.append(-1)
            else:
                resu.append(resu0[k])
        state_dt = (datetime.datetime.strptime(resu[1], "%Y%m%d")).strftime('%Y-%m-%d')
        try:
            sql_insert = "INSERT INTO stock_all(state_dt,stock_code,open,close,high,low,vol,amount,pre_close,amt_change,pct_change) VALUES ('%s', '%s', '%.2f', '%.2f','%.2f','%.2f','%i','%.2f','%.2f','%.2f','%.2f')" % (
                state_dt, str(resu[0]), float(resu[2]), float(resu[5]), float(resu[3]), float(resu[4]), float(resu[9]),
                float(resu[10]), float(resu[6]), float(resu[7]), float(resu[8]))
            cursor.execute(sql_insert)
            db.commit()
        except Exception as err:
            print(err)
            continue
    cursor.close()
db.close()
print('All Finished!')
