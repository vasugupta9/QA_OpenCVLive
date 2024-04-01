input_filepath = './samples/opencv_live_episode_123/context.txt'
with open(input_filepath) as fh : 
    contents = fh.read()
print('char count:', len(contents))
print('word count:', len(contents.split()))