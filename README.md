# Chroma DB - Scripts

This Python project utilizes ChromaDB to manage and search vector data collections, providing a robust structure for storing and querying information. The repository includes functionalities for creating, deleting, and searching collections, along with an example of integration with ChatGPT.

## Technologies Used
- Python 3
- ChromaDB

> **Author**: João Pedro Rodrigues Matias | <joaopedrord2001@gmail.com>


## Structure

```bash
├── src                       
│   ├── app.py                # Example application for ChatGPT integration using ChromaDB
│   ├── create.py             # Script to create a new collection and insert data in ChromaDB
│   ├── delete.py             # Script to delete collections or specific data from ChromaDB
│   ├── search_collections.py # Script to list and search existing collections in ChromaDB
│   └── vector_count.py       # Script to count vectors in a specified ChromaDB collection
```

## How to Use

1. **Initial Setup:**  
   Ensure that ChromaDB is set up and running so that the scripts can connect to it.

2. **Running the Scripts:**
   - To create a collection and insert data: `python src/create.py`
   - To delete a collection or data: `python src/delete.py`
   - To list collections: `python src/search_collections.py`
   - To count vectors: `python src/vector_count.py`

3. **Example of Integration with ChatGPT:**  
   Go to `src/app` to see how to integrate ChromaDB with ChatGPT, enabling vector-based searches to improve the accuracy of the model's responses.

## Requirements
- Python 3.x
- Dependencies specified in the `requirements.txt` file

