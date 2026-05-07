import pandas as pd 
x= [1,2,3,4]
y = pd.Series(x,index=["a","b","c","d"],dtype="float")
print(y)
yy={
    "d":[1,2,3,4],"c":[22222],"e":["a","b","c","d"]
}
zz=pd.Series(yy)
print(zz)

xc = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10]])
print(xc)
