# GyPsY

Contributers : [Rohit Saha](https://github.com/RohitSaha), [Aparna Krishnakumar](https://github.com/Aparnaakk), [Sourav Sharan](https://github.com/SouravSharan), [Sree Harsha Nelaturu](https://github.com/TheBigFundamental)

Using Identification trees to recommend activity(Themes) to people based on certain classifiers : 

Possible classifiers : 
<ul>
<li> Age
<li> Gender
<li> Moods
<li> Timestamp
<li> Weather
<li> Solo/Group
</ul>

Target classifier :
<ul>
<li> Themes
</ul>

For running the project,
Key files required are :
<ol>
<li> data_places.csv - Contains data for mapping to places
<li> data_train.csv - Contains data required for training Identification tree
<li> EmotionAPIIntegration.py - Use of Microsoft Cognitive services in order to capture emotion from image
<li> generate_places_from_themes.py - Code required to map themes to places
<li> updated_id_tree.py - Core Identification tree program
<li> Gypsy.py - Main file required to run the program
</ol>
Once these resources are compiled, run Gypsy.py to access the program.

Sample:
[INPUT]
<ul>
<li>Emotion : "Neutral"
<li>What is your age?18
<li>What is your gender (Male/Female)?Male
<li>Would you prefer an Outdoor or Indoor? Outdoor
<li>Would you like to go out in the Early Morning, Morning, Afternoon or Evening? Afternoon
<li>Would you prefer to go Solo or in a Group?Group
</ul>

[OUTPUT]
<ul>
<li>You should try to do one of the following:
<li>Observe crocodiles at the Crocodile Bank
<li>Go have a picnic at Thollakapiar Poonga, Mandavelipakkam
<li>Cycle and View the animals and beautiful greenery at Vandalur Zoo
</ul>
