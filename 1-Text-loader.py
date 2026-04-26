from langchain_community.document_loaders import TextLoader

#Here utf-8 is used to catch and read any speacial characters in the file etc
loader = TextLoader('Data/cricket.txt', encoding='utf-8')

#This load function always returns a list of documents because it is assumed that user always loads a bunch of files and not a single one
docs = loader.load()

# print("\n=====quick demo view==========\n")
# print("This shows the actual document list object : \n ", docs)

# print("\n This shows the type of document :  ", type(docs))
# print("\n The length of the list is : ", len(docs))
# print("\n The content of the 1st element of the list : \n", docs[0])

#Lets try to use this document object
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

chain = prompt | model | parser 

#Here the content we can send the content of the document by accessing the page_content attribute of the document object.
result = chain.invoke({'poem' : docs[0].page_content})

print("\n========final outputs===============\n")
print(result)