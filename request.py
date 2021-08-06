Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'SeniorCitizen':0,'Tenure':1, 'MonthlyCharges':29.85, 'TotalCharges':29.85})
print(r.json())