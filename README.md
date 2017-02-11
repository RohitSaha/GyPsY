# GyPsY
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
> data_places.csv - Contains data for mapping to places
> data_train.csv - Contains data required for training Identification tree
> EmotionAPIIntegration.py - Use of Microsoft Cognitive services in order to capture emotion from image
> generate_places_from_themes.py - Code required to map themes to places
> updated_id_tree.py - Core Identification tree program
> Gypsy.py - Main file required to run the program

Contributors :
Rohit Saha
Aparna Krishnakumar
Sourav Sharan
Sree Harsha Nelaturu
