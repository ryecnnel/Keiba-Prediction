import pandas as pd
import re
import tool


YM = tool.ym()

# priconne~を連結する
df = pd.read_csv('data/priconne.csv')


for ym in YM:
    anal = df[df['YM'] == int(ym)]
    element = {
        'YM'      : ym,
        'DL'      : anal['Title'].str.contains('ダウンロード突破').sum(), 
        'NewChar' : anal['Title'].str.contains('キャラ').sum(),
        'Update'  : anal['Title'].str.contains('アップデートの').sum(),
        'Colab'   : anal['Title'].str.contains('コラボ').sum(),
        'Cam'     : anal['Title'].str.contains('配布').sum() + anal['Title'].str.contains('倍').sum(),
        'MT'      : anal['Title'].str.contains('メンテナンス').sum(),
        'RegEvent': anal['Title'].str.contains('イベントクエスト').sum(),
        'limited' : anal['Title'].str.contains('期間限定').sum(),
        'AddStory': anal['Title'].str.contains('追加').sum(),
        'Fukkoku' : anal['Title'].str.contains('復刻').sum(),
        'Prize'   : anal['Title'].str.contains('記念').sum(),
        
        }
    if ym == YM[0]:
        df01 = pd.DataFrame([element])
    else:
        df02 = pd.DataFrame([element])
        df01 = pd.concat([df01, df02], ignore_index=True)

df01.to_csv('data/priconne_analysis.csv')
