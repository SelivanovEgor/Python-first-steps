import xml.etree.ElementTree as xml

tree = xml.parse('file.xml')
root = tree.getroot()
files = []
for elem in root:
    for item in elem.findall('item'):
        files.append(item.find('description').text.split())
print(files)
words = {}
quentity = 0
for i in range(0, len(files)):
    for word in files[i]:
        if (word not in words) and (len(word) > 6):
            words[word] = 1
        elif (word in words) and (len(word) > 6):
            quentity = words[word]
            words[word] = quentity + 1

list_d = list(words.items())
list_d.sort(key=lambda i: i[1])
list_d.reverse()
print("Топ 10 слов:")
for i in range(0, 10):
    print(list_d[i][0], ':', list_d[i][1])
