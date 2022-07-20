# read text from file 
file_location = './drive/My Drive/DataAnalysis/.txt'
with open(file_location) as f:
  data = f.read()
  data = ' '.join(data.split('\n'))

#separate user messages and datetime of the chat
import re
pattern = '\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}\s-\s'
user_messages = re.split(pattern, data)[1:]
message_dates =  re.findall(pattern, data)
print(data)
print(user_messages)
# print(message_dates)
# load user messages and dates into dataframe
import pandas as pd
df = pd.DataFrame({'user_message':user_messages, 'message_date': message_dates})
# convert message_date type
df['message_date'] = pd.to_datetime(df['message_date'], format='%d/%m/%Y, %H:%M - ')

df.rename(columns={'message_date': 'date'}, inplace=True)

# separate users and messages 
users = []
messages = []
for message in df['user_message']:
  entry = re.split('([\w\W]+?):\s', message)
  if entry[1:]:# user name
    users.append(entry[1])
    messages.append(entry[2])
  else:
    users.append('group_notification')
    messages.append(entry[0])

df['user'] =  users
df['message'] = messages
df.drop(columns=['user_message'], inplace=True)

print(df.tail())




# data cleaning 
# 1. remove all the <Media omitted> messages
images = df[df['message'] == '<Media omitted> ']
print("Total number of Images + Videos Shared: ", len(images))
df.drop(images.index, inplace=True)
# 2. remove all group notifications
notifications = df[df['user'] == 'group_notification']
print("Total Group Notifications: ", len(notifications))
df.drop(notifications.index, inplace=True)

# reset the index 
df.reset_index(inplace=True, drop=True)
df.tail()





import emoji
from collections import Counter
# Count all the emojis in the chat.
emoji_counter = Counter()
emojis_list = map(lambda x: ''.join(x.split()), emoji.UNICODE_EMOJI['en'].keys())
r = re.compile('|'.join(re.escape(p) for p in emojis_list))
for index, row in df.iterrows():
  emojis_found = r.findall(row['message'])
  for emoji_f in emojis_found:
    emoji_counter[emoji_f] +=1

for item in emoji_counter.most_common(10):
  print(f'{item[0]} - {item[1]}')






import emoji
from collections import Counter
# Count all the emojis in the chat.
emoji_counter = Counter()
# emojis_list = map(lambda x: ''.join(x.split()), emoji.UNICODE_EMOJI.keys())
# print(list(emojis_list))
# r = re.compile('|'.join(re.escape(p) for p in emojis_list))
emojis_iter = map(lambda y: y, emoji.UNICODE_EMOJI['en'].keys())
regex_set = re.compile('|'.join(re.escape(em) for em in emojis_iter))
for index, row in df.iterrows():
  emojis_found = regex_set.findall(row['message'])
  for emoji_f in emojis_found:
    emoji_counter[emoji_f] +=1

for item in emoji_counter.most_common(10):
  print(f'{item[0]} - {item[1]}')
  
  
  
  
  
  type(emoji.UNICODE_EMOJI)
emoji.UNICODE_EMOJI.val




#3 sleep cycle 
df['hour'] = df['date'].apply(lambda x: x.hour)
df.groupby(['hour']).size().sort_index().plot(x="hour", kind='bar')





from wordcloud import WordCloud, STOPWORDS
all_words = ' '
stopwords = STOPWORDS.update(['lo', 'ge', 'Lo', 'illa', 'yea', 'ella', 'en', 'na', 'En', 'yeah', 'alli', 'ide', 'okay', 'ok', 'will'])
for msg in df['message'].values:
  words = str(msg).lower().split()
  for word in words:
    all_words = all_words + word + ' '

wordcloud = WordCloud(width = 1000, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(all_words) 


wordcloud.to_image()