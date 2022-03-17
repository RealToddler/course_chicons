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


def compare_last_name(comp1, comp2):
    return comp1['last_name'] < comp2['last_name']

def sort_by_competitors_by_last_name(dico_comp):
    lname_list = []
    for key in dico_comp.keys():
        lname_list.append(dico_comp[key]['last_name'])
    for i in range(1, len(lname_list)):
        lname = lname_list[i]
        j = i - 1
        while j >=0 and compare_last_name(lname, lname_list[j]):
            lname_list[j+1] = lname_list[j]
            j -= 1
        lname_list[j+1] = lname
    return lname_list

def sort_by_competitors_by_performance(dico_comp):
    comp_list = []
    for key in dico_comp.keys():
        comp_list.append(dico_comp[key])
    for i in range(1, len(comp_list)):
        perf = comp_list[i]['performance']
        j = i - 1
        if perf == None:
            comp_list.append(comp_list.pop(comp_list[i]))
            continue
        while j >=0 and Time.compare(perf, comp_list[j]['performance']):
            comp_list[j+1] = comp_list[j]
            j -= 1
        comp_list[j+1] = comp_list[i]
    return comp_list
        

if __name__ == '__main__':
    pass    


