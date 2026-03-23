## Vector DB Use Case

A traditional keyword-based database search would not be sufficient for searching large legal contracts. Keyword search only matches exact words and may miss relevant information if different terminology is used. For example, a contract might describe termination clauses using phrases like "agreement cancellation" or "contract ending" rather than the exact keyword "termination". A keyword search system may fail to capture such semantic meanings.

Vector databases solve this problem by using embeddings, which represent text as numerical vectors capturing semantic meaning. When a lawyer asks a question such as "What are the termination clauses?", the system converts the question into an embedding and compares it with embeddings of contract sections. The vector database then retrieves the most semantically similar sections even if the wording is different.

This approach enables semantic search instead of simple keyword matching. It allows the system to understand the intent behind the question and return relevant passages from long documents. Vector databases are optimized for fast similarity searches across large embedding datasets.

In such a system, contracts would first be divided into smaller chunks such as paragraphs. Each chunk would be converted into embeddings and stored in a vector database. When a query is asked, the system retrieves the most similar chunks and returns them to the user. Therefore, vector databases significantly improve accuracy and usability when searching large legal documents.
