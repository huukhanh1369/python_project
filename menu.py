"""
Alien Invasion Main Menu - menu.py
Giao diện chọn chế độ chơi
"""

import pygame
import pygame.font


class MainMenu:
    """A class to display the main menu."""
    
    def __init__(self, screen, screen_rect):
        """Initialize menu attributes."""
        self.screen = screen
        self.screen_rect = screen_rect
        self.bg_color = (230, 230, 230)
        
        # Font settings
        self.title_font = pygame.font.SysFont(None, 72)
        self.button_font = pygame.font.SysFont(None, 48)
        self.text_color = (30, 30, 30)
        self.button_color = (0, 255, 0)
        self.button_hover_color = (0, 200, 0)
        
        # Create mode buttons
        self.create_buttons()
    
    def create_buttons(self):
        """Create game mode buttons."""
        button_width = 300
        button_height = 60
        
        # INFINITE MODE button
        self.infinite_rect = pygame.Rect(0, 0, button_width, button_height)
        self.infinite_rect.center = self.screen_rect.center
        self.infinite_rect.top = self.screen_rect.centery - 100
        
        # LIMITED MODE button
        self.limited_rect = pygame.Rect(0, 0, button_width, button_height)
        self.limited_rect.center = self.screen_rect.center
        self.limited_rect.top = self.screen_rect.centery
        
        # # CHALLENGE MODE button
        # self.challenge_rect = pygame.Rect(0, 0, button_width, button_height)
        # self.challenge_rect.center = self.screen_rect.center
        # self.challenge_rect.top = self.screen_rect.centery + 100
        
        # Render button texts
        self.infinite_text = self.button_font.render(
            "Infinite Mode", True, (255, 255, 255))
        self.infinite_text_rect = self.infinite_text.get_rect(
            center=self.infinite_rect.center)
        
        self.limited_text = self.button_font.render(
            "Limited Mode", True, (255, 255, 255))
        self.limited_text_rect = self.limited_text.get_rect(
            center=self.limited_rect.center)
        
        # self.challenge_text = self.button_font.render(
        #     "Challenge Mode", True, (255, 255, 255))
        # self.challenge_text_rect = self.challenge_text.get_rect(
        #     center=self.challenge_rect.center)
    
    def draw_menu(self, mouse_pos):
        """Draw the menu to the screen."""
        # Fill background
        self.screen.fill(self.bg_color)
        
        # Draw title
        title = self.title_font.render(
            "ALIEN INVASION", True, self.text_color)
        title_rect = title.get_rect()
        title_rect.center = self.screen_rect.center
        title_rect.top = 50
        self.screen.blit(title, title_rect)
        
        # Draw subtitle
        subtitle = self.button_font.render(
            "Choose Game Mode", True, self.text_color)
        subtitle_rect = subtitle.get_rect()
        subtitle_rect.center = self.screen_rect.center
        subtitle_rect.top = 150
        self.screen.blit(subtitle, subtitle_rect)
        
        # Draw buttons with hover effect
        self._draw_button(self.infinite_rect, self.infinite_text, 
                         self.infinite_text_rect, mouse_pos)
        self._draw_button(self.limited_rect, self.limited_text, 
                         self.limited_text_rect, mouse_pos)
        # self._draw_button(self.challenge_rect, self.challenge_text, 
        #                  self.challenge_text_rect, mouse_pos)
        
        pygame.display.flip()
    
    def _draw_button(self, rect, text, text_rect, mouse_pos):
        """Draw a single button with hover effect."""
        # Check if mouse is over button
        if rect.collidepoint(mouse_pos):
            color = self.button_hover_color
        else:
            color = self.button_color
        
        # Draw button
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, self.text_color, rect, 3)
        
        # Draw text
        self.screen.blit(text, text_rect)
    
    def check_mode_selected(self, mouse_pos):
        """Check which game mode was selected."""
        if self.infinite_rect.collidepoint(mouse_pos):
            return "infinite"
        elif self.limited_rect.collidepoint(mouse_pos):
            return "limited"
        # elif self.challenge_rect.collidepoint(mouse_pos):
        #     return "challenge"
        return None