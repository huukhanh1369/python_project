import pygame
import os

def create_game_images():
    # Tạo thư mục images nếu chưa có
    if not os.path.exists('images'):
        os.makedirs('images')

    pygame.init()

    # --- 1. TẠO ẢNH TÀU (SHIP) ---
    # Kích thước nhỏ gọn: 60x50
    ship_surf = pygame.Surface((60, 50), pygame.SRCALPHA)
    # Vẽ hình tam giác màu xanh đại diện cho tàu
    pygame.draw.polygon(ship_surf, (0, 100, 255), [(30, 0), (60, 50), (0, 50)])
    pygame.image.save(ship_surf, 'images/ship.png')
    print("Đã tạo: images/ship.png")

    # --- 2. TẠO ẢNH QUÁI VẬT (ALIEN) ---
    # Kích thước nhỏ gọn: 60x50
    alien_surf = pygame.Surface((60, 50), pygame.SRCALPHA)
    # Vẽ hình bầu dục màu đỏ đại diện cho quái vật
    pygame.draw.ellipse(alien_surf, (255, 0, 0), [0, 0, 60, 50])
    # Vẽ mắt cho ngầu
    pygame.draw.circle(alien_surf, (255, 255, 0), (20, 20), 5)
    pygame.draw.circle(alien_surf, (255, 255, 0), (40, 20), 5)
    pygame.image.save(alien_surf, 'images/alien.png')
    print("Đã tạo: images/alien.png")

    print("\nHOÀN TẤT! Bây giờ bạn hãy chạy lại file main.py")

if __name__ == '__main__':
    create_game_images()