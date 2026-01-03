from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()
def main():
    
    model = ChatOpenAI(temperature=0)
    
    tools = []
    agent_executor = create_react_agent(model, tools)

    print("Welcome, I am your AI assistant. Type 'quit' to exit.")
    print("You can chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            break

        print("\nAssistant: ", end="", flush=True)
        
       
        for chunk in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):   
            
            if "agent" in chunk:
                for message in chunk["agent"]["messages"]:
                    
                    if message.content:
                        print(message.content, end="", flush=True)
        print()            

if __name__ == "__main__":
    main()