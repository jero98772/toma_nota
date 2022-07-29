#rercusion but how?#def tryTimes(mins,hours):
#mins hours are boolean array,  bits to puts, position

s=int(input())
if s<0:
	print(0)
leds=[]
hh=[1,2,4,8]
mm=[1,2,4,8,16,32]
for i in range(s):
	leds.append(0)
