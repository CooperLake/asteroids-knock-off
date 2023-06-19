# asteroids-knock-off

A simple recreation of the classic arcade game "Asteroids"

## Technologies

created using Pygame, aswell as the built in Math and random modules

## basic functionality

The program uses random number generators to calculate the size, speed, location, angle, and time of departure, making sure each play through is unique.
the player starts in the center of the screen and is represented but a small white square. The player uses WASD to move the rectangle and the goal is to not get hit. the player can press SPACEBAR to fire a canon which produces a horizontal beam that if contacts any asteroids, destroys them.
by the asteroids. Holding down the RSHIFT or LSHIFT button allows the user to move twice as fast. the asteroids fire on an interval between 0 and 20 seconds. if the user get hits by an asteroid they will be taken to a red screen where they will see a button saying try again. clicking it or pressing the RETURN key will reset the asteroids and it will reroll all the random number generators yielding a new experience. if the player can survive 25 seconds they will be taken to a green screen telling them they have won and giving them the option to play again.

A blue bar appears at the top of the screen which represents the canons charge
