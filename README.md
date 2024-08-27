# Bajillion Search Engine

## Project Overview
The Bajillion Search Engine is a small-scale, text-based search engine developed using Python. This project serves as a hands-on application of CS106A programming skills, demonstrating how concepts learned in the course can be utilized to build powerful applications like search engines. The project involves building an inverted index and implementing search functionality to retrieve documents based on user queries.

## Key Features
- **Inverted Index Construction**: This is the backbone of the search engine, where each term from the documents is indexed with the list of documents it appears in. This structure enables efficient query processing.
- **Search Functionality**: Users can search for documents containing specific terms. The search engine processes these queries using the inverted index to find and retrieve relevant documents.
- **Handling of Common Elements in Lists**: Part of the project also included writing a function to identify common elements in two lists, which is integrated into the search functionality to handle multiple term queries effectively.

## Technologies Used
- **Python**: Primary programming language for building the search engine.
- **File I/O**: Handling reading from and writing to text files to build the index and process queries.

## How to Use
1. **Setting up the Environment**:
   - Ensure Python is installed on your system.
   - Download the project files from the GitHub repository.

2. **Running the Search Engine**:
   - Navigate to the project directory in your terminal.
   - Run the command `python searchengine.py small` to build the index from documents in the specified directory.
   - To search, use the command `python searchengine.py small -s` and follow the prompts to enter search queries.

3. **Using the Web Interface
   - Start the server using python SimpleServer.py.
   - Open a web browser and navigate to http://localhost:8000 to use the search engine through the web interface.

4. **Using the Search Engine**:
   - Enter a search query after the prompt. The engine will display files containing the terms from the query.
   - Press "Enter" with an empty query to exit the search mode.

## Conclusion
This project not only reinforced foundational programming skills but also provided insights into the practical applications of these skills in creating useful software tools. The Bajillion Search Engine is a testament to how a basic understanding of programming concepts can lead to the development of functional software applications.
