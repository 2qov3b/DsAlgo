import csv

csvFile = open("test.csv", 'w+', newline='')
try:
  writer = csv.writer(csvFile)
  writer.writerow(('num', 'num + 2', 'num x 2'))
  for i in range(10):
    writer.writerow((i, i+2, i*2))
finally:
  csvFile.close()
