from document_processor import DocumentProcessor

# Initialize the document processor
processor = DocumentProcessor()

# Process a document
file_path = "data/a_scandal_in_bohemia.pdf"
processor.process_document(file_path)

# Define a query
query = "What is the main mystery in the story?"

# Verify the document was processed correctly
print("Test 1: Retrieving context before reset")
relevant_docs = processor.retrieve_relevant_context(query)
if relevant_docs:
    print(f"First chunk preview: {relevant_docs[0].page_content[:100]}...")
else:
    print("No relevant documents found.")

# TODO: Call the method to clear the vector store
processor.reset()

print()

# TODO: Verify that no documents are returned after reset
relevant_docs = processor.retrieve_relevant_context(query)
if relevant_docs:
    print("Document reset not success")
else:
    print("No relevant documents found after reset")