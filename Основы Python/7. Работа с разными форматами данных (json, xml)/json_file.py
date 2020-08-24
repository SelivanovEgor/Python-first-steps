import json
from pprint import pprint
from collections import Counter


def search(stroki):
    news_s = ""
    for news in stroki["rss"]["channel"]["items"]:
        news_s += news["description"]
    print(news_s)
    news_stroki = news_s.split()
    quentity = 0
    words = {}
    for word in news_stroki:
        if (word not in words) and (len(word) > 6):
            words[word] = 1
        elif (word in words) and (len(word) > 6):
            quentity = words[word]
            words[word] = quentity + 1
    print(words)
    list_words = list(words.items())
    list_words.sort(key=lambda i: i[1])
    list_words.reverse()
    return list_words


def main():
    with open('file.json', encoding='utf-8') as json_file:
        stroki = json.load(json_file)
        top_words = search(stroki)
        print("Топ 10 слов:")
        for i in range(0, 10):
            print(top_words[i][0], ':', top_words[i][1])

if __name__ == "__main__":
    main()
