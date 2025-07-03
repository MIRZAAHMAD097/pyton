#lesson 18
import pandas as pd

#homework 2

#1
df  = pd.read_csv( r'C:\Users\User\Documents\py\tackoverflow_qa (1).csv', parse_dates=['creationdate'])


q1 = df[df['creationdate']< '2024-01-01']
print("before 2014: \n", q1.head())
#2
q2 = df[df['score'] > 50]
print("score more than 50: ", q2.head())
#3
q3 = df[df['score']>= 50 & (df['score'] <= 100)]
print("score between 50 and 100: ", q3.head())
#4
q4 = df[df['ans_name']== 'Scott Boston']
print("answered by Scott Boston:\n", q4.head())
#5
users = ['Demitri', 'doug', 'Nick Crawford', 'Joe Kington', 'Wes McKinney']
q5 = df[df['ans_name'].isin(users)]
print("name of 5 users:\n ", q5.head())
#6
q6 = df[
    (df['creationdate'] >= '2014-03-03') &
    (df['creationdate'] <= '2014-10-01') &
    (df['ans_name'] == 'Unutbu') &
    (df['score'] < 5)
 ]
print("created between march and october in 2014, by Unutbu, score < 5:\n", q6.head())
#7
q7 = df[((df['score'] > 5) & (df['score'] < 10)) | (df['viewcount'] > 10000)]
print("score between 5 and 10 or viewcount more than 10000:\n", q7.head())
#8
q8 = df[df['ans_name'] != 'Scott Boston']
print("not answered by Scott Boston:\n", q8.head())


#homework 3
import pandas as pd


titanic_df = pd.read_csv(r"C:\Users\User\Documents\py\titanic.csv")
print(titanic_df.head())
#1
q1 = titanic_df[
    (titanic_df['Sex'] == 'female') &
    (titanic_df['Pclass'] == 1) &
    (titanic_df['Age'].between(20,30))
]

print("female in class 1, age 20-30:\n", q1.head())
#2
q2 = titanic_df[titanic_df['Fare'] > 100]
print("passengers who paid more than 100$:\n", q2.head())

#3
q3 = titanic_df[
    (titanic_df['Survived'] == 0) &
    (titanic_df['SibSp'] == 0) &
    (titanic_df['Parch'] == 0)
]

print("survived and alone:\n", q3.head())
#4
q4 = titanic_df[
    (titanic_df['Embarked'] == 'C') &
    (titanic_df['Fare'] > 50)            
                ] 
print("embarked and paid more than 50:\n", q4.head())
#5
q5 = titanic_df[
    (titanic_df['SibSp'] > 0) &
    (titanic_df['Parch'] > 0)
]
print("passenger who has parents and siblings or spouses:\n", q5.head())
#6
q6 = titanic_df[
    (titanic_df['Age'] <= 15) &
    (titanic_df['Survived'] == 1)
]
print("passengers aged 15 or younger and didn't survived:\n", q6.head())
#7
q7 = titanic_df[
    (titanic_df['Cabin'].notna()) &
    (titanic_df['Fare'] > 200)
]
print("cabin not null and fare more than 200$:\n", q7.head())
#8
q8 = titanic_df[titanic_df['PassengerId'] % 2 == 1]
print("odd passengers:\n", q8.head())
#9
q9 = titanic_df[titanic_df['Ticket'].duplicated(keep=False) == False]
print("unique tickets:\n", q9.head())
#10
q10 = titanic_df[
    titanic_df['Name'].str.contains('Miss', case=False) &
    (titanic_df['Pclass'] == 1)
]
print("Miss in name and class 1:\n", q10.head())
