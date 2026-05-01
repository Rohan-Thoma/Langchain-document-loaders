from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

#This acts a wrapper for other document loaders which take the file inputs etc
loader = DirectoryLoader(
    path = 'Data/Books', #This is the folder name
    glob = "*pdf", #This shows the type of file patterns which need to be grabbed.
    loader_cls=PyPDFLoader #This is the actual document loader which loads the files etc
)
 
docs = loader.lazy_load()

print("\n Metadata printing with lazy load \n:")

limit = 0
for document in docs:
    print(document.metadata)
    limit+=1
    if limit ==5:
        break


