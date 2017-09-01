import pandas as pd
import numpy as np
import scipy as sp 
from scipy import stats
from scipy.special import stdtr

#reads in non-asian heads data 
ndata = pd.read_excel("SuperLiteData.xlsx", skip_footer = 15)
print(ndata)
nNonasian = 9 
nndof = nNonasian - 1
print()
print()

#reads in asian heads data 
adata = pd.read_excel("SuperLiteData.xlsx", skiprows = 15)
print(adata)
nAsian = 10
nadof = nAsian - 1

print()
print()
print("Non-Asian Data Summary")
print("---------------------------")
print("Circumference data is: " , ndata["Circumference"].sum(), ndata["Circumference"].mean(), ndata["Circumference"].min(), ndata["Circumference"].max(), ndata["Circumference"].std(), ndata["Circumference"].std()**2)
print("OETT top data is: " , ndata["OETT top"].sum(), ndata["OETT top"].mean(), ndata["OETT top"].min(), ndata["OETT top"].max(), ndata["OETT top"].std(), ndata["OETT top"].std()**2)
print("OETT bottom data is: " , ndata["OETT bottom"].sum(), ndata["OETT bottom"].mean(), ndata["OETT bottom"].min(), ndata["OETT bottom"].max(), ndata["OETT bottom"].std(), ndata["OETT bottom"].std()**2)
print("IPD data is: " , ndata["IPD"].sum(), ndata["IPD"].mean(), ndata["IPD"].min(), ndata["IPD"].max(), ndata["IPD"].std(), ndata["IPD"].std()**2)
print("IPD Left data is: " , ndata["Left"].sum(), ndata["Left"].mean(),ndata["Left"].min(),ndata["Left"].max(), ndata["Left"].std(), ndata["Left"].std()**2)
print("IPD Right data is: " , ndata["Right"].sum(), ndata["Right"].mean(),ndata["Right"].min(),ndata["Right"].max(), ndata["Right"].std(), ndata["Right"].std()**2)
print()
print()
print("Asian Data Summary")
print("---------------------------")
print("Circumference data is: " , adata["Circumference"].sum(), adata["Circumference"].mean(),adata["Circumference"].min(),adata["Circumference"].max(), adata["Circumference"].std(), adata["Circumference"].std()**2)
print("OETT top data is: " , adata["OETT top"].sum(), adata["OETT top"].mean(),adata["OETT top"].min(),adata["OETT top"].max(), adata["OETT top"].std(), adata["OETT top"].std()**2)
print("OETT bottom data is: " , adata["OETT bottom"].sum(), adata["OETT bottom"].mean(),adata["OETT bottom"].min(),adata["OETT bottom"].max(), adata["OETT bottom"].std(), adata["OETT bottom"].std()**2)
print("IPD data is: " , adata["IPD"].sum(), adata["IPD"].mean(),adata["IPD"].min(),adata["IPD"].max(), adata["IPD"].std(), adata["IPD"].std()**2)
print("IPD Left data is: " , adata["Left"].sum(), adata["Left"].mean(),adata["Left"].min(),adata["Left"].max(), adata["Left"].std(), adata["Left"].std()**2)
print("IPD Right data is: " , adata["Right"].sum(), adata["Right"].mean(),adata["Right"].min(),adata["Right"].max(), adata["Right"].std(), adata["Right"].std()**2)

print()
print()
print("t-test calculations")
print("---------------------------")
print("Circumference Probability Calculations")
tf = (adata["Circumference"].mean() - ndata["Circumference"].mean())/((((adata["Circumference"].std()**2)/(nAsian)) + ((ndata["Circumference"].std()**2)/(nNonasian)))**(1/2))
dof = ((((adata["Circumference"].std()**2)/nAsian) + ((ndata["Circumference"].std()**2)/nNonasian))**2)/(((adata["Circumference"].std()**2)**2)/(nAsian**2*nadof) + ((ndata["Circumference"].std()**2)**2)/(nNonasian**2*nndof))
pf = 2*stdtr(dof, -np.abs(tf))
print("formula:              t = %g  p = %g" % (tf, pf))
print(dof)

print()
print("OETT top Probability Calculations")
tfO = (adata["OETT top"].mean() - ndata["OETT top"].mean())/((((adata["OETT top"].std()**2)/(nAsian)) + ((ndata["OETT top"].std()**2)/(nNonasian)))**(1/2))
dofO = ((((adata["OETT top"].std()**2)/nAsian) + ((ndata["OETT top"].std()**2)/nNonasian))**2)/(((adata["OETT top"].std()**2)**2)/(nAsian**2*nadof) + ((ndata["OETT top"].std()**2)**2)/(nNonasian**2*nndof))
pfO = 2*stdtr(dofO, -np.abs(tfO))
print("formula:              t = %g  p = %g" % (tfO, pfO))
print(dofO)

print()
print("OETT bottom Probability Calculations")
tfb = (adata["OETT bottom"].mean() - ndata["OETT bottom"].mean())/((((adata["OETT bottom"].std()**2)/(nAsian)) + ((ndata["OETT bottom"].std()**2)/(nNonasian)))**(1/2))
dofb = ((((adata["OETT bottom"].std()**2)/nAsian) + ((ndata["OETT bottom"].std()**2)/nNonasian))**2)/(((adata["OETT bottom"].std()**2)**2)/(nAsian**2*nadof) + ((ndata["OETT bottom"].std()**2)**2)/(nNonasian**2*nndof))
pfb = 2*stdtr(dofb, -np.abs(tfb))
print("formula:              t = %g  p = %g" % (tfb, pfb))
print(dofb)

print()
print("IPD Probability Calculations")
tfipd = (adata["IPD"].mean() - ndata["IPD"].mean())/((((adata["IPD"].std()**2)/(nAsian)) + ((ndata["IPD"].std()**2)/(nNonasian)))**(1/2))
dofipd = ((((adata["IPD"].std()**2)/nAsian) + ((ndata["IPD"].std()**2)/nNonasian))**2)/(((adata["IPD"].std()**2)**2)/(nAsian**2*nadof) + ((ndata["IPD"].std()**2)**2)/(nNonasian**2*nndof))
pfipd = 2*stdtr(dofipd, -np.abs(tfipd))
print("formula:              t = %g  p = %g" % (tfipd, pfipd))
print(dofipd)

print()
print("IPD Left Probability Calculations")
tfleft= (adata["Left"].mean() - ndata["Left"].mean())/((((adata["Left"].std()**2)/(nAsian)) + ((ndata["Left"].std()**2)/(nNonasian)))**(1/2))
dofleft = ((((adata["Left"].std()**2)/nAsian) + ((ndata["Left"].std()**2)/nNonasian))**2)/(((adata["Left"].std()**2)**2)/(nAsian**2*nadof) + ((ndata["Left"].std()**2)**2)/(nNonasian**2*nndof))
pfleft = 2*stdtr(dofleft, -np.abs(tfleft))
print("formula:              t = %g  p = %g" % (tfleft, pfleft))
print(dofleft)

print()
print("IPD Right Probability Calculations")
tfright = (adata["Right"].mean() - ndata["Right"].mean())/((((adata["Right"].std()**2)/(nAsian)) + ((ndata["Right"].std()**2)/(nNonasian)))**(1/2))
dofright = ((((adata["Right"].std()**2)/nAsian) + ((ndata["Right"].std()**2)/nNonasian))**2)/(((adata["Right"].std()**2)**2)/(nAsian**2*nadof) + ((ndata["Right"].std()**2)**2)/(nNonasian**2*nndof))
pfright = 2*stdtr(dofright, -np.abs(tfright))
print("formula:              t = %g  p = %g" % (tfright, pfright))
print(dofright)
