import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder as label_encoders

import pandas as pd
from sklearn.metrics import accuracy_score,precision_score,roc_auc_score,roc_curve
from flask import Flask, request, render_template

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
plt.rcParams['figure.figsize']=[15,6]
import warnings
warnings.filterwarnings("ignore")

patient_data = pd.DataFrame()
chosen_disease = ""
def __init__(self, patient_data, chosen_disease):
    self.patient_data= patient_data
    self.chosen_disease = chosen_disease
# app = Flask(__name__)

# Load the dataset
df = pd.read_csv('Disease_symptom.csv')  


df = df.dropna()

print(df)

df.head()

for i in ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing']:
    df[i] = df[i].replace({'Yes':1,'No':0})
    
for i in ['Blood Pressure', 'Cholesterol Level']:
    df[i] = df[i].replace({'Low':1,'Normal':2,'High':3})
    
df.head()
    

# changing all to numeric values 
df['Disease'] = df['Outcome Variable'].replace({'Positive':1,'Negative':0})
df['Gender'] = df['Gender'].replace({'Male':1,'Female':0})


# x and y varibles for trainig
y = df['Disease']
x = df[['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 'Age','Gender', 'Blood Pressure', 'Cholesterol Level']]
df = df[df['Outcome Variable'] == chosen_disease]

# print(df) 
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.30,random_state=42)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def train(model_name):
    
    print("For the {}".format(model_name))
    model_name.fit(xtrain,ytrain)
    y_pred_train = model_name.predict(xtrain)
    y_pred_test = model_name.predict(xtest)

    # print(y_pred_train)
    print("The TRAIN accuracy is ",accuracy_score(y_pred_train, y_pred_test))



    # print("The TRAIN accuracy is",accuracy_score(ytrain,y_pred_train))
    # print("The ROC score for TRAIN data is",roc_auc_score(ytrain,y_pred_train))

    # print("--"*50)
    # print("The TEST accuracy is",accuracy_score(ytest,y_pred_test))
    # print("The ROC score for TEST data is",roc_auc_score(ytest,y_pred_test))


def get_risk_level(model, user_data):
    # Filter the dataframe to include only rows with the specified disease
    # disease_df = df[df['Disease'] == disease]
    
    # Prepare input data for prediction
    # input_data = disease_df.drop(['Disease'], axis=1)
    for column, le in label_encoders.items():
        user_data[column] = le.transform(user_data[column])
    
    # Make predictions using the trained model
    predictions = model.predict_proba(user_data)
    
    # Assuming 'Positive' class is index 1 in the classes array
    risk_factor = predictions[:, 1].mean()
    
    # Define thresholds for risk levels
    if risk_factor > 0.8:
        risk_level = "high risk"
    elif risk_factor > 0.6:
        risk_level = "medium risk"
    else:
        risk_level = "low risk"
    
    return risk_level

    
    
# use flask in this class
if __name__ == "__main__":
    rf=RandomForestClassifier()
    train(rf)
    get_risk_level(rf,patient_data)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
plt.barh(xtrain.columns,rf.fit(xtrain,ytrain).feature_importances_)
plt.show()
# df.head()
    
    
# uncomment for ploting , you should more ->>
r=3
c=5
it=1
for i in df.columns:
    plt.subplot(r,c,it)
    if df[i].dtype=='object':
        sns.countplot(y=df[i])
    else:
        sns.kdeplot(df[i])
        plt.grid()
    it+=1
plt.tight_layout()
plt.show()


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    



