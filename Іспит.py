a = open("file.txt",'r',encoding='utf8')
word = input("Введіть шукаєме слово: ")
splited = f.read().split('\n\n')
c = 0
for i in splited:
    for b in i.split():

        if b == tegword:
            print("Потрібний абзац: "+ i +"\n")
            c += 1

if c == 0:
    print("Слово не знайдено.")