import csv

source_file = 'csv/source.csv'
target_file = 'target/_shopdata.ejs'
counter = 0

with open(source_file, encoding="utf-8") as f:
  source_data = csv.reader(f)

  for row in source_data:
    before_name = row[1]
    after_name = row[0]

    with open(target_file, encoding="utf-8") as f:
      after_file = f.read()
      after_file = after_file.replace(before_name, after_name)
      # print(before_name, after_name)

    with open('target/after/_shopdata_changed.ejs', 'w', encoding="utf-8") as f:
      f.write(after_file)
      print(row[0])
      counter += 1

print('end')
print(counter)