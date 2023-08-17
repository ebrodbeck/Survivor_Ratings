# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 09:21:22 2023

@author: brodbeck
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

a=.7

df=pd.read_csv('Survivor Season Ratings.csv')
dfav=pd.read_csv('suv_avgs.csv')
diff=pd.read_excel('diffs.xlsx')
dfavred=dfav[dfav.Site=='Reddit']

g3, b3 = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
#g2=plt.figure()
sns.kdeplot(ax=b3[0],data=diff,x='Reddit',hue='Tribes',fill=True,alpha=0.1,linewidth=2,palette=['Dodgerblue','Blue','Navy'])
b3[0].set(title="Reddit Rating vs Number of Tribes", xlabel="Rating")
#g3=plt.figure()
sns.kdeplot(ax=b3[1],data=diff,x='Reddit',hue='Format',fill=True,alpha=0.1,linewidth=2,palette=['Dodgerblue','Blue','Navy'])
b3[1].set(title="Reddit Rating vs Casting Format", xlabel="Rating")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#Season	Reddit	IMDB	RT	IMDB-Reddit	RT-Reddit
f01=plt.figure(figsize=(15,5))
a01=sns.lineplot(data=diff,x='Season',y='Reddit-IMDB',color='Black',label='Reddit-IMDB',linewidth=2.5)
a01=sns.lineplot(data=diff,x='Season',y='Reddit-RT',color='Red',label='Reddit-RotTom',linewidth=2.5)
a01.set_xticks(np.arange(1, 41, 1))
a01.set_ylabel('Difference (Reddit - Other Site)')
a01.set_title('Difference in Ratings - Negative=Reddit Over-dislikes, Positive = Reddit Over-likes')
plt.xlim(1,40)
plt.grid(True)
a01.text(x=5,y=-3.3,s='Thailand')
a01.text(x=22,y=-3.2,s='Redemption Isl.')
a01.text(x=24,y=-2.8,s='One World')
a01.text(x=35,y=-3,s='Ghost Island')
a01.text(x=38.5,y=-3.2,s='S39')
a01.text(x=5.5,y=1.8,s='Pearl Islands')
a01.text(x=14,y=1.8,s='China')
a01.text(x=17,y=1.7,s='Gabon')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

g1, b1 = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))
sns.kdeplot(ax=b1[0, 0],data=diff,x='Reddit',hue='Race',fill=True,alpha=.1,linewidth=2)
sns.kdeplot(ax=b1[0, 1],data=diff,x='Reddit',hue='Gender',fill=True,alpha=.1,linewidth=2)
sns.kdeplot(ax=b1[1, 0],data=diff,x='Reddit',hue='Age',fill=True,alpha=.1,linewidth=2)
sns.kdeplot(ax=b1[1, 1],data=diff,x='Reddit',hue='Race_Gender',fill=True,alpha=.01,linewidth=2)
b1[0, 0].set(title="Reddit Rating vs Winner Race", xlabel="Rating")
b1[0, 1].set(title="Reddit Rating vs Winner Gender", xlabel="Rating")
b1[1, 0].set(title="Reddit Rating vs Winner Age", xlabel="Rating")
b1[1, 1].set(title="Reddit Rating vs Winner Race+Gender", xlabel="Rating")
b1[1, 1].text(x=9, y=.06, s="Sandra (N=2)")
b1[0,0].text(x=9, y=.06, s="Sandra (N=2)")

#b1.set_title('Reddit's Rating vs Race of Winner')

#Season	Reddit	IMDB	RT	IMDB-Reddit	RT-Reddit
#f0=plt.figure(figsize=(10,5))
#a0=sns.barplot(data=dfav,x='Season',y='Rating',hue='Site',palette=['Orange','Yellow','Black'])
#plt.ylim(3,10)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

f00=plt.figure(figsize=(15,5))
a00=sns.barplot(data=dfavred,x='Season',y='Rating',color='lightblue',edgecolor='Navy')#,yerr=dfavred['std'])
a00.set_title('Survivor Seasons Ranked by Reddit')
a00.set_ylabel('Average Rating')
plt.ylim(0,10)


#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


g4, b4 = plt.subplots(nrows=3, ncols=2, figsize=(15, 15))               
#f1=plt.figure()
sns.kdeplot(ax=b4[0,0],data=df, x="S1", fill=True,alpha=a, label="Borneo",color=sns.color_palette("Blues",n_colors=10)[0])
sns.kdeplot(ax=b4[0,0],data=df, x="S2", fill=True,alpha=a, label="Outback",color=sns.color_palette("Blues",n_colors=10)[1])
sns.kdeplot(ax=b4[0,0],data=df, x="S3", fill=True,alpha=a, label="Africa",color=sns.color_palette("Blues",n_colors=10)[2])
sns.kdeplot(ax=b4[0,0],data=df, x="S4", fill=True,alpha=a, label="Marquesas",color=sns.color_palette("Blues",n_colors=10)[3])
sns.kdeplot(ax=b4[0,0],data=df, x="S5", fill=True,alpha=a, label="Thailand",color='darkgray')
sns.kdeplot(ax=b4[0,0],data=df, x="S6", fill=True,alpha=a, label="Amazon",color=sns.color_palette("Blues",n_colors=10)[4])
sns.kdeplot(ax=b4[0,0],data=df, x="S7", fill=True,alpha=a, label="Pearl Islands",color='purple')
sns.kdeplot(ax=b4[0,0],data=df, x="S8", fill=True,alpha=a, label="All Stars",color=sns.color_palette("Blues",n_colors=10)[5])
sns.kdeplot(ax=b4[0,0],data=df, x="S9", fill=True,alpha=a, label="Vanuatu",color=sns.color_palette("Blues",n_colors=10)[6])
sns.kdeplot(ax=b4[0,0],data=df, x="S10", fill=True,alpha=a, label="Palau",color=sns.color_palette("Blues",n_colors=10)[7])
sns.kdeplot(ax=b4[0,0],data=df, x="S11", fill=True,alpha=a, label="Guatemala",color=sns.color_palette("Blues",n_colors=10)[8])
sns.kdeplot(ax=b4[0,0],data=df, x="S12", fill=True,alpha=a, label="Panama",color=sns.color_palette("Blues",n_colors=10)[9])
b4[0,0].set(title='Old School Era',xlabel=' ')
b4[0,0].set_xlim(0,10)
b4[0,0].legend(loc='upper left')#, bbox_to_anchor=(1.02, 0.5))
#f2=plt.figure()
sns.kdeplot(ax=b4[0,1],data=df, x="S13", fill=True,alpha=a, label="Cook Islands",color=sns.color_palette("Blues",n_colors=10)[0])
sns.kdeplot(ax=b4[0,1],data=df, x="S14", fill=True,alpha=a, label="Fiji",color=sns.color_palette("Blues",n_colors=10)[1])
sns.kdeplot(ax=b4[0,1],data=df, x="S15", fill=True,alpha=a, label="China",color=sns.color_palette("Blues",n_colors=10)[2])
sns.kdeplot(ax=b4[0,1],data=df, x="S16", fill=True,alpha=a, label="Micronesia",color='Purple')
sns.kdeplot(ax=b4[0,1],data=df, x="S17", fill=True,alpha=a, label="Gabon",color=sns.color_palette("Blues",n_colors=10)[4])
sns.kdeplot(ax=b4[0,1],data=df, x="S18", fill=True,alpha=a, label="Tocancins",color=sns.color_palette("Blues",n_colors=10)[5])
b4[0,1].set_title('Experimental Era')
b4[0,1].set_xlabel(' ')
b4[0,1].set_xlim(0,10)
b4[0,1].legend(loc='upper left')#, bbox_to_anchor=(1.02, 0.5))
#f3=plt.figure()
sns.kdeplot(ax=b4[1,0],data=df, x="S19", fill=True,alpha=a, label="Samoa",color=sns.color_palette("Blues",n_colors=5)[0])
sns.kdeplot(ax=b4[1,0],data=df, x="S20", fill=True,alpha=a, label="Heroes v Villains",color='Purple')
sns.kdeplot(ax=b4[1,0],data=df, x="S21", fill=True,alpha=a, label="Nicaragua",color=sns.color_palette("Blues",n_colors=5)[1])
sns.kdeplot(ax=b4[1,0],data=df, x="S22", fill=True,alpha=a, label="Redemption Island",color=sns.color_palette("Blues",n_colors=5)[2])
sns.kdeplot(ax=b4[1,0],data=df, x="S23", fill=True,alpha=a, label="SoPa",color=sns.color_palette("Blues",n_colors=5)[3])
sns.kdeplot(ax=b4[1,0],data=df, x="S24", fill=True,alpha=a, label="One World",color=sns.color_palette("Blues",n_colors=5)[4])
b4[1,0].set_title('Hantz Era')
b4[1,0].set_xlabel(' ')
b4[1,0].set_xlim(0,10)
b4[1,0].legend(loc='upper left')#, bbox_to_anchor=(1.02, 0.5))
#f4=plt.figure()
sns.kdeplot(ax=b4[1,1],data=df, x="S25", fill=True,alpha=a, label="Phillipines",color=sns.color_palette("Blues",n_colors=3)[0])
sns.kdeplot(ax=b4[1,1],data=df, x="S26", fill=True,alpha=a, label="Caramoan",color=sns.color_palette("Blues",n_colors=3)[1])
sns.kdeplot(ax=b4[1,1],data=df, x="S27", fill=True,alpha=a, label="BvW1",color=sns.color_palette("Blues",n_colors=3)[2])
sns.kdeplot(ax=b4[1,1],data=df, x="S28", fill=True,alpha=a, label="Cagayan",color='Purple')
b4[1,1].set_title('Renaissance Era')
b4[1,1].set_xlabel(' ')
b4[1,1].set_xlim(0,10)
b4[1,1].legend(loc='upper left')#, bbox_to_anchor=(1.02, 0.5))
#f5=plt.figure()
sns.kdeplot(ax=b4[2,0],data=df, x="S36", fill=True,alpha=a, label="Ghost Island",color='darkgray')
sns.kdeplot(ax=b4[2,0],data=df, x="S29", fill=True,alpha=a, label="San Juan Del Sur",color=sns.color_palette("Blues",n_colors=6)[0])
sns.kdeplot(ax=b4[2,0],data=df, x="S30", fill=True,alpha=a, label="Worlds Apart",color=sns.color_palette("Blues",n_colors=6)[1])
sns.kdeplot(ax=b4[2,0],data=df, x="S31", fill=True,alpha=a, label="Second Chance",color='Purple')
sns.kdeplot(ax=b4[2,0],data=df, x="S32", fill=True,alpha=a, label="Kaoh Rong",color=sns.color_palette("Blues",n_colors=6)[2])
sns.kdeplot(ax=b4[2,0],data=df, x="S33", fill=True,alpha=a, label="MvGx",color=sns.color_palette("Blues",n_colors=6)[3])
sns.kdeplot(ax=b4[2,0],data=df, x="S34", fill=True,alpha=a, label="Game Changers",color=sns.color_palette("Blues",n_colors=6)[4])
sns.kdeplot(ax=b4[2,0],data=df, x="S35", fill=True,alpha=a, label="HvHvH",color=sns.color_palette("Blues",n_colors=6)[5])
b4[2,0].set_title('Big Moves Era')
b4[2,0].set_xlabel('Rating')
b4[2,0].set_xlim(0,10)
b4[2,0].legend(loc='upper left')#, bbox_to_anchor=(1.02, 0.5))
#f6=plt.figure()
sns.kdeplot(ax=b4[2,1],data=df, x="S37", fill=True,alpha=a, label="DvG",color='Purple')
sns.kdeplot(ax=b4[2,1],data=df, x="S38", fill=True,alpha=a, label="Edge of Extinction",color=sns.color_palette("Blues",n_colors=5)[0])
sns.kdeplot(ax=b4[2,1],data=df, x="S39", fill=True,alpha=a, label="Island of Idols",color='darkgray')
sns.kdeplot(ax=b4[2,1],data=df, x="S40", fill=True,alpha=a, label="Winners at War",color=sns.color_palette("Blues",n_colors=5)[1])
sns.kdeplot(ax=b4[2,1],data=df, x="S41", fill=True,alpha=a, label="41",color=sns.color_palette("Blues",n_colors=5)[2])
sns.kdeplot(ax=b4[2,1],data=df, x="S42", fill=True,alpha=a, label="42",color=sns.color_palette("Blues",n_colors=5)[3])
sns.kdeplot(ax=b4[2,1],data=df, x="S43", fill=True,alpha=a, label="43",color=sns.color_palette("Blues",n_colors=5)[4])
b4[2,1].set_title('Big Twists Era')
b4[2,1].set_xlabel('Rating')
b4[2,1].set_xlim(0,10)
b4[2,1].legend(loc='upper left')#, bbox_to_anchor=(1.02, 0.5))