#!/usr/bin/python3
# -*- coding: utf-8 -*-
import Time

"""
:mod:`Competitor` module

:author: `FIL - Département Informatique - Université de Lille <http://portail.fil.univ-lille1.fr>`_

:date: Juin, 2019

Module for competitor representation.
A competitor

"""



def create (first_name, last_name, sex, birth_date, bib_num):
    """
    
    :param first_name: first name of a competitor
    :type name: string
    :param last_name: last name of a competitor
    :type name: string
    :param sex: sex of a competitor 'M' or 'F'
    :type name: string
    :param birth_date: birth date of the competitor, format is "DD/MM/YYY"
    :type birth_date: string
    :param bib_num: bib number of the competitor
    :type bib_num: int    
    :return: a new record for this competitor
    :rtype: Competitor
    :UC: bib_num > 0 and sex in 'MF'
    """
    assert bib_num > 0 and sex in 'MF'
    return {
        'bib_num' : bib_num,
        'first_name' : first_name,
        'last_name' : last_name,
        'sex' : sex,
        'birth_date' : birth_date,
        'performance' : None
    }

def get_firstname (comp):
    """
    
    :param comp:
    :type comp: Competitor
    :return: first name of competitor comp
    :rtype: str
    :UC: none
    """
    return comp['first_name']

def get_lastname (comp):
    """
    
    :param comp:
    :type comp: Competitor
    :return: last name of competitor comp
    :rtype: str
    :UC: none
    """
    return comp['last_name']

def get_birthdate (comp):
    """

    :param comp:
    :type comp: Competitor
    :return: birthdate of competitor comp
    :rtype: str
    :UC: none

    """
    return comp['birth_date']

def get_bib_num (comp):
    """

    :param comp:
    :type comp: Competitor
    :return: bib number of competitor comp
    :rtype: str
    :UC: none

    """
    return comp['bib_num']

def get_performance (comp):
    """

    :param comp:
    :type comp: Competitor
    :return: performance of competitor comp
    :rtype: time
    :UC: none
    """
    return comp['performance']

def get_sex (comp):
    """

    :param comp:
    :type comp: Competitor
    :return: sex of competitor comp
    :rtype: time
    :UC: none
    """
    return comp['sex']

def set_performance (comp, d):
    """

    :param comp: competitor to be modified
    :type comp: Competitor
    :param d: performance of competitor comp
    :type d: time
    :return: None
    :Side effect: performance of competitor comp is modified with value d
    :UC: none
    """
    comp['performance'] = d

def to_string(competitor):
    """
    :param competitor: a competitor
    :type comp: Competitor
    :return: a string representation for given competitor, form is "[bib] : first last (sex - birth)"
    """
    return "[{}]: {} {} ({} - {}) ".format(get_bib_num(competitor),get_firstname(competitor),get_lastname(competitor),
                                           get_sex(competitor),get_birthdate(competitor))


# 6 - TRIS

# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def compare_last_name(competitor1, competitor2):
    """
    This function returns True if the first competitor's last name appears 
    after the name of the second competitor's last name  in alphabetical order.
    compare_last_name() admit two args:
    - competitor1 (type dict) = > first competitor's object.
    - competitor2 (type dict) = > second competitor's object.
    """
    return competitor1['last_name'] < competitor2['last_name']


# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def sort_competitors_by_last_name(competitorsDict):
    """
    This function sorts the competitors' dict alphabetically on the competitors' last names 
    and returns it as a list.
    sort_competitors_by_last_name() only admit one arg:
    - competitorsDict (type dict) => dict that contains every competitors' data.
    """
    # creating a list of every competitors to sort them using a sort by insertion algorithm
    competitorsList = [competitorsDict[competitor] for competitor in competitorsDict]
    # sort by insertion
    for i in range(1, len(competitorsList)):
        lastName = competitorsList[i]
        j = i - 1
        while j >= 0 and compare_last_name(lastName, competitorsList[j]):
            competitorsList[j + 1] = competitorsList[j]
            j -= 1
        competitorsList[j + 1] = lastName
    return competitorsList


# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def sort_competitors_by_performance(competitorsDict):
    """
    This function sorts the competitors' dict on the competitors' performances and returns it as a list.
    Competitors performance-less are sorted alphabetically at the end of the list.
    sort_competitors_by_performance() only admit one arg:
    - competitorsDict (type dict) => dict that contains every competitors' data.
    """
    # creating a list of every competitors with performances recorded
    # to sort them using a sort by insertion algorithm
    withPerf = [
        competitorsDict[competitor] for competitor in competitorsDict \
            if competitorsDict[competitor]['performance'] != None
            ]
    # creating a dict with all competitors performance-less in order to sort them alphabetically 
    # using sort_competitors_by_last_name() function above
    perfLess = {competitor: competitorsDict[competitor] for competitor in competitorsDict \
            if competitorsDict[competitor]['performance'] == None
            }
    # sort by insertion on competitors with performances recorded
    for i in range(1, len(withPerf)):
        performance = withPerf[i]
        j = i - 1
        while j >= 0 and Time.compare(performance['performance'], withPerf[j]['performance'])[0] == '-':
            withPerf[j + 1] = withPerf[j]
            j -= 1
        withPerf[j + 1] = performance
    return withPerf + sort_competitors_by_last_name(perfLess) # concatenate competitors sorted by performances and
                                                            # competitors performance-less sorted alphabetically 
                                                            # at the end of the list


    
if __name__ == '__main__':
    pass    
