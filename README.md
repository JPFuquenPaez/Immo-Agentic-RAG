# ImmoRAG: Real Estate Assistant

![Python Version](https://img.s://img.shields.io/badge/licensemg.moRAG is a sophisticated real estate assistant that leverages Retrieval Augmented Generation (RAG) to provide accurate property information through natural language queries. Built with LangGraph and Chroma vector database, this application combines semantic search capabilities with generative AI to deliver contextually relevant responses about real estate listings.

![ImmoRAG Architecture](https://via.placeholder.com/iew](#overview)
- [How It Works](#how-it-works)
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
- [Usage](#usage)
- [Example Queries](#example-queries)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Overview

ImmoRAG addresses the challenge of finding relevant real estate information by enabling natural language queries against property data. Rather than browsing through hundreds of listings, users can simply ask questions like "Find apartments larger than 61m² in Lyon centre" and receive accurate, contextualized responses.

## How It Works

ImmoRAG implements Agent RAG (Retrieval Augmented Generation), combining document retrieval systems with generative AI:

### Key Components

#### Retrieval System
- **Vector Store**: Utilizes ChromaDB to store and retrieve property information based on semantic similarity[1].
- **Embeddings**: Generated using SentenceTransformers (`all-mpnet-base-v2`) to capture semantic meaning of text[1].

#### Generative AI Model
- **Language Model (LLM)**: Uses Qwen 2.5 (7B parameters) to interpret queries and generate human-like responses[1].
- **Integration**: LLM augments responses with factual data from retrieved documents.

#### Agent Framework
- **State Management**: Maintains conversation context using LangGraph's state architecture[1].
- **Tools and Actions**: Performs vector searches and generates responses based on user inputs.

### Workflow

1. **User Query**: User inputs a natural language question
2. **Query Interpretation**: LLM extracts intent and key search terms
3. **Document Retrieval**: Vector store finds semantically similar property listings
4. **Response Generation**: LLM generates coherent responses based on retrieved documents
5. **User Interaction**: Results displayed via Streamlit interface

## Features

- **Natural Language Querying**: Ask about properties using everyday language
- **Semantic Search**: Vector embeddings enable concept-based searching beyond keyword matching[1]
- **Streamlit Interface**: User-friendly web application for interaction
- **Modular Design**: Clean, maintainable codebase divided into focused components[2]
- **Contextual Memory**: Maintains conversation history for follow-up questions

## Screenshots

![ImmoRAG Interface](https://via.placeholder.com/800x500?text=Immo interface showing a sample query and response*

## Installation

### Prerequisites

- Python 3.10 or higher
- 4GB+ RAM recommended
- Internet connection (for embedding model downloads)

### Dependencies

```
langchain>=0.1.0
chromadb>=0.4.18
sentence-transformers>=2.2.2
streamlit>=1.28.0
langgraph>=0.0.15
pandas>=2.0.0
```

### Setup Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/immoRAG.git
   cd immoRAG
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv immo_agentic_rag
   source immo_agentic_rag/bin/activate  # On Windows use: immo_agentic_rag\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Vector Store**:
   ```bash
   python -m immo_rag.ingest
   ```
   This creates a vector database from your property data using ChromaDB[1].

## Usage

### Running the Streamlit App

1. **Activate the Virtual Environment** (if not already active):
   ```bash
   source immo_agentic_rag/bin/activate
   ```

2. **Start the Streamlit App**:
   ```bash
   streamlit run immo_rag/streamlit_app.py
   ```

3. **Access the Web Interface**:
   Open your browser and navigate to http://localhost:8501

### Using the Assistant

1. Type your real estate query in the chat input
2. The assistant will retrieve relevant property listings
3. Results include property details and similarity scores
4. Continue the conversation with follow-up questions

## Example Queries

Here are some sample queries you can try:

```
"Show me apartments in Lyon with more than 2 bedrooms"
"What's the average price for properties near Paris city center?"
"Find properties with a DPE rating of A or B"
"Are there any apartments with a terrace in Marseille?"
```

## Project Structure

```
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

The codebase follows modular programming principles to enhance maintainability and collaboration[2]:

- **config.py**: Central configuration settings
- **data_loader.py**: Handles CSV data processing and document conversion
- **retriever.py**: Manages vector embeddings and semantic search
- **tools.py**: Defines custom tools for the agent framework
- **agent.py**: Implements LangGraph state management
- **streamlit_app.py**: Web interface implementation

## Troubleshooting

### Common Issues

**Issue**: Vector store creation fails
- **Solution**: Ensure your CSV data is properly formatted and accessible in the data directory

**Issue**: LLM fails to load
- **Solution**: Check that you have Ollama installed and the Qwen2.5 model is available

**Issue**: Module not found errors
- **Solution**: Verify your virtual environment is activated and all dependencies are installed

**Issue**: Slow response times
- **Solution**: Consider reducing the vector database size or optimizing embedding parameters

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes and commit them (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

Please ensure your code follows the project's style and includes appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

