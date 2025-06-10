# Non-Agentic LLM with Tool Call

This project demonstrates a simple but effective pattern for using LLMs with tools, serving as a stepping stone towards more complex agentic systems. It shows how to:

1. Use an LLM to recognize when a tool should be used
2. Delegate the actual task to a specialized tool
3. Process and return the results

## Project Structure

- `non_agentic_llm_with_tool.py`: Main script demonstrating the LLM + tool pattern
- `json_conversion_tool.py`: Tool implementation for converting structured text to JSON

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure Ollama is running locally with the qwen2:7b model:
```bash
ollama pull qwen2:7b
```

## Usage

Run the main script to see examples of different types of structured data being converted to JSON:

```bash
python non_agentic_llm_with_tool.py
```

The script includes examples for:
- Project Information
- Personal Information
- Product Information
- Weather Data

## How It Works

1. The LLM is given a system prompt that instructs it to:
   - Recognize JSON conversion requests
   - Not attempt the conversion itself
   - Acknowledge that it will use the tool

2. When a JSON conversion is requested:
   - The LLM acknowledges the request
   - The `process_llm_response` function detects this acknowledgment
   - The `format_to_json` tool is called with the original input
   - The tool uses another LLM call to perform the actual conversion

3. The result is returned as a properly formatted JSON object

## Key Features

- Clear separation of concerns between LLM and tool
- Robust error handling
- Flexible input format
- Customizable messages
- Multiple example use cases

## Requirements

See `requirements.txt` for full list of dependencies.

## Notes

This implementation represents a "pre-agentic" pattern where:
- The LLM is used for recognition and routing
- Tools handle the actual task execution
- The system is deterministic and predictable

It serves as a good foundation for understanding how to build more complex agentic systems. 