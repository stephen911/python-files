# Import libraries to be used
import pandas as pd
import numpy as np
import re
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import *
import datetime as dt
from matplotlib.ticker import MaxNLocator
import regex
import emoji
from seaborn import *
#from heatmap import heatmap
from wordcloud import WordCloud , STOPWORDS , ImageColorGenerator
from nltk import *
from plotly import express as px



#filepath = input("C:\Users\tarique.akhtar\Downloads\WhatsAppSchoolChat.txt")
df = pd.read_csv(r"_chat", sep = "delimiter",
                skip_blank_lines = True, header = None)


df.head(20)


#df.shape


### Checking no. of authors of group
#df['sender'].nunique()



### Checking authors of group
df['sender'].unique()




### Word Cloud of mostly used word in our Group
text = " ".join(review for review in df.Message)
wordcloud = WordCloud(stopwords=STOPWORDS, background_color="white").generate(text)
  ### Display the generated image:
plt.figure( figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()




### Creates a list of unique Authors
l = df.sender.unique()
for i in range(len(l)):
  ### Filtering out messages of particular user
  req_df = df[df["sender"] == l[i]]
  ### req_df will contain messages of only one particular user
  print(l[i],'  ->  ',req_df.shape[0])
  
  



  
X = activity_data["sender"][:10]
Y = activity_data.n_count[:10]

plt.figure(figsize=[10,10])

plt.title("Top 10 Active Members", size = 16)

plt.bar(x = X, height= Y, color = "seagreen")
plt.xticks(rotation = 90, size = 12)
plt.yticks(size = 12)

for i in range(0,10):
    plt.annotate(s = Y[i], xy = (i-0.25,Y[i]+5), size = 12)

plt.show()




z = df['Date'].value_counts() 
z1 = z.to_dict() #converts to dictionary
df['Msg_count'] = df['Date'].map(z1)
### Timeseries plot 
fig = px.line(x=df['Date'],y=df['Msg_count'])
fig.update_layout(title='Analysis of number of messages using TimeSeries plot.',
                  xaxis_title='Month',
                  yaxis_title='No. of Messages')
fig.update_xaxes(nticks=20)
fig.show()




from matplotlib import *
def daily_msgs(df, plot=False):
    grouped = df.groupby("Date", as_index=False)["sender"]
    df_ = grouped.count()
    df_.columns = ["Date", "Count"]
    if plot:
        plt.figure(figsize=[10,10])

        plt.title("Daily Message Count", size = 16)
        plt.bar(x=df_["Date"], height=df_["Count"], color = "seagreen")
        plt.xticks(rotation = 90, size = 12)
        plt.yticks(size = 12)

    return df_
daily_msgs(df, plot=True)






fig = plt.figure(figsize=[20,10])
mpl.rcParams['font.size'] = 14.0

fig.suptitle("Activity wrt Time Meridian", size = 16)

gs = GridSpec(2,3) # 2 rows and 3 columns
ax1 = fig.add_subplot(gs[0,0]) # first row, first col
ax2 = fig.add_subplot(gs[0,1]) # first row, second col
ax3 = fig.add_subplot(gs[1,0]) # second row, first col
ax4 = fig.add_subplot(gs[1,1]) # second row, second col
ax5 = fig.add_subplot(gs[:,2]) # all row, third col

# Pie plot for messages shared in AM time meridian
ax1.pie(amhourcounts.values, labels = amhourcounts.index)
ax1.set_title("AM")
# Bar plot for messages shared in AM time meridian
ax2.bar(amhourcounts.index,amhourcounts.values)

# Pie plot for messages shared in PM time meridian
ax3.pie(pmhourcounts.values, labels = pmhourcounts.index)
ax3.set_title("PM")
# Bar plot for messages shared in PM time meridian
ax4.bar(pmhourcounts.index,pmhourcounts.values)

# Bar plot showing AM vs PM
ax5.bar(["AM","PM"], [len(amhours),len(pmhours)])
ax5.annotate(s = str(round(100*len(amhours)/(len(amhours)+len(pmhours)))) + "%", xy = [0,len(amhours)/2], color = "white", size = 14, horizontalalignment = "center")
ax5.annotate(s = str(round(100*len(pmhours)/(len(amhours)+len(pmhours)))) + "%", xy = [1,len(pmhours)/2], color = "white", size = 14, horizontalalignment = "center")



plt.show()