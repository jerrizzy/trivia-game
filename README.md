# trivia-game
A game using time to test reading speed/knowledge by increasing/decreasing playing time-based on selected answers. 

![Screen Shot 2024-06-06 at 1 27 45 AM](https://github.com/jerrizzy/trivia-game/assets/37149800/5879693e-3c3e-4de9-afbb-df3d8625b1f7)

The game was built using Python classes to store the question-answer objects.
After constructing all the question objects via the Python classes, we imported them into Pygame.

![Screen Shot 2024-06-06 at 1 28 15 AM](https://github.com/jerrizzy/trivia-game/assets/37149800/bf53d25d-3d53-4533-bb60-0e7394fed448)

The gameplay is for each question the player has four answers in a box, different colors, and only one has a 100% accurate answer. 
Based on which box the player chooses determines if 5 seconds get added to the gameplay time, 5 seconds is removed, no time is removed or kills the whole game if the answer is egregiously wrong.

To choose a box, player musts click on the box. 
Used collidepoint method is used to pinpoint the position of the boxes on the screen.

###BUGS TO FIX###

After gameplay time is not reset back to the initial 60 seconds.

to play game:
Open trivia-game in VsCode
then 
python lib/mygame.py
