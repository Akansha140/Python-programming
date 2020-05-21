#Q1 (a) How many rows and columns there are in the Heart Disease UCI data set?

import pandas as pd
heart = pd.read_csv('/Users/akanshakhare/PycharmProjects/Assessment 1/heart.csv')
row_count = len(heart.axes[0])
column_count = len(heart.axes[1])
print('Number of rows in the Heart Disease UCI data set:',row_count)
print('Number of columns in the Heart Disease UCI data set:', column_count)


#Q1 (b) What sex is the 3rd person in the data set, i.e. on the third row?

Sex = heart.sex[2]
print(Sex,'sex is the 3rd person in the data set')

#Q2 How many people have type 3 chest pain?

Chest_pain_count = heart.cp.value_counts()
print('total number of persons who have type 3 chest pain are', Chest_pain_count[3])

## Q3 (a) What age is the youngest person in this dataset?
Min_age = heart.age.min()
print('Youngest person age is', Min_age)

#Q3 (b) What age is the oldest person in this dataset?
Max_age = heart.age.max()
print('Oldest person age is', Max_age)

## Q4 How many people are in the group (50,60)?

heart['age_groups'] = pd.cut(heart['age'], range(20,90,10), labels=['20-30','30-40','40-50','50-60','60-70','70-80'])
print(heart['age_groups'].value_counts()['50-60'])














