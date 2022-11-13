import csv
import json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):

    # create a dictionary
    data = {
        "records": []
    }

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for row in csvReader:
                record = {
                    "serial_no": float(row["Serial No."]),
                    "gre_score": float(row["GRE Score"]),
                    "toefl_score": float(row["TOEFL Score"]),
                    "university_rating": float(row["University Rating"]),
                    "sop": float(row["SOP"]),
                    "lor": float(row["LOR "]),
                    "cgpa": float(row["CGPA"]),
                    "research": float(row["Research"]),
                    "admission_points": 0.0
                }
                data["records"].append(record)
    # Open a json writer, and use the json.dumps()
    # function to dump data
    percent = 1
    size = len(data["records"])
    newSize = 150#round(size * percent)
    data["records"] = data["records"][:newSize]
    print(len(data["records"]))
    
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


# Driver Code

# Decide the two file paths according to your
# computer system
csvFilePath = r'requestBodys/data/202220_Laboratorio_3_data_university_admission_test.csv'
jsonFilePath = r'requestBodys/predict/predict_data_150.json'

# Call the make_json function
make_json(csvFilePath, jsonFilePath)
