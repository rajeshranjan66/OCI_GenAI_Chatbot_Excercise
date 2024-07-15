import chromadb
from langchain_community.vectorstores import Chroma
from chromadb.config import Settings

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers.document_compressors import CohereRerank
import json
from langchain_community.llms import OCIGenAI
from langchain_community.embeddings import OCIGenAIEmbeddings
import oci

import os
from uuid import uuid4

unique_id = uuid4().hex[0:8]
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = f"TOGAF_Chatbot - {unique_id}"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = "<<>>>>"  # Update to your API ke
#In this demo we will explore using RetirvalQA chain to retrieve relevant documents and send these as a context in a query.
# We will use Chroma vectorstore.


#Step 1 - this will set up chain , to be called later
print("LangSmith Project id"+unique_id)
def create_chain():
    client = chromadb.HttpClient(host="127.0.0.1",settings=Settings(allow_reset=True))
    embeddings = OCIGenAIEmbeddings(
    model_id="cohere.embed-english-v3.0",
    service_endpoint="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com",
    compartment_id="<<Your comp Id>>"
    )
    db = Chroma(client=client, embedding_function=embeddings)
    #retv = db.as_retriever(search_type="mmr", search_kwargs={"k": 7})
    retv = db.as_retriever(search_kwargs={"k": 8})

    llm = OCIGenAI(
        model_id="cohere.command",
        service_endpoint="https://inference.generativeai.us-chicago-1.oci.oraclecloud.com",
        compartment_id="Your comp Id>",
        model_kwargs={"max_tokens":200}
        )
    memory = ConversationBufferMemory(llm=llm, memory_key="chat_history", return_messages=True, output_key='answer')

    qa = ConversationalRetrievalChain.from_llm(llm, retriever=retv , memory=memory,
                                               return_source_documents=True)
    return qa

#Step 2 - create chain, here we create a ConversationalRetrievalChain.

chain = create_chain()

#Step 3 - here we declare a chat function
def chat(user_message):
    # generate a prediction for a prompt
    bot_json = chain.invoke({"question": user_message})
    print(bot_json)
    return {"bot_response": bot_json}

#Step 4 - here we setup Streamlit text input and pass input text to chat function.
# chat function returns the response and we print it.

if __name__ == "__main__":
    import streamlit as st
    st.set_page_config(page_title="TOGAF Virtual Assistant")
    st.title("TOGAF Virtual Assistant")
    st.subheader("Welcome to The Open Group Architecture Framework (TOGAF) Virtual Assistant")
    col1 , col2 = st.columns([4,1])

    user_input = st.chat_input()
    with col1:
        col1.subheader("*** Ask me anything about TOGAF ***")
        #col2.subheader("References")
        if "messages" not in st.session_state:
            st.session_state.messages = []
        if user_input:
            bot_response = chat(user_input)
            st.session_state.messages.append({"role" : "chatbot", "content" : bot_response})
            #st.write("OU Assistant Response: ", bot_response)
            for message in st.session_state.messages:
                st.chat_message("user")
                st.write("Question: ", message['content']['bot_response']['question'])
                st.chat_message("assistant")
                st.write("Answer: ", message['content']['bot_response']['answer'])
            #with col2:
                st.chat_message("assistant")
                for doc in message['content']['bot_response']['source_documents']:
                    st.write("Reference: ", doc.metadata['source'] + "  \n"+ "-page->"+str(doc.metadata['page']))
