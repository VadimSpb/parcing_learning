import pandas as pd
from hh_parcer import hh_parcer

if __name__=='__main__':
    df = hh_parcer()
    print(df.to_string())
    print('На superjob.ru не обнаружено интересующих меня вакансий')