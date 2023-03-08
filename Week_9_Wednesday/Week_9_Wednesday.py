
# Animal guessing game

#----------------------------------------------------------------Classes----------------------------------------------------------------

class Animal: # Class for animals
    
    mName = ""
    m_Questions = list()

    def __init__(self, sName):
        self.mName = sName

    def AddNewQuestion(self, sQuestion): # Function for adding new questions

        self.m_Questions.append(sQuestion)

#----------------------------------------------------------------Classes----------------------------------------------------------------

#----------------------------------------------------------------Functions----------------------------------------------------------------

def ProgramStarter(s_GuessedAnimals):

    print("\nPlease think of an animal....")

    input("When you are ready, please press enter to begin.......\n")

    sAnimalName = input("\nPlease enter the name of your first animal: \n")

    s_GuessedAnimals.append(Animal(sAnimalName))

    Animal.AddNewQuestion("Please enter a question to which the answer could be for a " + s_GuessedAnimals[0].mName + ": \n")

    return s_GuessedAnimals

def MakeAGuess(s_GuessedAnimals):

    return s_GuessedAnimals

#----------------------------------------------------------------Functions----------------------------------------------------------------

#----------------------------------------------------------------Main Function----------------------------------------------------------------
def Main(): # Function for the main body of code

    bContinue = True
    s_GuessedAnimals = list()

    while bContinue == True:

        print("-------------------Animal Guessing Game-------------------")

        if len(s_GuessedAnimals) == 0:
            s_GuessedAnimals = ProgramStarter(s_GuessedAnimals)

        else:
            MakeAGuess(s_GuessedAnimals)

#----------------------------------------------------------------Main Function----------------------------------------------------------------

#-------------------------------------------------------------Code Starts Running-------------------------------------------------------------

Main() # Run the main body of code