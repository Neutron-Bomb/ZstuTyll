import json

def main():
    with open('./tytk.json', encoding='utf-8') as f:
        tytk_old = json.loads(f.read())
    with open('./data.txt', encoding='utf-8') as f:
        tytk_new = eval(f.read())
    with open('./merge.json', 'a', encoding='utf-8') as f:
        output = {}
        notfind = list()
        for item in tytk_new:
            if item[1] in tytk_old:
                output[item[1]] = tytk_old[item[1]]
            else:
                notfind.append(item)
        f.write(json.dumps(output, ensure_ascii=False))
        for i in notfind:
            print(i)


if __name__ == '__main__':
    main()