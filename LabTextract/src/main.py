import boto3

def detect_text_in_document(document_path):
    # Initialize Textract client
    textract = boto3.client('textract')

    # Read the document content
    with open(document_path, 'rb') as document:
        image_bytes = document.read()

    # Call Textract to detect text in the document
    response = textract.detect_document_text(Document={'Bytes': image_bytes})

    # Print detected text
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            print(item['Text'])

if __name__ == "__main__":
    document_path = 'path/to/your/document.jpg'  # Update with your document path
    detect_text_in_document(document_path)