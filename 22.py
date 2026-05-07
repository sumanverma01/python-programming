import matplotlib.pyplot as plt
x = [ 10,20, 30, 40]
y = [ "a","b","c","d"]
ex= [ 0.4, 0, 0 ,0]

plt.pie(x,labels=y,explode=ex,autopct="%0.3f%%",shadow=True,radius=1,labeldistance=1.2,startangle=100)
plt.show()