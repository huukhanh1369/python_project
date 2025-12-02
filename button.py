"""
Alien Invasion Button - button.py
Tạo nút Play để bắt đầu/chơi lại game
"""

import pygame.font


class Button:
    """A class to create a button for the game."""
    
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # Green
        self.text_color = (255, 255, 255)  # White
        
        # Set up the font for rendering text
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button's rect object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # The button message needs to be prepped only once
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        # Render the text message
        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        
        # Get the rect of the message and center it on the button
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw blank button and then draw message."""
        # Draw the rectangular button
        self.screen.fill(self.button_color, self.rect)
        
        # Draw the text message on the button
        self.screen.blit(self.msg_image, self.msg_image_rect)