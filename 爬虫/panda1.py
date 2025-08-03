import pandas as pd  
film_names=['霸王别姬','肖申克的救赎','天下','五十万','昔我往矣']  
scores=['9.7','3.3','4.6','2.6','4.6']  
df=pd.DataFrame()  
df["电影名称"]=film_names  
df["评分"]=scores  
print(df)  
df.to_excel("电影信息.xlsx",index=False)