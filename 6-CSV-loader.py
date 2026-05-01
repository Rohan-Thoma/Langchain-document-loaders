from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Data/Social_Network_Ads.csv')

data = loader.load()

print("This shows the length of the actual document list object : \n ", len(data))

print("\n This shows the actual document page content : \n ", data[0].page_content)