import csv
from Diabetes.models import PersonalInformation, LabReports, MedicalHistory, Lifestyle



def run():

    with open('/Users/namrathashivanichalasani/Desktop/DataBase Management/Project/Data/diabetes-2.csv') as csvfile:
       reader = csv.DictReader(csvfile)
       for row in reader:
           Personal_Information = PersonalInformation(SEQN = int(row['seqn']), Gender = int(row['gender']), Age = int(row['age']), Race = int(row['race_ethnicity']), Height = float(row['height']), Weight = float(row['weight']), Bmi =float(row['bmi']))
           Personal_Information.save()

           personal_info = PersonalInformation.objects.get(SEQN = int(row['seqn']))


           Lab_Reports = LabReports.objects.create(SEQN = personal_info, Diabetes_Status = int(row['condition']), HbA1c = float(row['A1C_level']), Glucose = float(row['glucose']), cholesterol = float(row['cholesterol']), Triglycerides = float(row['triglycerides']), Blood_Pressure_Systolic = float(row['systolic_bp']), Blood_Pressure_Diastolic = float(row['diastolic_bp']))
           Lab_Reports.save()

           Life_style = Lifestyle.objects.create(SEQN = personal_info, ActivityLevel =float(row['physical_activity_level']))
           Life_style.save()

           Medical_History = MedicalHistory.objects.create(SEQN = personal_info)
           Medical_History.save()


    print('CSV file imported successfully')
