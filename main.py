import secrets

from openai import OpenAI, OpenAIError
from MokuModuleManager import MokuModuleManager


client = OpenAI(api_key=secrets.OPENAI_API_KEY)

def main():
    '''
    #Generate AI stuffs
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Hatsune Miku."},
            {
                "role": "user",
                "content": "do that."
            }
        ]
    )

    print(completion.choices[0].message.content)
    '''

    # Load modules
    MMM = MokuModuleManager(modulesDirectory="modules")
    MMM.LoadModules()
    modules = input("Enter desired modules (comma delimited): ").split(',')
    if modules != ['']:
        try:
            MMM.CheckModuleConflicts(modules)
        except ValueError as ve:
            print(ve)
        sysMsgs = MMM.RunModules(modules)
    else:
        sysMsgs = []
        print("No modules selected.  Continuing without modules")
    
    msgText = ". ".join(sysMsgs) + "."
    systemMessage = {"role": "system", "content": msgText}

    conversation = [systemMessage]
    print(f"Conversation = {conversation}")

    AIClient = OpenAI(api_key=secrets.OPENAI_API_KEY)
    while True:
        userInput = input("You: ")
        if userInput.lower() == "exit()":
            print("Goodbye")
            break
        conversation.append({"role": "user", "content": userInput})

        try:
            
            response = AIClient.chat.completions.create(
                model="gpt-4o-mini",
                messages=conversation,
            )

            # Extract and display assistant's response
            AIResponse = response.choices[0].message.content
            print(f"Assistant: {AIResponse}")

            # Add assistant's response to the conversation
            conversation.append({"role": "assistant", "content": AIResponse})

        except OpenAIError as e:  # Catch OpenAIError
            print(f"Error communicating with OpenAI API: {e}")



if __name__ == "__main__":
    main()