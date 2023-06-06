from Diabetes.models import PersonalInformation, LabReports, MedicalHistory, Lifestyle

# Print all PersonalInformation objects
personal_infos = PersonalInformation.objects.all()
for personal_info in personal_infos:
    print(personal_info.SEQN,personal_info.Name, personal_info.Gender, personal_info.Age, personal_info.Race, personal_info.Height, personal_info.Weight, personal_info.Bmi, personal_info.Email, personal_info.phone_number)

# Print all LabReports objects
lab_reports = LabReports.objects.all()
for lab_report in lab_reports:
    print(lab_report.SEQN, lab_report.Diabetes_Status, lab_report.HbA1c, lab_report.Glucose, lab_report.cholesterol, lab_report.Triglycerides, lab_report.Blood_Pressure_Systolic, lab_report.Blood_Pressure_Diastolic)

# Print all MedicalHistory objects
medical_histories = MedicalHistory.objects.all()
for medical_history in medical_histories:
    print(medical_history.SEQN, medical_history.Pregnancy, medical_history.PCOD, medical_history.DiabetesPedigree)

# Print all Lifestyle objects
lifestyles = Lifestyle.objects.all()
for lifestyle in lifestyles:
    print(lifestyle.SEQN, lifestyle.SmokingStatus, lifestyle.AlcoholConsumption, lifestyle.ActivityLevel, lifestyle.SleepDuration)

