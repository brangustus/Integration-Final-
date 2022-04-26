""""Anime Recommendation Generator"""
__author__ = "Brandon Johnson"

# importing zone
import time


# import math
# import random


# Calculator for all functions using any 2 given numbers (sprint 1)
def mini_calculator():
    """calculation function for the requirements"""
    random_num1 = float(input("Any integer: "))
    random_num2 = float(input("Any integer: "))
    # boolean
    print(random_num1 == random_num2)
    print(random_num2 != random_num2)
    print(not (random_num2 != random_num2))
    if 2 < random_num1 < 4:
        print("I like this number")
    if random_num2 < 0 or random_num2 < 100:
        print("cool number")
    # calculator
    print("Exponential: ", format(random_num1 ** random_num2, ".2f"))
    print("Multiplication: ", format(random_num1 * random_num2, ".2f"))
    print("Division: ", format(random_num1 / random_num2, ".2f"))
    print("Modulus", format(random_num1 % random_num2, ".2f"))
    print("Division(no remainder): ", format(random_num1 // random_num2,
                                             ".2f"))
    print("Addition: ", format(random_num1 + random_num2, ".2f"))
    print("Subtraction: ", format(random_num1 - random_num2, ".2f"))


mini_calculator()

time.sleep(2)


def str_concatinator():
    """this concatenates 2 strings"""
    random_str1 = input("\nenter anything here: ")
    random_str2 = input("enter anything here: ")
    # prints the first input 10 times
    print(random_str1 * 10)
    # prints the first input next to the second (concatenates the strings)

    print(random_str1 + random_str2)


str_concatinator()

time.sleep(5)


# categories: Action,Comedy,Horror,Sports,Drama
def anime_generator():
    """main program assigning an anime based on user preferences"""
    category_loop_counter = 0
    while category_loop_counter == 0:
        category_list = ["action", "comedy", "horror", "sports", "dramas"]
        print("\nAction: 0\nComedy: 1\nHorror: 2\nSports: 3\nDramas: 4")
        fav_category = int(
            input("\nEnter the number of your favorite category here: "))
        if fav_category <= 4:
            # picking a category
            try:
                if category_list[fav_category] == "action":
                    print("\nYour favorite Category is Action.")
                    category_loop_counter += 1
                elif category_list[fav_category] == "comedy":
                    print("\nYour favorite Category is Comedy.")
                    category_loop_counter += 1
                elif category_list[fav_category] == "horror":
                    print("\nYour favorite Category is Horror.")
                    category_loop_counter += 1
                elif category_list[fav_category] == "sports":
                    print("\nYour favorite Category is Sports.")
                    category_loop_counter += 1
                elif category_list[fav_category] == "dramas":
                    print("\nYour favorite Category is Dramas.")
                    category_loop_counter += 1
                else:
                    print("That's not a valid category.")
            except:
                print("That's not a valid category.")
        else:
            print("That's not a valid category.")

        time.sleep(2)

    anime_loop_counter = 0
    while anime_loop_counter == 0:
        # picking an anime
        if fav_category == 0:
            print(
                "1: Fighting Giants\n2: Sword Fighting\n3: Mechas and Drills"
                "\n4: Psychic Battles"
                "\n5: Realistic super powers with severe drawbacks")
            action_anime = int(input("Enter only one (1,2,3,4,5): "))
            if action_anime == 1:
                print("I recommend: Attack on titan")
                anime_loop_counter += 1
            elif action_anime == 2:
                print("I recommend: Bleach")
                anime_loop_counter += 1
            elif action_anime == 3:
                print("I recommend: Guran Lagan")
                anime_loop_counter += 1
            elif action_anime == 4:
                print("I recommend: Mob Psycho 100")
                anime_loop_counter += 1
            elif action_anime == 5:
                print("I recommend: Darker than black")
                anime_loop_counter += 1
            else:
                print("that is not a valid input")

        if fav_category == 1:
            print(
                "1: Funny english dub about ghosts\n2: Comedy about "
                "schoolgirls\n3: Funny anime about a samurai "
                "\n4: Hilarious adventurers guild featuring a traveler, "
                "a goddess, and a masochist "
                "\n5: Comedy about college frats and the a diving club ("
                "HIGHLY RECOMMEND)")
            comedy_anime = int(input("Enter only one (1,2,3,4,5): "))
            if comedy_anime == 1:
                print("I recommend: Ghost Stories (english dub)")
                anime_loop_counter += 1
            elif comedy_anime == 2:
                print("I recommend: Azumanga Dai-oh")
                anime_loop_counter += 1
            elif comedy_anime == 3:
                print("I recommend: Gintama")
                anime_loop_counter += 1
            elif comedy_anime == 4:
                print("I recommend: Konosuba")
                anime_loop_counter += 1
            elif comedy_anime == 5:
                print("I recommend: Grand Blue")
                anime_loop_counter += 1
            else:
                print("that is not a valid input")

        if fav_category == 2:
            print(
                "1: Very gory story about a cursed high school\n2: Very "
                "gruesome anime about demons and feasting on humans "
                "\n3: Anime about demons taking over a high school murdering "
                "highschoolers "
                "\n4: An immortal vampire fighting Nazis, zombies, "
                "and priests in no particular order "
                "\n5: Highschool whose arm was taken over by an alien "
                "parasyte inhabiting who has made the "
                "decision to kill the other alien intruders(HIGHLY RECOMMEND)")
            horror_anime = int(input("Enter only one (1,2,3,4,5): "))
            if horror_anime == 1:
                print("I recommend: Another")
                anime_loop_counter += 1
            elif horror_anime == 2:
                print("I recommend: Blood-C")
                anime_loop_counter += 1
            elif horror_anime == 3:
                print("I recommend: Corpse Party")
                anime_loop_counter += 1
            elif horror_anime == 4:
                print("I recommend: Hellsing")
                anime_loop_counter += 1
            elif horror_anime == 5:
                print("I recommend: Parasyte the Maxim")
                anime_loop_counter += 1
            else:
                print("that is not a valid input")

        if fav_category == 3:
            print("1: baseball\n2: Boxing\n3: Volleyball"
                  "\n4: Martial arts and muscles"
                  "\n5: Basketball (HIGHLY RECOMMEND)")
            sports_anime = int(input("Enter only one (1,2,3,4,5): "))
            if sports_anime == 1:
                print("I recommend: Ace of Diamond")
                anime_loop_counter += 1
            elif sports_anime == 2:
                print("I recommend: Hajime no Ippo")
                anime_loop_counter += 1
            elif sports_anime == 3:
                print("I recommend: Haikyu!!")
                anime_loop_counter += 1
            elif sports_anime == 4:
                print("I recommend: Baki")
                anime_loop_counter += 1
            elif sports_anime == 5:
                print("I recommend: Kuroko's Basketball")
                anime_loop_counter += 1
            else:
                print("that is not a valid input")

        if fav_category == 4:
            print(
                "1: love story between two highschoolers\n2: Story about a "
                "split group of highschoolers reunited by "
                "the ghost of their late friend\n3: a film about 2 close "
                "friends gradually growing apart and the time they lost "
                "\n4: a highschool in the afterlife (limbo) where teens who "
                "experienced trauma work to get over it before they can pass "
                "on to heaven "
                "\n5: Story about a trauma ridden pianist and an ill "
                "violinist who with the violinist's help, works to overcome "
                "his trauma and play for her "
                " and the blossoming love between them (HIGHLY RECOMMEND)")
            drama_anime = int(input("Enter only one (1,2,3,4,5): "))
            if drama_anime == 1:
                print("I recommend: Clannad")
                anime_loop_counter += 1
            elif drama_anime == 2:
                print("I recommend: Ano Hara")
                anime_loop_counter += 1
            elif drama_anime == 3:
                print("I recommend: 5 centimeters per second")
                anime_loop_counter += 1
            elif drama_anime == 4:
                print("I recommend: Angel Beats")
                anime_loop_counter += 1
            elif drama_anime == 5:
                print("I recommend: Your lie in April")
                anime_loop_counter += 1
            else:
                print("that is not a valid input")

            time.sleep(5)


def menu():
    """menu for all functions within this program"""
    continue_program = True
    while continue_program:
        print("\nwould you like to generate an anime category recommendation?",
              "\nenter 1 for yes", "\nenter 0 for no", "\n1 or 0: ")
        user_continue = int(input("continue?: "))
        if user_continue == 1:
            anime_generator()
        elif user_continue == 0:
            print("thank you for using my program :)")
            continue_program = False
        else:
            print("try a valid input, 1 or 0")


menu()
