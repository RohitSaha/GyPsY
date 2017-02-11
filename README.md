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
<ol>
<li> data_places.csv - Contains data for mapping to places
<li> data_train.csv - Contains data required for training Identification tree
<li> EmotionAPIIntegration.py - Use of Microsoft Cognitive services in order to capture emotion from image
<li> generate_places_from_themes.py - Code required to map themes to places
<li> updated_id_tree.py - Core Identification tree program
<li> Gypsy.py - Main file required to run the program
</ol>

Contributors :
<ul>
<li>Rohit Saha
<li>Aparna Krishnakumar
<li>Sourav Sharan
<li>Sree Harsha Nelaturu
