import matplotlib.pyplot as plt
import matplotlib.patches as patches

"""
color A <-> T  ,C <-> G ,%AT <->, A/T, %CG <-> C/G
colors = ["red", "blue", "green","yellow","brown","pink","purple","orange"]
"""
#colors = {"A":"red","T":"green","C":"blue","G":"yellow","A/T":"orange","%AT":"purple","C/G":"brown","%CG":"pink"}
#textcolor = {"A":"green","T":"red","C":"yellow":"G":"blue","A/T":"purple","%AT":"orange","C/G":"pink","%CG":"brown"}
def plotATCG(total_adenine,total_guanine,total_cytosine,total_thymine):
	#total_adenine_thymine = total_adenine/total_thymine
	#total_guanine_cytosine= total_guanine/total_cytosine
	square_color = "blue"
	total = total_adenine + total_guanine + total_cytosine + total_thymine
	percentage_adenine = (total_adenine/total)*100
	percentage_guanine = (total_guanine/total)*100
	percentage_cytosine = (total_cytosine/total)*100
	percentage_thymine = (total_thymine/total)*100
	print(percentage_adenine,percentage_guanine,percentage_cytosine,percentage_thymine)
	adeninexy = [-50+percentage_adenine,50+percentage_adenine]
	guaninexy = [50+percentage_guanine,50+percentage_guanine]
	cytosinexy = [-50+percentage_cytosine,50+percentage_cytosine]
	thyminexy = [50+percentage_thymine,50+percentage_thymine]
	print(adeninexy,guaninexy,cytosinexy,thyminexy )
#A|C
#G|T
	plt.plot(0.5,0.5, linestyle="None", marker="s",markersize=50, mfc="orange")
	plt.plot(-percentage_adenine,percentage_adenine, linestyle="None", marker="s",markersize=percentage_adenine, mfc="red") 
	#plt.annotate(0,0,s="adenine")
	plt.plot(-percentage_guanine,-percentage_guanine, linestyle="None", marker="s",markersize=percentage_guanine, mfc="green") 	
	plt.plot(cytosinexy[0],cytosinexy[1], linestyle="None", marker="s",markersize=percentage_cytosine, mfc="blue", mec=square_color) 
	plt.plot(thyminexy[0],thyminexy[1], linestyle="None", marker="s",markersize=percentage_thymine, mfc="blue") 

#plt.grid(visible=False, axis='y')
#plt.xlim(0.5, 4.5)
#plt.ylim(-0.5, 6.5)
	plt.show()
plotATCG(600,400,300,700)
