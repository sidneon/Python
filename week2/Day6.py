import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
'''
#Q1. Create a histogram with multiple data overlaid

data1 = np.random.normal(loc=0, scale=1, size=1000)
data2 = np.random.normal(loc=2, scale=1.5, size=1000)
data3 = np.random.normal(loc=4, scale=2, size=1000)

plt.hist(data1, bins=30, alpha=0.5, label="Data1", color="blue")
plt.hist(data2, bins=30, alpha=0.5, label="Data2", color="red")
plt.hist(data3, bins=30, alpha=0.5, label="Data3", color="green")
plt.title("Histogram with Multiple data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

#Q2. Use seaborn to create a violin plot or box for visualizing distribution

tips = sns.load_dataset("tips")

sns.violinplot(x="day", y="total_bill",  data=tips)
sns.boxplot(x="day", y="total_bill", data=tips)

plt.title("Violin plot")
plt.show()
print(tips.columns)
'''
#Q3. Combine multiple plots in a single figure using matplotlib subset

x = np.linspace(0, 10, 100)
y1 = np.sin(x) 
y2 = np.cos(x)
y3 = np.tan(x)

plt.figure(figsize=(10, 8), )
#subplot of sine wave
plt.subplot(2, 2, 1)
plt.plot(x, y1, label="Sine wave", color= "blue")
plt.title("Sine Wave")
plt.xlabel("X-aixs")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()

#subplot of cosine wave
plt.subplot(2, 2, 2)
plt.plot(x, y2, label="Cosine Wave", color="green")
plt.title("Cosine Wave")
plt.xlabel("X-aixs")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()

#Tangent Wave
plt.subplot(2, 2, 3)
plt.plot(x, y3, label="Tangent Wave")
plt.title("Tangent Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-label")
plt.grid(True)
plt.legend()
#Cosine and Sine wave

plt.subplot(2, 2, 4)
plt.plot(x, y1, label="Sine Wave")
plt.plot(x, y2, label="Cosine_Wave", color="red")
plt.title("Sine and Cosine")
plt.xlabel("X-aixs")
plt.ylabel("Y-axis")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

