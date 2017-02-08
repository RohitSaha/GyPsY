#mapping moods and other factors to themes using identification trees by calculating disorder and quality of a test

import math

#sample data
titles=['age','gender','mood','themes']
data=[['forty','male','happy','activity'],
	  ['fifty','female','happy','food'],
	  ['thirty','male','sad','food']]

#removes themes from titles
def only_feat(titles):
	of=[]
	for each in titles:
		if each!="themes":
			of.append(each)
	return of
	
#calculates the index of a given feature
def index(input):
	output=0
	for each in titles:
		if input==each:
			output=titles.index(each)
	return output

#returns a list of all the values under a given feature/theme
def feat_entries(feat,given_data):
	val=[]
	i=index(feat)
	for row in data:
		val.append(row[i])
	return val

#returns a list of UNIQUE values under a given feature/theme
def unique_val(feat,given_data):
	unique=[]
	entries=feat_entries(feat,given_data)
	for each in entries:
		if unique.count(each)==0:
			unique.append(each)
	return unique

#returns the most frequent value under themes
def default(feat,given_data):
	default=[]
	theme_total=feat_entries(feat,given_data)
	uniq_th=unique_val(feat,given_data)
	for each in uniq_th:
		v=theme_total.count(each)
		default.append(v)
	i=max(default)
	x=default.index(i)
	return uniq_th[x]

#returns a list of only the data that contains the required value of a feature
def modify_data(feat,value,given_data):
	data_mod=[]
	ind=index(feat)
	for row in given_data:
		if (row[ind]==value):
			data_mod.append(row)
	return data_mod


#finds the quality?disorder of a given feature/test	
def quality(given_data,feat):	
	values=unique_val(feat,given_data)
	quality=0.0
	m=len(data)
	dis=0.0
	for each in values:
		data_mod=[]
		ind=index(feat)
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

#choose feature with least disorder    
def choose_feat(titles,given_data):
	feat=None
	temp=[]
	for each in titles:
		var=quality(given_data,each)
		temp.append(var)
	min_disorder=min(temp)
	feat=titles[temp.index(min_disorder)]
	return feat

def remove_used_feat(feat,given_data):
	i=index(feat)
	new_data=[]

	for row in given_data:
		temp=[]
		for j in range(len(row)):
			if row[j]!=row[i]:
				temp.append(row[j])
		new_data.append(temp)
	
	return new_data

def used_feat(header,best):
	header_new=[]
	for each in header:
		if each!=best:
			header.append(each)
			

#creates itree	
def create_itree(given_data,titles):
	header=only_feat(titles)
	best=choose_feat(header,given_data)
	new_title=used_feat(titles,best)
	new_header=used_feat(header,best)
	new_data=remove_used_feat(best,given_data)
	
	tree={best:{}}
	
	for val in unique_val(best,given_data):
		data_mod=modify_data(best,val,new_data)
		total_themes=feat_entries("themes",data_mod)
		
		if ((len(new_header))<=0):
			var=default("themes",given_data)
			tree[best][val]=var
			
		elif((total_themes.count(total_themes[0])==len(total_themes))):
			tree[best][val]=total_themes[0]
			 
		else:
			tree[best][val]=create_itree(data_mod,new_title)
			
	return tree
		
	
#printed functions to make sure they were working properly
print index("themes")		
print feat_entries("themes",data)
print unique_val("themes",data)	
print default("themes",data)
print quality(data,"age")
print choose_feat(titles,data)

