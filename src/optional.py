import Time, Competitor, course_chicon

# getting data
competitors = course_chicon.read_competitors("inscrits.csv")
performances = course_chicon.read_performances("performances.csv")
course_chicon.merge_performances(competitors, performances)

# 8 COMPLEMENTS

# 8.1 - Pour les fonctions de sélection
# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def select_competitor(competitors, check):
    """
    This function returns the list of competitors which respect the condition 
    of the given predicate function.
    select_competitor() admit two args:
    - competitors (type dict) => dict which contains every competitors objet.
    - check (type func) => predicate function.
    """
    return [competitor for competitor in competitors.values() if check(competitor)]


# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def check_if_1980(competitor):
    """
    This function is a predicate function. It checks if the given competitor 
    was born in 1980 returning True or False.
    check_if_1980() only admit one arg:
    - competitor (type dict) => dict which contains competitor's data.
    """
    return Competitor.get_birthdate(competitor).endswith("1980")


# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def check_if_woman(competitor):
    """
    This function is a predicate function. It checks if the given competitor 
    is a woman returning True or False.
    check_if_woman() only admit one arg:
    - competitor (type dict) => dict which contains competitor's data.
    """
    return Competitor.get_sex(competitor) == 'F'
    

# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def select_competitor_if_woman(competitors):
    """
    This function returns the list of every female competitors using lambda expression.
    select_competitor_if_woman() only admit one arg:
    - competitor (type dict) => dict which contains competitor's data.
    """
    check = lambda competitor: Competitor.get_sex(competitor) == 'F'
    return [competitor for competitor in competitors.values() if check(competitor)]


# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def select_competitor_by_birth_year(competitors):
    """
    This function returns the list of every competitors born in 1980 using lambda expression.
    select_competitor_by_birth_year() only admit one arg:
    - competitor (type dict) => dict which contains competitor's data.
    """
    check = lambda competitor: Competitor.get_birthdate(competitor).endswith("1980")
    return [competitor for competitor in competitors.values() if check(competitor)]


# 8.2 Pour les tris
# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def sort_competitors(competitorsDict, sortRelation):
    """
    This function sorts the competitors' dict on the competitors' on a relation chosen by the user and returns it as a list.
    sort_competitors() admit two args:
    - competitorsDict (type dict) => dict that contains every competitors' data.
    - sortRelation (type func) => predicate function
    """
    # sort by insertion
    competitorsList = [competitor for competitor in competitorsDict.values()]
    for i in range(1, len(competitorsList)):
        competitor = competitorsList[i]
        j = i - 1
        while j >= 0 and sortRelation(competitor, competitorsList[j]):
            competitorsList[j + 1] = competitorsList[j]
            j -= 1
        competitorsList[j + 1] = competitor
    return competitorsList


# REFACTO : DONE, WORKING : ISSUES WHEN PERFORMANCE = 'None', DOCSTRING : DONE, COMMENT : DONE
def sort_by_perf(competitor1, competitor2):
    """
    This function is a predicate function. It compares the difference between two competitors performances. 
    sort_by_perf() admit two arg:
    - competitor1 (type dict) = > dict which contains first competitor's data.
    - competitor2 (type dict) = > dict which contains second competitor's data.
    """
    if competitor1["performance"] == None or competitor2["performance"] == None:
        return True
    else:
        return Time.compare(competitor1['performance'], competitor2['performance'])[0] == '-'

# REFACTO : DONE, WORKING : ISSUES WHEN PERFORMANCE = 'None', DOCSTRING : DONE, COMMENT : DONE
def sort_by_last_name(competitor1, competitor2):
    """
    This function returns True if the first competitor's last name appears 
    after the name of the second competitor's last name  in alphabetical order.
    compare_last_name() admit two args:
    - competitor1 (type dict) = > first competitor's object.
    - competitor2 (type dict) = > second competitor's object.
    """
    return competitor1['last_name'] < competitor2['last_name']


# FUNCTIONS CALLS

# print(select_competitor(competitors, check_if_1980))
# print(sort_competitors(competitors, sort_by_perf))
# print(sort_competitors(competitors, sort_by_last_name))