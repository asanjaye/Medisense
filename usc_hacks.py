import pandas as pd
import requests

# Function to convert XML to JSON
def convert_xml_to_json(xml_data=None):
    api_url = 'https://api.factmaven.com/xml-to-json'  # Updated API endpoint
    payload = {'xmlData': xml_data}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}  # Added headers for form data
    response = requests.post(api_url, data=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Read the XML file
with open('data.xml', 'r') as file:  # Replace 'data.xml' with the path to XML file
    xml_data = file.read()

# Convert the XML data to JSON
json_data = convert_xml_to_json(xml_data=xml_data)

# Convert the JSON data to a DataFrame
df = pd.json_normalize(json_data)

# Assuming entries are stored in a list under the 'entry' field in the JSON data
entries = df['entry'][0]

# Create an empty list to store the rows
rows = []

# Loop through the entries and extract the required data
for entry in entries:
    resource = entry['resource']  # Assuming the relevant data is stored in the 'resource' attribute of each entry
    disease_name = resource['disease']['name']  # Adjust these lines to match the structure of your FHIR data
    fever = resource['symptoms']['fever']  # Convert to 'Yes'/'No'
    cough = resource['symptoms']['cough']  # Convert to 'Yes'/'No'
    fatigue = resource['symptoms']['fatigue']  # Convert to 'Yes'/'No'
    difficulty_breathing = resource['symptoms']['difficultyBreathing']  # Convert to 'Yes'/'No'
    age = resource['patient']['age']
    gender = resource['patient']['gender']
    blood_pressure = resource['vitals']['bloodPressure']
    cholesterol_level = resource['vitals']['cholesterolLevel']
    outcome_variable = resource['outcome']['variable']
    
    # Convert booleans to 'Yes'/'No'
    fever = 'Yes' if fever else 'No'
    cough = 'Yes' if cough else 'No'
    fatigue = 'Yes' if fatigue else 'No'
    difficulty_breathing = 'Yes' if difficulty_breathing else 'No'
    
    # Append the row to the rows list
    rows.append([
        disease_name, fever, cough, fatigue,
        difficulty_breathing, age, gender,
        blood_pressure, cholesterol_level, outcome_variable
    ])

# Create a DataFrame from the rows list
df = pd.DataFrame(rows, columns=[
    'Disease Name', 'Fever', 'Cough', 'Fatigue',
    'Difficulty Breathing', 'Age', 'Gender',
    'Blood Pressure', 'Cholesterol Level', 'Outcome Variable'
])

# changing all to numeric values
    df['Outcome Variable'] = df['Outcome Variable'].replace({'Positive':1,'Negative':0})
    df['Gender'] = df['Gender'].replace({'Male':1,'Female':0})

# Convert each row of the DataFrame into an array and store in a list
rows_as_arrays = df.values.tolist()

