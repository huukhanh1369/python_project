"""
Alien Invasion Game Configuration - config.py
Cấu hình chế độ chơi
"""

# ===== CHỌN CHỈ MỘT CÁI =====
# Để None để hiển thị menu chọn
GAME_MODE = None

# Hoặc chọn trực tiếp:
# GAME_MODE = "infinite"   # Chơi vô tận
# GAME_MODE = "limited"    # Chế độ giới hạn (10 level)
# GAME_MODE = "challenge"  # Chế độ thử thách

# ===== CẤU HÌNH CHI TIẾT =====
MAX_LEVEL = 10
SHIPS_ALLOWED = 3
SPEEDUP_SCALE = 1.3
SCORE_SCALE = 1.5
ALIEN_POINTS = 50