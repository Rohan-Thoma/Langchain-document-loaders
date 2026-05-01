from langchain_community.document_loaders import WebBaseLoader

url = "https://www.marutisuzukidrivingschool.com/"

loader = WebBaseLoader(url)

docs = loader.load()

print("This shows the length of the actual document list object : \n ", len(docs))

# print("\n This shows the actual document page content : \n ", docs[0].page_content)
 
#Lets try to use this document object
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'Answer the question \n {question} from the following text  - \n {text}',
    input_variables=['text', 'question'] 
)

chain = prompt | model | parser 

#Here the content we can send the content of the document by accessing the page_content attribute of the document object.
result = chain.invoke({'question' :" In how many days can a newbie learn driving from this driving school? ", 'text':  docs[0].page_content})

print("\n========final outputs===============\n")
print(result)