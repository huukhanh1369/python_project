"""
Alien Invasion Game Statistics - game_stats.py
Quản lý các thống kê của game (điểm, tàu, level, v.v.)
"""


class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        
        # High score should never be reset
        self.high_score = 0
        
        # Start Alien Invasion in an inactive state
        self.game_active = False
        
        # Track if player won (only in limited mode)
        self.game_won = False
        
        # Initialize the rest of the statistics
        self.reset_stats()
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        # Number of ships remaining
        self.ships_left = self.settings.ship_limit
        
        # Current score
        self.score = 0
        
        # Current level
        self.level = 1
        
        # Reset win flag
        self.game_won = False