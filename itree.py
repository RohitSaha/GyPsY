"""
mapping moods and other factors to themes using identification trees by calculating disorder and quality of a test.
Tests include age, gender,mood,weather, timestamp, etc
"""

import math

#sample data
titles=['age','gender','mood','themes']
data=[['forty','male','happy','activity'],
      ['forty','female','happy','food'],
      ['thirty','male','sad','food']]

def only_feat(titles):
	of=[]
	for each in titles:
		if each!="themes":
			of.append(each)
	return of

def index(input,titles):
	output=0
	for each in titles:
		if input==each:
			output=titles.index(each)
	return output

def feat_entries(feat,given_data,titles):
	val=[]
	i=index(feat,titles)
	for row in given_data:
		val.append(row[i])
	return val

def unique_val(feat,given_data,titles):
	unique=[]
	entries=feat_entries(feat,given_data,titles)
	for each in entries:
		if unique.count(each)==0:
			unique.append(each)
	return unique


def modify_data(feat,value,given_data,titles):
	data_mod=[]
	ind=index(feat,titles)
	for row in given_data:
		if (row[ind]==value):
			data_mod.append(row)				
	return data_mod

def quality(given_data,feat,titles):	
	values=unique_val(feat,given_data,titles)
	quality=0.0
	m=len(given_data)
	dis=0.0
	for each in values:
		data_mod=[]
		ind=index(feat,titles)
		for row in given_data:
			if (row[ind]==each):
				data_mod.append(row)
			
		n=len(data_mod)
		
		entr=0.0
		d=0.0
		val=[]
		for row in data_mod:
			val.append(row[len(row)-1])
		
		unique=[]
		for one in val:
			if unique.count(one)<=0:
				unique.append(one)
		

		for u in unique:
			c=0.0
			for row in data_mod:
				if (row[len(row)-1]==u):
					c+=1
			#calculates entropy
			entr += (-c/n)*math.log(c/n,2)
		
		#calculates disorder
		d += (n/float(m))*entr
		dis += d
		
	return dis

def choose_feat(titles,given_data):
	feat=None
	temp=[]
	for each in titles:
		var=quality(given_data,each,titles)
		temp.append(var)
	min_disorder=min(temp)
	feat=titles[temp.index(min_disorder)]
	return feat

def create_itree(given_data,titles):
	header=only_feat(titles)
	

	best=choose_feat(header,given_data)
	
	
	tree={best:{}}

	
	for val in unique_val(best,given_data,titles):
		
		data_mod=modify_data(best,val,given_data,titles)
		
		total_themes=feat_entries("themes",data_mod,titles)
		
		if((total_themes.count(total_themes[0])==len(total_themes))):
			
            		tree[best][val]=total_themes[0]
			

		else:
			subtree=create_itree(data_mod,titles)

			tree[best][val]=subtree

		
			
	return tree

print (create_itree(data,titles))
