if weather=="Indoor":
	if time=="Afternoon":
		if age=="12-17":
			if gender=="Female":
				if moods=="sadness":
					if num=="Solo":
						print "Shopping"
					else:
						print "Food"
			
			else:
				print "Entertainment"
			
		elif age=="18-24":
			if moods=="anger":
				if gender=="Female":
					if num=="Solo":
						print "Entertainment"
			
			elif moods=="neutral":
				if num=="Solo":
					print "Entertainment"
				
				else:
					print "Shopping"

		elif age=="25-34":
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

		elif age=="35-44":
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

		elif age=="45-54":
			if mood=="happiness":
				print "Food"
			elif mood=="neutral":
				print "Entertainment"
			else:
				print "Religious"

		elif age=="55-64":
			if mood=="anger":
				print "Religious"
			else:
				print "Food"

	elif time=="Early Morning":
		if moods=="anger":
			if gender=="Female":
				print "Food"
		elif moods=="sadness":
			if age=="25-34":
				print "Food"
		elif moods=="happiness":
			print "Entertainment"
		else:
			print "Religious"

	elif time=="Evening":	
		if age=="12-17":
			if moods=="anger":
				if num=="Solo":
					if gender=="Male":
						print "Entertainment"
			elif moods=="happiness":
				if gender=="Male":
					print "Entertainment"
			else:
				print "Food"
		
		elif age=="18-24":
			if moods=="happiness":
				if num=="Group":
					if gender=="Female":
						print "Food"
						
			else:
				print "Entertainment"
				
		elif age=="25-34":
			if moods=="anger":
				print "Food"
			
			if moods=="neutral":
				if num=="Solo":
					print "Entertainment"
					
			else:
				print "Religious"
				
		elif age=="35-44":
			if moods=="happiness":
				print "Entertainment"
			elif moods=="neutral":
				if num=="Group":
					print "Food"
				else:
					print "Religious"
					
		elif age=="45-54":
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
		if age=="12-17":
			if mood=="neutral":
				print "Religious"
			if mood=="sadness":
				if gender=="Male":
					print "Religious"
			else:
				print "Food"
				
		elif age=="18-24":
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
		if age=="12-17":
			if gender=="Female":
				print "Nature"
			else:
				print "Activity"
		elif age=="18-24":
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
				
		elif age=="25-34":
			if moods=="anger":
				print "Activity"
			else:
				print "City Feels"
				
		elif age=="45-54":
			print "Activity"
			
		elif age=="35-44":
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
			if age=="12-17":
				print "Views"
			else:
				print "Nature"
				
		elif moods=="happiness":
			if age=="25-33":
				print "Views"
			else:
				print "City Feels"
		else:
			if age=="12-17":
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
		if age=="12-17":
			if gender=="Female":
				print "Views"
			else:
				print "Activity"
		elif age=="18-24":
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
				
		elif age=="25-34":
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
		elif age=="45-54":
			print "Nature"
		else:
			print "City Feels"
			
	elif time=="Morning":
		if moods=="anger":
			if age=="18-24":
				print "Views"
		elif moods=="happiness":
			if age=="25-34":
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
				
			
	
			
				
				
			
					
					
			
		
	
				
			
						
				
				
					
					
			
		
				
						
						
				
				
				
				
				
				
					
					
					
					
					
					
					
					

			
			
			
			
			
			
			
			
			
			
					
				
						