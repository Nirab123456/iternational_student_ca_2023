import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
int_stu_count_df = pd.read_csv('data/Internation_students_Canada.csv')
int_stu_pro_df = pd.read_csv('data/Internation_students_Province_Canada.csv')
int_stu_stu_lev_def = pd.read_csv('data/International_students_Study_Level.csv')
#convert the strings to lower case
int_stu_count_df.columns = int_stu_count_df.columns.str.lower()
int_stu_pro_df.columns = int_stu_pro_df.columns.str.lower()
int_stu_stu_lev_def.columns = int_stu_stu_lev_def.columns.str.lower()
#lower case the country of citizenship
int_stu_count_df['country of citizenship'] = int_stu_count_df['country of citizenship'].str.lower()
#lower case the province/territory
int_stu_pro_df['province/territory'] = int_stu_pro_df['province/territory'].str.lower()
#lower case the province/territory
int_stu_stu_lev_def['province/territory'] = int_stu_stu_lev_def['province/territory'].str.lower()
#lower case the study level
int_stu_stu_lev_def['study level'] = int_stu_stu_lev_def['study level'].str.lower()
#renme country of citizenship to country
int_stu_count_df = int_stu_count_df.rename(columns = {'country of citizenship':'country'})
#rename Province/territory to province
int_stu_pro_df = int_stu_pro_df.rename(columns = {'province/territory':'province'})
#rename Province/territory , study level to province
int_stu_stu_lev_def = int_stu_stu_lev_def.rename(columns = {'province/territory':'province'})
int_stu_stu_lev_def = int_stu_stu_lev_def.rename(columns = {'study level':'study'})


for i in range(2016,2024):
    #convert everything to numeric
    int_stu_count_df[str(i)] = pd.to_numeric(int_stu_count_df[str(i)])
    int_stu_pro_df[str(i)] = int_stu_pro_df[str(i)].str.replace(',', '')
    int_stu_pro_df[str(i)] = pd.to_numeric(int_stu_pro_df[str(i)])
    int_stu_stu_lev_def[str(i)] = pd.to_numeric(int_stu_stu_lev_def[str(i)])
   

#compare indevisual and deiifernce between 2 
    
#compare 2 provinces
while True:
    #select one country and check the number of students incresing rate each year
    province_1 = input('Enter the province name: ')
    if province_1 == 'q':
        break
    province_1 = province_1.lower()

    if province_1 in int_stu_pro_df['province'].values and province_1 in int_stu_pro_df['province'].values:
        data_map_1 = {}
        for i in range(2016,2024):
            all_data = int_stu_pro_df[int_stu_pro_df['province'] == province_1][str(i)].values
            total = 0
            for j in all_data:
                total += j
            data_map_1[i] = total
                
        
        #calculate the diffatrence frome previous year and the rate of incresing
        incresing_rate_1 = {}
        for i in range(2016,2023):
            incresing_rate_1[i] = (data_map_1[i+1] - data_map_1[i])/data_map_1[i] * 100
        
        #select another country and check the number of students incresing rate each year
        province = input('Enter the another province name: ')
        province = province.lower()
        if province == 'q':
            break
        if province in int_stu_pro_df['province'].values:
            data_map = {}
            for i in range(2016,2024):
                all_data = int_stu_pro_df[int_stu_pro_df['province'] == province][str(i)].values
                total = 0
                for j in all_data:
                    total += j
                data_map[i] = total
            
            #calculate the diffatrence frome previous year and the rate of incresing
            incresing_rate = {}
            for i in range(2016,2023):
                incresing_rate[i] = (data_map[i+1] - data_map[i])/data_map[i] * 100

            #compare the increasing rate of 2 countries
            for i in range(2016,2023):
                print (' the year is: ',i)
                print('The increasing rate of ',province_1, ' from ',i,' to ',i+1, ' is: ', incresing_rate_1[i])
                print('The increasing rate of ',province, ' from ',i,' to ',i+1, ' is: ', incresing_rate[i])
                print('The difference between ',province_1, ' and ',province, ' from ',i,' to ',i+1, ' is: ', incresing_rate_1[i] - incresing_rate[i])
                print('---------------------------------------------------------------------------------')
                #print 2016 to 2023            
