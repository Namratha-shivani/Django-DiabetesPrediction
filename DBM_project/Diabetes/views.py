from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
import joblib
import pickle
import csv
import pandas as pd
import numpy as np

from .models import PersonalInformation, LabReports, Lifestyle, MedicalHistory, demographic_data


def Diabetes(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def Diabetesinformation(request):
     return render(request,'information.html') 


def takeatest(request):

    if request.method == 'POST':
        ethinicity_map = {
              "Mexican American": 1,
              "Other Hispanic": 2,
              "Non-Hispanic White": 3,
              "Non-Hispanic Black": 4,
              "Other Race": 5

        }
        ethinicity = request.POST['Ethinicity']
        ethinicity_value = ethinicity_map[ethinicity]
        
        physical_activity_map  ={
            'Inactive':1,
            'Minimally active': 2,
            'Moderately active': 3,
            'Highly active': 4
        }

        physical_activity = request.POST['excercise']
        physical_value = physical_activity_map[physical_activity]

        data = {
            'age': int(request.POST['Age']),
            'gender': 1 if request.POST['Gender']=='male' else 2,
            'height': float(request.POST['Height']),
            'weight': float(request.POST['Weight']),
            'bmi': float(request.POST['BMI']),
            'Ethinicity' : ethinicity_value,
            'Email': request.POST['email'],
            'Phone Number': request.POST['phone'],
            
            'systolic_bp' : int(request.POST['Systolic Blood pressure']),
            'Diastolic_bp' : int(request.POST['Diastolic Blood pressure']),
            'cholesterol' : float(request.POST['Cholesterol levels']),
            'triglycerides' : float(request.POST['Triglyceride']),
            'physical_activity_level': physical_value,
            

        }

        with open('Diabetes/machine_learning/classifier.pkl','rb') as f:
            dt = pickle.load(f)
        
        X = [[data['gender'],data['age'],data['bmi'],data['weight'],data['triglycerides'],data['systolic_bp'], data['cholesterol'], data['physical_activity_level']]]   

        result = dt.predict(X)[0]

        last_record = PersonalInformation.objects.last()
        seqn = last_record.SEQN + 1 if last_record else 1

        Personal_Information = PersonalInformation(
            SEQN = seqn,
            Gender = data['gender'],
            Age = data['age'],
            Race = data['Ethinicity'],
            Height = data['height'],
            Weight = data['weight'],
            Bmi = data['bmi'],
            Email = data['Email'],
            phone_number = data['Phone Number'],
            Name = request.POST['name'],
        )
        Personal_Information.save()
        
        
        Lab_Reports = LabReports(
            SEQN =Personal_Information ,
            Diabetes_Status = result,
            
            
            cholesterol = data['cholesterol'],
            Triglycerides = data['triglycerides'],
            Blood_Pressure_Systolic = data['systolic_bp'],
            Blood_Pressure_Diastolic = data['Diastolic_bp']
        )
        Lab_Reports.save()

        Medical_History = MedicalHistory(
            SEQN = Personal_Information,
            DiabetesPedigree = 1 if  request.POST['Family history']=='yes' else 0,
            PCOD = 1 if request.POST['PCOD']=='yes' else 0,
            Pregnancy = 1 if request.POST['Pregnancy'] == 'yes' else 0
            
        )
        Medical_History.save()

        lifestyle_map  ={
            'none':0,
            'Rarely': 1,
            'Occasionally': 2,
            'Regularly': 3
        }

        smoking = request.POST['smoking']
        smoking_value = lifestyle_map[smoking]

        alcohol = request.POST['alcohol']
        alcohol_value = lifestyle_map[alcohol]

        sleep_map  ={
            '5':2,
            '5-8': 1,
            '8': 0
        }

        sleep = request.POST['sleep']
        sleep_value = sleep_map[sleep]

        Life_style = Lifestyle( 
            SEQN = Personal_Information,
            SmokingStatus = smoking_value,
            AlcoholConsumption = alcohol_value,
            ActivityLevel = data['physical_activity_level'],
            SleepDuration = sleep_value
        )
        Life_style.save()


        final_result = ''
        if (result == 0 ):
            final_result = 'Non Diabetes'
        elif (result == 1):
            final_result = 'Pre-diabetes'
        else:
            final_result = 'Diabetes'
        return render(request, 'results.html', {'result':final_result})

    return render(request, 'takeatest.html')


def your_form_submission_view(request):
     return redirect('takeatest')


def import_csv(request):
    
    with open('/Users/namrathashivanichalasani/Desktop/DataBase Management/Project/Data/diabetes-2.csv') as csvfile:
       reader = csv.DictReader(csvfile)
       for row in reader:
           PersonalInformation = PersonalInformation(SEQN = row['SEQN'], Gender = row['gender'], Age = row['age'], Race = row['race_ethnicity'], Height = row['height'], Weight = row['weight'], Bmi = row['bmi'])
           PersonalInformation.save()

           LabReports = LabReports(SEQN = row['SEQN'], Diabetes_status = row['condition'], HbA1c = row['A1C_level'], Glucose = row['Glucose'], cholesteral = row['cholesterol'], Triglycerides = row['triglycerides'], Blood_Pressure_Systole = row['systolic_bp'], Blood_Pressure_Diastolic = row['diatolic_bp'])
           LabReports.save()

           Lifestyle = Lifestyle(SEQN = row['SEQN'])
           Lifestyle.save()

           MedicalHistory = MedicalHistory(SEQN = row['SEQN'])
           MedicalHistory.save()


    return HttpResponse('CSV file imported successfully')

def import_stats_data(request):
   
    with open('/Users/namrathashivanichalasani/Downloads/stats_data.csv') as csvfile:
       reader = csv.DictReader(csvfile)
       for row in reader:
           data = demographic_data(region = row['Region'], country = row['Country/Territory'],year_2000= row['2000'], year_2011 = row['2011'], year_2021 = row['2021'], year_2030 = row['2030'], year_2045 = row['2045'])
           data.save()


    return HttpResponse('CSV file imported successfully')





df3=pd.read_json('https://cdn.jsdelivr.net/gh/highcharts/highcharts@v7.0.0/samples/data/world-population-density.json')



def map(request):

    demo_data = demographic_data.objects.all()
    df2= pd.DataFrame(list(demo_data.values('country','year_2021')))
    df2.columns=['Country/Region','values']
    df2['Country/Region']= ['United States' if x == 'United States of America' else x for x in df2['Country/Region']]
    df2=df2.sort_values(by='values',ascending=False)
    countryNames=list(df2['Country/Region'].values)
    countsVal=list(df2['values'].values)
    maxVal=max(countsVal)
    overallCount=sum(countsVal)
    logVals=list(np.log(ind) if ind != 0 else 0 for ind in countsVal )
    uniqueCountryNames=pd.unique(df2['Country/Region'])
    dataForMapGraph=[]
    for i in uniqueCountryNames:
        try:
            tempdf=df3[df3['name']==i]
            temp={}
            temp["code3"]=list(tempdf['code3'].values)[0]
            temp["name"]=i
            temp["value"]=df2[df2['Country/Region']==i]['values'].sum()
            temp["code"]=list(tempdf['code'].values)[0]
            dataForMapGraph.append(temp)
        except:
            pass
    
    context = {'maxVal': maxVal, 'dataForMapGraph': dataForMapGraph, 'uniqueCountryNames': uniqueCountryNames, 'countryNames':countryNames, 'countsVal':countsVal,'logVals':logVals, 'overallCount':overallCount, 'df2':df2, 'demo_data': demo_data}
    lab_reports = LabReports.objects.exclude(HbA1c__isnull=True)
    lab_data = pd.DataFrame(list(lab_reports.values('HbA1c','Diabetes_Status')))
    Grouped = lab_data.groupby('Diabetes_Status')
    dia = Grouped.get_group(2)
    predia = Grouped.get_group(1)   
    non_dia = Grouped.get_group(0)
    df_dia = dia[['Diabetes_Status','HbA1c']].values.tolist()
    df_predia = predia[['Diabetes_Status','HbA1c']].values.tolist()
    df_nondia = non_dia[['Diabetes_Status','HbA1c']].values.tolist()
    
    return render(request, 'map.html', {'dataForMapGraph':dataForMapGraph, 'maxVal':maxVal,'df_dia':df_dia, 'df_predia':df_predia, 'df_non_dia': df_nondia})























