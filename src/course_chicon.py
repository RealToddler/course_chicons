import Competitor
import Time

def read_competitors(file_path):
    dico_part = {}
    str_part = 'participant_'
    with open(file_path, encoding='utf-8') as inscrits:
        reader = inscrits.readlines()
        without_header = reader[1:]
        bib = 1
        for line in without_header:
            line = line.strip("\n")
            line = line.split(';')
            dico_part[str_part + str(bib)] = Competitor.create(line[0], line[1], line[2], line[3], bib)
            bib += 1
    return dico_part

def show_competitors(comp):
    for competitor in comp.keys():
        print(Competitor.to_string(comp[competitor]))

def select_comp_by_bdate(comp_list, bdate):
    search_result = []
    for comp in comp_list.values():
        if comp['birth_date'].endswith(bdate):
            search_result.append(comp)
    return search_result

def select_comp_by_name(comp_list, name):
    search_result = []
    for comp in comp_list.values():
        if name in comp['last_name']:
            search_result.append(comp)
    return search_result

def read_performances(file_path):
    dico_perf = {}
    with open(file_path) as perf:
        perf_with_h = perf.readlines()
        final_perf = perf_with_h[1:]
        for line in final_perf:
            split_line = line.strip("\n")
            split_line = split_line.split(';')
            dico_perf[int(split_line[0])] = Time.create(split_line[1], split_line[2], split_line[3])
        return dico_perf

def merge_performances(dico_comp, dico_perf):
    for perf in list(dico_perf.items()):
        for match_bib in dico_comp.keys():
            if str(perf[0]) in match_bib:
                dico_comp[match_bib]['performance'] = perf[1]
    return dico_comp

def print_results(dict_comp):
    for racer in dict_comp.values():
        racer_string = Competitor.to_string(racer) + f"      => {racer['performance']}"
        print(racer_string)

def save_results(comp):
    with open("saved_results.csv", "w") as saved_results:
        header = ";".join(list(comp.values())[0].keys()) + "\n"
        saved_results.write(header)
        for competitor in comp.values():
            competitor = list(competitor.values())
            competitor[0] = str(competitor[0]) #prevent error while join (with bib_num being an integer)
            to_write = ";".join(competitor[:3]) + " " + competitor[5] + "\n"
            saved_results.write(to_write)


def select_competitor(competitors, check, criteria):
    search_result = []
    for competitor in competitors.values():
         if check(competitor):
             search_result.append(competitor, criteria)
    return search_result

def check_year(competitor, year):
    if competitor['birth_date'].endswith(year):
        return True
    return False

def check_sex(competitor, sex):
    if competitor['sex'] == sex:
        return True
    return False

def select_comp_by_sex(competitors, sex):
    search_result = []
    check = lambda comp: comp['sex'] == sex
    for competitor in competitors.values():
        if check(competitor):
            search_result.append(competitor)
    return search_result

def select_comp_by_birth_year(competitors, year):
    search_result = []
    check = lambda comp: comp['birth_date'].endswith(year)
    for competitor in competitors.values():
        if check(competitor):
            search_result.append(competitor)
    return search_result

def sort_competitors(dico_comp, sort_relation):
    comp_list = [competitor for competitor in dico_comp.values()]
    for i in range(1, len(comp_list)):
        j = i - 1
        while j >=0 and sort_relation(comp_list[i], comp_list[j]):
            comp_list[j+1] = comp_list[j]
            j -= 1
        comp_list[j+1] = comp_list[i]
    return comp_list

def sort_by_last_name(competitor1, competitor2):
    return competitor1['last_name'] < competitor2['last_name']

def sort_by_perf(competitor1, competitor2):
    if competitor2['performance'] == None or competitor1['performance'] < competitor2['performance']:
        return True
    return False

def sort_with_lambda(competitors, criteria):
    sorted_competitors = [competitor for competitor in competitors.values()]
    return sorted_competitors.sort(key=lambda comp: comp[criteria])