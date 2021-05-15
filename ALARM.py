#1st install tinytag
!pip install tinytag

#Then, go ahead and execute this piece of code I have written:
# ALARM LOOP
import time
from tinytag import TinyTag
tag = TinyTag.get('/content/Back_In_Black_sample.ogg.mp3')
'''print('This track is by %s.' % tag.artist)
print('It is %f seconds long.' % tag.duration)'''
for i in range(0,10):
  from google.colab import output
  output.eval_js('new Audio("https://upload.wikimedia.org/wikipedia/en/1/19/Back_In_Black_sample.ogg").play()')
  start_time = time.time()
  seconds = tag.duration
  while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time > seconds:
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        break
