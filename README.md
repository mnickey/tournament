# Swiss Style Tournament
This repository shows how one can create a reusable Swiss Style tournament. 

A Swiss-system tournament is a tournament which uses a non-elimination format. There are several rounds of competition, but considerably fewer rounds than in a round-robin tournament, so each competitor (team or individual) does not play every other competitor. Competitors meet one-to-one in each round and are paired using a predetermined set of rules designed to ensure that as far as possible a competitor plays competitors with the same current score, subject to not playing the same opponent more than once. The winner is the competitor with the highest aggregate points earned in all rounds. http://en.wikipedia.org/wiki/Swiss-system_tournament

To run or use:

1. Clone this repository at `https://github.com/mnickey/tournament`
2. Ensure that your vagrant is up and running. To do so, type in vagrant up where your vagrant file is stored.
3. This is followed by vagrant ssh
4. Type in `cd /vagrant/tournament/`
5. To run, type in `python tournament_test.py`
6. Enjoy 

If all goes well you should see something similar to the following:

```
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py 
Here I am in the database
1. Old matches can be deleted.
2. Player records can be deleted.
3. After deleting, countPlayers() returns zero.
4. After registering a player, countPlayers() returns 1.
5. Players can be registered and deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
[(1037, 'Twilight Sparkle', 1039, 'Applejack'), (1038, 'Fluttershy', 1040, 'Pinkie Pie')]
8. After one match, players with one win are paired.
Success!  All tests pass!
```

* Functionality: Passes the unit tests
* Table Design: Has meaningful names
* Column Design: Table columns have meaningful names
* Code Quality: Code is ready for personal review and formatted well.
* Comemnts: Comments are used to detail complex areas of code and to show testing process.
* Documentation: README is included and demonstrates the steps to successfully run the application.
