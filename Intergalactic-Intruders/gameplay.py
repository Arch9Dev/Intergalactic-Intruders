import pygame
import constants


import pygame
import constants

def show_gameplay():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("GAMEPLAY")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if constants.BACK_BUTTON.collidepoint(event.pos):
                    pygame.display.set_caption("DIFFICULTY")
                    return

        screen.fill(constants.PURPLE)
        # Placeholder content
        placeholder_text = constants.FONT.render("Gameplay Placeholder", True, constants.BLACK)
        screen.blit(placeholder_text, (constants.SCREEN_WIDTH // 2 - 100, constants.SCREEN_HEIGHT // 2))


        # Render back button with border
        pygame.draw.rect(screen, constants.RED, constants.BACK_BUTTON)
        pygame.draw.rect(screen, constants.BLACK, constants.BACK_BUTTON, 2)  # Draw border
        back_text = constants.FONT.render("BACK", True, constants.BLACK)
        screen.blit(back_text, (constants.BACK_BUTTON.x + 20, constants.BACK_BUTTON.y + 10))
        
        
        
        pygame.display.update()
