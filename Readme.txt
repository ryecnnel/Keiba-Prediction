実行環境
    Anaconda VScode Python 3.7.11 64-bit

インストール済パッケージの一覧表示
    (Scraping) yuyaarai@yuyanoAir Scraping % pip list
    Package             Version
    ------------------- ---------
    beautifulsoup4      4.9.3
    bs4                 0.0.1
    certifi             2021.5.30
    future              0.18.2
    Keras-Applications  1.0.8
    Keras-Preprocessing 1.1.2
    mock                4.0.3
    numpy               1.21.1
    pandas              1.3.1
    pip                 21.1.3
    python-dateutil     2.8.2
    pytz                2021.1
    selenium            3.141.0
    setuptools          51.1.1
    six                 1.15.0
    soupsieve           2.2.1
    urllib3             1.26.6
    wheel               0.36.2

    多分beautifulsoup4(bs4)とpandasがあればできると思います。

Scraping.py
    対象のサイトを開き、データをスクレイピングします。
    今回は各月ニュースアーカイブページの見出しと月を保存し、CSVファイルに出力します。

DataEdit.py
    Scraping.pyで出力したCSVファイル（今回はpriconne.csv）を読み込み、各月の各指定単語の出現回数を
    データフレームとして表現し、CSVファイルとして出力します。

