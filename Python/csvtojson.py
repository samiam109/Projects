import json

csv_file = open('sample.csv', 'r')
jason_dump = open('json_dump.json', 'w+')
file_data =[]
jason_data = []

for line in csv_file:
    line = line.strip('\n')
    file_data.append(line.split(','))

for e in file_data[1:]:
    payload = {'verificationLevel': int(e[0]), 'userID': int(e[1])}
    jason_data.append(payload)
#print(jason_data)
jason_dump.write(json.dumps(jason_data))
csv_file.close()
jason_dump.close()
