import secrets

from openai import OpenAI # type: ignore
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
    try:
        MMM.CheckModuleConflicts(modules)
    except ValueError as ve:
        print(ve)
        return
    MMM.RunModules(modules)


if __name__ == "__main__":
    main()