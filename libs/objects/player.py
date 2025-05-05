from libs import tiles
import pygame

class Player:
    def __init__(self, sub_frame_count, frame_count, movement, pre_movement, x, y, last_movement, spritesheet):
        self.sub_frame_count = sub_frame_count
        self.frame_count = frame_count
        self.movement = movement
        self.pre_movement = pre_movement
        self.x = x
        self.y = y
        self.last_movement = last_movement
        self.player_spritesheet = spritesheet
        self.frame = self.player_spritesheet.get_tile_scalled(self.frame_count, (64,64))
        self.switch_frame = 5
        self.add_frame_count = 0
    def move(self, keys):
        self.pre_movement = self.movement
        self.movement = 0
        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.y -= 4
            self.movement = 1
            self.add_frame_count = 5
            self.switch_frame = 5
            self.last_movement = 1
            self.frame = self.player_spritesheet.get_tile_scalled(self.frame_count+self.add_frame_count, (64,64))
        elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.y += 4
            self.movement = 2
            self.add_frame_count = 0
            self.switch_frame = 5
            self.last_movement = 2
            self.frame = self.player_spritesheet.get_tile_scalled(self.frame_count+self.add_frame_count, (64,64))
        else:
            self.movement = 0
        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.x -= 4
            self.movement = 3
            self.last_movement = 3
            self.add_frame_count = 10
            self.switch_frame = 7
            self.frame = pygame.transform.flip(self.player_spritesheet.get_tile_scalled(self.frame_count+self.add_frame_count, (64,64)), True, False)
        elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.x += 4
            self.movement = 4
            self.add_frame_count = 10
            self.switch_frame = 7
            self.frame = self.player_spritesheet.get_tile_scalled(self.frame_count+self.add_frame_count, (64,64))
            self.last_movement = 4
        if self.pre_movement == self.movement and self.movement != 0:
            self.sub_frame_count += 1
            print(self.frame_count+self.add_frame_count, self.movement, self.pre_movement, self.sub_frame_count)
            if self.sub_frame_count == 4:
                self.frame_count += 1
                self.sub_frame_count = 0
            print(self.add_frame_count+self.switch_frame)
            if self.frame_count+self.add_frame_count >= self.add_frame_count+self.switch_frame:
                self.frame_count = 1
        else:
            self.frame_count = 0
            self.add_frame_count = 0
            self.switch_frame = 0
            self.frame = self.player_spritesheet.get_tile_scalled(self.frame_count, (64,64))
            print(self.frame_count+self.add_frame_count, self.movement, self.pre_movement, self.sub_frame_count)
            self.sub_frame_count = 0