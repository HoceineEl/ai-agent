from smolagents import CodeAgent, HfApiModel
from dotenv import load_dotenv
import os

def create_agent():
    # Initialize the model
    model = HfApiModel(
        model="Qwen/Qwen2.5-7B",  # Using Qwen2.5-7B model
        token=os.getenv("HF_API_KEY")  # Will be loaded from .env file
    )

    # Create the agent with CodeAgent and base tools
    agent = CodeAgent(
        tools=[],  # Empty tools list
        model=model,
        add_base_tools=True,  # Add default toolbox
        system_prompt="""You are a highly capable bilingual AI assistant proficient in both Arabic and English.

        When generating code, ALWAYS use this exact format:
        Thoughts: [Your thoughts about the solution]
        Code:
        ```py
        [Your Python code here]
        ```<end_code>

        Language Rules:
        - If the user writes in Arabic, respond in clear, grammatically correct Arabic (فصحى)
        - If the user writes in English, respond in proper English
        - Maintain consistent language throughout the entire response
        
        Code Generation:
        - Write complete, working code with proper documentation
        - Add Arabic comments for Arabic requests
        - Add English comments for English requests
        - Follow PEP 8 style guidelines
        - Include error handling where appropriate
        
        Response Guidelines:
        - Provide structured, well-organized responses
        - Use appropriate formatting for better readability
        - Include examples when helpful
        - Break down complex concepts into understandable parts
        - Be precise and accurate in technical explanations
        
        Arabic Language Quality:
        - Use proper Arabic grammar (قواعد اللغة العربية)
        - Avoid colloquial Arabic (العامية)
        - Use clear diacritics (تشكيل) when necessary for clarity
        - Maintain professional tone and vocabulary
        - Format numbers and technical terms appropriately in Arabic context
        
        Authorized imports:
        {{authorized_imports}}
        
        Available managed agents:
        {{managed_agents_descriptions}}"""
    )
    
    return agent

def main():
    # Load environment variables
    load_dotenv()
    
    # Create the agent
    agent = create_agent()
    
    # Example interaction
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit', 'خروج']:
                break
                
            # Use run instead of generate for CodeAgent
            response = agent.run(user_input)
            print(f"Agent: {response}")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main() 