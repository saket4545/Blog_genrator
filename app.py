import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

def getllama_response(input_text,no_of_words,blog_style):
    llm = CTransformers(model="C:\\Users\\saket\\OneDrive\\Desktop\\langchain\\blog_genrator\\model\\llama-2-7b-chat.ggmlv3.q8_0.bin", model_type="llama", config={'max_new_tokens': 256, 'temperature': 0.6})



    template ="""
        please write a blog for {blog_style} job profile about a topic {input_text} with {no_of_words} words
        """
    
    prompt= PromptTemplate(input_variables=["style","text","n_words"],template=template)

    response=llm(prompt.format(blog_style=blog_style,input_text=input_text,no_of_words=no_of_words))
    print(response)
    return response











st.set_page_config(page_title="LangChain", 
                    page_icon=":📜:",
                    layout="centered",
                    initial_sidebar_state="collapsed")



st.header("Welcome to blog generator📜")

input_text= st.text_input("Enter the topic here")
col1,col2 = st.columns([4,4])

with col1:
    no_of_words= st.text_input("No of words")

with col2:
    blog_style=st.selectbox("Select blog style",("Reserachers","Datascientist","common people"),index=0)

submit= st.button("GENERATE")

if submit:
    st.write(getllama_response(input_text,no_of_words,blog_style))


