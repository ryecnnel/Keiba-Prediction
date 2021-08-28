def ym():
    ym = []
    y = ["2018", "2019", "2020", "2021"]
    m = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    for i in y:
        for j in m:
            ym.append(i+j)
            if i == "2021" and j == "07":
                break
    return ym


def main():
    YM = ym()
    for i in YM:
        url = "https://priconne-redive.jp/news/?ym=" + i
        print(url)

if __name__ == "__main__":
    main()