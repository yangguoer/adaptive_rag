### Generate

from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# Prompt

prompt = hub.pull("rlm/rag-prompt")
print("prompt:", prompt)
# LLM
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, openai_api_base="https://api.openai-proxy.com/v1")


# Post-processing
def format_docs(docs):
    page_contents = []
    for doc in docs:
        # print("doc:",doc)
        if isinstance(doc, list) and len(doc) > 0:
            page_content = doc[0].page_content
            page_contents.append(page_content)
        else:
            page_contents.append(docs.page_content)
    return "\n\n".join(page_contents)


# Chain
rag_chain = prompt | llm | StrOutputParser()

# Run
# docs_txt = format_docs(docs)
# generation = rag_chain.invoke({"context": docs_txt, "question": question})
# print(generation)