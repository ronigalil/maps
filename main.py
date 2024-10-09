import pygame

import Screen

houses_list = []


def add_house(address, space_available, text):
    house = {'address': address, 'space_available': space_available, 'text': text}
    houses_list.append(house)
def city_soldier(soldier_requirements, houses_list):
    for house in range(0, len(houses_list)):
        houses_available = []
        if houses_list[house]['city'] == soldier_requirements['city']:
            if space_available(houses_list[house], soldier_requirements):
                houses_available.append(houses_list[house])


def space_available(house, soldier_requirements):
    if house['space'] >= soldier_requirements['space']:
        return house

pygame.init()
Screen.initialize_screen()


print("hello")
print("hi")
print("shalom")
