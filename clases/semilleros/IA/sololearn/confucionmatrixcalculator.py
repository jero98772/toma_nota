tp, fp, fn, tn = [int(x) for x in input().split()]
total=tp+fp+fn+tn
accuracy=(tp+tn)/total
print(round(accuracy,4))
precision=tp/(tp+fp)
print(round(precision,4))
recall=tp/(tp+fn)
print(round(recall,4))
f1=2*((precision*recall)/(precision+recall))
print(round(f1,4))