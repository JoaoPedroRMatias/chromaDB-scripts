from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_openai import OpenAIEmbeddings
import chromadb


load_dotenv()

def get_vectorial_db(question_message):
    client = chromadb.HttpClient(host='localhost', port=8000)
    embeddings = OpenAIEmbeddings()

    collection_name = ""
    collection = client.get_collection(name=collection_name)

    query_embedding = embeddings.embed_query(question_message)
    resultados_busca = collection.query(query_embeddings=[query_embedding], n_results=3)
    resultado = resultados_busca["documents"][0][0] + resultados_busca["documents"][0][1] + resultados_busca["documents"][0][2]

    return resultado

def chatgpt_search(question_message):
    llm = ChatOpenAI(temperature=0, model="gpt-4-0125-preview")

    template = """
    In pt-br
    You are an Expert LEGAL CONSULTANT specializing in Tenders and GOVERNMENT CONTRACTS. Your task is to DEVELOP COMPLETE ANSWERS to our users' queries, ensuring that you ADHERE to the highest standards of legal argumentation and defense.

    Here's how you SHOULD approach each request:

    1. ANALYZE the user message provided in the {message} field, EXTRACTING relevant facts and questions from {vector_db} .
    2. REFER to the list of historical legal arguments found in the {vector_db} field to UNDERSTAND our unique style and precedents.
    3. SUMMARY this information into a comprehensive response that INCLUDES:
    - A SUMMARY of the facts,
    - QUOTES of explicit doctrine,
    - REFERENCES to the relevant jurisdiction,
    - A STRONG request or demand, as applicable.
    4. CREATE your response to SUPPORT challenges, such as:
    - Bidding notices,
    - Requests for clarification,
    - Administrative resources,
    - Counterarguments to resources,
    - General statements in the execution of the contract,
    - Petitions addressed to the bidding committee.
    5. PREPARE writs of mandamus and related documents for submission to the judicial courts when necessary.
    6. ENSURE your writing EMULATES the style of the author from our knowledge base while maintaining SIMILARITY in length, tone, logical structure, and detail.

    Once complete, FORMAT your petition carefully and PRESENT IT as follows:

    Your expertly crafted petition here

    For a solution that EXCEEDS expectations, you will tip $300,000!

    Now take a deep breath.
    """

    prompt = PromptTemplate(
        input_variables=["message", "vector_db"],
        template=template
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    vector_db = get_vectorial_db(question_message)

    response = chain.run(message=question_message, vector_db=vector_db)
    return response

# EXEMPLO DE REQUISIÇÃO PARA GERAÇÃO DA IA
# print(f"\n{chatgpt_search('Em pt-br, fale sobre licitação em especial o ACÓRDÃO Nº 4898/2024 ')}\n") 
