# ImmoRAG: Real Estate Assistant

ImmoRAG is a sophisticated real estate assistant application designed to help users query and retrieve information about real estate properties using natural language processing and vector search capabilities. This project leverages advanced AI models and simple RAG to provide accurate and fast responses to user queries.

Agent RAG is an approach that combines the power of retrieval systems with generative AI models to provide accurate and contextually relevant responses to user queries. This methodology is particularly useful in applications like ImmoRAG, where users need precise information retrieval augmented by natural language understanding.

## Key Components

### Retrieval System

- **Vector Store:** Utilizes embeddings to convert textual data into high-dimensional vectors, enabling efficient similarity searches. In ImmoRAG, the vector store is managed by ChromaDB, which stores and retrieves property information based on semantic similarity.
- **Embeddings:** Generated using models like SentenceTransformers, these embeddings capture the semantic meaning of text, allowing for accurate retrieval of relevant documents.

### Generative AI Model

- **Language Model (LLM):** A generative model that understands and generates human-like text. In ImmoRAG, the LLM is used to interpret user queries and generate responses based on the retrieved information.
- **Integration:** The LLM is integrated with the retrieval system to augment its responses with factual data, ensuring that the generated text is both coherent and accurate.

### Agent Framework

- **State Management:** The agent maintains a state that includes user inputs, retrieved documents, and generated responses. This state management allows for contextual conversations where the agent can refer back to previous interactions.
- **Tools and Actions:** The agent can perform various actions, such as querying the vector store or generating text, based on the user's input. These actions are defined as tools within the agent framework.

## Workflow

### User Query

The user inputs a query in natural language, such as "Find apartments larger than 61 m2 in Lyon centre."

### Query Interpretation

The LLM interprets the query to understand the user's intent and extracts relevant keywords or phrases.

### Document Retrieval

The retrieval system uses the interpreted query to search the vector store for the most semantically similar documents. These documents contain information about real estate properties.

### Response Generation

The LLM generates a coherent and contextually relevant response based on the retrieved documents. This response is augmented with factual data to ensure accuracy.

### User Interaction

The generated response is presented to the user through the Streamlit interface, allowing for further interaction and refinement of queries.

## Benefits

- **Accuracy:** By combining retrieval and generation, Agent RAG ensures that the responses are not only coherent but also factually accurate, based on the retrieved documents.
- **Contextual Understanding:** The agent can maintain context across multiple interactions, allowing for more natural and meaningful conversations.
- **Scalability:** The modular design of the agent framework allows for easy integration of new tools and data sources, making the system scalable and adaptable to changing requirements.


## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Natural Language Querying:** Ask questions about real estate properties in natural language.
- **Semantic Search:** Utilizes vector embeddings for accurate and efficient search results.
- **Streamlit Interface:** A user-friendly web interface for interacting with the assistant.
- **Modular Design:** Clean and maintainable codebase with separate modules for data loading, vector storage, and agent management.

## Installation

### Prerequisites

- Python 3.10 or higher
- Virtual environment (recommended)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/immoRAG.git
   cd immoRAG
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv immo_agentic_rag
   source immo_agentic_rag/bin/activate  # On Windows use `immo_agentic_rag\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Vector Store:**

   Run the ingestion script to create the vector store from your data:

   ```bash
   python -m immo_rag.ingest
   ```

## Usage

### Running the Streamlit App

1. **Activate the Virtual Environment:**

   ```bash
   source immo_agentic_rag/bin/activate  # On Windows use `immo_agentic_rag\Scripts\activate`
   ```

2. **Start the Streamlit App:**

   ```bash
   streamlit run immo_rag/streamlit_app.py
   ```

3. **Interact with the Assistant:**

   Open your web browser and navigate to `http://localhost:8501` to interact with the real estate assistant. Enter your queries in natural language to retrieve property information.

## Project Structure

```plaintext
immoRAG/
├── immo_rag/
│   ├── __init__.py
│   ├── config.py           # Configuration settings
│   ├── data_loader.py      # Data loading and processing
│   ├── retriever.py        # Vector store management
│   ├── tools.py            # Custom tools definition
│   ├── agent.py            # Agent setup and graph
│   ├── ingest.py           # Data ingestion script
│   └── streamlit_app.py    # Streamlit web interface
├── requirements.txt        # Project dependencies
├── setup.py                # Package installation script
├── README.md               # Project documentation
└── data/                   # Directory for data files
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
