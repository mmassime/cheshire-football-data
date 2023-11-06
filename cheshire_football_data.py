from cat.mad_hatter.decorators import tool, hook, plugin
from pydantic import BaseModel
from datetime import datetime, date
from footballscraper import Leagues


def docstring_parameter(*sub):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(*sub)
        return obj
    return dec

leagues = {'Serie A' : Leagues.SerieA(), 
           'Premier League' : Leagues.PremierLeague(),
           'Bundesliga' : Leagues.Bundes(),
           'La Liga': Leagues.LaLiga(),
           'Ligue 1': Leagues.Ligue1()}

@tool
def serie_a(tool_input, cat):
    """Replies to questions about current state of the italian football league, Serie A. 
    Input is always None"""
        
    res = "This is the table of the league \n"
    res += str(leagues["Serie A"].get_table())
    return res

@tool
@docstring_parameter(str(list(leagues['Serie A'].get_teams().keys())))
def team_serie_a(tool_input, cat):
    """Replies to questions about a team that plays in the italian football league, Serie A. 
    Input is a string with the name of the team from this list {0}"""
        
    team = leagues['Serie A'].get_teams()[tool_input]
    res = "These are the players\n"
    for player in team.get_players().items():
        res += str(player[1]) + ", "
    res += "These are the matches\n"
    for match in team.get_matches():
        res += match[0] + "-" +match[2] + " " + match[1] +" " + match[4] + ", "
    return res

@tool
def premier_league(tool_input, cat):
    """Replies to questions about current state of the british football league, Premier League. 
    Input is always None"""
        
    res = "This is the table of the league \n"
    res += str(leagues["Premier League"].get_table())
    return res

@tool
@docstring_parameter(str(list(leagues['Premier League'].get_teams().keys())))
def team_premier_league(tool_input, cat):
    """Replies to questions about a team that plays in the british football league, Premier League. 
    Input is a string with the name of the team from this list {0}"""
        
    team = leagues["Premier League"].get_teams()[tool_input]
    res = "These are the players\n"
    for player in team.get_players().items():
        res += str(player[1]) + ", "
    res += "These are the matches\n"
    for match in team.get_matches():
        res += match[0] + "-" +match[2] + " " + match[1] +" " + match[4] + ", "
    return res

@tool
def bundesliga(tool_input, cat):
    """Replies to questions about current state of the german football league, Bundesliga. 
    Input is always None"""
        
    res = "This is the table of the league \n"
    res += str(leagues["Bundesliga"].get_table())
    return res

@tool
@docstring_parameter(str(list(leagues['Bundesliga'].get_teams().keys())))
def team_bundesliga(tool_input, cat):
    """Replies to questions about a team that plays in the german football league, Bundesliga. 
    Input is a string with the name of the team from this list {0}"""
        
    team = leagues["Bundesliga"].get_teams()[tool_input]
    res = "These are the players\n"
    for player in team.get_players().items():
        res += str(player[1]) + ", "
    res += "These are the matches\n"
    for match in team.get_matches():
        res += match[0] + "-" +match[2] + " " + match[1] +" " + match[4] + ", "
    return res

@tool
def la_liga(tool_input, cat):
    """Replies to questions about current state of the spanish football league, La Liga. 
    Input is always None"""
        
    res = "This is the table of the league \n"
    res += str(leagues['La Liga'].get_table())
    return res

@tool
@docstring_parameter(str(list(leagues['La Liga'].get_teams().keys())))
def team_la_liga(tool_input, cat):
    """Replies to questions about a team that plays in the spanish football league, La Liga. 
    Input is a string with the name of the team from this list {0}"""
        
    team = leagues['La Liga'].get_teams()[tool_input]
    res = "These are the players\n"
    for player in team.get_players().items():
        res += str(player[1]) + ", "
    res += "These are the matches\n"
    for match in team.get_matches():
        res += match[0] + "-" +match[2] + " " + match[1] +" " + match[4] + ", "
    return res

@tool
def ligue_1(tool_input, cat):
    """Replies to questions about current state of the french football league, Ligue 1. 
    Input is always None"""
        
    res = "This is the table of the league \n"
    res += str(leagues['Ligue 1'].get_table())
    return res

@tool
@docstring_parameter(str(list(leagues['Ligue 1'].get_teams().keys())))
def team_ligue_1(tool_input, cat):
    """Replies to questions about a team that plays in the french football league, Ligue 1. 
    Input is a string with the name of the team from this list {0}"""
        
    team = leagues['Ligue 1'].get_teams()[tool_input]
    res = "These are the players\n"
    for player in team.get_players().items():
        res += str(player[1]) + ", "
    res += "These are the matches\n"
    for match in team.get_matches():
        res += match[0] + "-" +match[2] + " " + match[1] +" " + match[4] + ", "
    return res