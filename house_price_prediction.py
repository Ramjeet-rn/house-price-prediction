import pandas as pd
from sklearn.linear_model import LinearRegression

data=pd.read_csv('house_prices.csv')
X=data[['Area','Bedrooms','Age']]
y=data['Price']
model=LinearRegression()
model.fit(X,y)

area=float(input('Area: '))
bed=int(input('Bedrooms: '))
age=float(input('Age: '))
pred=model.predict([[area,bed,age]])
print(f'Predicted Price: ₹{pred[0]:,.2f}')
