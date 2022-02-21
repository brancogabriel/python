from datetime import datetime, timedelta

data1 = datetime(2022, 2, 19, 16, 36, 26)
print(data1.strftime('%d/%m/%Y %H:%M:%S')) #formatação da data no padrão br

data2 = datetime.strptime('19/02/2022', '%d/%m/%Y')
print(data2)
print(data2.timestamp())