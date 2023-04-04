# Pokedex by Hongpeng, Harry and Neil.
# Note: Hopefully the comments and docstring are sufficient! -\_(._.)_/-
# Happy using!

import pandas as pd
import csv
import fileinput

url = 'https://raw.githubusercontent.com/thatsmycroissant/Pokedex---ft-Neil-Hongpeng/main/Pokemon.csv'
df = pd.read_csv(url)

#adding a temp dataframe with the names of the pokemon entirely in lowercase

df_lower = df.copy()
df_lower['lower_case_names'] = [i.lower() for i in df_lower['Name']]

df = df.set_index(['No'])

# Useful Functions:
def check_df(df): # Check valid input
    '''
    This function checks the existence of a specific pokemon.
    '''
    if len(df) == 0:
        print("\n No such pokemon\n") # Error handling.
    else:
        dataframe = df
        print(dataframe.to_string())

def pokeTypeStat(df,n): # menu item 1
    '''
    Displays number, n, of pokemons with their type and statistics.
    '''
    dataframe = df[:n]
    print(dataframe.to_string()) # prints pokemons uptill index no. "n"

def pokeSpecType(df,type): # menu item 2
    '''
    Displays the first pokemon of a specific type.
    '''
    type = type[0].upper()+type[1:] # Capitalising first letter to suit the way the types were saved.
    df1 = df.loc[(df['Type 1'] == type) | (df['Type 2'] == type)] # Access a group of rows and columns by label(s) or a boolean array.
    check_df(df1[:1]) # Utilising check_df() function declared above.

def pokeSpecStat(df, stat): # menu item 3
    '''
    Display all pokemon of a specific base stat.
    '''
    df1 = df.loc[df['Total'] == stat] # Access a group of rows and columns by label(s) or a boolean array.
    check_df(df1) # Utilising check_df() function declared above.

def pokeMiniStat(df,sp_attck, sp_defense, speed): # menu item 4
    '''
    Display all pokemon with a minimum set of specific statistics.
    '''
    df1 = df.loc[(df['Sp. Atk'] >= sp_attck) & (df['Sp. Def'] >= sp_defense)] # Access a group of rows and columns by label(s) or a boolean array.
    df2 = df1.loc[df['Speed'] >= speed] # Access a group of rows and columns by label(s) or a boolean array.
    if len(df2) == 0:
        print("\n No pokemon with such powerful stats \n") # Error handling.
    else:
        print(df2.to_string()) # to string used to display all data without truncation

def pokeLegeType(df,type1,type2): # menu item 5
    '''
    Displays all legendary pokemon with specific type 1 and type 2.
    '''
    type1 = type1[0].upper()+type1[1:] # These two capitalise the first letter and concaternate to fit the way the data was stored.
    type2 = type2[0].upper()+type2[1:]
    df1 = df.loc[(df['Legendary'])] # These three simply access a group of rows and columns by label(s) or a boolean array.
    df2 = df1.loc[(df['Type 1'] == type1)]
    df3 = df2.loc[(df['Type 2'] == type2)]
    if len(df3) == 0:
        print("\n No legendary pokemon of that type\n") # Error handling.
    else:
        dataframe = df3
        print(dataframe.to_string())

def pokeBattle(df): # menu item 6
    '''
    Pick two pokemons to compare the higher overall stat to see which one wins.
    '''

    pokemon1 = input("Enter the name of the first Pokemon for this fight: ")
    pokemon1test = pokemon1.lower()
    # pokemon1test = pokemon1[0].upper() + pokemon1[1::]
    pokemon2 = input("Enter the name of the second Pokemon for this fight: ")
    # pokemon2test = pokemon2[0].upper() + pokemon2[1::]
    pokemon2test = pokemon2.lower()

    try:
        df1 = df.loc[df['lower_case_names'] == pokemon1test, 'Total'].values[0] # These two access a group of rows and columns by label(s) or a boolean array.
        df2 = df.loc[df['lower_case_names'] == pokemon2test, 'Total'].values[0]
        if (df1 > df2): # comparison to see winnner
            print("")
            print(f"{pokemon1test} wins")
        elif (df1 < df2):
            print("")
            print(f"{pokemon2test} wins")
        else:
            print("")
            print("Both Pokemon tied this battle")
        print(f"{pokemon1test}: {df1} vs {pokemon2test}: {df2}") # prints individual pokemon stat
    except:
        print("Invalid pokemon(s)!")

def docs():
    print("\nWhat would you like to do?\n1. Read the docs\n2. Get help")
    userToDo = input("Option: ")
    if userToDo == "1":
        print("\nDev Docs:\nAuthors: Hongpeng, Harry and Neil\nDate: 2/4/2023\n3. Changelog: V1(Current Version)")
    elif userToDo == "2":
        print("\nThis program is relatively simple to use and understand. It's foolproof, basically.")
    else:
        print("\nInvalid option!\n")



# Main Menu Function:
def menu(): # menu
    '''
    This docstring displays what this function does. This menu() function displays the main menu for the user, as well as runs the function.
    '''
    
    end = False # while loop to ensure code does not terminate without user approval

    while end != True:
        print("\nPokemon super search engine (not ripoff).") # menu options
        print("Enter your selection: (E.g. Key in '1' for option 1.)")
        print("1. Display Pokemon with their types and statistics: ")
        print("2. Display the first pokemon of a specific type: ")
        print("3. Display all the pokemon of a specific base stat: ")
        print("4. Display all the pokemon with a minimum set of special stats: ")
        print("5. Display all legendary pokemon with specific type 1 and type 2: ")
        print("6. Pick two pokemons to battle each other: ")
        print("7. Help / Dev Docs")
        print("0. Quit")

        inp = input("Select feature here: ") # user selects option
        try: # Error handling.
            inp = int(inp)
        except:
            print("\nNot implemented yet? Try something different...")
            print("\nDo you want to continue? (y/n)") # user option to continue
            userContinue = input("Option: ")
            if userContinue.lower() == "y":
                end = False
            elif userContinue.lower() == "n":
                print("\nAlright, quitting program...\n")
                end = True
            else:
                print("\nInvalid Choice!\n")
            continue
    
        if inp == 0:
            print("\nAre you sure? (y/n)")
            userContinue = input("Option: ")
            if userContinue.lower() == "y":
                print("\nAlright, quitting program...\n")
                end = True # Ending while loop.
            elif userContinue.lower() == "n":
                print("\nSure, going back...\n")
                end = False # Re-entering program loop
            else:
                print("\nInvalid choice!\n")
                end = False # Re-entering program loop

        elif inp == 1: # menu item 1
            num_pokemon = input("How many pokemon should I display: ")
            try: # Error handling.
                num_pokemon = int(num_pokemon)

                if num_pokemon > 800 or num_pokemon <1: # Checking range of user input, so not more than the data limit can be displayed.
                    print("\nInvalid input!\n")
                    continue
                else:
                    print("")
                    pokeTypeStat(df, num_pokemon)
                
                print("\nDo you want to continue? (y/n)")    # user option to continue
                userContinue = input("Option: ")
                if userContinue.lower() == "y":
                    end = False
                elif userContinue.lower() == "n":
                    print("\nAlright, quitting program...\n")
                    end = True
                else:
                    print("\nInvalid Choice!\n")
        
            except:
                print("\nInvalid input!\n")
                continue

        elif inp == 2: # menu item 2
            pokemon_type = input("Which type should the pokemon be: ")
        
            if not type(pokemon_type) == str: # error handling
                print("\nInvalid input!\n")
                continue
            else:
                print("")
                pokeSpecType(df, pokemon_type)

                print("\nDo you want to continue? (y/n)")    # user option to continue
                userContinue = input("Option: ")
                if userContinue.lower() == "y":
                    end = False
                elif userContinue.lower() == "n":
                    print("\nAlright, quitting program...\n")
                    end = True
                else:
                    print("\nInvalid Choice!\n")

        elif inp == 3: # menu item 3
            base_stat = input("Enter base stat of pokemon here: ")
            try: # error handling
                base_stat = int(base_stat)

                if type(base_stat) == int:
                    print("")
                    pokeSpecStat(df, base_stat)

                    print("\nDo you want to continue? (y/n)")    # user option to continue
                    userContinue = input("Option: ")
                    if userContinue.lower() == "y":
                        end = False
                    elif userContinue.lower() == "n":
                        print("\nAlright, quitting program...\n")
                        end = True
                    else:
                        print("\nInvalid Choice!\n")
                else:
                    print("\nInvalid input!\n")
            
            except:
                print("\nInvalid input!\n")
                continue

        elif inp == 4: # menu item 4
            sp_atk = input("Enter the min special attack: ")
            sp_defense = input("Enter the min special defense: ")
            speed = input("Enter the min. speed: ")

            try: # error handling
                sp_atk = int(sp_atk)
                sp_defense = int(sp_defense)
                speed = int(speed)

                if type(sp_atk) == int:
                    print("")
                    pokeMiniStat(df, sp_atk, sp_defense, speed)

                    print("\nDo you want to continue? (y/n)")    # user option to continue
                    userContinue = input("Option: ")
                    if userContinue.lower() == "y":
                        end = False
                    elif userContinue.lower() == "n":
                        print("\nAlright, quitting program...\n")
                        end = True
                    else:
                        print("\nInvalid Choice!\n")
                else:
                    print("\nInvalid input!\n")

            except:
                print("\nInvalid input!\n")

        elif inp == 5: # menu item 5
            pokemon_type_1 = input("What should the first pokemon type be: ")
            pokemon_type_2 = input("What should the second pokemon type be: ")

            try:
                print("")
                pokeLegeType(df,pokemon_type_1,pokemon_type_2)
            except:
                print("\nInvalid pokemon!\n")

            print("\nDo you want to continue? (y/n)")    # user option to continue
            userContinue = input("Option: ")
            if userContinue.lower() == "y":
                end = False
            elif userContinue.lower() == "n":
                print("\nAlright, quitting program...\n")
                end = True
            else:
                print("\nInvalid Choice!\n")
    
        elif inp == 6: # menu item 6
            pokeBattle(df_lower) # utilisation of battle function

            print("\nDo you want to continue? (y/n)")    # user option to continue
            userContinue = input("Option: ")
            if userContinue.lower() == "y":
                end = False
            elif userContinue.lower() == "n":
                print("\nAlright, quitting program...\n")
                end = True
            else:
                print("\nInvalid Choice!\n")
        
        elif inp == 7:
            docs()
            print("\nDo you want to continue? (y/n)") # user option to continue
            userContinue = input("Option: ")
            if userContinue.lower() == "y":
                end = False
            elif userContinue.lower() == "n":
                print("\nAlright, quitting program...\n")
                end = True
            else:
                print("\nInvalid Choice!\n")
                continue

        else:
            print("\nNot implemented yet? Try something else...")

            print("\nDo you want to continue? (y/n)") # user option to continue
            userContinue = input("Option: ")
            if userContinue.lower() == "y":
                end = False
            elif userContinue.lower() == "n":
                print("\nAlright, quitting program...\n")
                end = True
            else:
                print("\nInvalid option!\n")



# Execution of code:
menu()