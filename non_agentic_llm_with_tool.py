from smolagents import LiteLLMModel
from pprint import pprint
import json
from json_conversion_tool import format_to_json

def process_llm_response(response: str, original_input: str) -> str:
    """
    Process the LLM's response and handle JSON conversion if needed.
    """
    # Try to parse as JSON first
    try:
        json.loads(response)
        return response
    except json.JSONDecodeError:
        # If not JSON, use the format_to_json tool
        return format_to_json(original_input)

def run_conversion(data: str, message: str = "Can you convert this to JSON format?"):
    """Run the conversion process with given data and message."""
    # Initialize the model
    model = LiteLLMModel(
        model_id="ollama_chat/qwen2:7b",  # Or try other Ollama-supported models
        api_base="http://127.0.0.1:11434",  # Default Ollama local server
        num_ctx=8192,
    )
    
    # Example usage with proper message format
    messages = [
        {"role": "system", "content": [{"type": "text", "text": (
            "You are a helpful AI assistant with access to various tools. "
            "IMPORTANT: When users ask for JSON conversion or formatting:\n"
            "1. DO NOT attempt to convert the data to JSON yourself\n"
            "2. DO NOT provide any JSON output\n"
            "3. Simply respond with: 'I'll use the format_to_json tool to convert this for you.'\n"
            "For other requests, respond directly. Always be clear and helpful."
        )}]},
        {"role": "user", "content": [{"type": "text", "text": (
            f"{data}\n\n{message}"
        )}]}
    ]
    response = model.generate(messages)
    print("\nResponse1:")
    pprint(response.__dict__)
    
    # Process the response and use tools if needed
    result = process_llm_response(response.__dict__["content"], data)
    
    # Print the result
    print("\nResponse2:")
    print(json.dumps(result, indent=2))

def main():
    # Example 1: Project Information
    project_data = """
    Project Name: Hugging Face Agents Course
    Description: A comprehensive learning journey for AI agents
    Type: Educational Course
    Status: Active
    Version: 1.0
    Tags: AI, Machine Learning, Agents, Education
    """
    print("\n=== Example 1: Project Information ===")
    run_conversion(project_data)
    
    # Example 2: Personal Information
    personal_data = """
    Name: John Doe
    Age: 30
    Address: 123 Main St
    Phone: 555-0123
    Email: john.doe@example.com
    Occupation: Software Engineer
    """
    print("\n=== Example 2: Personal Information ===")
    run_conversion(personal_data)
    
    # Example 3: Product Information
    product_data = """
    Product: Laptop
    Price: 999.99
    Specs: 16GB RAM, 512GB SSD
    In Stock: Yes
    Warranty: 2 years
    Brand: TechPro
    """
    print("\n=== Example 3: Product Information ===")
    run_conversion(product_data)
    
    # Example 4: Custom Message
    weather_data = """
    Location: New York
    Temperature: 72°F
    Condition: Sunny
    Humidity: 45%
    Wind: 8 mph
    """
    custom_message = "Please convert this weather data into a JSON structure."
    print("\n=== Example 4: Weather Data with Custom Message ===")
    run_conversion(weather_data, custom_message)

if __name__ == "__main__":
    main() 