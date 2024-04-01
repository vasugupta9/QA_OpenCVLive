# pip3 install openai 
# pip3 install dotenv
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os

client = OpenAI()

# response = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
#   ]
# )


# add openai_api_key to environment variables
# While you can provide an api_key keyword argument, using python-dotenv may be preferred so that your API Key is not stored in source control
# steps - create .env file and add api key as OPENAI_API_KEY="My API Key"
_ = load_dotenv(find_dotenv()) # finds .env file and adds key-value pairs specified in .env to enviornment variables
openai_api_key   = os.environ.get("OPENAI_API_KEY") 
print("openai_api_key: ", openai_api_key)
if (openai_api_key is None) :
    print('OpenAI API key not found. Please check .env file exists with key "OPENAI_API_KEY" present in file')
    exit()
if (len(openai_api_key.strip()) == 0) :
    print('Missing OpenAI API key - please provide api key value in .env file as OPENAI_API_KEY="My API Key"')
    exit()