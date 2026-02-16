import csv
#reading to csv file
with open(r"C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\data.csv",'r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
#writing to csv file
with open(r"C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\writecsv.csv", 'w') as file:
    writer=csv.writer(file)
    writer.writerow(["id","name","marks"])
    writer.writerow([1, "rion", 99])
    writer.writerow([2, "billu", 89])

#appending the data to csv file
with open(r"C:\Users\rionb\PycharmProjects\Python-seleniun-proj\Dataformats\data.csv",'a', newline="") as file:
    writer=csv.writer(file)
    writer.writerow([3,"Kiran",88])

