from langchain_community.embeddings import OCIGenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.embeddings import CohereEmbeddings
#The class `Chroma` was deprecated in LangChain 0.2.9 and will be removed in 0.4. An updated version of the class exists in the langchain-chroma package and should be used instead. 
#To use it run `pip install -U langchain-chroma` and import as `from langchain_chroma import Chroma`.

from langchain_chroma import Chroma 


pdf_loader = PyPDFDirectoryLoader("./pdf-docs")

loaders = [pdf_loader]

documents = []
for loader in loaders:
    documents.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(chunk_size=2500, chunk_overlap=100)
all_documents = text_splitter.split_documents(documents)

print(f"Total number of documents: {len(all_documents)}")

#Step 1 - setup OCI Generative AI llm

embeddings = OCIGenAIEmbeddings(
    model_id="cohere.embed-english-v3.0",
    service_endpoint="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com",
    compartment_id="<<Your comp Id>>>",
    model_kwargs={"truncate":True}
)

#Step 2 - since OCIGenAIEmbeddings accepts only 96 documents in one run , we will input documents in batches.

# Set the batch size
batch_size = 96

# Calculate the number of batches
num_batches = len(all_documents) // batch_size + (len(all_documents) % batch_size > 0)


db = Chroma(embedding_function=embeddings , persist_directory="./chromadb")
retv = db.as_retriever()

# Iterate over batches
for batch_num in range(num_batches):
    # Calculate start and end indices for the current batch
    start_index = batch_num * batch_size
    end_index = (batch_num + 1) * batch_size
    # Extract documents for the current batch
    batch_documents = all_documents[start_index:end_index]
    # Your code to process each document goes here
    retv.add_documents(batch_documents)
    print(start_index, end_index)

#Step 4 - here we persist the collection
#In 0.4.x, Chroma no longer supports the manual persistence method, so you should not be calling it if you use newer Chroma and LC. 
#Don't worry your data is saved the moment the docs are added to Chroma with Chroma.from_documents.
#db.persist()





