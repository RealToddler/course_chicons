import Competitor
import Time

# 3 - GESTION DES INSCRITS


# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def read_competitors(fileName):
    """
    This function returns a dict of competitors object from data read into a csv file.
    read_competitors() only admit one arg: 
    - fileName (str type) => csv file's name.
    """
    participantsDict = {} # initializing the dict which competitors will be saved
    try:
        with open("data/" + fileName, 'r', encoding="utf-8") as file:
            participants = file.readlines()
            participants.remove(participants[0]) # removing csv header
            bib = 1
            for participant in participants:
                participant = participant.rstrip().split(';')
                # updating participantsDict creating a competitor object (which is actually a dict)
                participantsDict['participant_' + str(bib)] = Competitor.create( 
                    participant[0], 
                    participant[1], 
                    participant[2], 
                    participant[3], 
                    bib
                )
                bib += 1 # bib increment
    except FileNotFoundError:
        return "Incorrect file name"
    return participantsDict


# 4 - MANIPUALTIONS DU DICTIONNAIRE

# 4.1 - Affichage
# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def show_competitors(competitors):
    """
    This function shows every single competitor's object contained into a main dict.
    show_competitors() only admit one arg:
    - competitors (type dict) => dict which contains every competitors objet.
    """
    for competitor in competitors.keys():
        print(Competitor.to_string(competitors[competitor]))


# 4.2 - Sélections
# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def select_competitor_by_birth_year(competitors, birthYear):
    """
    This function returns the list of every competitors who were born during the selected year.
    select_comp_by_birth_year() only admit two args:
    - competitors (type dict) => dict which contains every competitors objet.
    - birthYear (type int or str) => birth's year on which you want to select the competitors.
    """
    return [
        competitor for competitor in competitors.values() if Competitor.get_birthdate(competitor).endswith(str(birthYear))
        ]


# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def select_competitor_by_name(competitors, lastName):
    """
    This function returns the list of every competitors who have the selected last name.
    select_comp_by_name() only admit two args:
    - competitors (type dict) => dict which contains every competitors objet.
    - lastName (type str) => last name's on which you want to select the competitors.
    """
    return [
        competitor for competitor in competitors.values() if Competitor.get_lastname(competitor) == lastName
    ]


# 5 - REPORT DES PERFORMANCES

# 5.1 - Lecture des performances
# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def read_performances(fileName):
    """
    This function returns a dict of performances object from data read into a csv file.
    read_performance() only admit one arg: 
    - fileName (str type) => csv file's name.
    """
    performanceDict = {} # initializing the dict which competitors will be saved
    with open("data/" + fileName, 'r', encoding="utf-8") as file:
        performances = file.readlines()
        performances.remove(performances[0]) # removing csv header
        for performance in performances:
            performance = performance.rstrip().split(';')
            # updating performanceDict creating a performance object (which is actually a dict)
            performanceDict[int(performance[0])] = Time.create(
                int(performance[1]), 
                int(performance[2]), 
                int(performance[3])
            )
        return performanceDict


# 5.2 - Report
# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def merge_performances(competitors, performances):
    """
    This function merges competitors performances from dict performances into competitors dict.
    merge_performances() only admit two args:
    - competitors (type dict) => dict which contains every competitors objet.
    - performances (type dict) => dict which contains competitors performances objet.
    """
    for competitor in competitors:
        try: # prevent an error if bib number doesn't exist in performances
            bib = competitors[competitor]["bib_num"]
            performance = performances[bib]
            Competitor.set_performance(competitors[competitor], performance)
        except KeyError:
            pass


# 7 - PUBLICATION ET SAUVEGARDE DES RESULTATS

# 7.1 - Affichage des résultats
# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def print_results(competitors):
    """
    This function shows every single competitor's with their respective performance.
    print_results() only admit one arg:
    - competitors (type dict) => dict which contains every competitors objet.
    """
    for competitor in competitors:
        if competitor["performance"] != None:
            print(Competitor.to_string(competitor) + "\t=> "+ Time.to_string(competitor["performance"]))
        else:
            print(Competitor.to_string(competitor))


# REFACTO : DONE, WORKING : TRUE, DOCSTRING : DONE, COMMENT : DONE
def save_results(competitors):
    """
    This function saves the race's results into a .txt file.
    save_results() only admit one arg:
    - competitors (type dict) => dict which contains every competitors objet.
    """
    with open("data/saved_results.csv", 'w', encoding="utf-8") as savedFile:
        # writing header into save file
        header = "Num_dossard; Prénom; Nom; Performance\n"
        savedFile.write(header)
        
        for competitor in competitors:
            # setting up every date to save into the save file
            bib = str(competitors[competitor]["bib_num"])
            firstName = competitors[competitor]["first_name"]
            lastName = competitors[competitor]["last_name"]

            # ternary used to prevent type('None') error
            performance = Time.to_string(competitors[competitor]["performance"]) \
                if competitors[competitor]["performance"] else "Non répertoriée"

            # writing into the save file    
            toWrite = bib + ";" + firstName + ";" + lastName + ";" + performance + "\n"
            savedFile.write(toWrite)


# FUNCTIONS CALLS

# setting up data
competitors = read_competitors("inscrits.csv")
performances = read_performances("performances.csv")
merge_performances(competitors, performances)

# show results by alphabetical order (uncomment the print_results() to make it works function):
sortedByLastName = Competitor.sort_competitors_by_last_name(competitors)
# print_results(sortedByLastName)

# show results by performance order (uncomment the print_results() to make it works function):
sortedByPerformance = Competitor.sort_competitors_by_performance(competitors)
# print_results(sortedByPerformance)

# save data into .txt file:
save_results(competitors)