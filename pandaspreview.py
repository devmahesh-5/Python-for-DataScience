import pandas as pd
data={
    "name":['Jared Diamond',"Sarah O'Donnel","Brian Martin","David Hassel","Clara Rodriquez","Jennifer Lorentz","Susan Clark","Margareth Jones","John Bertsch","Jake Timmerman","Joshua Connor","John Matsuda","Eddy Johnson","Rebecah Anderson","Linda Carter","Richard Swayze","Andrew King"],
    "gender":['M','F','M','M','F','F','F','F','M','M','M','M','M','F','F','M','M'],

    "age":[32,33,43,32,33,34,32,33,34,35,36,37,38,39,40,41,42],
    #height in cm
    "height":[165.3,160.3,167.3,168.3,164.3,160.3,171.3,172.3,173.3,174.3,175.3,176.3,177.3,178.3,179.3,180.3,181.3],
    "weight":[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81],
    "grade":[3,2,'N',2,1,'N',2,1,3,2,1,3,2,1,3,2,1],
    "absence":['Y','N','Y','N','Y','N','Y','N','Y','N','Y','N','Y','N','Y','N','Y'],
    "bloodtype":['A','B','AB','O','A','B','AB','O','A','B','AB','O','A','B','AB','O','A']
}

df=pd.DataFrame(data)
filtered_df=df[df['age']>40]
value_counts=df['gender'].value_counts()
female=value_counts.get('F')
male=value_counts.get('M')
height=df['height']
avgMaleHeight=df[df['gender']=='M']['height'].mean();
avgFemaleHeight=df[df['gender']=='F']['height'].mean();

print(male,":",female)
print("Average Male Height:",avgMaleHeight)
print("Average Female Height:",avgFemaleHeight)
df['height']=df['height']/100

commonBloodtype=df['bloodtype'].value_counts().idxmax()
print("The most common bloodtype is:",commonBloodtype)
#sort by height
df=df.sort_values(by='height',ascending=True)

print(df)
# print(filtered_df)