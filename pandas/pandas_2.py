import pandas as pd

condition = 'MAx'
url = 'http://72.itmc.org.cn:80/JS001/data/user/13965/80/fj_order_data.csv'
chipo = pd.read_csv(url, sep=',')
aa = []

for i in chipo['item_price']:
    aa.append(i[1:])
chipo['asd'] = aa
chipo['asd'] = chipo['asd'].astype(float)
chipo['qwe'] = chipo['asd'] * chipo['quantity']
requ = (chipo.groupby('item_name')['qwe'].sum()).sort_values(ascending=False)
if condition.lower() == 'max':
    print(requ.index[0])
else:
    print(requ.index[-1])
