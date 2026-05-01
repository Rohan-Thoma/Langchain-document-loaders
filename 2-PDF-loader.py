from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Data/dl-curriculum.pdf")

docs = loader.load()

print("This shows the length of the actual document list object : \n ", len(docs))

print("\n This shows the actual document page content : \n ", docs[0].page_content)

print("\n This shows the actual document metadata : \n ", docs[1].metadata)