import pandas as pd
import numpy as np

#reads in non-asian heads data 
ndata = pd.read_excel("SuperLighData.xlsx", skip_footer = 16)
print(ndata)
print()
print()
print("Circumference data is: " , ndata["Circumference"].sum(), ndata["Circumference"].mean(), ndata["Circumference"].min(), ndata["Circumference"].max(), ndata["Circumference"].std(), ndata["Circumference"].std()**2)
print("OETT top data is: " , ndata["OETT top"].sum(), ndata["OETT top"].mean(), ndata["OETT top"].min(), ndata["OETT top"].max(), ndata["OETT top"].std(), ndata["OETT top"].std()**2)
print("OETT bottom data is: " , ndata["OETT bottom"].sum(), ndata["OETT bottom"].mean(), ndata["OETT bottom"].min(), ndata["OETT bottom"].max(), ndata["OETT bottom"].std(), ndata["OETT bottom"].std()**2)
print("IPD data is: " , ndata["IPD"].sum(), ndata["IPD"].mean(), ndata["IPD"].min(), ndata["IPD"].max(), ndata["IPD"].std(), ndata["IPD"].std()**2)
print("IPD Left data is: " , ndata["Left"].sum(), ndata["Left"].mean(),ndata["Left"].min(),ndata["Left"].max(), ndata["Left"].std(), ndata["Left"].std()**2)
print("IPD Right data is: " , ndata["Right"].sum(), ndata["Right"].mean(),ndata["Right"].min(),ndata["Right"].max(), ndata["Right"].std(), ndata["Right"].std()**2)
nNonasian = 9 

#reads in asian heads data 
adata = pd.read_excel("SuperLighData.xlsx", skiprows = 15)
print(adata)
print()
print()
print("Circumference data is: " , adata["Circumference"].sum(), adata["Circumference"].mean(),adata["Circumference"].min(),adata["Circumference"].max(), adata["Circumference"].std(), adata["Circumference"].std()**2)
print("OETT top data is: " , adata["OETT top"].sum(), adata["OETT top"].mean(),adata["OETT top"].min(),adata["OETT top"].max(), adata["OETT top"].std(), adata["OETT top"].std()**2)
print("OETT bottom data is: " , adata["OETT bottom"].sum(), adata["OETT bottom"].mean(),adata["OETT bottom"].min(),adata["OETT bottom"].max(), adata["OETT bottom"].std(), adata["OETT bottom"].std()**2)
print("IPD data is: " , adata["IPD"].sum(), adata["IPD"].mean(),adata["IPD"].min(),adata["IPD"].max(), adata["IPD"].std(), adata["IPD"].std()**2)
print("IPD Left data is: " , adata["Left"].sum(), adata["Left"].mean(),adata["Left"].min(),adata["Left"].max(), adata["Left"].std(), adata["Left"].std()**2)
print("IPD Right data is: " , adata["Right"].sum(), adata["Right"].mean(),adata["Right"].min(),adata["Right"].max(), adata["Right"].std(), adata["Right"].std()**2)
nAsian = 10

