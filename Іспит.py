def edit_text():
    with open("text.txt", "r") as file:
        data = file.readlines()
        for i1, i in enumerate(data):
            if "\n" in i:
                data[i1] = i[:-1]
        return data


def result(text, a):
    for count, time in enumerate(text):
        text[count] = time.split(" ")
    for i in text:
        if int(i[1]) > a:
            print(f"час - {i[0]} параметр - {i[1]}")


def main():
    while True:
        parametr = input("Введіть параметр AAA -> ")
        if parametr.isdigit():
            result(edit_text(), int(parametr))
            break
        else:
            print("Потрібно ввести цифри,спробуйте ще раз.\n")


main()
