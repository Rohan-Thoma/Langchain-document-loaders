from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

#This acts a wrapper for other document loaders which take the file inputs etc
loader = DirectoryLoader(
    path = 'Data/Books', #This is the folder name
    glob = "*pdf", #This shows the type of file patterns which need to be grabbed.
    loader_cls=PyPDFLoader #This is the actual document loader which loads the files etc
)
 
docs = loader.load()

#This actually loads all the pages from all the documents in a single list
print("\n Number of documents loaded = ", len(docs))

#This shows the content of the 1st page
print("\n This shows the 10th page document page content : \n ", docs[10].page_content)

#Lets see the content of the 2nd page
print("\n This shows the 2nd page document metadata : \n ", docs[1].metadata)


docs = loader.lazy_load()

print("\n Metadata printing with lazy load \n:")
for document in docs[1:5]:
    print(document.metadata)


