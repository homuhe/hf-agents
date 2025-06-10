from tools import tool
from typing import List, Dict
from smolagents import LiteLLMModel
import json

@tool
def format_to_json(text: str) -> Dict:
    """
    Converts a structured text into JSON format using an LLM.
    
    Args:
        text: A string containing key-value pairs or structured data
        
    Returns:
        A dictionary containing the parsed JSON data
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
    
    # Parse and return the JSON
    try:
        return json.loads(response.__dict__["content"])
    except json.JSONDecodeError:
        return {"error": "Failed to parse JSON", "raw_content": response.__dict__["content"]}

# Example usage
if __name__ == "__main__":
    # Create a tool instance
    json_tool = format_to_json
    
    # Print tool information
    print(f"Tool Name: {json_tool.name}")
    print(f"Description: {json_tool.description}")
    print(f"Arguments: {json_tool.arguments}")
    print(f"Outputs: {json_tool.outputs}")
    
    # Example function call
    test_text = """
    Project Name: Test Project
    Description: A test project
    Type: Test
    Status: Active
    """
    result = json_tool.func(test_text)
    print(f"\nResult: {json.dumps(result, indent=2)}") 