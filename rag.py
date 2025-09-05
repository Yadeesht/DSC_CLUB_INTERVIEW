from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import Document,Settings,VectorStoreIndex,SimpleDirectoryReader
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor
from llama_index.llms.ollama import Ollama

llm = Ollama(model="gemma3:1b", request_timeout=120.0)

Settings.llm=llm
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

Settings.chunk_size = 512      
Settings.chunk_overlap = 64

content=SimpleDirectoryReader(input_files=["data.pdf"]).load_data()

index=VectorStoreIndex.from_documents(content)

retriever=VectorIndexRetriever(index=index,
                             similarity_top_k=3,)

query_engine=RetrieverQueryEngine(
    retriever=retriever,
    node_postprocessors=[SimilarityPostprocessor(similarity_cutoff=0.7)]
)

responce=query_engine.query("Scope of Interpretability means?")
print(responce)


