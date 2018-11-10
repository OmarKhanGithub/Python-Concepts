f = open('FullQuestion.txt','r')
message = f.read()

portion = message.split('?')
questionWithBreaks = portion[0]
question = questionWithBreaks.replace('\n', ' ')

answers = portion[1].split('\n')

global answer1
global answer2
global answer3
global total1
global total2
global total3

answer1 = answers[2]
answer2 = answers[4]
answer3 = answers[6]
total1 = 1
total2 = 1
total3 = 1

print('Question:', question)
print('Answer 1:', answer1)
print('Answer 2:', answer2)
print('Answer 3:', answer3)

questionT = question.split(' ')

first = questionT[:int(len(questionT)/2)]
fixedFirst = " ".join(str(x) for x in first)

second = questionT[int(len(questionT)/2):]
fixedSecond = " ".join(str(x) for x in second)


bigAnswer1 = fixedSecond + ' ' + answer1 + ' ' + answer2 + ' ' + answer3 
import urllib.request

try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
import urllib.request

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()


for j in search(question, tld="co.in", num=2, stop=1, pause=2.5): 
    f = opener.open(j)
    print(j)
    if '#' not in j:
        s = f.read()
        freq1 = str(s).count(answer1)
        freq2 = str(s).count(answer2)
        freq3 = str(s).count(answer3)
        total1 = total1 + freq1
        total2 = total2 + freq2
        total3 = total3 + freq3

print("Done Search #1")
if total1 + total2 + total3 == 0 or (total1 == total2 and total1 == total3):
	for j in search(bigAnswer1, tld="co.in", num=4, stop=1, pause=2.5):
		f = opener.open(j)
		s = f.read()

		freq1 = str(s).count(answer1)
		freq2 = str(s).count(answer2)
		freq3 = str(s).count(answer3)
		total1 = total1 + freq1
		total2 = total2 + freq2
		total3 = total3 + freq3
    
print("Answer 1: %",(total1/(total1+total2+total3))*100)
print("Answer 2: %",(total2/(total1+total2+total3))*100)
print("Answer 3: %",(total3/(total1+total2+total3))*100)
    
#f.close()
