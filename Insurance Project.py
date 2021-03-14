# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 09:49:15 2021

@author: Pradana Dharma
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

with open('insurance.csv') as insurance_data:
    insurance_read = [{k:v for k, v in row.items()}
                      for row in csv.DictReader(insurance_data)]

#Making lists of variables
    
    age = []
    sex = []
    bmi = []
    children = []
    smoker = []
    region = []
    charges = []
    
    for item in insurance_read:
        age.append(int(item['age']))
        sex.append(item['sex'])
        bmi.append(item['bmi'])
        children.append(item['children'])
        smoker.append(item['smoker'])
        region.append(item['region'])
        charges.append(float(item['charges']))
        
#Plotting the data with matplotlib scatter plot
        
    #plt.scatter(age, charges, s=1)
    #plt.show()
    
    #plt.scatter(sex, charges, s=1)
    #plt.show()
    
    #plt.scatter(bmi, charges, s=1)
    #plt.show()
    
    #plt.scatter(children, charges, s=1)
    #plt.show()
    
    #plt.scatter(smoker, charges, s=1)
    #plt.show()
    
    #plt.scatter(region, charges, s=1)
    #plt.show()

#Calculating average insurance cost using for loops

    total_cost = 0
    
    for cost in range(len(charges)):
        total_cost += cost
    
        
    average_insurance_cost = total_cost/(len(age))
    print('The average cost of insurance in the sample is ' + str(round(average_insurance_cost, 2)) + ' dollars.')
          
#Calculating average insurance cost for male correspondents

    male_cost = 0
    
    for item in insurance_read:
        if item['sex'] == 'male':
            male_cost += float(item['charges'])
    
    average_male_cost = male_cost/(len(age))
    print('The average insurance cost for male correspondents is ' + str(round(average_male_cost, 2)) + ' dollars.')

#Calculating average insurance cost for female correspondents with different coding

    female_cost = sum(float(d['charges']) for d in insurance_read if d['sex'] == 'female')
    average_female_cost = female_cost/len(age)
        
    print('The average insurance cost for female correspondents is ' + str(round(average_female_cost, 2)) + ' dollars.')

#Difference between male to female cost

    difference_cost_gender = average_male_cost - average_female_cost
    print('The difference of costs between male and female correspondents is ' + str(round(difference_cost_gender, 2)) + ' dollars.')
    
#Why male insurance cost is more expensive than female? Smoker?

    male_who_smokes = 0
    female_who_smokes = 0
    
    for i in insurance_read:
        if i['sex'] == 'male' and i['smoker'] == 'yes':
            male_who_smokes += 1
        if i['sex'] == 'female' and i ['smoker'] == 'yes':
            female_who_smokes += 1  
      
    total_male = 0
    total_female = 0
    
    for i in insurance_read:
        if i['sex'] == 'male':
            total_male += 1
        if i['sex'] == 'female':
            total_female += 1
            
    percent_smoker_in_males = male_who_smokes/total_male
    percent_smoker_in_females = female_who_smokes/total_female
    
    print('Why does the average cost between male and female correspondents differs?'
          ' it turns out the percentage of male smoker is ' + str(round(percent_smoker_in_males * 100, 2)) + ' %, which is bigger compared to female smoker of '
          + str(round(percent_smoker_in_females * 100, 2)) + '%')

#Insurance cost based on region using for loops and conditionals

    avg_cost_region = {}
    
    def avg_insurance_cost_region(reg):
        total_cost_reg = sum(float(d['charges']) for d in insurance_read if d['region'] == reg)
        avg_cost_reg = round(total_cost_reg/region.count(reg), 2)
        
        return avg_cost_reg
    
#Adding up avg_cost_region dict

    avg_cost_region['Northeast'] = avg_insurance_cost_region('northeast')
    avg_cost_region['Souetheast'] = avg_insurance_cost_region('southeast')
    avg_cost_region['Southwest'] = avg_insurance_cost_region('southwest')
    avg_cost_region['Northwest'] = avg_insurance_cost_region('northwest')
    
    print('The average cost of insurance based on regions are: ' + str(avg_cost_region))
    
#Different avg cost between smoker and non smoker using Numpy

    smoker_charges =  []
    non_smoker_charges = []
    
    for detail in insurance_read:
        if detail['smoker'] == 'yes':
            smoker_charges.append(float(detail['charges']))
        else:
            non_smoker_charges.append(float(detail['charges']))
    
    avg_smoker_charge = np.mean(smoker_charges)
    avg_non_smoker_charge = np.mean(non_smoker_charges)
    
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    smoker_type = ['Non Smoker', 'Smoker']
    avg_charge= [avg_non_smoker_charge, avg_smoker_charge]
    ax.bar(smoker_type, avg_charge, width = 0.2)
    
#Different avg cost for 10 years increment in age using numpy plot using matplotlib

    cost_age_18to30 = []
    cost_age_31to40 = []
    cost_age_41to50 = []
    cost_age_51to60 = []
    cost_age_61to64 = []
    
    for detail in insurance_read:
        if 18 >= int(detail['age']) < 31:
            cost_age_18to30.append(float(detail['charges']))
        elif 31 >= int(detail['age']) < 41:
            cost_age_31to40.append(float(detail['charges']))
        elif 41 >= int(detail['age']) < 51:
            cost_age_41to50.append(float(detail['charges']))
        elif 51 >= int(detail['age']) < 60:
            cost_age_51to60.append(float(detail['charges']))
        else:
            cost_age_61to64.append(float(detail['charges']))
            
    avg_cost_18to30 = np.mean(cost_age_18to30)
    avg_cost_31to40 = np.mean(cost_age_31to40)
    avg_cost_41to50 = np.mean(cost_age_41to50)
    avg_cost_51to60 = np.mean(cost_age_51to60)
    avg_cost_60to64 = np.mean(cost_age_61to64)
    
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    age_range = ['Age 18-30', 'Age 31-40', 'Age 41-50', 'Age 51-60', 'Age 61-64']
    avg_charge_age = [avg_cost_18to30, avg_cost_31to40, avg_cost_41to50, avg_cost_51to60, avg_cost_60to64]
    ax.bar(age_range, avg_charge_age, width = 0.2)
    plt.show()

#Avg difference cost of 10 year increment of age

    avg_cost_difference_age = ((avg_cost_31to40-avg_cost_18to30)+(avg_cost_41to50-avg_cost_31to40)+(avg_cost_51to60-avg_cost_41to50)+(avg_cost_60to64-avg_cost_51to60))/6
    
    
    