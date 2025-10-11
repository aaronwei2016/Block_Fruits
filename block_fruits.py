import pygame
import random
import json
from datetime import datetime
pygame.init()
shop_time = pygame.time.get_ticks()
start_time = pygame.time.get_ticks()
start_atk = pygame.time.get_ticks()
enemy_hit = pygame.time.get_ticks()
width = 1200
height = 800 
center_x = width / 2
center_y = height / 2
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Block Fruits")
enemies = pygame.sprite.Group()
pi = pygame.image.load("player.png")
x, y = pi.get_size()
pic = pygame.transform.scale(pi, (x - 20, y - 20))
current_island = None
blox_coins = 0
items = [
    {
        "name": "COMBAT",
        "position": 90
    }
]



        


def show_controls():
    controls = [
        "CONTROLS:",
        "Attack:ENTER",
        "Attack Mode:Left-Click",
        "Special Attack1:Z",
        "Special Attack2:X",
        "Interact With NPC:E",
        "Move:W/A/S/D",
        "Controls Page:C",
        "P:Updates",
        "i:Shop"
    ]
    y = 150
    for control in controls:
        label = pygame.font.Font(None, 35).render(control, True, (255, 255, 255))
        screen.blit(label, (center_x - 190, y))
        y += 50




         
chatting = False
def ability_teacher():
    global chatting, page
    for island in islands:
        if island.enemy_name == "Monkey":
            dealer = {
                "image": pygame.image.load("NPCS/ability_teacher.png"),
                "rect": pygame.Rect(island.rect.x + 190, island.rect.y + 200, 242, 346)
            }
            screen.blit(dealer["image"], dealer["rect"])
            screen.blit(pygame.font.Font(None, 30).render("Ability Teacher", True, (255, 255, 255)), (dealer["rect"].x + 30, dealer["rect"].y + 150))
            if pygame.Rect(dealer["rect"].x + 30, dealer["rect"].y + 162, 142, 186).colliderect(player["rect"]):
                screen.blit(pygame.font.Font(None, 30).render("[E]Talk To Teacher", True, (255, 255, 255)), (dealer["rect"].x, dealer["rect"].y + 200))
                key = pygame.key.get_pressed()
                if key[pygame.K_e]:
                    chatting = True
                if chatting:
                    chatting = True
                    page = "abilitys"


def rubber_z():
    global direction_aim, direction
    if player["current_fruit"]:
        for _ in range(player["current_fruit"]["range"]):
            fruit = player["current_fruit"]
            fruit_x = center_x - pic.get_width() / 2
            fruit_y = center_y - pic.get_height() / 2
            if direction == "left":
                if fruit["type"] != "BUDDHA" and fruit["type"] != "COMBAT":
                    special_atk = {
                        "x": fruit_x,
                        "direction": "left",
                        "y": fruit_y,
                        "image": player["current_fruit"]["left_atk"],
                        "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                        "stamina": 1
                    }
                elif fruit["type"] == "BUDDHA":
                    special_atk = {
                        "x": fruit_x,
                        "direction": "left",
                        "y": fruit_y,
                        "image": player["current_fruit"]["special_image"],
                        "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                        "stamina": 1
                    }
                else:
                    special_atk = {
                        "x": fruit_x,
                        "direction": "left",
                        "y": fruit_y,
                        "image": player["current_fruit"]["special_image2"],
                        "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                        "stamina": 1
                    }
                special_atks.append(special_atk)
            elif direction == "right":
                if fruit["type"] != "BUDDHA" and fruit["type"] != "COMBAT":
                    special_atk = {
                        "x": fruit_x,
                        "direction": "right",
                        "y": fruit_y,
                        "image": player["current_fruit"]["right_atk"],
                        "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                        "stamina": 1
                    }
                elif fruit["type"] == "BUDDHA":
                    special_atk = {
                        "x": fruit_x,
                        "direction": "right",
                        "y": fruit_y,
                        "image": player["current_fruit"]["special_image"],
                        "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                        "stamina": 1
                    }
                else:
                    special_atk = {
                        "x": fruit_x,
                        "direction": "right",
                        "y": fruit_y,
                        "image": player["current_fruit"]["special_image"],
                        "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                        "stamina": 1
                    }
                special_atks.append(special_atk)
            elif direction == "up":
                if fruit["type"] != "BUDDHA" and fruit["type"] != "COMBAT":
                    special_atk = {
                        "x": fruit_x,
                        "direction": "up",
                        "y": fruit_y,
                        "image": player["current_fruit"]["up_atk"],
                        "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                        "stamina": 1
                    }
                elif fruit["type"] == "BUDDHA":
                    special_atk = {
                        "x": fruit_x,
                        "direction": "up",
                        "y": fruit_y,
                        "image": player["current_fruit"]["special_image"],
                        "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                        "stamina": 1
                    }
                else:
                    special_atk = {
                        "x": fruit_x,
                        "direction": "up",
                        "y": fruit_y,
                        "image": player["current_fruit"]["special_image"],
                        "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                        "stamina": 1
                    }
                special_atks.append(special_atk)
            elif direction == "down":
                if fruit["type"] != "BUDDHA" and fruit["type"] != "COMBAT":
                    special_atk = {
                        "x": fruit_x,
                        "direction": "down",
                        "y": fruit_y,
                        "image": player["current_fruit"]["down_atk"],
                        "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                        "stamina": 1
                    }
                elif fruit["type"] == "BUDDHA":
                    special_atk = {
                        "x": fruit_x,
                        "direction": "down",
                        "y": fruit_y,
                        "image": player["current_fruit"]["special_image"],
                        "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                        "stamina": 1
                    }
                else:
                    special_atk = {
                        "x": fruit_x,
                        "direction": "down",
                        "y": fruit_y,
                        "image": player["current_fruit"]["special_image"],
                        "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                        "stamina": 1
                    }
                special_atks.append(special_atk)
   


def ultra_z():
    if player["current_fruit"]:
        fruit = player["current_fruit"]
        fruit_x = center_x - pic.get_width() / 2
        fruit_y = center_y - pic.get_height() / 2
        if fruit["type"] != "BUDDHA":
            special_atk = {
                "x": fruit_x,
                "direction": "left",
                "y": fruit_y,
                "image": player["current_fruit"]["left_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        else:
            special_atk = {
                "x": fruit_x,
                "direction": "left",
                "y": fruit_y,
                "image": player["current_fruit"]["special_image"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        if fruit["type"] != "BUDDHA":
            special_atk = {
                "x": fruit_x,
                "direction": "right",
                "y": fruit_y,
                "image": player["current_fruit"]["right_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        else:
            special_atk = {
                "x": fruit_x,
                "direction": "right",
                "y": fruit_y,
                "image": player["current_fruit"]["special_image"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        if fruit["type"] != "BUDDHA":
            special_atk = {
                "x": fruit_x,
                "direction": "up",
                "y": fruit_y,
                "image": player["current_fruit"]["up_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        else:
            special_atk = {
                "x": fruit_x,
                "direction": "up",
                "y": fruit_y,
                "image": player["current_fruit"]["special_image"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        if fruit["type"] != "BUDDHA":
            special_atk = {
                "x": fruit_x,
                "direction": "down",
                "y": fruit_y,
                "image": player["current_fruit"]["down_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        else:
            special_atk = {
                "x": fruit_x,
                "direction": "down",
                "y": fruit_y,
                "image": player["current_fruit"]["special_image"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        if fruit["type"] != "BUDDHA":
            special_atk = {
                "x": fruit_x,
                "direction": "up and left",
                "y": fruit_y,
                "image": player["current_fruit"]["left_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        else:
            special_atk = {
                "x": fruit_x,
                "direction": "up and left",
                "y": fruit_y,
                "image": player["current_fruit"]["special_image"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        if fruit["type"] != "BUDDHA":
            special_atk = {
                "x": fruit_x,
                "direction": "down and right",
                "y": fruit_y,
                "image": player["current_fruit"]["right_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        else:
            special_atk = {
                "x": fruit_x,
                "direction": "down and right",
                "y": fruit_y,
                "image": player["current_fruit"]["special_image"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        if fruit["type"] != "BUDDHA":
            special_atk = {
                "x": fruit_x,
                "direction": "down and left",
                "y": fruit_y,
                "image": player["current_fruit"]["down_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        else:
            special_atk = {
                "x": fruit_x,
                "direction": "down and left",
                "y": fruit_y,
                "image": player["current_fruit"]["special_image"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        if fruit["type"] != "BUDDHA":
            special_atk = {
                "x": fruit_x,
                "direction": "up and right",
                "y": fruit_y,
                "image": player["current_fruit"]["right_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        else:
            special_atk = {
                "x": fruit_x,
                "direction": "up and right",
                "y": fruit_y,
                "image": player["current_fruit"]["special_image"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)



def mega_z():
    if player["current_fruit"]:
        if direction == "left":
            atk = {
                "x": 0,
                "y": 0,
                "direction": "up",
                "image": player["current_fruit"]["up_atk"],
                "rect": pygame.Rect(center_x - player["image"].get_width() + 50, height - 100, 90, 90),
                "stamina": 5
            }
            special_atks.append(atk)
            atk = {
                "x": 0,
                "y": 0,
                "direction": "down",
                "image": player["current_fruit"]["up_atk"],
                "rect": pygame.Rect(center_x - player["image"].get_width() + 50, 100, 90, 90),
                "stamina": 5
            }
            special_atks.append(atk)
        if direction == "right":
            atk = {
                "x": 0,
                "y": 0,
                "direction": "up",
                "image": player["current_fruit"]["up_atk"],
                "rect": pygame.Rect(center_x + player["image"].get_width() / 2 + 50, height - 100, 90, 90),
                "stamina": 5
            }
            special_atks.append(atk)
            atk = {
                "x": 0,
                "y": 0,
                "direction": "down",
                "image": player["current_fruit"]["up_atk"],
                "rect": pygame.Rect(center_x + player["image"].get_width() / 2 + 50, 100, 90, 90),
                "stamina": 5
            }
            special_atks.append(atk)
        




def super_z():
    if player["current_fruit"]:
        new_attack = {
            "x": center_x - player["image"].get_width() / 2 - 40,
            "y": 0,
            "direction": "down",
            "stamina": 2,
            "image": player["current_fruit"]["down_atk"],
            "rect": pygame.Rect(center_x - player["image"].get_width() - 40, 0, 90, 90)
        }
        special_atks.append(new_attack)
        new_attack = {
            "x": center_x - player["image"].get_width() / 2 - 140,
            "y": 0,
            "direction": "down",
            "stamina": 2,
            "image": player["current_fruit"]["down_atk"],
            "rect": pygame.Rect(center_x - player["image"].get_width() - 140, 0, 90, 90)
        }
        special_atks.append(new_attack)
        new_attack = {
            "x": center_x - player["image"].get_width() / 2 - 240,
            "y": 0,
            "direction": "down",
            "stamina": 2,
            "image": player["current_fruit"]["down_atk"],
            "rect": pygame.Rect(center_x - player["image"].get_width() - 240, 0, 90, 90)
        }
        special_atks.append(new_attack)
        new_attack = {
            "x": center_x - player["image"].get_width() / 2 - 340,
            "y": 0,
            "direction": "down",
            "stamina": 2,
            "image": player["current_fruit"]["down_atk"],
            "rect": pygame.Rect(center_x - player["image"].get_width() - 340, 0, 90, 90)
        }
        special_atks.append(new_attack)
        new_attack = {
            "x": center_x - player["image"].get_width() / 2 + 280,
            "y": 0,
            "direction": "down",
            "stamina": 2,
            "image": player["current_fruit"]["down_atk"],
            "rect": pygame.Rect(center_x - player["image"].get_width() + 280, 0, 90, 90)
        }
        special_atks.append(new_attack)
        new_attack = {
            "x": center_x - player["image"].get_width() / 2 + 380,
            "y": 0,
            "direction": "down",
            "stamina": 2,
            "image": player["current_fruit"]["down_atk"],
            "rect": pygame.Rect(center_x - player["image"].get_width() + 380, 0, 90, 90)
        }
        special_atks.append(new_attack)
        new_attack = {
            "x": center_x - player["image"].get_width() / 2 + 480,
            "y": 0,
            "direction": "down",
            "stamina": 2,
            "image": player["current_fruit"]["down_atk"],
            "rect": pygame.Rect(center_x - player["image"].get_width() + 480, 0, 90, 90)
        }
        special_atks.append(new_attack)
        new_attack = {
            "x": center_x - player["image"].get_width() / 2 + 580,
            "y": 0,
            "direction": "down",
            "stamina": 2,
            "image": player["current_fruit"]["down_atk"],
            "rect": pygame.Rect(center_x - player["image"].get_width() + 580, 0, 90, 90)
        }

        special_atks.append(new_attack)
def bombing():
    super_z()


def dark_slash():
    global direction_aim, direction, clicked, attacking
    if player["current_fruit"]:
        clicked = True
        attacking = True
        start_atk = pygame.time.get_ticks()
        direction_aim = direction
        atk_elapsed = now - start_atk
        fruit = player["current_fruit"]
        if atk_elapsed <= 100:
            if player["current_fruit"]["type"] != "BOMB" and player["current_fruit"]["type"] != "PARTY" and player["current_fruit"]["type"] != "BUDDHA" and player["current_fruit"]["type"] != "THUNDER" and player["current_fruit"]["type"] != "MAGMA" and player["current_fruit"]["type"] != "PAIN V2" and player["current_fruit"]["type"] != "PAIN":
                if direction_aim == "up":
                    
                    if player["current_fruit"]["up_atk"] is not None:
                        attack_rect = pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height() / 2 - 40, 90, 90)
                        screen.blit(fruit["up_atk"], (center_x - pic.get_width() / 2, center_y - pic.get_height() / 2 - 40))
                    else:
                        attack_rect = pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height() / 2, pic.get_width(), pic.get_height())
                elif direction_aim == "down":
                    if player["current_fruit"]["down_atk"] is not None:
                        attack_rect = pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height() / 2 + 80, 90, 90)
                        screen.blit(fruit["down_atk"], (center_x - pic.get_width() / 2, center_y - pic.get_height() / 2 + 80))
                    else:
                        attack_rect = pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height(), pic.get_width(), pic.get_height())
                if direction_aim == "left":
                    if player["current_fruit"]["left_atk"] is not None:
                        attack_rect = pygame.Rect(center_x - pic.get_width() / 2 - 40, center_y - pic.get_height() / 2, 90, 90)
                        screen.blit(fruit["left_atk"], (center_x - pic.get_width() / 2 - 40, center_y - pic.get_height() / 2 + player["current_fruit"]["left_atk"].get_height() / 2))
                    else:
                        attack_rect = pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height() / 2, pic.get_width(), pic.get_height())
                elif direction_aim == "right":
                    if player["current_fruit"]["right_atk"] is not None:
                        attack_rect = pygame.Rect(center_x + pic.get_width(), center_y - pic.get_height() / 2, 90, 90)
                        screen.blit(fruit["right_atk"], (center_x - pic.get_width() / 2 + 120, center_y - pic.get_height() / 2 + player["current_fruit"]["left_atk"].get_height() / 2))
                    else:
                        attack_rect = pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height() / 2, pic.get_width(), pic.get_height())
           
                                                                                                                                
        if elapsed >= 101:
            attacking = False
            start_atk = pygame.time.get_ticks()
            attack_rect = None

direction_aim = None

def dash_z():
    global direction, direction_aim, clicked
    if player["current_fruit"]:
        for island in islands:
            if player["current_fruit"]["type"] != "DARK V2":
                player["speed"] = 400
            elif player["current_fruit"]["type"] == "BUDDHA":
                if not transformed:
                    player["speed"] = 600
                if player["rect"].get_width() >= 180 * 3:
                    player["speed"] = 1200
            else:
                player["speed"] = 700
            if page == "home":
                if direction == "up":
                    future_y = player["rect"].copy()
                    future_y.y -= 5
                    direction = "up"
                    for enemy in island.enemies:
                        enemy.rect.y += player["speed"]
                    island.rect.y += player["speed"]
                    player["y"] -= player["speed"]
                    if not driving_boat:
                        boat["rect"].y += player["speed"]
                    if player["current_fruit"]["type"] != "RUBBER" and player["current_fruit"]["type"]!= "DARK V2":
                        new_attack = {
                            "x": center_x - player["image"].get_width() / 2,
                            "y": 0,
                            "direction": "down",
                            "stamina": 2,
                            "image": player["current_fruit"]["down_atk"],
                            "rect": pygame.Rect(center_x - player["image"].get_width() / 2, center_y - player["image"].get_height() / 2, player["image"].get_width(), player["image"].get_height())
                        }

                        special_atks.append(new_attack)
                    else:
                        new_attack = {
                            "x": center_x - player["image"].get_width() / 2,
                            "y": 0,
                            "direction": "down",
                            "stamina": 2,
                            "image": None,
                            "rect": pygame.Rect(center_x - player["image"].get_width() / 2, center_y - player["image"].get_height() / 2, player["image"].get_width(), player["image"].get_height())
                        }

                        special_atks.append(new_attack)
                    
                        
                if direction == "down":
                    future_y = player["rect"].copy()
                    future_y.y += 5
                    direction = "down"
                    for enemy in island.enemies:
                        enemy.rect.y -= player["speed"]
                    island.rect.y -= player["speed"]
                    player["y"] += player["speed"]
                    if not driving_boat:
                        boat["rect"].y -= player["speed"]
                    if player["current_fruit"]["type"] != "RUBBER" and player["current_fruit"]["type"]!= "DARK V2":
                        new_attack = {
                            "x": center_x - player["image"].get_width() / 2,
                            "y": 0,
                            "direction": "up",
                            "stamina": 2,
                            "image": player["current_fruit"]["up_atk"],
                            "rect": pygame.Rect(center_x - player["image"].get_width() / 2, center_y - player["image"].get_height() / 2, player["image"].get_width(), player["image"].get_height())
                        }

                        special_atks.append(new_attack)
                    else:
                        new_attack = {
                            "x": center_x - player["image"].get_width() / 2,
                            "y": 0,
                            "direction": "down",
                            "stamina": 2,
                            "image": None,
                            "rect": pygame.Rect(center_x - player["image"].get_width() / 2, center_y - player["image"].get_height() / 2, player["image"].get_width(), player["image"].get_height())
                        }

                        special_atks.append(new_attack)
                if direction == "left":
                    future_y = player["rect"].copy()
                    future_y.x -= 5
                    direction = "left"
                    for enemy in island.enemies:
                        enemy.rect.x += player["speed"]
                    island.rect.x += player["speed"]
                    player["x"] -= player["speed"]
                    if not driving_boat:
                        boat["rect"].x += player["speed"]
                    if player["current_fruit"]["type"] != "RUBBER" and player["current_fruit"]["type"] != "DARK V2":
                        new_attack = {
                            "x": center_x - player["image"].get_width() / 2,
                            "y": 0,
                            "direction": "right",
                            "stamina": 2,
                            "image": player["current_fruit"]["right_atk"],
                            "rect": pygame.Rect(center_x - player["image"].get_width() / 2, center_y - player["image"].get_height() / 2, player["image"].get_width(), player["image"].get_height())
                        }

                        special_atks.append(new_attack)
                    else:
                        new_attack = {
                            "x": center_x - player["image"].get_width() / 2,
                            "y": 0,
                            "direction": "down",
                            "stamina": 2,
                            "image": None,
                            "rect": pygame.Rect(center_x - player["image"].get_width() / 2, center_y - player["image"].get_height() / 2, player["image"].get_width(), player["image"].get_height())
                        }

                        special_atks.append(new_attack)
                if direction == "right":
                    future_y = player["rect"].copy()
                    future_y.x += 5
                    direction = "right"
                    for enemy in island.enemies:
                        enemy.rect.x -= player["speed"]
                    island.rect.x -= player["speed"]
                    player["x"] += player["speed"]
                    if not driving_boat:
                        boat["rect"].x -= player["speed"]
                    if player["current_fruit"]["type"] != "RUBBER" and player["current_fruit"]["type"]!= "DARK V2":
                        new_attack = {
                            "x": center_x - player["image"].get_width() / 2,
                            "y": 0,
                            "direction": "left",
                            "stamina": 2,
                            "image": player["current_fruit"]["left_atk"],
                            "rect": pygame.Rect(center_x - player["image"].get_width() / 2, center_y - player["image"].get_height() / 2, player["image"].get_width(), player["image"].get_height())
                        }

                        special_atks.append(new_attack)
                    else:
                        new_attack = {
                            "x": center_x - player["image"].get_width() / 2,
                            "y": 0,
                            "direction": "down",
                            "stamina": 2,
                            "image": None,
                            "rect": pygame.Rect(center_x - player["image"].get_width() / 2, center_y - player["image"].get_height() / 2, player["image"].get_width(), player["image"].get_height())
                        }

                        special_atks.append(new_attack)
                if player["current_fruit"]["type"] == "RUBBER" or player["current_fruit"]["type"] == "DARK V2":
                    clicked = True
                    attacking = True
                    start_atk = pygame.time.get_ticks()
                    direction_aim = direction
                    if player["current_fruit"]:
                        fruit = player["current_fruit"]
                    dark_slash()
                    
                for atk in special_atks[:]:
                    if direction == "up":
                        atk["rect"].y += player["speed"] / 6
                    if direction == "down":
                        atk["rect"].y -= player["speed"] / 6
                    if direction == "left":
                        atk["rect"].x += player["speed"] / 6
                    if direction == "right":
                        atk["rect"].x -= player["speed"] / 6
                for bomb in bombs[:]:
                    if direction == "up":
                        bomb["rect"].y += player["speed"] / 6
                    if direction == "down":
                        bomb["rect"].y -= player["speed"] / 6
                    if direction == "right":
                        bomb["rect"].x += player["speed"] / 6
                    if direction == "left":
                        bomb["rect"].x -= player["speed"] / 6
                player["speed"] = 15



def godly_z():
    if player["current_fruit"]:
        for island in islands:
            for enemy in island.enemies:
                dark_slash()
                if enemy.rect.colliderect(player["rect"]):
                    if direction == "up":
                        enemy.rect.y -= 400
                    elif direction == "down":
                        enemy.rect.y += 400
                    if direction == "left":
                        enemy.rect.x -= 400
                    elif direction == "right":
                        enemy.rect.x += 400
                    enemy.health -= player["current_fruit"]["damage"]
        


wsws = pygame.image.load("fruits/attacks/bladeleft.png")
swords = [
    {
        "Name": "Dark Blade",
        "type": "DARK",
        "damage": 500,
        "special": rubber_z,
        "special_name": "Violent Toss",
        "special_nametwo": "Million Swords",
        "specialtwo": super_z,
        "left_atk": wsws,
        "right_atk": pygame.transform.flip(wsws, True, False),
        "up_atk": wsws,
        "buying_img": None,
        "image": wsws,
        "cool": 4,
        "range": 1,
        "awakend": False,
        "mas": 1,
        "down_atk": pygame.image.load("fruits/attacks/Dark_Blade.png")
    }
]


def buy_sword(fruit):
    if player["money"] >= sword["cost"]:
        new_fruit = {
                "image": fruit["buying_img"],
                "rect": fruit["img_rect"],
                "left_atk": fruit["left_atk"],
                "right_atk": fruit["right_atk"],
                "up_atk": fruit["up_atk"],
                "down_atk": fruit["down_atk"],
                "type": fruit["type"],
                "damage": fruit["damage"],
                "special": fruit["special"],
                "special_name": fruit["special_name"],
                "range": fruit["range"],
                "special_nametwo": fruit["special_nametwo"],
                "specialtwo": fruit["specialtwo"],
                "cool": fruit["cool"],
                "mas": 1,
                "awakend": False
        }
        player["block_fruits"].append(new_fruit)
            
player = {
    "health": 100,
    "image": pic.copy(),
    "bounty": 0,
    "lvl": 1,
    "max_health": 100,
    "stats_now": 0,
    "stats_need": 40,
    "energy": 100,
    "damage": 5,
    "block_fruits": [
        {
            "left_atk": None,
            "right_atk": None,
            "rect": pygame.Rect(0, 0, 0, 0),
            "up_atk": None,
            "down_atk": None,
            "type": "COMBAT",
            "damage": 9,
            "mas": 1,
            "special_name": "Quick Dash",
            "special": dash_z,
            "special_nametwo": "Sword Toss",
            "specialtwo": rubber_z,
            "range": 1,
            "cool": 2,
            "special_image": pygame.image.load("fruits/attacks/sword.png"),
            "special_image2": pygame.transform.flip(pygame.image.load("fruits/attacks/sword.png"), True, False),
            "awakend": False
        }
    ],
    "rect": pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height() / 2, pic.get_width(), pic.get_height()),
    "money": 100,
    "speed": 10,
    "current_fruit": None,
    "x": center_x - pic.get_width() / 2,
    "y": center_y - pic.get_height() / 2
}
player["current_fruit"] = player["block_fruits"][0]
attack_rect = None





font = pygame.font.Font(None, 36)
current_type = "COMBAT"
boat_owned = False
def buy(block_fruit):
    pygame.draw.rect(screen, (194, 178, 128), (0, 0, 300, 300))
    for fruit in block_fruit:
        if fruit["type"] == "BUDDHA":
            new_fruit = {
                "image": fruit["buying_img"],
                "rect": fruit["img_rect"],
                "left_atk": fruit["left_atk"],
                "right_atk": fruit["right_atk"],
                "up_atk": fruit["up_atk"],
                "down_atk": fruit["down_atk"],
                "type": fruit["type"],
                "damage": fruit["damage"],
                "special": fruit["special"],
                "special_name": fruit["special_name"],
                "special_image": fruit["special_image"],
                "range": fruit["range"],
                "special_nametwo": fruit["special_nametwo"],
                "specialtwo": fruit["specialtwo"],
                "cool": fruit["cool"],
                "mas": 1,
                "awakend": False
            }
        elif fruit["type"] == "PAIN V2":
            new_fruit = {
                "image": fruit["buying_img"],
                "rect": fruit["img_rect"],
                "left_atk": fruit["left_atk"],
                "right_atk": fruit["right_atk"],
                "up_atk": fruit["up_atk"],
                "down_atk": fruit["down_atk"],
                "type": fruit["type"],
                "damage": fruit["damage"],
                "special": fruit["special"],
                "special_name": fruit["special_name"],
                "normal": fruit["normal"],
                "range": fruit["range"],
                "special_nametwo": fruit["special_nametwo"],
                "specialtwo": fruit["specialtwo"],
                "cool": fruit["cool"],
                "mas": 1,
                "awakend": False
            }
        else:
            new_fruit = {
                "image": fruit["buying_img"],
                "rect": fruit["img_rect"],
                "left_atk": fruit["left_atk"],
                "right_atk": fruit["right_atk"],
                "up_atk": fruit["up_atk"],
                "down_atk": fruit["down_atk"],
                "type": fruit["type"],
                "damage": fruit["damage"],
                "special": fruit["special"],
                "special_name": fruit["special_name"],
                "range": fruit["range"],
                "special_nametwo": fruit["special_nametwo"],
                "specialtwo": fruit["specialtwo"],
                "cool": fruit["cool"],
                "mas": 1,
                "awakend": False
            }
        player["block_fruits"].append(new_fruit)
special_atks = []
direction = None

page = "home"

xs = 90
def add(item):
   global xs
   if len(items) < 9:
       item_name = {
           "name": item,
           "position": items[-1]["position"] + 105
        }
       items.append(item_name)
       
   else:
        return

super_small = pygame.font.Font(None, 25)
def draw_items():
    for item in items:
        label = super_small.render(f"{item['name']}", True, (255, 255, 255))
        pygame.draw.rect(screen, (150, 150, 150), (item["position"] - 20, height - 160, 85, 70))
        screen.blit(label, (item["position"] - 15, height - 135))
        

hit = False
def show_fruits():
    pygame.draw.rect(screen, (225, 225, 0), (center_x - 250, center_y - 350, 500, 700), border_radius=15)
    for island in islands:
        if current_island:
            for fruit in current_island.block_fruits:
                screen.blit(fruit["image"], fruit["rect"])
                label = font.render(f"{fruit['Name']}, ${fruit['cost']}", True, (0, 0, 0))
                screen.blit(label, (fruit["rect"].x, fruit["rect"].y + fruit["image"].get_height() + 19))

ww = pygame.image.load("fruits/attacks/Parrot_Eagle.png")
w2 = pygame.image.load("fruits/attacks/Lightning.png")
class Enemy(pygame.sprite.Sprite):
    def __init__(self, xp, name, hp, speed, damage, lvl, image, x, y, r, reward):
        super().__init__()
        self.image = pygame.image.load(f"enemies/{image}")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.damage =  damage
        self.level = lvl
        self.health = hp
        self.range = r
        self.speed = speed
        self.name = name
        self.xp_given = xp
        self.reward = reward
        self.charge = 0
        self.attacks = []
        
    def update(self):
        global enemy_attacked, direction_aim, hit, hit_timey, enemy_hit
        hit_timey = now - enemy_hit
        if self.charge <= 50:
            if self.rect.x < player["rect"].x and self.rect.x > player["rect"].x - self.range:
                self.rect.x += self.speed

            if self.rect.y < player["rect"].y and self.rect.y > player["rect"].y - self.range:
                self.rect.y += self.speed
            if self.rect.x > player["rect"].x and self.rect.x < player["rect"].x + self.range:
                self.rect.x -= self.speed
            if self.rect.y > player["rect"].y  and self.rect.y < player["rect"].y + self.range:
                self.rect.y -= self.speed
        if self.name == "Tryant Of The Skies" and self.charge <= 0 and pygame.Rect(self.rect.x - self.image.get_width(), self.rect.y - self.image.get_height(), self.image.get_width() * 2 + ww.get_width(), self.image.get_height() * 2 + ww.get_height()).colliderect(player["rect"]) and not enemy_attacked:
            player["health"] -= self.damage
            hit = True
            self.charge = 100
        if self.charge > 0:
            self.charge -= 2
        if self.charge <= 0 and self.name != "Tryant Of The Skies" and self.rect.colliderect(player["rect"]) and not hit:
            player["health"] -= self.damage
            hit = True
        if self.charge <= 0 and self.name == "Tryant Of The Skies":
            screen.blit(pygame.transform.flip(ww, True, False), (self.rect.x - self.image.get_width() / 2, self.rect.y))
            screen.blit(ww, (self.rect.x + self.image.get_width(), self.rect.y))
        if attack_rect and self.rect.colliderect(attack_rect):
            self.health -= player["damage"]
            if direction_aim == "up":
                self.rect.y -= 20
            elif direction_aim == "down":
                self.rect.y += 20
            elif direction_aim == "left":
                self.rect.x -= 20
            else:
                self.rect.x += 20
            enemy_attacked = True
        if (
            pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height() / 2, pic.get_width(), pic.get_height())
            ).colliderect(self.rect) and attacking:
            self.health -= player["damage"]
            if direction_aim == "up":
                self.rect.y -= 20
            elif direction_aim == "down":
                self.rect.y += 20
            elif direction_aim == "left":
                self.rect.x -= 20
            else:
                self.rect.x += 20
            enemy_attacked = True
            
        label = small.render(f"lvl{self.level}", True, (255, 255, 255))
        screen.blit(label, (self.rect.x - 2, self.rect.y - 20))

        
    
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y




        

filename = "blox_fruits.json"

colors = [
    (80, 200, 120),
    (20, 140, 60),
    (173, 216, 230),
    (79, 195, 247),
    (255, 36, 0),
    (255, 247, 179),
    (186, 85, 211)
]


messages = [
    {
        "name": "You Are A Pirate At Starter Pirate Island",
        "color": (0, 255, 0),
        "y_pos": 50
    },
    {
        "name": "Press C To Open Controls Page.",
        "color": (0, 255, 0),
        "y_pos": 80
    },
    {
        "name": "Go To The Blox Fruit Dealer To Buy A Fruit.",
        "color": (255, 255, 0),
        "y_pos": 120
    },
    {
        "name": "BOMB EVENT IS HERE!",
        "color": (0, 0, 0),
        "y_pos": 150
    },
    {
        "name": "The Tryant Of The Skies...",
        "color": (0, 255, 0),
        "y_pos": 180
    },
    {
        "name": "Follow The Line To Go To Head To The Celestal Domain",
        "color": (255, 0, 0),
        "y_pos": 220
    }
]

def add_message(message_name, message_color, poss):
    if len(messages) < 5:
        new_message = {
            "name": message_name,
            "color": message_color,
            "y_pos": poss
        }
        messages.append(new_message)
    else:
        new_message = {
            "name": message_name,
            "color": message_color,
            "y_pos": poss
        }
        messages.append(new_message)
        for message in messages:
            message["y_pos"] -= 30

def display_messages():
    for message in messages:
        label = super_small.render(message["name"], True, message["color"])
        screen.blit(label, (25, message["y_pos"]))

filename = "blox_data.json"    
def save():
    data = {
        "money": player["money"],
        "lvl": player["lvl"],
        "stats_now": player["stats_now"],
        "stats_need": player["stats_need"]
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load():
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            player["money"] = data.get("money", 0)
            player["lvl"] = data.get("lvl", 1)
            player["stats_need"] = data.get("stats_need", 40)
            player["stats_now"] = data.get("stats_now", 0)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error: {e}")


background_x = 500
background_y = 350  
islands = pygame.sprite.Group()
class Island(pygame.sprite.Sprite):
     def __init__(self, enemy_xp, enemy_name, went, name, quest, radius, x, y, color, enemy_image, health, level, reward, fruits):
        super().__init__()
        self.name = name
        self.went = went
        self.radius = radius
        self.color = color
        self.quest = quest
        self.xp = enemy_xp
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        self.rect.x = x
        self.rect.y = y
        self.enemies = pygame.sprite.Group()
        self.enemy_image = enemy_image
        self.enemy_health = health
        self.level = level
        self.bonus = reward
        self.block_fruits = fruits
        self.enemy_name = enemy_name
        pygame.draw.circle(screen, self.color, (self.rect.x, self.rect.y), self.radius)
     def spawn_enemys(self, count):    
        for i in range(count):
            if self.name != "Celestal Domain":
                enemy = Enemy(
                    name=self.enemy_name,
                    hp=self.enemy_health,
                    speed=random.randint(1, 2),
                    damage=3,
                    lvl=self.level,
                    image=self.enemy_image,
                    x=random.randint(self.rect.x + 100, self.rect.x + 320),
                    y=random.randint(self.rect.y - 100, self.rect.y + 100),
                    r=209,
                    xp=self.xp,
                    reward=self.bonus
                )
            else:
                enemy = Enemy(
                    name=self.enemy_name,
                    hp=self.enemy_health,
                    speed=player["speed"] - 1,
                    damage=90,
                    lvl=self.level,
                    image=self.enemy_image,
                    x=random.randint(self.rect.x + 100, self.rect.x + 320),
                    y=random.randint(self.rect.y - 100, self.rect.y + 100),
                    r=609,
                    xp=self.xp,
                    reward=self.bonus
                )
            self.enemies.add(enemy)

        

island_positions = [
    pygame.Rect(0, 0, 10, 10),
    pygame.Rect(0, -2000, 10, 10),
    pygame.Rect(-2400, -2300, 10, 10),
    pygame.Rect(-4300, -2300, 10, 10),
    pygame.Rect(-4300, -4300, 10, 10),
    pygame.Rect(-4300, -5900, 10, 10),
    pygame.Rect(-2900, 10, 10, 10)
]



lvls = [
    5,
    14,
    25,
    50,
    200,
    300,
    999
]


hps = [
    100,
    300,
    994,
    2750,
    7000,
    10000,
    20000
]
    


enemys = [
    "bandit.png",
    "monkey.png",
    "yeti.png",
    "swan.png",
    "hell_guard.png",
    "angel.png",
    "RIP.png",
]

rewards = [
    60,
    140,
    200,
    400,
    1200,
    2000,
    2000
]

names = [
    "Bandit",
    "Monkey",
    "Yeti",
    "Swan",
    "Hell's Guard",
    "Heaven's Guard",
    "Tryant Of The Skies"
]
index = 0

givens = [
    40,
    167,
    340,
    694,
    1000,
    3000,
    12000
]


names2 = [
    "Pirate Starter Village",
    "Jungle",
    "Frozen Island",
    "Kitsune Island",
    "Hells Palace",
    "Heaven",
    "Celestal Domain"
]

names = [
    "Bandit",
    "Monkey",
    "Yeti",
    "Swan",
    "Hell's Guard",
    "Heaven's Guard",
    "Tryant Of The Skies"
]


quests = [
    {
        "name": "Bandits",
        "number": 5,
        "money": 400,
        "xp": 800,
        "now": 0
    },
    {
        "name": "Monkeys",
        "number": 6,
        "money": 800,
        "xp": 1200,
        "now": 0
    },
    {
        "name": "Yetis",
        "number": 12,
        "money": 2400,
        "xp": 1900,
        "now": 0
    },
    {
        "name": "Swans",
        "number": 15,
        "money": 5000,
        "xp": 4500,
        "now": 0
    },
    {
        "name": "Hell Guards",
        "number": 10,
        "money": 7500,
        "xp": 4500,
        "now": 0
    },
    {
        "name": "Heaven Guards",
        "number": 30,
        "money": 20000,
        "xp": 15000,
        "now": 0
    },
    {
        "name": "Tryant Of The Skies",
        "number": 1,
        "money": 10000,
        "xp": 20500,
        "now": 0
    }
]
quest_earned = False
current_quest = None
def draw_quest():
    global current_island, quest_earned, current_quest, questing
    if questing and current_quest:
        label = small.render(f"Defeat {current_quest['number']} {current_quest['name']}", True, (255, 255, 255))
        screen.blit(label, (100, center_y - 80))
        label2 = small.render(f"{current_quest['name']} ({current_quest['now']}/{current_quest['number']})", True, (255, 255, 255))
        screen.blit(label2, (100, center_y - 50))
        quest_earned = True

questing = False
clicking = False
def draw_quest_npc():
    global questing, current_quest, chatting, clicked
    for island in islands:
        quest_giver = {
            "image": pygame.image.load("NPCS/quest_dealer.png"),
            "rect": pygame.Rect(island.rect.x + 650, island.rect.y + 300, 150, 250)
        }
        screen.blit(quest_giver["image"], (quest_giver["rect"].x, quest_giver["rect"].y))
        label = pygame.font.Font(None, 25).render("Quest Giver", True, (255, 255, 255))
        screen.blit(label, (quest_giver["rect"].x + 70, quest_giver["rect"].y + 170))

        keys = pygame.key.get_pressed()
        if pygame.Rect(island.rect.x + 700, island.rect.y + 450, 150, 250).colliderect(player["rect"]):
            screen.blit(super_small.render("[E]Select A Quest", True, (255, 255, 255)), (quest_giver["rect"].x + 30, quest_giver["rect"].y + 240))
            if keys[pygame.K_e] and not questing:
                current_quest = current_island.quest.copy()
                clicked = True
                add_message("Quest Accepted!", (255, 255, 0), messages[-1]["y_pos"] + 30)
                questing = not questing
 
wispy = pygame.image.load("fruits/attacks/wisp.png")
pain = pygame.image.load("updates/thunderupdate.png")
updates = [
    {
        "image": pain,
        "y_pos": 60,
        "name": "PAIN VS THUNDER",
        "log": [
            "Cooming Soon...",
            "Cooming Soon...",
            "Cooming Soon..."
        ]
    }
]
def transform_z():
    global transformed, pic
    if player["current_fruit"]["type"] == "BUDDHA":
       if not transformed:
           player["image"] = pygame.transform.scale(player["image"], (player["image"].get_width() * 2, player["image"].get_height() * 2))
           player["block_fruits"][0]["damage"] = 500
           transformed = True
       else:
           pic = pygame.transform.scale(pic, (180, 180))
           player["image"] = pic
           transformed = False
           player["block_fruits"][0]["damage"] = 9

def chase_z():
    global direction_aim, direction
    if player["current_fruit"]:
        for _ in range(player["current_fruit"]["range"]):
            fruit = player["current_fruit"]
            fruit_x = center_x - pic.get_width() / 2
            fruit_y = center_y - pic.get_height() / 2
            special_atk = {
                "x": fruit_x,
                "direction": "all",
                "y": fruit_y,
                "image": player["current_fruit"]["left_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)




def gravity_z():
    if player["current_fruit"]:
        pos = pygame.mouse.get_pos()
        special_atk = {
            "x": 0,
            "direction": "down",
            "y": 0,
            "image": player["current_fruit"]["left_atk"],
            "rect": pygame.Rect(pos[0] - player["current_fruit"]["left_atk"].get_width() / 2, pos[1], 90, 90),
            "stamina": 1
        }
        
        special_atks.append(special_atk)


def warp_z():
    if player["current_fruit"]:
        pos = pygame.mouse.get_pos()
        directions = [
            "right",
            "left",
            "up",
            "down",
            "up and right",
            "up and left",
            "down and right",
            "down and left"
        ]
        for i in range(len(directions)):
            special_atk = {
                "x": 0,
                "direction": directions[i],
                "y": 0,
                "image": player["current_fruit"]["left_atk"],
                "rect": pygame.Rect(pos[0] - player["current_fruit"]["left_atk"].get_width() / 2, pos[1] - player["current_fruit"]["left_atk"].get_height() / 2, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
            






def god_z():
    if player["current_fruit"]:
        if direction == "left" or direction == "right":
            fruit = player["current_fruit"]
            fruit_x = center_x - pic.get_width() / 2
            fruit_y = center_y - pic.get_height() / 2
            special_atk = {
                "x": fruit_x,
                "direction": "all",
                "y": fruit_y,
                "image": player["current_fruit"]["left_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
            special_atk = {
                "x": fruit_x,
                "direction": "all",
                "y": fruit_y,
                "image": player["current_fruit"]["left_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y + player["image"].get_height(), 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
            special_atk = {
                "x": fruit_x,
                "direction": "all",
                "y": fruit_y,
                "image": player["current_fruit"]["left_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y - player["image"].get_height() / 2, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
        else:
            fruit = player["current_fruit"]
            fruit_x = center_x - pic.get_width() / 2
            fruit_y = center_y - pic.get_height() / 2
            special_atk = {
                "x": fruit_x,
                "direction": "all",
                "y": fruit_y,
                "image": player["current_fruit"]["left_atk"],
                "rect": pygame.Rect(fruit_x, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
            special_atk = {
                "x": fruit_x,
                "direction": "all",
                "y": fruit_y,
                "image": player["current_fruit"]["left_atk"],
                "rect": pygame.Rect(fruit_x - player["image"].get_width() / 2, fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)
            special_atk = {
                "x": fruit_x,
                "direction": "all",
                "y": fruit_y,
                "image": player["current_fruit"]["left_atk"],
                "rect": pygame.Rect(fruit_x + player["image"].get_width(), fruit_y, 90, 90),
                "stamina": 1
            }
            special_atks.append(special_atk)


def semi_z():
    if player["current_fruit"]:
        fruit = player["current_fruit"]
        if fruit["type"] == "QUAKE":
            new_atk = {
                "image": pygame.image.load("fruits/attacks/sea.png"),
                "direction": "down",
                "stamina": 100000000000000000000000000000000000000000000000000000000,
                "rect": pygame.Rect(-100, center_y - 280, pygame.image.load("fruits/attacks/sea.png").get_width(), pygame.image.load("fruits/attacks/sea.png").get_height()),
            }
            special_atks.append(new_atk)



def show_updates():
    for update in updates:
        label = small.render(f"{update['name']}", True, (0, 0, 0))
        screen.blit(update["image"], (290, update["y_pos"]))
        pygame.draw.rectect(screen, (255, 255, 0), (290, update["y_pos"] - 40, update["image"].get_width(), 40))
        screen.blit(label, (305, update["y_pos"] - 30))
        pygame.draw.rect(screen, (0, 0, 0), (290, update["y_pos"] + 160, 300, 150))
        y22 = update["y_pos"] + 170
        for log in update["log"]:
            label = super_small.render(log, True, (255, 255, 0))
            screen.blit(label, (300, y22))
            y22 += 40
def all_z():
    ultra_z()
    super_z()
island_fruits = [
##First Island Block Fruits
    [
        {
            "image": pygame.image.load("fruits/shopping/rocketfruit.png"),
            "buying_img": pygame.image.load("fruits/buying/rocketfruit.png"),
            "Name": "Rocket Fruit",
            "cost": 0,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y - 300, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y - 300, 70, 70),
            "left_atk": pygame.image.load("fruits/attacks/rocketleft.png"),
            "right_atk": pygame.image.load("fruits/attacks/rocketright.png"),
            "up_atk": pygame.image.load("fruits/attacks/rocketup.png"),
            "down_atk": pygame.image.load("fruits/attacks/rocketdown.png"),
            "type": "ROCKET",
            "damage": 15,
            "special": rubber_z,
            "special_name": "Nuke Fist",
            "range": 1,
            "specialtwo": super_z,
            "special_nametwo": "Missile Barrage",
            "cool": 2
        },
        {
            "image": pygame.image.load("fruits/shopping/rubberfruit.png"),
            "buying_img": pygame.image.load("fruits/buying/rubberfruit.png"),
            "Name": "Rubber Fruit",
            "cost": 4500,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y - 100, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y - 100, 70, 70),
            "left_atk": pygame.image.load("fruits/attacks/rubberleft.png"),
            "right_atk": pygame.image.load("fruits/attacks/rubberright.png"),
            "up_atk": pygame.image.load("fruits/attacks/rubberup.png"),
            "down_atk": pygame.image.load("fruits/attacks/rubberdown.png"),
            "type": "RUBBER",
            "damage": 30,
            "special": rubber_z,
            "special_name": "Rubber Rocket",
            "specialtwo": dash_z,
            "special_nametwo": "Rubber Cannon",
            "range": 1,
            "cool": 2
        }
    ],
##Second Island Block Fruits
    [
        {
            "image": pygame.image.load("fruits/shopping/lightfruit.png"),
            "buying_img": pygame.image.load("fruits/buying/light.png"),
            "Name": "Light Fruit",
            "cost": 9000,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y - 300, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y - 300, 70, 70),
            "left_atk": pygame.image.load("fruits/attacks/buddha.png"),
            "right_atk": pygame.image.load("fruits/attacks/buddha.png"),
            "up_atk": pygame.image.load("fruits/attacks/buddha.png"),
            "down_atk": pygame.image.load("fruits/attacks/buddha.png"),
            "type": "LIGHT",
            "damage": 90,
            "special": rubber_z,
            "special_name": "Star Shot",
            "specialtwo": super_z,
            "special_nametwo": "Divine Light",
            "range": 20,
            "cool": 4
        },
        {
            "image": pygame.image.load("fruits/shopping/magmafruit.png"),
            "buying_img": pygame.image.load("fruits/buying/magmafruit.png"),
            "Name": "Magma Fruit",
            "cost": 8500,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y - 100, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y - 100, 70, 70),
            "left_atk": pygame.transform.scale(pygame.image.load("fruits/attacks/meteor.png"), (pygame.image.load("fruits/attacks/meteor.png").get_width() * 2, pygame.image.load("fruits/attacks/meteor.png").get_height() * 2)),
            "right_atk": pygame.transform.scale(pygame.image.load("fruits/attacks/meteor.png"), (pygame.image.load("fruits/attacks/meteor.png").get_width() * 2, pygame.image.load("fruits/attacks/meteor.png").get_height() * 2)),
            "up_atk": pygame.transform.scale(pygame.image.load("fruits/attacks/meteor.png"), (pygame.image.load("fruits/attacks/meteor.png").get_width() * 2, pygame.image.load("fruits/attacks/meteor.png").get_height() * 2)),
            "down_atk": pygame.transform.scale(pygame.image.load("fruits/attacks/meteor.png"), (pygame.image.load("fruits/attacks/meteor.png").get_width() * 2, pygame.image.load("fruits/attacks/meteor.png").get_height() * 2)),
            "type": "MAGMA",
            "damage": 77,
            "special": gravity_z,
            "special_name": "Magma Summon",
            "specialtwo": super_z,
            "special_nametwo": "Magma Meteors",
            "range": 1,
            "cool": 2
        }
    ],
##Third Island Block fruits
    [
        {
            "image": pygame.image.load("fruits/shopping/buhhdafruit.png"),
            "buying_img": pygame.image.load("fruits/buying/buhhdafruit.png"),
            "Name": "Buddha Fruit",
            "cost": 10000,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y - 300, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y - 300, 70, 70),
            "left_atk": pygame.image.load("fruits/attacks/buddha.png"),
            "right_atk": pygame.image.load("fruits/attacks/buddha.png"),
            "up_atk": pygame.image.load("fruits/attacks/buddha.png"),
            "down_atk": pygame.image.load("fruits/attacks/buddha.png"),
            "type": "BUDDHA",
            "rect2": pygame.Rect(center_x - 170, center_y, 130, 130),
            "damage": 300,
            "special": transform_z,
            "special_name": "Transform",
            "special_image": pygame.image.load("fruits/attacks/buddha.png"),
            "specialtwo": dash_z,
            "special_nametwo": "Buddha Dash",
            "range": 1,
            "cool": 6
        },
        {
            "image": pygame.image.load("fruits/shopping/lovefruit.png"),
            "buying_img": pygame.image.load("fruits/buying/lovefruit.png"),
            "Name": "Love Fruit",
            "cost": 6980,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y + 100, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y + 100, 70, 70),
            "left_atk": pygame.image.load("fruits/attacks/heart.png"),
            "right_atk": pygame.image.load("fruits/attacks/heart.png"),
            "up_atk": pygame.image.load("fruits/attacks/heart.png"),
            "down_atk": pygame.image.load("fruits/attacks/heart.png"),
            "type": "LOVE",
            "damage": 150,
            "special": rubber_z,
            "rect2": pygame.Rect(center_x - 100, center_y + 100, 155, 155),
            "special_name": "Carming Heart",
            "specialtwo": ultra_z,
            "special_nametwo": "Heart Explosion",
            "range": 5,
            "cool": 4
        }
    ],
##fourth island fruits
    [
        {
            "image": pygame.image.load("fruits/shopping/Quake_Fruit.png"),
            "buying_img": pygame.image.load("fruits/buying/kitsunefruit.png"),
            "Name": "Quake Fruit",
            "cost": 12999,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y - 300, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y - 300, 70, 70),
            "left_atk": pygame.image.load("fruits/attacks/kitsuneleft.png"),
            "right_atk": pygame.image.load("fruits/attacks/kitsuneright.png"),
            "up_atk": pygame.image.load("fruits/attacks/kitsuneleft.png"),
            "down_atk": pygame.image.load("fruits/attacks/kitsunedown.png"),
            "type": "QUAKE",
            "rect2": pygame.Rect(center_x - 170, center_y, 130, 130),
            "damage": 520,
            "special": godly_z,
            "special_name": "Quake Punch",
            "specialtwo": semi_z,
            "special_nametwo": "Seaquake",
            "range": 2,
            "cool": 0.90
        },
        {
            "image": pygame.image.load("fruits/shopping/painfruit.png"),
            "buying_img": pygame.image.load("fruits/buying/kitsunefruit.png"),
            "Name": "Pain Fruit",
            "cost": 0,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y + 100, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y + 100, 70, 70),
            "left_atk": pygame.transform.flip(wispy, True, False),
            "right_atk": wispy,
            "up_atk": pygame.transform.flip(wispy, True, False),
            "down_atk": pygame.transform.flip(wispy, True, False),
            "type": "PAIN",
            "damage": 800,
            "normal": rubber_z,
            "special": god_z,
            "special_name": "Angony Chase",
            "specialtwo": warp_z,
            "special_nametwo": "Rage Summon",
            "range": 10,
            "cool": 6
        }
    ],
##Fifth island fruits
    [
        {
            "image": pygame.transform.scale(pygame.image.load("fruits/shopping/party_bomb.png"), (180, 180)),
            "buying_img": pygame.image.load("fruits/buying/kitsunefruit.png"),
            "Name": "PARTY",
            "cost": 0,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y - 300, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y - 300, 70, 70),
            "left_atk": pygame.transform.flip(pygame.image.load("fruits/attacks/bomb_party.png"), True, False),
            "right_atk": pygame.image.load("fruits/attacks/bomb_party.png"),
            "up_atk": pygame.image.load("fruits/attacks/bomb_party.png"),
            "down_atk": pygame.image.load("fruits/attacks/bomb_party.png"),
            "rect2": pygame.Rect(center_x - 170, center_y, 130, 130),
            "type": "PARTY",
            "damage": 600,
            "special": chase_z,
            "special_name": "Disco Bomb",
            "specialtwo": bombing,
            "special_nametwo": "Bombly Downfall",
            "range": 2,
            "cool": 10
        },
        {
            "image": pygame.image.load("fruits/shopping/Bomb_Fruit.png"),
            "buying_img": pygame.image.load("fruits/buying/kitsunefruit.png"),
            "Name": "Bomb Fruit",
            "cost": 0,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y + 100, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y + 100, 70, 70),
            "left_atk": pygame.transform.flip(pygame.image.load("fruits/attacks/bomb.png"), True, False),
            "right_atk": pygame.image.load("fruits/attacks/bomb.png"),
            "up_atk": pygame.image.load("fruits/attacks/bomb.png"),
            "down_atk": pygame.image.load("fruits/attacks/bomb.png"),
            "rect2": pygame.Rect(660, center_y, 130, 130),
            "type": "BOMB",
            "damage": 200,
            "normal": rubber_z,
            "special": rubber_z,
            "special_name": "Bomb Throw",
            "specialtwo": chase_z,
            "special_nametwo": "Targeted Bomb",
            "range": 10,
            "cool": 14
        }
    ],
## heaven fruits
    [
        {
            "image": pygame.transform.scale(pygame.image.load("fruits/shopping/party_bomb.png"), (180, 180)),
            "buying_img": pygame.image.load("fruits/buying/kitsunefruit.png"),
            "Name": "PARTY",
            "cost": 0,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y - 300, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y - 300, 70, 70),
            "left_atk": pygame.transform.flip(pygame.image.load("fruits/attacks/bomb_party.png"), True, False),
            "right_atk": pygame.image.load("fruits/attacks/bomb_party.png"),
            "up_atk": pygame.image.load("fruits/attacks/bomb_party.png"),
            "down_atk": pygame.image.load("fruits/attacks/bomb_party.png"),
            "rect2": pygame.Rect(center_x - 170, center_y, 130, 130),
            "type": "PARTY",
            "damage": 600,
            "special": rubber_z,
            "special_name": "Disco Bomb",
            "specialtwo": bombing,
            "special_nametwo": "Bombly Downfall",
            "range": 2,
            "cool": 10
        },
        {
            "image": pygame.image.load("fruits/shopping/Bomb_Fruit.png"),
            "buying_img": pygame.image.load("fruits/buying/kitsunefruit.png"),
            "Name": "Bomb Fruit",
            "cost": 0,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y + 100, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y + 100, 70, 70),
            "left_atk": pygame.transform.flip(pygame.image.load("fruits/attacks/bomb.png"), True, False),
            "right_atk": pygame.image.load("fruits/attacks/bomb.png"),
            "up_atk": pygame.image.load("fruits/attacks/bomb.png"),
            "down_atk": pygame.image.load("fruits/attacks/bomb.png"),
            "rect2": pygame.Rect(660, center_y, 130, 130),
            "type": "BOMB",
            "damage": 200,
            "normal": rubber_z,
            "special": rubber_z,
            "special_name": "Bomb Throw",
            "specialtwo": chase_z,
            "special_nametwo": "Targeted Bomb",
            "range": 10,
            "cool": 14
        }
    ],
##Celestal domain Fruits
    [
        {
            "image": pygame.image.load("fruits/shopping/Lightning_Fruit.png"),
            "buying_img": pygame.image.load("fruits/buying/kitsunefruit.png"),
            "Name": "Thunder Fruit",
            "cost": 0,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y - 300, 155, 155),
            "rect2": pygame.Rect(center_x - 170, center_y, 130, 130),
            "img_rect": pygame.Rect(center_x - 100, center_y - 300, 70, 70),
            "left_atk": pygame.image.load("fruits/attacks/Lightning.png"),
            "right_atk": pygame.image.load("fruits/attacks/Lightning.png"),
            "up_atk": pygame.image.load("fruits/attacks/Lightning.png"),
            "down_atk": pygame.image.load("fruits/attacks/Lightning.png"),
            "type": "THUNDER",
            "damage": 500,
            "special": god_z,
            "special_name": "Sky Wraith",
            "specialtwo": super_z,
            "special_nametwo": "Thunder Storm",
            "range": 2,
            "cool": 6
        },
        {
            "image": pygame.image.load("fruits/shopping/flame_fruit.png"),
            "buying_img": pygame.image.load("fruits/buying/kitsunefruit.png"),
            "Name": "Flame Fruit",
            "cost": 0,
            "bought": False,
            "rect": pygame.Rect(center_x - 100, center_y + 100, 155, 155),
            "img_rect": pygame.Rect(center_x - 100, center_y + 100, 70, 70),
            "left_atk": pygame.image.load("fruits/attacks/dragonleft.png"),
            "right_atk": pygame.image.load("fruits/attacks/dragonright.png"),
            "up_atk": pygame.image.load("fruits/attacks/dragonup.png"),
            "down_atk": pygame.transform.flip(pygame.image.load("fruits/attacks/dragonup.png"), False, True),
            "type": "FLAME",
            "damage": 300,
            "normal": rubber_z,
            "special": rubber_z,
            "special_name": "Fire Pistol",
            "specialtwo": super_z,
            "special_nametwo": "Flame Meteors",
            "range": 10,
            "cool": 6
        }
    ]
]

def shop():
    pygame.draw.rect(screen, (255, 0, 0), (center_x - 250, center_y - 200, 600, 500))
    fruits = island_fruits[-3]
    y = center_x - 170
    for fruit in fruits:
        screen.blit(fruit["image"], (y, center_y))
        y += fruit["image"].get_width() + 100
    label = pygame.font.Font(None, 50).render("Bombing Bundle", True, (255, 255, 255))
    screen.blit(label, (center_x - 100, center_y - 180))
    screen.blit(pygame.image.load("special/thunder.png"), (center_x - 230, center_y - 130))
    screen.blit(pygame.image.load("special/pain.png"), (center_x + 220, center_y - 130))
def roll():
    r = random.randint(1, 100)
    one = 0
    if r <= 15:
        one = random.randint(3, 4)
    elif r <= 28:
        one = 2
    elif r <= 65:
        one = random.randint(0, 1)
    else:
        one = 0
    new_fruit = island_fruits[one][random.randint(0, 1)]
    add_message(f"You Rolled {new_fruit['type']}!", (255, 105, 180),  messages[-1]["y_pos"] + 30)
    if len(player["block_fruits"]) > 1:
        player["block_fruits"] = player["block_fruits"][:-1]
        items.remove(items[-1])
    buy([new_fruit])
    add(new_fruit["type"])
    save()
    







for i in range(7):
    island = Island(
        went=False,
        enemy_xp=givens[i],
        enemy_name=names[i],
        name=names2[i],
        quest=quests[i],
        radius=600,
        x=island_positions[i].x,
        y=island_positions[i].y,
        color=colors[i],
        enemy_image=enemys[i],
        health=hps[i],
        level=lvls[i],
        reward=rewards[i],
        fruits=island_fruits[i]
    )
    islands.add(island)
for island in islands:
    if island.name != "Celestal Domain":
        island.spawn_enemys(7)
    else:
        island.spawn_enemys(1)
        
direction = None
clicked = False
attacking = False
direction_aim = None
clicky = False
mode = None
enemy_attacked = False
small = pygame.font.Font(None, 30)

def check_island():
    global current_island
    for island in islands:
        if island.rect.colliderect(player["rect"]):
            current_island = island      

boats = [
    {
        "name": " Dinghy",
        "image": pygame.image.load("boats/dinghy.png"),
        "rect": pygame.Rect(-100, center_y, 179, 117),
        "cost": 1000,
        "owned": False
    }
]



def buy_boat(boat):
    global boat_owned
    if player["money"] >= boat["cost"]:
        if boat["owned"] is False:
            player["money"] -= boat["cost"]
            boat["owned"] = True
        elif boat["owned"]:
            boat["owned"] = True
        boat_owned = True
            
        
def draw_boats():
    for boat in boats:
        screen.blit(boat["image"], boat["rect"])
        

chatting = False
fruit_dealers = []
already_fruit = False
def draw_NPC():
    global page, already_fruit, chatting, clicked
    for island in islands:
        blox_fruit_dealer = {
            "image": pygame.image.load("NPCS/fruit_dealer.png"),
            "rect": pygame.Rect(island.rect.x + 700, island.rect.y + 90, 172, 291)
        }
        if island.enemy_name == "Yeti":
            gacha = {
                "image": pygame.image.load("NPCS/summer_gacha.png"),
                "rect": pygame.Rect(island.rect.x + 250, island.rect.y + 240, 122, 191)
            }
            screen.blit(gacha["image"], (gacha["rect"].x - 140, gacha["rect"].y - 100))
            if gacha["rect"].colliderect(player["rect"]) and not already_fruit:         
                screen.blit(super_small.render("[E]Interact", True, (255, 255, 255)), (gacha["rect"].x, gacha["rect"].y - 90 + 190))
                if key[pygame.K_e]:
                    if not clicked:
                        clicked = True
                        page = "rolling"
        if island.enemy_name == "Bandit":
            robot = {
                "image": pygame.image.load("NPCS/robotmega.png"),
                "rect": pygame.Rect(island.rect.x + 250, island.rect.y + 240, 122, 191)
            }
            screen.blit(robot["image"], (robot["rect"].x - 25, robot["rect"].y - 100))
            if robot["rect"].colliderect(player["rect"]):       
                screen.blit(super_small.render("[E]Interact", True, (255, 255, 255)), (robot["rect"].x, robot["rect"].y - 90 + 190))
                if pygame.key.get_pressed()[pygame.K_e]:
                    if not clicked:
                        clicked = True
                        page = "robotmega"
                
        if island.enemy_name == "Heaven's Guard":
            man = {
                "image": pygame.image.load("NPCS/defenseman.png"),
                "rect": pygame.Rect(island.rect.x + 250, island.rect.y + 240, 122, 191)
            }
            screen.blit(man["image"], (man["rect"].x - 140, man["rect"].y - 100))
            label = pygame.font.Font(None, 25).render(f"Strong Healer", True, (255, 255, 255))
            screen.blit(label, (man["rect"].x - 100, man["rect"].y + 40))
        
            if man["rect"].colliderect(player["rect"]) and not already_fruit:         
                screen.blit(super_small.render("[E]Interact", True, (255, 255, 255)), (man["rect"].x, man["rect"].y - 90 + 190))
                if key[pygame.K_e]:
                    if not clicked:
                        clicked = True
                        page = "defense"
        if island.enemy_name != "":
            key = pygame.key.get_pressed()
            screen.blit(blox_fruit_dealer["image"], blox_fruit_dealer["rect"])
            label = pygame.font.Font(None, 25).render(f"Blox Fruit Dealer", True, (255, 255, 255))
            screen.blit(label, (blox_fruit_dealer["rect"].x + 10, blox_fruit_dealer["rect"].y + 110))
            if blox_fruit_dealer["rect"].colliderect(player["rect"]) and not already_fruit:         
                screen.blit(super_small.render("[E]Buy Block Fruit", True, (255, 255, 255)), (blox_fruit_dealer["rect"].x, blox_fruit_dealer["rect"].y + 190))
                if key[pygame.K_e]:
                    chatting = True
                if chatting:
                    chatting = True
                    page = "fruits"
            
         
       
                
     
           
     
transformed = False
exiting = False
def draw_UI():
    for island in islands:
        label = pygame.font.Font(None, 40).render(f"{player['x']}    {player['y']}", True, (255, 255, 255))
        screen.blit(label, (width - 350, 50))
        label2 = pygame.font.Font(None, 40).render(f"${player['money']}", True, (0, 255, 0))
        screen.blit(label2, (50, center_y))
        labely = pygame.font.Font(None, 40).render(f"Lvl.{player['lvl']}({player['stats_now']}/{player['stats_need']})", True, (255, 255, 255))
        screen.blit(labely, (50, center_y + 80))


musicnow = "Drip_Fruits.mp3"
music = pygame.mixer.Sound(f"music/{musicnow}")
music.play(-1)
running = True
clock = pygame.time.Clock()
dead_enemies = []
z = pygame.image.load("zz.png")
x = pygame.image.load("xx.png")
driving_boat = False
cool_down = 0
sended = False
cool_down2 = 0
load()
raining = False
bombs = []
while running:
    now = pygame.time.get_ticks()
    elapsed = now - start_time
    now2 = pygame.time.get_ticks()
    atk_elapsed = now2 - start_atk
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            clicked = False
            enemy_attacked = False
            clicked = False
        elif event.type == pygame.MOUSEBUTTONUP:
            clicky = False
                        
        elif event.type == pygame.KEYDOWN:
             hit = False
             if len(player["block_fruits"]) > 0:

                                
                if event.key == pygame.K_1:         
                    player["current_fruit"] = player["block_fruits"][0]
                if len(player["block_fruits"]) >= 2:
                    if event.key == pygame.K_2:         
                        player["current_fruit"] = player["block_fruits"][1]
                if len(player["block_fruits"]) >= 3:
                    if event.key == pygame.K_3:         
                        player["current_fruit"] = player["block_fruits"][2]
                if len(player["block_fruits"]) >= 4:
                    if event.key == pygame.K_4:         
                        player["current_fruit"] = player["block_fruits"][3]
                if len(player["block_fruits"]) >= 5:
                    if event.key == pygame.K_5:         
                        player["current_fruit"] = player["block_fruits"][4]
                if len(player["block_fruits"]) >= 6:
                    if event.key == pygame.K_6:         
                        player["current_fruit"] = player["block_fruits"][5]
                if len(player["block_fruits"]) >= 7:
                    if event.key == pygame.K_7:         
                        player["current_fruit"] = player["block_fruits"][6]
                if len(player["block_fruits"]) >= 9:
                    if event.key == pygame.K_9:         
                        player["current_fruit"] = player["block_fruits"][8]

                if len(player["block_fruits"]) >= 8:
                    if event.key == pygame.K_8:         
                        player["current_fruit"] = player["block_fruits"][7]

                if event.key == pygame.K_o:
                    if player["money"] >= 100000 and player["lvl"] >= 130:
                        player["block_fruits"].append(swords[0])
                        add(swords[0]["type"])
                        player["money"] -= 100000
                        add_message("You gained DARK BLADE!", (0, 0, 255), messages[-1]["y_pos"] + 30)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            if event.button == 1:
                if page != "abilitys" and pygame.Rect(width - 90, 70, 50, 50).collidepoint(pos):
                    page = "home"
                    already_fruit = False
                    chatting = False
                if page == "abilitys":
                    if pygame.Rect(width - 290, center_y, 140, 50).collidepoint(pos):
                        if player["money"] >= 300:
                            player["current_fruit"]["damage"] += random.randint(1, 3)
                            player["money"] -= 300
                    elif pygame.Rect(width - 290, center_y + 100, 140, 50).collidepoint(pos):
                        page = "home"
                        chatting = False
                        already_fruit = False
                if page == "rolling":
                    if pygame.Rect(width - 290, center_y, 140, 50).collidepoint(pos):
                        if player["lvl"] >= 15 and player["money"] >= 10000:
                            player["money"] -= 10000
                            roll()
                            if transformed:
                                player["image"] = pygame.transform.scale(player["image"], (180, 180))
                                transformed = False
                    elif pygame.Rect(width - 290, center_y + 100, 140, 50).collidepoint(pos):
                        page = "home"
                        chatting = False
                        already_fruit = False
                if page == "robotmega":
                    if pygame.Rect(width - 290, center_y, 140, 50).collidepoint(pos):
                        if player["lvl"] >= 250 and player["money"] >= 10000:
                            player["money"] -= 100000
                            new_sword = {
                                "Name": "Dark Blade",
                                "type": "DARK V2",
                                "damage": 800,
                                "special": dash_z,
                                "special_name": "Samurai Wrath",
                                "special_nametwo": "Dark Slash",
                                "specialtwo": rubber_z,
                                "left_atk": wsws,
                                "right_atk": pygame.transform.flip(wsws, True, False),
                                "up_atk": wsws,
                                "buying_img": None,
                                "image": wsws,
                                "cool": 6,
                                "range": 1,
                                "awakend": False,
                                "mas": 1,
                                "down_atk": pygame.image.load("fruits/attacks/Dark_Blade.png")
                            }
                            player["block_fruits"].append(new_sword)
                            add(new_sword["type"])
                    elif pygame.Rect(width - 290, center_y + 100, 140, 50).collidepoint(pos):
                        page = "home"
                        chatting = False
                        already_fruit = False
                if page == "defense":
                    if pygame.Rect(width - 290, center_y, 140, 50).collidepoint(pos):
                        if player["health"] <= 190 and player["money"] >= 1000:
                            player["money"] -= 1000
                            
                            player["health"] += 10
                            if player["health"] >= player["max_health"]:
                                player["max_health"] += 10
                    elif pygame.Rect(width - 290, center_y + 100, 140, 50).collidepoint(pos):
                        page = "home"
                        chatting = False
                        already_fruit = False
                if page == "shop":
                    for fruit in island_fruits[-3]:
                        if page == "shop" and not clicky:
                            if fruit["rect2"].collidepoint(pos):
                                if blox_coins >= 0:
                                    clicky = True
                                    blox_coins -= fruit["cost"]
                                    if len(player["block_fruits"]) > 1:
                                        player["block_fruits"] = player["block_fruits"][:-1]
                                        items.remove(items[-1])
                                    buy([fruit])
                                    add(fruit["type"])
                                    if transformed:
                                        player["image"] = pygame.transform.scale(player["image"], (180, 180))
                                        transformed = False
                                    player["current_fruit"] = player["block_fruits"][-1]
                                    add_message(f"You Got Rewarded {fruit['Name']}!", (255, 0, 0), messages[-1]["y_pos"] + 30)
                                    save()   
                for island in islands:
                    for fruit in current_island.block_fruits:
                        if page == "fruits" and not clicky:
                            if fruit["rect"].collidepoint(pos):
                                if fruit["bought"] is False and player["money"] >= fruit["cost"]:
                                    clicky = True
                                    player["money"] -= fruit["cost"]
                                    if len(player["block_fruits"]) > 1:
                                        player["block_fruits"] = player["block_fruits"][:-1]
                                        items.remove(items[-1])
                                    buy([fruit])
                                    if transformed:
                                        
                                        player["image"] = pygame.transform.scale(player["image"], (180, 180))
                                        transformed = False
                                    add(fruit["type"])
                                    player["current_fruit"] = player["block_fruits"][-1]
                                    add_message(f"You Bought The {fruit['Name']}!", (255, 0, 0), messages[-1]["y_pos"] + 30)
                                    save()
                    
            elif event.button == 3:
                if not clicky:
                    clicky = True
                    if mode != "atk":
                        mode = "atk"
                    else:
                        mode = None
                

    clock.tick(60)
    screen.fill((0, 105, 148))
    key = pygame.key.get_pressed()
    if player["lvl"] >= 100:
        if not sended:
            add_message(f"A GOD HAS ARRIVED!", (255, 0, 0), messages[-1]["y_pos"] + 30)
            sended = True
    if elapsed // 1000 >= 60:
        
        if not raining:
            raining = True
            add_message("The Bombs Pour...", (255, 0, 0), messages[-1]["y_pos"] + 30)
        elif raining:
            raining = False
            add_message("The Bombing Ends...", (255, 0, 0), messages[-1]["y_pos"] + 30)
        thing = pygame.image.load("fruits/attacks/bomb.png")
        for _ in range(5):
            for island in islands:
                bomb = {
                    "image": thing,
                    "rect": pygame.Rect(island.rect.x + random.randint(0, width), island.rect.x - 400, thing.get_width(), thing.get_height())
                }
                bombs.append(bomb)
        start_time = pygame.time.get_ticks()
    
    if not raining:
        bombs.clear()
                
    for island in islands:
        if island.rect.colliderect(player["rect"]):
            current_island = island
    if player["health"] <= 0:
        player["money"] -= 100
        player["health"] = 100
        save()
        for island in islands:
            for enemy in island.enemies.copy():
                enemy.kill()
            if island.name != "Celestal Domain":
                island.spawn_enemys(7)
            else:
                island.spawn_enemys(1)
                add_message("Wings of Wrath Spread", (0, 0, 255), messages[-1]["y_pos"] + 30)
    if player["money"] < 0:
        player["money"] = 0
    for island in islands:
        if island.name == "Pirate Starter Village":
            island.went = True
    for island in islands:
        if island is not current_island:
            if player["lvl"] >= island.level and not island.went:
                add_message(f"You Are Now Ready For {island.name}", (0, 255, 0), messages[-1]["y_pos"] + 30)
                island.went = True
                save()
    if quest_earned and current_quest["now"] >= current_quest["number"]:
        player["money"] += current_quest["money"]
        player["stats_now"] += current_quest["xp"]
        current_island.quest["now"] = 0
        current_quest = None
        questing = False
        quest_earned = False
        add_message("You Completed A Quest!", (255, 192, 203), messages[-1]["y_pos"] + 30)
        save()
        
    player["damage"] = player["current_fruit"]["damage"]
    for island in islands:
        pygame.draw.circle(screen, island.color, (island.rect.centerx, island.rect.centery), island.radius)
        island.enemies.draw(screen)
        island.enemies.update()
    draw_UI()
    draw_NPC()
    if current_island.name == "Frozen Island" or current_island.name == "Kitsune Island":
        musicnow = "Drip_Fruits.mp3"
    else:
        musicnow = "enemys.mp3"
    if player["health"] < player["max_health"]:
        player["health"] += 0.05
    draw_quest_npc()
    if questing:
        draw_quest()
    check_island()
    draw_items()
    draw_boats()
    screen.blit(player["image"], (center_x - player["image"].get_width() / 2, center_y - player["image"].get_height() / 2))
    pygame.draw.rect(screen, (255, 0, 0), (60, height - 80, player["max_health"] * 4, 59))
    pygame.draw.rect(screen, (0, 255, 0), (60, height - 80, player["health"] * 4, 59))
    if len(special_atks) > 0:
        for atk in special_atks[:]:
            if atk["image"] is not None:
                screen.blit(atk["image"], atk["rect"])
            for island in islands:
                for enemy in island.enemies:
                    if enemy.rect.colliderect(atk["rect"]):
                        atk["stamina"] -= 1
                        save()
                        enemy.health -= player["current_fruit"]["damage"] + 11
                        if atk in special_atks:
                            if atk["stamina"] <= 0:
                                special_atks.remove(atk)
            if atk["direction"] == "left":
                atk["rect"].x -= 9
            if atk["direction"] == "right":
                atk["rect"].x += 9
            if atk["direction"] == "up":
                atk["rect"].y -= 9
            if atk["direction"] == "down":
                atk["rect"].y += 9
            if atk["direction"] == "up and left":
                atk["rect"].y -= 9
                atk["rect"].x -= 9
            if atk["direction"] == "down and left":
                atk["rect"].y += 9
                atk["rect"].x -= 9
            if atk["direction"] == "up and right":
                atk["rect"].y -= 9
                atk["rect"].x += 9
            if atk["direction"] == "down and right":
                atk["rect"].y += 9
                atk["rect"].x += 9
            elif atk["direction"] == "all":
                for enemy in current_island.enemies:
                    if atk["rect"].x < enemy.rect.x and atk["rect"].x > enemy.rect.x - width:
                        atk["rect"].x += 4
                    if atk["rect"].x > enemy.rect.x and atk["rect"].x < enemy.rect.x + width:
                        atk["rect"].x -= 4
                    if atk["rect"].y < enemy.rect.y and atk["rect"].y > enemy.rect.y - height:
                        atk["rect"].y += 4
                    if atk["rect"].y > enemy.rect.y and atk["rect"].y < enemy.rect.y + height:
                        atk["rect"].y -= 4
            for island in islands:
                for enemy in island.enemies:
                    if enemy.rect.colliderect(atk["rect"]):
                        atk["stamina"] -= 1
                        save()
                        if player["current_fruit"]["type"] == "BOMB":
                            if atk["direction"] == "left":
                                enemy.rect.x -= 190
                            elif atk["direction"] == "right":
                                enemy.rect.x += 190
                            elif atk["direction"] == "up":
                                enemy.rect.y -= 190
                            elif atk["direction"] == "down":
                                enemy.rect.y += 190
                        enemy.health -= player["current_fruit"]["damage"] + 11
                        if atk in special_atks:
                            if atk["stamina"] <= 0:
                                special_atks.remove(atk)
            if atk["rect"].x < -100 or atk["rect"].x > width + 100 or atk["rect"].y < -100 or atk["rect"].y > height + 100:
                if atk in special_atks:
                    special_atks.remove(atk)
    if page != "home" and page == "fruits":
        pygame.draw.rect(screen, (255, 0, 0), (width - 90, 70, 50, 50), border_radius=10)
        screen.blit(pygame.font.Font(None, 40).render("X", True, (255, 255, 255)), (width - 75, 80))

        show_fruits()
    for island in islands:
        if island.name == "Celestal Domain":
            pygame.draw.line(screen, island.color, (player["rect"].x + pic.get_width() / 2, player["rect"].y + pic.get_height() / 2), (island.rect.x, island.rect.y), 4)
    if page != "home" and page == "updates":
        show_updates()
        pygame.draw.rect(screen, (255, 0, 0), (width - 90, 70, 50, 50), border_radius=10)
        screen.blit(pygame.font.Font(None, 40).render("X", True, (255, 255, 255)), (width - 75, 80))

    if player["stats_now"] >= player["stats_need"]:
        player["lvl"] += 1
        player["stats_need"] += 120
        player["stats_now"] = 0
        save()
    ability_teacher()
    if player["current_fruit"]["mas"] >= 300:
        player["current_fruit"]["mas"] = 300
        if player["current_fruit"]["awakend"] is False:
            add_message(f"You Have Awakend {player['current_fruit']['type']}!", (0, 255, 0), messages[-1]["y_pos"] + 30)
            player["current_fruit"]["damage"] += player["current_fruit"]["damage"] / 4
            player["current_fruit"]["cool"] / 2
            player["current_fruit"]["awakend"] = True
    for island in islands:
        for enemy in island.enemies.copy():
            if enemy.health <= 0:
                enemy.kill()
                player["stats_now"] += enemy.xp_given
                player["bounty"] += 10
                player["money"] += enemy.reward
                if player["current_fruit"]["mas"] < 300:
                    player["current_fruit"]["mas"] += 100
                else:
                    player["current_fruit"]["mas"] = 300
                new_enemy = Enemy(
                    name=island.enemy_name,
                    hp=island.enemy_health,
                    speed=random.randint(1, 2),
                    damage=3,
                    xp=island.xp,
                    lvl=island.level,
                    image=island.enemy_image,  
                    x=random.randint(island.rect.x + 100, island.rect.x + 320),
                    y=random.randint(island.rect.y - 100, island.rect.y + 100),
                    r=209,
                    reward=island.bonus
                )
                island.enemies.add(new_enemy)
                if quest_earned:
                    current_quest["now"] += 1
                if enemy.name == "Tryant Of The Skies":
                    blox_coins += 200
                    add_message("Wings Dissapear, And Then Reappears...", (255, 0, 0), messages[-1]["y_pos"] + 30)
                save()

                               
    if key[pygame.K_RETURN] and mode == "atk" and not attacking:
        clicked = True
        attacking = True
        start_atk = pygame.time.get_ticks()
        direction_aim = direction
        if player["current_fruit"]:
            fruit = player["current_fruit"]
    if raining:
        for bomb in bombs:
            screen.blit(bomb["image"], (bomb["rect"].x, bomb["rect"].y))
            bomb["rect"].y += 5
            if bomb["rect"].colliderect(player["rect"]):
                player["health"] -= player["health"] // 4
                hit = True
            for island in islands:
                for enemy in island.enemies:
                    if bomb["rect"].colliderect(enemy.rect):
                        enemy.health -= enemy.health // 4
                        if bomb in bombs:
                            bombs.remove(bomb)
    if page == "abilitys":
        things = [
            "Upgrade your Fruits damage?",
            "Im not kidding Bro."
        ]
        y = center_y
        pygame.draw.rect(screen, (120, 120, 120), (center_x - 170, center_y - 20, 400, 120))
        for thing in things:
            label = small.render(thing, True, (255, 255, 255))
            screen.blit(label, (center_x - 150, y))
            y += 40
        pygame.draw.rect(screen, (120, 120, 120), (width - 290, center_y, 140, 50), border_radius=0)
        screen.blit(pygame.font.Font(None, 40).render("Yes", True, (255, 255, 255)), (width - 270, center_y + 10))
        pygame.draw.rect(screen, (120, 120, 120), (width - 290, center_y + 100, 140, 50), border_radius=0)
        screen.blit(pygame.font.Font(None, 40).render("No", True, (255, 255, 255)), (width - 270, center_y + 110))
    if page == "robotmega":
        if player["lvl"] >= 250:
            things = [
                "Hello. You must have Dark",
                "Blade. I can upgrade it to",
                "V2 if yo give me 100000$"
            ]
        if player["lvl"] < 250:
            things = [
                "Idk what are you. Get",
                "out of here and stop",
                "talking to me!!!!!!!!!"
            ]
        y = center_y
        pygame.draw.rect(screen, (120, 120, 120), (center_x - 170, center_y - 20, 400, 120))
        for thing in things:
            label = small.render(thing, True, (255, 255, 255))
            screen.blit(label, (center_x - 150, y))
            y += 40
        pygame.draw.rect(screen, (120, 120, 120), (width - 290, center_y, 140, 50), border_radius=0)
        screen.blit(pygame.font.Font(None, 40).render("Okay", True, (255, 255, 255)), (width - 270, center_y + 10))
        pygame.draw.rect(screen, (120, 120, 120), (width - 290, center_y + 100, 140, 50), border_radius=0)
        screen.blit(pygame.font.Font(None, 40).render("No", True, (255, 255, 255)), (width - 270, center_y + 110))
    
    if page == "rolling":
        things = [
            "Hello, Im Zioles.",
            "I sell physical fruits.",
            "I'll give you a one."
        ]
        y = center_y
        pygame.draw.rect(screen, (120, 120, 120), (center_x - 170, center_y - 20, 400, 120))
        for thing in things:
            label = small.render(thing, True, (255, 255, 255))
            screen.blit(label, (center_x - 150, y))
            y += 40
        pygame.draw.rect(screen, (120, 120, 120), (width - 290, center_y, 140, 50), border_radius=0)
        screen.blit(pygame.font.Font(None, 40).render("Yes", True, (255, 255, 255)), (width - 270, center_y + 10))
        pygame.draw.rect(screen, (120, 120, 120), (width - 290, center_y + 100, 140, 50), border_radius=0)
        screen.blit(pygame.font.Font(None, 40).render("No", True, (255, 255, 255)), (width - 270, center_y + 110))
    if page == "defense":
        if player["health"] <= 40:
            things = [
                "Hey. Are you alright?",
                "You must be injured!",
                "I'll boost your health!."
            ]
        else:
            things = [
                "Hey. You look strong.",
                "The max health is 200",
                "I'll boost your health!"
            ]
        y = center_y
        pygame.draw.rect(screen, (120, 120, 120), (center_x - 170, center_y - 20, 400, 120))
        for thing in things:
            label = small.render(thing, True, (255, 255, 255))
            screen.blit(label, (center_x - 150, y))
            y += 40
        pygame.draw.rect(screen, (120, 120, 120), (width - 290, center_y, 140, 50), border_radius=0)
        screen.blit(pygame.font.Font(None, 40).render("Okay", True, (255, 255, 255)), (width - 270, center_y + 10))
        pygame.draw.rect(screen, (120, 120, 120), (width - 290, center_y + 100, 140, 50), border_radius=0)
        screen.blit(pygame.font.Font(None, 40).render("No Way", True, (255, 255, 255)), (width - 270, center_y + 110))
    
    
    if mode == "atk":
        pygame.draw.rect(screen, (100, 100, 100), (width - 200, height - 300, 200, 300), border_radius=9)
        if player["current_fruit"]:
            if player["current_fruit"]:
                if cool_down2 > 0:
                    pygame.draw.rect(screen, (170, 170, 170), (width - 164, height - 190, cool_down2 * 2, 30))

                if cool_down > 0:
                    pygame.draw.rect(screen, (170, 170, 170), (width - 164, height - 250, cool_down * 2, 30))
                screen.blit(z, (width - 200, height - 250))
                screen.blit(x, (width - 200, height - 190))
                label = pygame.font.Font(None, 28).render(f"{player['current_fruit']['special_name']}", True, (255, 255, 255))
                screen.blit(label, (width - 160, height - 250))
                label2 = pygame.font.Font(None, 28).render(f"{player['current_fruit']['special_nametwo']}", True, (255, 255, 255))
                screen.blit(label2, (width - 160, height - 190))                                       
                labe2 = font.render(f"{player['current_fruit']['type']}", True, (255, 255, 255))
                screen.blit(pygame.font.Font(None, 55).render(f"MAS.{player['current_fruit']['mas']}", True, (255, 255, 255)), (width - 180, height - 125))
        else:
            labe2 = font.render(f"{current_type}", True, (255, 255, 255))
        
    
        screen.blit(labe2, (width - 181, height - 287))
        if attacking and not clicked:
           clicked = True
           if atk_elapsed <= 100:

               if player["current_fruit"]["type"] != "FLAME" and player["current_fruit"]["type"] != "BOMB" and player["current_fruit"]["type"] != "PARTY" and player["current_fruit"]["type"] != "BUDDHA" and player["current_fruit"]["type"] != "THUNDER" and player["current_fruit"]["type"] != "MAGMA" and player["current_fruit"]["type"] != "PAIN V2" and player["current_fruit"]["type"] != "PAIN":
                   if direction_aim == "up":
                       if player["current_fruit"]["up_atk"] is not None:
                           attack_rect = pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height() / 2 - 40, 90, 90)
                           screen.blit(fruit["up_atk"], (center_x - pic.get_width() / 2, center_y - pic.get_height() / 2 - 40))
                       else:
                           attack_rect = pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height() / 2, pic.get_width(), pic.get_height())
                   elif direction_aim == "down":
                       if player["current_fruit"]["down_atk"] is not None:
                           attack_rect = pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height() / 2 + 80, 90, 90)
                           screen.blit(fruit["down_atk"], (center_x - pic.get_width() / 2, center_y - pic.get_height() / 2 + 80))
                       else:
                           attack_rect = pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height(), pic.get_width(), pic.get_height())
                   if direction_aim == "left":
                       if player["current_fruit"]["left_atk"] is not None:
                           attack_rect = pygame.Rect(center_x - pic.get_width() / 2 - 40, center_y - pic.get_height() / 2, 90, 90)
                           screen.blit(fruit["left_atk"], (center_x - pic.get_width() / 2 - 40, center_y - pic.get_height() / 2 + player["current_fruit"]["left_atk"].get_height() / 2))
                       else:
                           attack_rect = pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height() / 2, pic.get_width(), pic.get_height())
                   elif direction_aim == "right":
                       if player["current_fruit"]["right_atk"] is not None:
                           attack_rect = pygame.Rect(center_x + pic.get_width(), center_y - pic.get_height() / 2, 90, 90)
                           screen.blit(fruit["right_atk"], (center_x - pic.get_width() / 2 + 120, center_y - pic.get_height() / 2 + player["current_fruit"]["left_atk"].get_height() / 2))
                       else:
                           attack_rect = pygame.Rect(center_x - pic.get_width() / 2, center_y - pic.get_height() / 2, pic.get_width(), pic.get_height())

                        
                                                                                                                                    
           if elapsed >= 101:
               attacking = False
               start_atk = pygame.time.get_ticks()
               attack_rect = None
    if mode != "atk":
        player["speed"] = 15
    for island in islands:
        for boat in boats:
            if page == "home":
                if key[pygame.K_w]:
                    future_y = player["rect"].copy()
                    future_y.y -= 5
                    direction = "up"
                    for enemy in island.enemies:
                        enemy.rect.y += player["speed"]
                    island.rect.y += player["speed"]
                    player["y"] -= player["speed"]
                    if not driving_boat:
                        boat["rect"].y += player["speed"]
                    
                        
                if key[pygame.K_s]:
                    future_y = player["rect"].copy()
                    future_y.y += 5
                    direction = "down"
                    for enemy in island.enemies:
                        enemy.rect.y -= player["speed"]
                    island.rect.y -= player["speed"]
                    player["y"] += player["speed"]
                    if not driving_boat:
                        boat["rect"].y -= player["speed"]
                if key[pygame.K_a]:
                    future_y = player["rect"].copy()
                    future_y.x -= 5
                    direction = "left"
                    for enemy in island.enemies:
                        enemy.rect.x += player["speed"]
                    island.rect.x += player["speed"]
                    player["x"] -= player["speed"]
                    if not driving_boat:
                        boat["rect"].x += player["speed"]
                if key[pygame.K_d]:
                    future_y = player["rect"].copy()
                    future_y.x += 5
                    direction = "right"
                    for enemy in island.enemies:
                        enemy.rect.x -= player["speed"]
                    island.rect.x -= player["speed"]
                    player["x"] += player["speed"]
                    if not driving_boat:
                        boat["rect"].x -= player["speed"]
                        
                for atk in special_atks[:]:
                    if key[pygame.K_w]:
                        atk["rect"].y += player["speed"] / 6
                    if key[pygame.K_s]:
                        atk["rect"].y -= player["speed"] / 6
                    if key[pygame.K_a]:
                        atk["rect"].x += player["speed"] / 6
                    if key[pygame.K_d]:
                        atk["rect"].x -= player["speed"] / 6
                for bomb in bombs[:]:
                    if key[pygame.K_w]:
                        bomb["rect"].y += player["speed"] / 6
                    if key[pygame.K_s]:
                        bomb["rect"].y -= player["speed"] / 6
                    if key[pygame.K_a]:
                        bomb["rect"].x += player["speed"] / 6
                    if key[pygame.K_d]:
                        bomb["rect"].x -= player["speed"] / 6


    if key[pygame.K_p]:
        if page == "home":
            page = "updates"
    elif key[pygame.K_z] and mode == "atk" and not attacking and not clicked:
        if player["current_fruit"]["special"] and cool_down <= 0:
            if player["current_fruit"]["special_name"] != "":
                player["current_fruit"]["special"]()

            clicked = True
            cool_down = 100
    elif key[pygame.K_x] and mode == "atk" and not attacking and not clicked:
        if player["current_fruit"]["specialtwo"] and cool_down2 <= 0:
            if player["current_fruit"]["special_nametwo"] != "":
                player["current_fruit"]["specialtwo"]()
            clicked = True
            cool_down2 = 100
    elif key[pygame.K_c] and not clicked:
        if page != "controls":
            page = "controls"
        else:
            page = "home"
        clicked = True
    if page == "controls":
        show_controls()
    if cool_down > 0:
        cool_down -= player["current_fruit"]["cool"]
    if cool_down2 > 0:
        cool_down2 -= player["current_fruit"]["cool"] / 2
    if key[pygame.K_i] and not clicked:
         clicked = True
         if page != "shop":
             page = "shop"
         else:
             page = "home"
    if page == "shop":
        shop()

    
    display_messages()
    pygame.display.flip()

save()
pygame.quit()
    
