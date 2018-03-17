writer = open("log.txt", mode='w', encoding="utf-8")
writer.write('我是陈贺')
writer.flush()
writer.close()
reader = open("log.txt", mode='r', encoding="utf-8")
result = reader.readline()

print(result)
reader.close()
