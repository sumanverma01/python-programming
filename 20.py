import matplotlib.pyplot as plt
x= [ "python","anconda","azgar","titanboa"]
y =[33, 35, 77, 22]
c= [ "r","g","b","y"]
plt.xlabel("language", fontsize=22)
plt.ylabel("number", fontsize=23)
plt.title("ies",fontsize=20)
plt.bar(x,y,width=0.5,color=c,align="edge",edgecolor="black",linewidth=10,linestyle=":",alpha=0.5,label="data" )
plt.legend(loc="center left")
plt.show()
