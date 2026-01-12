import pandas as pd
import numpy as np

# CONFIGURATION
districts = ['Guwahati', 'Jorhat', 'Silchar']
festivals = {'April': 'Rongali Bihu', 'October': 'Durga Puja'}

# CREATE MOCK DATA
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'Base_Demand': [1000, 1100, 1050, 1200, 1100, 1150, 1200, 1250, 1300, 1400, 1350, 1500]
}
df = pd.DataFrame(data)

# APPLY FESTIVAL SPIKE LOGIC (Resume Point: Predict demand spikes)
def predict_demand(row):
    demand = row['Base_Demand']
    if row['Month'] == 'April':
        return demand * 1.5  # 50% spike for Bihu
    elif row['Month'] == 'October':
        return demand * 1.8  # 80% spike for Puja
    return demand

df['Predicted_Demand'] = df.apply(predict_demand, axis=1)
df['Festival_Alert'] = df['Month'].map(festivals).fillna('Normal Period')

print("Forecasting demand for North-East Region...")
print(df[['Month', 'Predicted_Demand', 'Festival_Alert']])
