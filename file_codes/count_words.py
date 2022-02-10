file = open('.\\data\\in.txt')

data = file.read()
words = data.split('\n')
counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
        
#ordering dict
counts = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1])}

file_out = open('.\\data\\out.txt','w')


for i in counts.items():
    file_out.write(f"{i[0]}: {i[1]}\n")
