
import pandas as pd
from datetime import datetime

def fetch_race_data():
    data = {
        '選手名': ['山田太郎', '佐藤健', '田中翔'],
        '1着率': [12, 25, 8],
        '2着率': [18, 20, 10],
        '3着率': [20, 20, 12],
        '信頼度': [72, 88, 55],
        '取得日': [datetime.now().strftime('%Y-%m-%d')] * 3
    }
    df = pd.DataFrame(data)
    df.to_csv('data/latest_data.csv', index=False)

if __name__ == '__main__':
    fetch_race_data()
