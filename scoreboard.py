"""
Alien Invasion Scoreboard - scoreboard.py
Lớp quản lý hiển thị điểm, level, số tàu còn lại
"""

import pygame.font
from pygame.sprite import Group

from ship import Ship


class Scoreboard:
    """A class to report scoring information."""
    
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.large_font = pygame.font.SysFont(None, 72)
        
        # Prepare the initial score images
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.prep_game_over_text()
        self.prep_win_text()
    
    def prep_score(self):
        """Turn the score into a rendered image."""
        # Round score to nearest 10
        rounded_score = round(self.stats.score, -1)
        
        # Format score with comma separators
        score_str = "{:,}".format(rounded_score)
        
        # Render the score image
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)
        
        # Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        # Round high score to nearest 10
        high_score = round(self.stats.high_score, -1)
        
        # Format high score with comma separators
        high_score_str = "{:,}".format(high_score)
        
        # Render the high score image
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)
        
        # Center the high score at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    
    def prep_level(self):
        """Turn the level into a rendered image."""
        # Convert level to string
        level_str = str(self.stats.level)
        
        # Render the level image
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color)
        
        # Position the level below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        """Show how many ships are left."""
        # Create an empty group for ships
        self.ships = Group()
        
        # Create ship images for each ship remaining
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            
            # Position ships in the upper-left corner
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            
            # Add ship to the group
            self.ships.add(ship)
    
    def prep_game_over_text(self):
        """Prepare the game over text."""
        # Game Over text
        game_over_str = "GAME OVER"
        self.game_over_image = self.large_font.render(
            game_over_str, True, (255, 0, 0), self.settings.bg_color)
        self.game_over_rect = self.game_over_image.get_rect()
        self.game_over_rect.center = self.screen_rect.center
        self.game_over_rect.top = self.screen_rect.top + 50
    
    def prep_win_text(self):
        """Prepare the win text for limited mode."""
        # Victory text
        victory_str = "🎉 YOU WIN! 🎉"
        self.victory_image = self.large_font.render(
            victory_str, True, (0, 200, 0), self.settings.bg_color)
        self.victory_rect = self.victory_image.get_rect()
        self.victory_rect.center = self.screen_rect.center
        self.victory_rect.top = self.screen_rect.top + 50
        
        # Final score text
        final_score_str = f"Final Score: {int(self.stats.score):,}"
        self.final_score_image = self.font.render(
            final_score_str, True, self.text_color, self.settings.bg_color)
        self.final_score_rect = self.final_score_image.get_rect()
        self.final_score_rect.center = self.screen_rect.center
        self.final_score_rect.top = self.victory_rect.bottom + 40
    
    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        # Draw current score at top right
        self.screen.blit(self.score_image, self.score_rect)
        
        # Draw high score at top center
        self.screen.blit(self.high_score_image, self.high_score_rect)
        
        # Draw level below score
        self.screen.blit(self.level_image, self.level_rect)
        
        # Draw ships in upper-left corner
        self.ships.draw(self.screen)
    
    def show_game_over(self):
        """Display game over or victory screen."""
        # Update final score mỗi lần gọi
        final_score_str = f"Final Score: {int(self.stats.score):,}"
        self.final_score_image = self.font.render(
            final_score_str, True, self.text_color, self.settings.bg_color)
        self.final_score_rect = self.final_score_image.get_rect()
        self.final_score_rect.center = self.screen_rect.center
        
        if self.stats.game_won:
            # Show victory screen
            self.final_score_rect.top = self.victory_rect.bottom + 40
            self.screen.blit(self.victory_image, self.victory_rect)
            self.screen.blit(self.final_score_image, self.final_score_rect)
        else:
            # Show game over screen
            self.final_score_rect.top = self.game_over_rect.bottom + 40
            self.screen.blit(self.game_over_image, self.game_over_rect)
            self.screen.blit(self.final_score_image, self.final_score_rect)