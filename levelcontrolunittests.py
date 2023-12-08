import sys
import pygame
import constants

from GameStates.levels import levels

def perform_generic_unit_test(test_function, input_arguments: tuple, expected_outputs: tuple):
    ''' Performs a unit test on the provided test function, given a sequence of input arguments and a sequence of
    desired outputs.

    Args:
        test_function: the function to be unit tested.
        input_arguments: the arguments to be passed to our test function.
        expected_outputs: the desired outputs from our test function, given the above input arguments.

    Returns:
        None

    Upon a failed comparison, an AssertionError is raised. Upon an exception occurring, it is reported.

    '''
    try:
        results = test_function(*input_arguments)

        print("Testing: " + test_function.__name__)
        print("Input Arguments: " + str(input_arguments))
        print("Expected Outputs: " + str(expected_outputs))
        print("Actual Outputs: " + str((results,)))

        assert expected_outputs == (results,), "Test Failed- " + test_function.__name__ + "- Outputs do not match"

    except Exception as ex:
        print("Test Failed- " + test_function.__name__ + "- Exception thrown: " + type(ex).__name__)

    else:
        print("Test Passed!")

def return_input_arguments(input_arguments: tuple):
    '''Returns the input arguments. Used in conjunction with perform_generic_unit_test() to compare variables to
    their expected values.

    Args: 
        input_arguments: the input arguments.

    Returns:
        input_arguments: the input arguments.
    '''
    return input_arguments

# initialize pygame
pygame.init()

# create game window
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("The Aurora Armada")

gamestate = levels()



### INITIAL STATE UNIT TESTS ###
# Verifies that the user starts hovering over level 1
perform_generic_unit_test(return_input_arguments, (gamestate.current_level,), (0,))

# Verifies that the user starts with only level 1 unlocked
perform_generic_unit_test(return_input_arguments, (gamestate.unlocked_level,), (1,))

# Verifies that the total number of levels hasn't changed
perform_generic_unit_test(return_input_arguments, (gamestate.total_levels,), (15,))

# Verifies that the screen dimensions haven't changed
perform_generic_unit_test(return_input_arguments, ((gamestate.screen_rect.width, gamestate.screen_rect.height),), ((576, 768),))

# Verifies that the gamestate doesn't end immediately with no input
perform_generic_unit_test(return_input_arguments, (gamestate.done,), (False,))



### LEVEL SELECTION NAVIGATION UNIT TESTS ###
gamestate.unlocked_level = 15

gamestate.current_level = 7
# Verifies that arrow key navigation does what we expect while the user is in the center of the menu
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_UP,), (2,))
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_DOWN,), (12,))
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_LEFT,), (6,))
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_RIGHT,), (8,))

gamestate.current_level = 5
# Verifies that arrow key navigation does what we expect while the user is on the left side of the menu
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_UP,), (0,))
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_DOWN,), (10,))
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_LEFT,), (9,))
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_RIGHT,), (6,))

gamestate.current_level = 2
# Verifies that arrow key navigation does what we expect while the user is on the top side of the menu
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_UP,), (12,))
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_DOWN,), (7,))
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_LEFT,), (1,))
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_RIGHT,), (3,))

gamestate.current_level = 14
# Verifies that arrow key navigation does what we expect while the user is on the bottom right corner of the menu
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_UP,), (9,))
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_DOWN,), (4,))
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_LEFT,), (13,))
perform_generic_unit_test(gamestate.find_new_level, (pygame.K_RIGHT,), (10,))

gamestate.unlocked_level = 8

# Verifies that arrow key navigation does what we expect while the user is in the center of the menu and the user
# hasn't unlocked all levels
gamestate.current_level = 7
up_event = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_UP)
gamestate.get_event(up_event)
perform_generic_unit_test(return_input_arguments, (gamestate.current_level,), (2,))

gamestate.current_level = 7
down_event = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_DOWN)
gamestate.get_event(down_event)
perform_generic_unit_test(return_input_arguments, (gamestate.current_level,), (7,))

gamestate.current_level = 7
left_event = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_LEFT)
gamestate.get_event(left_event)
perform_generic_unit_test(return_input_arguments, (gamestate.current_level,), (6,))

gamestate.current_level = 7
right_event = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_RIGHT)
gamestate.get_event(right_event)
perform_generic_unit_test(return_input_arguments, (gamestate.current_level,), (7,))

# Verifies that pressing a key other than an arrow key or space/escape doesn't change the current level
gamestate.current_level = 7
irrelevant_event = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_r)
gamestate.get_event(irrelevant_event)
perform_generic_unit_test(return_input_arguments, (gamestate.current_level,), (7,))



### GAME STATE CHANGE UNIT TESTS ###

# Verifies that pressing space will bring the user to the customization menu
gamestate = levels()
space_event = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_SPACE)
gamestate.get_event(space_event)
perform_generic_unit_test(return_input_arguments, (gamestate.done,), (True,))
perform_generic_unit_test(return_input_arguments, (gamestate.next_state,), ("customization",))

# Verifies that pressing escape will bring the user to the outer menu
gamestate = levels()
escape_event = pygame.event.Event(pygame.KEYDOWN, key = pygame.K_ESCAPE)
gamestate.get_event(escape_event)
perform_generic_unit_test(return_input_arguments, (gamestate.done,), (True,))
perform_generic_unit_test(return_input_arguments, (gamestate.next_state,), ("menu",))

# Verifies that quitting will quit the game
gamestate = levels()
quit_event = pygame.event.Event(pygame.QUIT)
gamestate.get_event(quit_event)
perform_generic_unit_test(return_input_arguments, (gamestate.quit,), (True,))


# For testing pygame display, simply run main and navigate to the level selection menu from
# the outer menu.

sys.exit()
