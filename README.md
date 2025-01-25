# AI Agent with Qwen2.5-7B

This project implements an AI agent using the smolagents framework and Qwen2.5-7B model, capable of understanding both Arabic and English, with a focus on code generation.

## Setup Instructions

1. Create and activate a virtual environment:
```bash
python3 -m venv smolagent-env
source smolagent-env/bin/activate  # On Windows: smolagent-env\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Copy `.env.example` to `.env`
   - Add your Hugging Face API key to the `.env` file

## Usage

Run the agent:
```bash
python agent.py
```

The agent will start an interactive session where you can:
- Input messages in Arabic or English
- Request code generation
- Type 'quit' or 'exit' to end the session

## Features

- Bilingual support (Arabic and English)
- Code generation capabilities
- Interactive chat interface
- Extensible tool system

## Model Information

This project uses the Qwen2.5-7B model from Hugging Face, which offers:
- Strong multilingual capabilities
- Code generation support
- Free for use with API key
- Good balance of performance and resource usage 