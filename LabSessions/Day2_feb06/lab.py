#Q1
data=[(1, 3), (4, 1), (2, 2), (5, 0)]
sorteddata=sorted(data,key=lambda x:x[0])
print(sorteddata)
#Q2
from datetime import datetime
now = datetime.now()
get_year  = lambda x: x.year
get_month = lambda x: x.month
get_date  = lambda x: x.day
get_time  = lambda x: x.time()
print("Year :", get_year(now))
print("Month:", get_month(now))
print("Date :", get_date(now))
print("Time :", get_time(now))

#Q3
dict1 = {'a': 1, 'b': 2, 'c':3.2}
dict2 = {'c': 3}
dict3 = {'d': 4}
new_dict = {}
new_dict.update(dict1)
new_dict.update(dict2)
new_dict.update(dict3)
print(new_dict)

