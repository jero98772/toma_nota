txt=input()
tag1="<div class='name'>"
tag2="<div class='lastname'>"
endtag="</div>"
namepos1=txt.index(tag1)+len(tag1)
lastname1=txt.index(tag2)+len(tag2)
print(txt[namepos1:txt.index(endtag)]+txt[lastname1:txt.index(endtag,lastname1)])