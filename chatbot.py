# %%
!pip install pypdf
!pip install bardapi

# %%
from pypdf import PdfReader
from bardapi import Bard
import os
import time

# %%

from google.colab import drive
drive.mount('/content/drive')

# %% [markdown]
# Here add your file name and make changes to your directory based on your path

# %%
directory = '/content/drive/MyDrive/chatBotData/'
filename = 'yourpdfname.pdf'

# %% [markdown]
# /content/drive/MyDrive/chatBotData/mydata.pdf is the path where we save data for chat

# %%
# Getting access of PDF file 
pdffileobject = open(directory+filename,'rb')

# read the file 

pdfReader = PdfReader(pdffileobject)
text = []
summary = ''
# adding all the pages in a array of TEXT
for i in range(0,len(pdfReader.pages)):
  pageObj = pdfReader.pages[i].extract_text()
  pageObj = pageObj.replace('\t\r',"")
  pageObj = pageObj.replace('xa0',"")
  text.append(pageObj)
  # print(text)

# %% [markdown]
# <!-- below step is using for optimization purpose to merge multiple pages in one so bard can read in quick -->

# %% [markdown]
# This is a optimization part you can skip what i planned was as there will be multiple pages i will collab everthing in one page so bard can read easily.

# %%
def mergepages(list,charPerPage):
  newList = []
  for i in range(0,len(list),charPerPage):
    newList.append(''.join(list[i:i+charPerPage]))
  return newList

newListcreated = mergepages(text,3)
print(len(text))
print(len(newListcreated))



# %%


# %% [markdown]
# configure the BARD

# %%
os.environ['_BARD_API_KEY'] = "here add your Bard secret Key follwed by ."

# %%
api_key = os.environ.get('_BARD_API_KEY')

# %%
def userInteraction(prompt):
  Response = Bard().get_answer(prompt)['content']
  return Response

# %%
prompt = "your task is to act as chat bot dont go for conversation and your question * If he is a software engineer, you could ask How many years of experience does he have in software development?s .give exact answer"

Response = userInteraction(prompt)
print(Response)


