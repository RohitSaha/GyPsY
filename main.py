from EmotionAPIIntegration import get_emotion


moods = get_emotion()
age = raw_input("What is your age?")
gender = raw_input("What is your gender (Male/Female)?")
weather = raw_input("Would you prefer an outdoor or indoor? ")
time = raw_input("Would you like to go out in the Early Morning, Morning, Afternoon or Evening? ")
num = raw_input("Would you prefer to go Solo or in a Group?")

if weather=="Indoor":    
	if time=="Afternoon":            
		if age in range(12, 18):
			if gender=="Female":
				if moods=="sadness":
					if num=="Solo":
						print "Shopping"
					else:
						print "Food"
			else:
				print "Entertainment"
			
		elif age in range(18, 25):
			if moods=="anger":

				if gender=="Female":
                                    
					if num=="Solo":
						print "Entertainment"
			elif moods=="neutral":
				if num=="Solo":
					print "Entertainment"
				
				else:
					print "Shopping"

		elif age in range(25, 35):
			if moods=="anger":
				if (num=="Group" or gender=="Male"):
					print "Entertainment"
				else:
					print "Food"
			elif moods=="neutral":
				if num=="Group":
					print "Religious"
			else:
				print "Food"

		elif age in range(35, 45):
			if moods=="anger":
				if gender=="Female":
					print "Food"
				else:
					print "Religious"
			if moods=="happiness":
				print "Food"
			if mood=="neutral":
				if gender=="Female":
					print "Shopping"
			else:
				print "Entertainment"

		elif age in range(45, 55):
			if mood=="happiness":
				print "Food"
			elif mood=="neutral":
				print "Entertainment"
			else:
				print "Religious"

		elif age in range(55, 65):
			if mood=="anger":
				print "Religious"
			else:
				print "Food"

	elif time=="Early Morning":
		if moods=="anger":
			if gender=="Female":
				print "Food"
		elif moods=="sadness":
			if age in range(25, 35):
				print "Food"
		elif moods=="happiness":
			print "Entertainment"
		else:
			print "Religious"

	elif time=="Evening":	
		if age in range(12, 18):
			if moods=="anger":
				if num=="Solo":
					if gender=="Male":
						print "Entertainment"
			elif moods=="happiness":
				if gender=="Male":
					print "Entertainment"
			else:
				print "Food"
		
		elif age in range(18, 25):
			if moods=="happiness":
				if num=="Group":
					if gender=="Female":
						print "Food"
						
			else:
				print "Entertainment"
				
		elif age in range(25, 35):
			if moods=="anger":
				print "Food"
			
			if moods=="neutral":
				if num=="Solo":
					print "Entertainment"
					
			else:
				print "Religious"
				
		elif age in range(35, 45):
			if moods=="happiness":
				print "Entertainment"
			elif moods=="neutral":
				if num=="Group":
					print "Food"
				else:
					print "Religious"
					
		elif age in range(45, 55):
			if moods=="sadness":
				print "Food"
			else:
				print "Entertainment"
				
		else:
			if moods=="sadness":
				print "Food"
				
			else:
				print "Religious"
	elif time=="Morning":
		if age in range(12, 18):
			if mood=="neutral":
				print "Religious"
			if mood=="sadness":
				if gender=="Male":
					print "Religious"
			else:
				print "Food"
				
		elif age in range(18, 25):
			if moods=="anger":
				print "Religious"
			elif moods=="happiness":
				if gender=="Female":
					if num=="Solo":
						print "Religious"
				else:
					print "Entertainment"
					
			elif moods=="neutral":
				if gender=="Female":
					print "Religious"
			else:
				print "Food"
				
		else:
			print "Religious"
			
	else:
		print "Food"
		
else:
	if time=="Afternoon":
		if age in range(12, 18):
			if gender=="Female":
				print "Nature"
			else:
				print "Activity"
		elif age in range(18, 25):
			if moods=="anger":
				if num=="Solo":
					if gender=="Female":
						print "Nature"
			elif moods=="happiness":
				if gender=="Female":
					print "City feels"
			elif moods=="neutral":
				if gender=="Female":
					print "Nature"
				else:
					if num=="Group":
						print "City Feels"
						
			else:
				print "Activity"
				
		elif age in range(25, 35):
			if moods=="anger":
				print "Activity"
			else:
				print "City Feels"
				
		elif age in range(45, 55):
			print "Activity"
			
		elif age in range(35, 45):
			if moods=="anger":
				print "Nature"
			elif moods=="sadness":
				if gender=="Female":
					print "Nature"
			else:
				print "Activity"
				
		else:
			print "Nature"
	elif time=="Early Morning":
		if moods=="anger":
			if age in range(12, 18):
				print "Views"
			else:
				print "Nature"
				
		elif moods=="happiness":
			if age in range(25, 35):
				print "Views"
			else:
				print "City Feels"
		else:
			if age in range(12, 18):
				print "City Feels"
			elif age=="18-24":
				if gender=="Female":
					print "Views"
				else:
					if num=="Group":
						print "Views"
					else:
						print "Nature"
						
	elif time=="Evening":
		if age in range(12, 18):
			if gender=="Female":
				print "Views"
			else:
				print "Activity"
		elif age in range(18, 25):
			if moods=="anger":
				print 'Activity'
			elif moods=="happiness":
				if gender=="Female":
					print "Activity"
				else:
					print "City Feels"
			elif moods=="neutral":
				if num=="Group":
					print "City Feels"
			elif moods=="sadness":
				if gender=="Male":
					if num=="Solo":
						print "Activity"
			else:
				print "Views"
				
		elif age in range(25, 35):
			if moods=="anger":
				print "Activity"
			elif moods=="happiness":
				if num=="Solo":
					print "Nature"
			elif moods=="neutral":
				if gender=="Male":
					print "City Feels"
			else:
				print "Views"
		elif age in range(45, 55):
			print "Nature"
		else:
			print "City Feels"
			
	elif time=="Morning":
		if moods=="anger":
			if age in range(18, 25):
				print "Views"
		elif moods=="happiness":
			if age in range(25, 35):
				print "Activity"
		elif moods=="neutral":
			if num=="Group":
				print "Nature"
		elif moods=="sadness":
			print "Views"
		else:
			print "City Feels"
			
	else:
		if gender=="Male":
			if num=="Solo":
				print "Nature"
		else:
			print "Views" 
