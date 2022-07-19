# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 18:08:35 2020

@author: hp
"""

import sys
import pandas as pd
import numpy as np
import plotly.offline as po
import cufflinks as cf

po.init_notebook_mode(connected=True)
cf.go_offline()

def createdata(data):
    if(data==1):
        x = np.random.rand(100,5)
        df1 = pd.DataFrame(x,columns=['A','B','C','D','E'])
    elif(data==2):
        x = [0,0,0,0,0]
        r1 = [0,0,0,0,0]
        r2 = [0,0,0,0,0]
        r3 = [0,0,0,0,0]
        r4 = [0,0,0,0,0]
        print("Enter the Values of the Columns : ")
        i = 0
        for i in [0,1,2,3,4]:
            x[i] = input()
            i = i+1
        print("Enter the Values for First Row : ")
        i = 0
        for i in [0,1,2,3,4]:
            r1[i] = int(input())
            i = i+1
        print("Enter the Values for Second Row : ")
        i = 0
        for i in [0,1,2,3,4]:
            r2[i] = int(input())
            i = i+1
        print("Enter the Values for Third Row : ")
        i = 0
        for i in [0,1,2,3,4]:
            r3[i] = int(input())
            i = i+1
        print("Enter the Values for Fourth Row : ")
        i = 0
        for i in [0,1,2,3,4]:
            r4[i] = int(input())
            i = i+1
        df1 = pd.DataFrame([r1,r2,r3,r4],columns=x)
    elif(data==3):
        file = input("Enter the Name of the File : ")
        x = pd.read_csv(file)
        df1 = pd.DataFrame(x)
    else:
        print("DataFrame Creation Failed Please Enter in Between 1 to 3 and Try Again...")
        sys.exit()
    return(df1)

def main(cat):
    if(cat == 1):
        print("\nSelect the Type of Plot you need to Plot by Writing 1 to 6 -")
        print(" 1. Line Plot")
        print(" 2. Scatter Plot")
        print(" 3. Bar Plot")
        print(" 4. Histogram Plot")
        print(" 5. Box Plot")
        print(" 6. Surface Plot")
        plot = int(input())
        output = plotter(plot)
    elif(cat == 2):
        print("\nSelect the Type of Plot you need to Plot by Writing 1 to 7 -")
        print(" 1. Line Plot")
        print(" 2. Scatter Plot")
        print(" 3. Bar Plot")
        print(" 4. Histogram Plot")
        print(" 5. Box Plot")
        print(" 6. Surface Plot")
        print(" 7. Bubble Plot")
        plot = int(input())
        output = plotter2(plot)
    else:
        output = print("Please Enter 1 or 2 and Try Again!...")
    return(output)
        
def plotter(plot):
    if(plot==1):
        finalplot = df1.iplot(kind='scatter')
    elif(plot==2):
        finalplot = df1.iplot(kind='scatter',mode = 'markers',symbol = 'x',colorscale = 'paired')
    elif(plot==3):
        finalplot = df1.iplot(kind='bar')
    elif(plot==4):
        finalplot = df1.iplot(kind='hist')
    elif(plot==5):
        finalplot = df1.iplot(kind='box')
    elif(plot==6):  
        finalplot = df1.iplot(kind='surface')
    else:
        finalplot = print("Select only between 1 to 6 and Try Again!...")
    return(finalplot)

def plotter2(plot):
    col = int(input("Enter the Number of Columns you want to Plot by Selecting only 1,2 or 3 : "))
    if(col==1):
        colm = input("Enter the Column you want to Plot by Selecting any Column from DataFrame Head : ")
        if(plot==1):
            finalplot = df1[colm].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[colm].iplot(kind='scatter',mode = 'markers',symbol = 'x',colorscale = 'paired')
        elif(plot==3):
            finalplot = df1[colm].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[colm].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[colm].iplot(kind='box')
        elif(plot==6 or plot==7):  
            finalplot = print("Bubble Plot and Surface Plot Require more than one Column Argument...")
        else:
            finalplot = print("Select only between 1 to 7 and Try Again!...")
    elif(col==2):
        print("Enter the Column you want to Plot by Selecting any Column from DataFrame Head : ")
        x = input("First Column : ")
        y = input("Second Column : ")
        if(plot==1):
            finalplot = df1[[x,y]].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[[x,y]].iplot(kind='scatter',mode = 'markers',symbol = 'x',colorscale = 'paired')
        elif(plot==3):
            finalplot = df1[[x,y]].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[[x,y]].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[[x,y]].iplot(kind='box')
        elif(plot==6):  
            finalplot = df1[[x,y]].iplot(kind='surface')
        elif(plot==7):
            size = input("Please Enter Size Column for Bubble Plot : ")
            finalplot = df1.iplot(kind = 'bubble',x=x,y=y,size=size) 
        else:
            finalplot = print("Select only between 1 to 7 and Try Again!...")
    elif(col==3):
        print("Enter the Column you want to Plot by Selecting any Column from DataFrame Head : ")
        x = input("First Column : ")
        y = input("Second Column : ")
        z = input("Third Column : ")
        if(plot==1):
            finalplot = df1[[x,y,z]].iplot(kind='scatter')
        elif(plot==2):
            finalplot = df1[[x,y,z]].iplot(kind='scatter',mode = 'markers',symbol = 'x',colorscale = 'paired')
        elif(plot==3):
            finalplot = df1[[x,y,z]].iplot(kind='bar')
        elif(plot==4):
            finalplot = df1[[x,y,z]].iplot(kind='hist')
        elif(plot==5):
            finalplot = df1[[x,y,z]].iplot(kind='box')
        elif(plot==6):  
            finalplot = df1[[x,y,z]].iplot(kind='surface')
        elif(plot==7):
            size = input("Please Enter Size Column for Bubble Plot : ")
            finalplot = df1.iplot(kind = 'bubble',x=x,y=y,z=z,size=size) 
        else:
            finalplot = print("Select only between 1 to 7 and Try Again!...")
            exit(1)
    else:
        finalplot = print("Please Enter only 1,2 or 3 and Try Again!...")
    return(finalplot)

print("Select the Type of Data you need to Plot (By Writing 1,2 or 3) -")
print(" 1. Random Data with 100 Rows and 5 Columns")
print(" 2. Customize DataFrame with 5 Columns and 4 Rows")
print(" 3. Upload csv/json/txt File")
data = int(input())
df1 = createdata(data)
print("Your DataFrame Head is Given Below Check the Columns to Plot using Cufflinks...\n")
print(df1.head())
print("\nWhat Kind of Plot you Need, The Complete Data Plot or Columns Plot...")
cat = int(input("Press 1 for Plotting all Columns or Press 2 for Specifying Columns to Plot : "))
ch = 'y'
while(ch.lower()=='y'):
    main(cat)
    ch = input("Want to Plot Another Graph using the Same Data...[Y/N] : ")