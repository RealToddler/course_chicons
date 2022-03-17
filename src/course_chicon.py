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
    for competitor in comp:
        return(Competitor.to_string(comp[competitor]))

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

            dico_perf[int(split_line[0])] = split_line[1] + "h" + split_line[2] + "m" + split_line[3] + "s"
        return dico_perf

def merge_performances(dico_comp, dico_perf):
    print(dico_perf.items())
    for perf in list(dico_perf.items()):
        for match_bib in dico_comp.keys():
            if str(perf[0]) in match_bib:
                dico_comp[match_bib]['performance'] = perf[1]
    return dico_comp

def print_results(comp):
    for racer in comp:
        racer_string = Competitor.to_string(racer) + f"      => {racer['performance']}"
        print(racer_string)

def save_results(comp):
    with open("saved_results.csv", "w")