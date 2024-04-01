# pip3 install openai 
# pip3 install dotenv
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

def find_answer(input_context, question, openai_api_key):
    # set client
    client = OpenAI(api_key=openai_api_key)

    # Define conversion prompt
    prompt = f"Answer the following question delimited by triple backticks based on provided context also delimited by triple backticks.\n\nQuestion - ```{question}```\n\nContext - ```{input_context}```"
    print("Prompt:")
    print(prompt)
    print("="*100)

    # find/generate answer using LLM
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            { "role": "user", "content": prompt}
        ]
    )
    print('response\n')
    print(response)
    
    # extract answer 
    answer = response.choices[0].message.content.strip()
    return answer

# add openai_api_key to environment variables
# While you can provide an api_key keyword argument, using python-dotenv may be preferred so that your API Key is not stored in source control
# steps - create .env file and add api key as OPENAI_API_KEY="My API Key"
_ = load_dotenv(find_dotenv()) # finds .env file and adds key-value pairs specified in .env to enviornment variables
openai_api_key   = os.environ.get("OPENAI_API_KEY") 
#print("openai_api_key: ", openai_api_key)
if (openai_api_key is None) :
    print('OpenAI API key not found. Please check .env file exists with key "OPENAI_API_KEY" present in file')
    exit()
if (len(openai_api_key.strip()) == 0) :
    print('Missing OpenAI API key - please provide api key value in .env file as OPENAI_API_KEY="My API Key"')
    exit()

# define parameters 
context_filepath  = './samples/opencv_live_episode_123/context.txt' # shortened_context.txt
question_filepath = './samples/opencv_live_episode_123/question.txt'   

# read context 
with open(context_filepath) as fh : 
    input_context = fh.read()

# read question
with open(question_filepath) as fh : 
    question = fh.read()

answer = find_answer(input_context, question, openai_api_key)
print("answer:", answer)
