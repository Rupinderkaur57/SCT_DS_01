import pandas as pd
import matplotlib.pyplot as plt
#create a simple dataset with age and gender 
data={'Age':[25,30,22,40,35,28,22,22,33,27,29,30,42,38,36,44],
      'Gender':['Male','Female','Female','Male','Female','Male',
                'Female','Male','Female','Male','Male','Female',
                'Male','Male','Male','Female']
}
df=pd.DataFrame(data)
print(df)

plt.hist(df['Age'], bins=range(0,101,10),
         color='skyblue', edgecolor='black')
plt.xticks(range(0,101,10))
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age Distribution')
plt.show()

gender_counts=df['Gender'].value_counts()
gender_counts.plot(kind='bar',color='purple',edgecolor='black')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Distribution')
plt.show()