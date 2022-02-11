from datetime import datetime

date = str(datetime.now())[:10].split('-')

for d in date:
    print(d)