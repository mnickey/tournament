#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament
import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    print "Here I am in the database"
    # used to see if we are actually calling this function properly
    return psycopg2.connect("dbname=tournament")

def deleteMatches():
    """Remove all the match records from the database."""
    c.execute(""" DELETE FROM matches ;""")
    pass

def deletePlayers():
    """Remove all the player records from the database."""
    c.execute(" DELETE FROM player ; ")
    db.commit()

def countPlayers():
    """Returns the number of players currently registered."""
    c.execute(""" SELECT count(pname) AS playerCount FROM player; """)
    # pcount = c.execute(""" SELECT count(pname) AS playerCount FROM player; """)
    results = c.fetchall()
    # print "results:", results
    # print "results sub 0: ", results[0]
    # print "results sub 0 0: ", results[0][0]
    db.commit()
    return (results[0][0])

def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    c.execute("""INSERT INTO player (pname, wins, losses) VALUES (%s, 0, 0); """ ,(bleach.clean(name), ) )
    db.commit()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    c.execute("""SELECT id, pname, wins, (wins + losses) as matches FROM player;""")
    results = c.fetchall()
    # print "results: ", results
    return results

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    c.execute("""UPDATE player set wins = wins + 1 WHERE id=(%s); """, (winner,) )
    c.execute("""UPDATE player set losses = losses + 1 WHERE id=(%s); """, (loser,) )
    db.commit()
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name

    Theory:
      Get the count from the DB sorted by wins
      take a slice of the first two and make them a pair
      remove them from the pre-populated count
      continue to do so until all pairs are complete
    """

    from itertools import chain

    c.execute(""" SELECT id, pname FROM player ORDER BY wins DESC;""")
    results = c.fetchall()
    pairs = []
    for i in range(0, len(results), 2):
        pair = tuple(chain(*results[i:i+2]))
        pairs.append(pair)
    print pairs
    return pairs


db = connect()
c = db.cursor()

if __name__ == '__main__':
    # registerPlayer("Mike")
    # registerPlayer("Paula")
    # registerPlayer("Jenny")
    # registerPlayer("Tom")
    # registerPlayer("Michael")
    print (countPlayers())
    # commented out but confirmed that deleting the players works
    deletePlayers()
    # db.cursor.close()
    db.close
