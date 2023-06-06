import csv
from Diabetes.models import demographic_data


def run():

    with open('/Users/namrathashivanichalasani/Downloads/stats_data.csv') as csvfile:
       reader = csv.DictReader(csvfile)
       for row in reader:
           data = demographic_data(region = row['Region'], country = row['Country/Territory'], year_2000 = float(row['2000'].replace(',','')), year_2011 = float(row['2011'].replace(',','')), year_2021 = float(row['2021'].replace(',','')), year_2030 = float(row['2030'].replace(',','')), year_2045 = float(row['2045'].replace(',','')))
           data.save()
          

    print('CSV file imported successfully')
