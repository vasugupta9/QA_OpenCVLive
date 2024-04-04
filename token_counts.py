import tiktoken 

# encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
# print('encoding for gpt-3.5-turbo:', encoding) # prints <Encoding 'cl100k_base'>
# encoding = tiktoken.encoding_for_model("gpt-4-turbo-preview")
# print('encoding for gpt-4-turbo-preview:', encoding) # prints <Encoding 'cl100k_base'>

# encoding used by gpt-3.5-turbo and gpt-4-turbo-preview is cl100k_base
encoding = tiktoken.get_encoding("cl100k_base")
# sample_tokens = encoding.encode("tiktoken is great!")
# print(sample_tokens)

# read context 
episode = 129
context_filepath  = f'./samples/opencv_live_episode_{episode}/context.txt' 
with open(context_filepath) as fh : 
    input_context = fh.read()

# tokenize 
tokens = encoding.encode(input_context)
num_tokens = len(tokens)
print('num_tokens:', num_tokens)
