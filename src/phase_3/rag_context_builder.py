def build_rag_context(retrieved_docs):
    context = (
        "You are a healthcare information assistant. "
        "Use the information below to answer the user's question. "
        "You may suggest possible conditions but must not confirm a diagnosis. "
        "Always recommend consulting a qualified doctor.\n\n"
    )

    for i, doc in enumerate(retrieved_docs, 1):
        context += f"Medical Reference {i}:\n{doc}\n\n"

    return context


if __name__ == "__main__":
    from retrieve import retrieve_documents

    query = "I have blurry vision and eye pain, what could it be?"
    docs = retrieve_documents(query)
    rag_context = build_rag_context(docs)

    print(rag_context[:1500])