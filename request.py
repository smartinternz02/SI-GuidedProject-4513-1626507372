import requests
url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'SeniorCitizen':0,'Tenure':1, 'MonthlyCharges':29.85, 'TotalCharges':29.85})
print(r.json())
