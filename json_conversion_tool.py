from smolagents import tool
from smolagents.models import LiteLLMModel
import json

@tool
def format_to_json(text: str) -> str:
    """
    Converts a structured text into JSON format using an LLM.
    
    Args:
        text: A string containing key-value pairs or structured data
        
    Returns:
        A string containing the formatted JSON data
    """
    # Initialize the model
    model = LiteLLMModel(
        model_id="ollama_chat/qwen2:7b",
        api_base="http://127.0.0.1:11434",
        num_ctx=8192,
    )
    
    # Prepare the messages for the LLM
    messages = [
        {"role": "system", "content": [{"type": "text", "text": (
            "You are a precise JSON format converter. Your task is to:\n"
            "1. Extract key information from the input text\n"
            "2. Convert it into a valid JSON structure\n"
            "3. Use proper JSON syntax with double quotes for keys and string values\n"
            "4. Include only the JSON output without any additional text or explanation\n"
            "5. Ensure the output is properly formatted and valid JSON"
        )}]},
        {"role": "user", "content": [{"type": "text", "text": f"Convert the following to JSON format:\n{text}"}]}
    ]
    
    # Get response from LLM
    response = model.generate(messages)
    
    # Return the JSON string
    return response.__dict__["content"]

# Example usage
if __name__ == "__main__":
    # Example function call
    test_text = """
    Project Name: Test Project
    Description: A test project
    Type: Test
    Status: Active
    """
    result = format_to_json(test_text)
    print(f"\nResult: {result}") 