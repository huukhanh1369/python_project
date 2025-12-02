"""
Alien Invasion Settings - settings.py
Quản lý tất cả các thiết lập của game
"""

from config import *


class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        
        # FPS
        self.fps = 60
        
        # Game mode
        self.game_mode = GAME_MODE
        self.max_level = MAX_LEVEL
        
        # Ship settings
        self.ship_limit = SHIPS_ALLOWED
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Alien settings
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = SPEEDUP_SCALE
        
        # How quickly the alien point values increase
        self.score_scale = SCORE_SCALE
        
        # Initialize dynamic settings
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # Ship speed
        self.ship_speed = 3.0
        
        # Bullet speed
        self.bullet_speed = 8.0
        
        # Alien speed
        self.alien_speed = 1.0
        
        # Fleet direction: 1 represents right; -1 represents left
        self.fleet_direction = 1
        
        # Alien point value
        self.alien_points = ALIEN_POINTS
    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)