from immo_rag.agent import AgentManager

def main():
    print("Initializing real estate assistant...")
    agent = AgentManager()
    
    while True:
        try:
            query = input("\nYour question (type 'exit' to quit): ")
            if query.lower() == 'exit':
                break
                
            response = agent.run_query(query)
            print("\nAssistant Response:")
            print(response["messages"][-1].content)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()