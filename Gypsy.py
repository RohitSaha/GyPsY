from EmotionAPIIntegration import get_emotion
from generate_places_from_theme import get_place

moods = get_emotion()
age = raw_input("What is your age?")
gender = raw_input("What is your gender (Male/Female)?")
weather = raw_input("Would you prefer an Outdoor or Indoor? ")
time = raw_input("Would you like to go out in the Early Morning, Morning, Afternoon or Evening? ")
num = raw_input("Would you prefer to go Solo or in a Group?")

if weather=="Indoor":    
	if time=="Afternoon":            
		if age in range(12, 18):
			if gender=="Female":
				if moods=="sadness":
					if num=="Solo":
						result = "Shopping"
					else:
						result = "Food"
			else:
				result = "Entertainment"
			
		elif age in range(18, 25):
			if moods=="anger":

				if gender=="Female":
                                    
					if num=="Solo":
						result = "Entertainment"
			elif moods=="neutral":
				if num=="Solo":
					result = "Entertainment"
				
				else:
					result = "Shopping"

		elif age in range(25, 35):
			if moods=="anger":
				if (num=="Group" or gender=="Male"):
					result = "Entertainment"
				else:
					result = "Food"
			elif moods=="neutral":
				if num=="Group":
					result = "Religious"
			else:
				result = "Food"

		elif age in range(35, 45):
			if moods=="anger":
				if gender=="Female":
					result = "Food"
				else:
					result = "Religious"
			if moods=="happiness":
				result = "Food"
			if mood=="neutral":
				if gender=="Female":
					result = "Shopping"
			else:
				result = "Entertainment"

		elif age in range(45, 55):
			if mood=="happiness":
				result = "Food"
			elif mood=="neutral":
				result = "Entertainment"
			else:
				result = "Religious"

		elif age in range(55, 65):
			if mood=="anger":
				result = "Religious"
			else:
				result = "Food"

	elif time=="Early Morning":
		if moods=="anger":
			if gender=="Female":
				result = "Food"
		elif moods=="sadness":
			if age in range(25, 35):
				result = "Food"
		elif moods=="happiness":
			result = "Entertainment"
		else:
			result = "Religious"

	elif time=="Evening":	
		if age in range(12, 18):
			if moods=="anger":
				if num=="Solo":
					if gender=="Male":
						result = "Entertainment"
			elif moods=="happiness":
				if gender=="Male":
					result = "Entertainment"
			else:
				result = "Food"
		
		elif age in range(18, 25):
			if moods=="happiness":
				if num=="Group":
					if gender=="Female":
						result = "Food"
						
			else:
				result = "Entertainment"
				
		elif age in range(25, 35):
			if moods=="anger":
				result = "Food"
			
			if moods=="neutral":
				if num=="Solo":
					result = "Entertainment"
					
			else:
				result = "Religious"
				
		elif age in range(35, 45):
			if moods=="happiness":
				result = "Entertainment"
			elif moods=="neutral":
				if num=="Group":
					result = "Food"
				else:
					result = "Religious"
					
		elif age in range(45, 55):
			if moods=="sadness":
				result = "Food"
			else:
				result = "Entertainment"
				
		else:
			if moods=="sadness":
				result = "Food"
				
			else:
				result = "Religious"
	elif time=="Morning":
		if age in range(12, 18):
			if mood=="neutral":
				result = "Religious"
			if mood=="sadness":
				if gender=="Male":
					result = "Religious"
			else:
				result = "Food"
				
		elif age in range(18, 25):
			if moods=="anger":
				result = "Religious"
			elif moods=="happiness":
				if gender=="Female":
					if num=="Solo":
						result = "Religious"
				else:
					result = "Entertainment"
					
			elif moods=="neutral":
				if gender=="Female":
					result = "Religious"
			else:
				result = "Food"
				
		else:
			result = "Religious"
			
	else:
		result = "Food"
		
else:
	if time=="Afternoon":
		if age in range(12, 18):
			if gender=="Female":
				result = "Nature"
			else:
				result = "Activity"
		elif age in range(18, 25):
			if moods=="anger":
				if num=="Solo":
					if gender=="Female":
						result = "Nature"
			elif moods=="happiness":
				if gender=="Female":
					result = "City feels"
			elif moods=="neutral":
				if gender=="Female":
					result = "Nature"
				else:
					if num=="Group":
						result = "City Feels"
						
			else:
				result = "Activity"
				
		elif age in range(25, 35):
			if moods=="anger":
				result = "Activity"
			else:
				result = "City Feels"
				
		elif age in range(45, 55):
			result = "Activity"
			
		elif age in range(35, 45):
			if moods=="anger":
				result = "Nature"
			elif moods=="sadness":
				if gender=="Female":
					result = "Nature"
			else:
				result = "Activity"
				
		else:
			result = "Nature"
	elif time=="Early Morning":
		if moods=="anger":
			if age in range(12, 18):
				result = "Views"
			else:
				result = "Nature"
				
		elif moods=="happiness":
			if age in range(25, 35):
				result = "Views"
			else:
				result = "City Feels"
		else:
			if age in range(12, 18):
				result = "City Feels"
			elif age=="18-24":
				if gender=="Female":
					result = "Views"
				else:
					if num=="Group":
						result = "Views"
					else:
						result = "Nature"
						
	elif time=="Evening":
		if age in range(12, 18):
			if gender=="Female":
				result = "Views"
			else:
				result = "Activity"
		elif age in range(18, 25):
			if moods=="anger":
				result = 'Activity'
			elif moods=="happiness":
				if gender=="Female":
					result = "Activity"
				else:
					result = "City Feels"
			elif moods=="neutral":
				if num=="Group":
					result = "City Feels"
			elif moods=="sadness":
				if gender=="Male":
					if num=="Solo":
						result = "Activity"
			else:
				result = "Views"
				
		elif age in range(25, 35):
			if moods=="anger":
				result = "Activity"
			elif moods=="happiness":
				if num=="Solo":
					result = "Nature"
			elif moods=="neutral":
				if gender=="Male":
					result = "City Feels"
			else:
				result = "Views"
		elif age in range(45, 55):
			result = "Nature"
		else:
			result = "City Feels"
			
	elif time=="Morning":
		if moods=="anger":
			if age in range(18, 25):
				result = "Views"
		elif moods=="happiness":
			if age in range(25, 35):
				result = "Activity"
		elif moods=="neutral":
			if num=="Group":
				result = "Nature"
		elif moods=="sadness":
			result = "Views"
		else:
			result = "City Feels"
			
	else:
		if gender=="Male":
			if num=="Solo":
				result = "Nature"
		else:
			result = "Views"

places = get_place(result)

print "You should try to do one of the following:"
for i in places:
        print(i)
        
