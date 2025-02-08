import pygame
import sys

SCREEN_SIZE = (800, 600)
GAME_ICON = "snake.png"
GAME_TITLE = "Snake"
INITIAL_GAME_SPEED = 10
BACKGROUND_COLOR = (252, 232, 247)
APPLES = 3


def main():
    screen, clock = initialize_pygame()
    game_state = initialize_game_state()
    while game_state["program_running"]:
        clock.tick(game_state['game_speed'])
        events = get_events()
        print(events)
        update_game_state(events, game_state)
        update_screen(screen, game_state)
    perform_shutdown()


def initialize_pygame():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    icon = pygame.image.load(GAME_ICON)
    pygame.display.set_icon(icon)
    pygame.display.set_caption(GAME_TITLE)
    clock = pygame.time.Clock()
    return screen, clock


def initialize_game_state():
    game_state = {
        "program_running": True,
        "game_running": False,
        "game_paused": False,
        "game_speed": INITIAL_GAME_SPEED,
        "game_score": 0
    }
    return game_state


def get_events():
    events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           events.append("quit")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                events.append("up")
            elif event.key == pygame.K_DOWN:
                events.append("down")
            elif event.key == pygame.K_LEFT:
                events.append("left")
            elif event.key == pygame.K_RIGHT:
                events.append("right")
            elif event.key == pygame.K_SPACE:
                events.append("space")
            elif event.key == pygame.K_RETURN:
                events.append("enter")
            elif event.key == pygame.K_ESCAPE:
                events.append("escape")
    return events


def update_game_state(events, game_state):
    if "quit" in events:
        game_state["program_running"] = False
    elif not game_state["game_running"]:
        if "escape" in events:
            game_state["program_running"] = False
        elif "enter" in events:
            initialize_new_game(game_state)
            game_state["program_running"] = True
        elif game_state["game_paused"]:
             if "escape" in events:
                 game_state["game_running"] = False
             elif "space" in events:
                 game_state["game_paused"] = False
        else:
             if "escape" in events or "space" in events:
                 game_state["game_paused"] = True
             if "up" in events:
                 pass
             if "down" in events:
                 pass
             if "left" in events:
                 pass
             if "right" in events:
                 pass


def initialize_new_game(game_state):
    game_state["apples"] = place_apples(APPLES, game_state)
    game_state["direction"] = [1, 0]
    game_state["game_paused"] = False
    game_state["score"] = 0
    game_state["game_speed"] = INITIAL_GAME_SPEED



def place_apples(n, game_state):
    pass

def update_screen(screen, game_state):
    screen.fill(BACKGROUND_COLOR)
    pygame.display.flip()



def perform_shutdown():
    pygame.init()
    sys.exit()


main()












