import wikipedia
wikipedia.set_lang("ru")

while True:
    try:
        search = input("Что искать?\n")
        s = wikipedia.page(search)
        print(s.content)
    except:
        print()
        print('Возможные варианты:')
        print('===================')
        variants = wikipedia.search(search)
        for item in variants:
            print(item)
        print('===================')
