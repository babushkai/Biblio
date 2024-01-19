### Brilliant Sorting Algorithm
https://brilliant.org/wiki/sorting-algorithms/


pgvector and scann are both approximate nearest neighbor (ANN) libraries that can be used to efficiently search for similar vectors in a large dataset. However, there are some key differences between the two libraries:

Data structure: pgvector uses a product quantization (PQ) data structure, while scann uses a sparse vector quantization (SVQ) data structure. PQ is a vector quantization technique that divides the vector space into a grid of cells and assigns each vector to the closest cell. SVQ is a variant of PQ that is designed for sparse vectors.
Search algorithm: pgvector uses a hierarchical search algorithm to find similar vectors. The search algorithm starts by searching for similar vectors in the top level of the hierarchy. If no similar vectors are found, the search algorithm moves to the next level of the hierarchy and continues searching. scann uses a locality-sensitive hashing (LSH) algorithm to find similar vectors. LSH is a hashing technique that maps similar vectors to the same bucket. This allows scann to quickly find similar vectors by hashing the query vector and then searching the bucket that contains the query vector.
Scalability: pgvector is designed to be scalable to large datasets. It can be used to search for similar vectors in a dataset that contains billions of vectors. scann is also designed to be scalable, but it is not as scalable as pgvector. scann is better suited for datasets that contain millions of vectors.
Accuracy: pgvector and scann both offer high accuracy. However, pgvector is generally more accurate than scann. This is because pgvector uses a more sophisticated data structure and search algorithm.
Performance: pgvector is generally faster than scann. This is because pgvector uses a more efficient search algorithm. However, the performance of both libraries depends on the size of the dataset and the number of query vectors.
Overall, pgvector is a better choice for applications that require high accuracy and scalability. scann is a better choice for applications that require high performance and can tolerate lower accuracy.
