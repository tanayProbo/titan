import logging
from typing import List, Dict, Any

logger = logging.getLogger("titanx.pipeline.embedder")

class DocumentEmbedder:
    """
    Chunks extracted markdown text and generates vector embeddings.
    Supports dense vectors for semantic parsing and sparse vectors for keyword indexing.
    """
    def __init__(self, embedding_client: Any, chunk_size: int = 500, chunk_overlap: int = 50):
        self.embedding_client = embedding_client
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_into_chunks(self, text: str) -> List[str]:
        """Splits long text blocks using sliding windows to preserve context."""
        words = text.split()
        chunks = []
        i = 0
        while i < len(words):
            chunk_words = words[i : i + self.chunk_size]
            chunks.append(" ".join(chunk_words))
            i += self.chunk_size - self.chunk_overlap
        logger.info(f"Chunked document body into {len(chunks)} text chunks.")
        return chunks

    async def generate_dense_embeddings(self, chunks: List[str]) -> List[List[float]]:
        """Generates high-dimensional vector embeddings for input text chunks."""
        try:
            logger.info(f"Generating dense vector embeddings for {len(chunks)} chunks...")
            # In production, invokes embedding endpoints:
            # response = await self.embedding_client.embeddings.create(
            #     input=chunks,
            #     model="text-embedding-3-small"
            # )
            # return [item.embedding for item in response.data]
            
            # Skeleton mock representation (1536 dimensions):
            return [[0.015 * (x % 7) for x in range(1536)] for _ in chunks]
        except Exception as e:
            logger.error(f"Failed to generate dense vectors: {str(e)}")
            return []

    def generate_sparse_tokens(self, text: str) -> Dict[str, float]:
        """Generates BM25-like sparse weight values for keyword lookup search systems."""
        words = text.lower().split()
        total_words = len(words)
        if total_words == 0:
            return {}
        
        freqs = {}
        for word in words:
            freqs[word] = freqs.get(word, 0) + 1
            
        # Return term frequencies normalized
        return {word: float(count / total_words) for word, count in freqs.items()}
