import pygame
import sys
import os
from Quang import *
import time

class GUI:
    def __init__(self, width, height):
        pygame.init()

        self.WIDTH = width
        self.HEIGHT = height

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Hide and Seek')

        current_dir = os.path.dirname(os.path.abspath(__file__))
        directory = "IMAGES"
        background_path = os.path.join(current_dir, directory)
        background_path = os.path.join(background_path, "background.jpg")
        self.background = pygame.image.load(background_path)
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        self.LIGHT_PURPLE = (255, 153, 255)
        self.YELLOW = (255, 255, 0)
        self.BLUE = (0, 0, 255)
        self.RED = (255, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.HOVER_COLOR = (150, 150, 150)
        self.BUTTON_WIDTH = 150
        self.BUTTON_HEIGHT = 50
        self.button_spacing = 40
        self.button_x = (self.WIDTH - self.BUTTON_WIDTH) // 2
        self.button_y_start = (self.HEIGHT - (4 * self.BUTTON_HEIGHT + 3 * self.button_spacing)) // 2
        self.level = 0

    def read_matrix(self, file_txt):
        with open(file_txt, 'r') as file:
            HEIGHT, WIDTH = map(int, file.readline().split())
            matrix = []
            for _ in range(HEIGHT):
                row = list(map(int, file.readline().split()))
                matrix.append(row)

            remaining_lines = []
            for line in file:
                remaining_lines.append(list(map(int, line.strip().split())))
        
        for row in range(len(remaining_lines)):
            for i in range(remaining_lines[row][0], remaining_lines[row][2] + 1):
                for j in range(remaining_lines[row][1], remaining_lines[row][3] + 1):
                    matrix[i][j] = 1
        return matrix, HEIGHT, WIDTH

    def draw_button(self, x, y, text, WIDTH, HEIGHT, hover=False):
        color = self.HOVER_COLOR if hover else self.BLACK
        pygame.draw.rect(self.screen, color, (x, y, WIDTH, HEIGHT))
        font = pygame.font.Font(None, 36)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect(center=(x + WIDTH // 2, y + HEIGHT // 2))
        self.screen.blit(text_surface, text_rect)


    def draw_matrix(self, matrix, HEIGHT, WIDTH, start_x, start_y, end_x, end_y):
        cell_size_height = (end_y - start_y) // HEIGHT
        cell_size_width = (end_x - start_x) // WIDTH
        if cell_size_height < cell_size_width:
            cell_size = cell_size_height
        else:
            cell_size = cell_size_width

        pygame.draw.rect(self.screen, self.BLACK, (start_x - 1, start_y - 1, WIDTH * cell_size + 2, HEIGHT * cell_size + 2), 1)
        for i in range(HEIGHT):
            for j in range(WIDTH):
                x = start_x + j * cell_size
                y = start_y + i * cell_size
                cell = matrix[i][j]

                if cell % 20 == 3:
                    current_dir = os.path.dirname(os.path.abspath(__file__))
                    directory = "IMAGES"
                    image_path = os.path.join(current_dir, directory)
                    image_path = os.path.join(image_path, "seeker.png")
                    image = pygame.image.load(image_path)
                    image = pygame.transform.scale(image, (cell_size, cell_size))
                    # Blit image onto screen
                    self.screen.blit(image, (x, y))
                elif cell % 20 == 2:
                    current_dir = os.path.dirname(os.path.abspath(__file__))
                    directory = "IMAGES"
                    image_path = os.path.join(current_dir, directory)
                    image_path = os.path.join(image_path, "hider.jpg")
                    image = pygame.image.load(image_path)
                    image = pygame.transform.scale(image, (cell_size, cell_size))
                    # Blit image onto screen
                    self.screen.blit(image, (x, y))
                else:
                    if cell == 0:
                        color = self.WHITE
                    elif cell == -1:
                        color = self.GRAY
                    elif cell == 1:
                        color = self.BLACK
                    elif cell == 5:
                        color = self.LIGHT_PURPLE
                    elif cell == 19 or cell == 20:
                        color = self.YELLOW
                    pygame.draw.rect(self.screen, color, (x, y, cell_size, cell_size))
        pygame.display.flip()

    def draw_note(self, start_x, start_y, end_x, end_y):
        total_height = end_y - start_y
        total_width = end_x - start_x

        pygame.draw.rect(self.screen, self.BLACK, (start_x - 1, start_y - 1, total_width + 2, total_height + 2), 1)
        pygame.draw.rect(self.screen, self.WHITE, (start_x, start_y, total_width, total_height))

        font = pygame.font.Font(None, 35)
        text_surface = pygame.font.Font(None, 50).render("Score:", True, self.BLACK)
        text_rect = text_surface.get_rect(left=start_x + 25, top=start_y + 60)
        self.screen.blit(text_surface, text_rect)


        text_lines = [": Seeker", ": Hider", ": Obstacle", ": Seeker's Vision", ": Hider's Vision"]
        line_spacing = 60 

        # Draw each line of text
        for i, line in enumerate(text_lines):
            text_surface = font.render(line, True, self.BLACK)
            # Calculate the position to center the text horizontally
            text_rect = text_surface.get_rect(left = start_x + 60, top = start_y + total_width // 2 - 10 + i * line_spacing + line_spacing // 2)
            self.screen.blit(text_surface, text_rect)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        directory = "IMAGES"
        path = os.path.join(current_dir, directory)
        seeker_path = os.path.join(path, "seeker.png")
        seeker = pygame.image.load(seeker_path)
        seeker = pygame.transform.scale(seeker, (40, 40))
        self.screen.blit(seeker, (start_x + 10, start_y + 10 + total_width // 2))

        hider_path = os.path.join(path, "hider.jpg")
        hider = pygame.image.load(hider_path)
        hider = pygame.transform.scale(hider, (40, 40))
        self.screen.blit(hider, (start_x + 10, start_y + 10 + total_width // 2 + line_spacing))

        pygame.draw.rect(self.screen, self.BLACK, (start_x + 10, start_y + 10 + total_width // 2 + 2 * line_spacing, 40, 40))
        pygame.draw.rect(self.screen, self.YELLOW, (start_x + 10, start_y + 10 + total_width // 2 + 3 * line_spacing, 40, 40))
        pygame.draw.rect(self.screen, self.RED, (start_x + 10, start_y + 10 + total_width // 2 + 4 * line_spacing, 40, 40))


        pygame.display.flip()

    def solve_screen(self, map_matrix : Map):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            directory = "IMAGES"
            background_path = os.path.join(current_dir, directory)
            background_path = os.path.join(background_path, "background.jpg")
            self.background = pygame.image.load(background_path)
            self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
            self.screen.blit(self.background, (0, 0))
            partition = self.WIDTH // 16
            # Calculate button dimensions and positions
            if self.level == 1:
                font = pygame.font.Font(None, 50)
                text_surface = font.render("Level 1", True, self.BLACK)
                text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 50))
                self.screen.blit(text_surface, text_rect)

            elif self.level == 2:
                font = pygame.font.Font(None, 50)
                text_surface = font.render("Level 2", True, self.BLACK)
                text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 50))
                self.screen.blit(text_surface, text_rect)

            elif self.level == 3:
                font = pygame.font.Font(None, 50)
                text_surface = font.render("Level 3", True, self.BLACK)
                text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 50))
                self.screen.blit(text_surface, text_rect)

            map_matrix.getVision()
            start_x_matrix = partition * 0.5
            start_y_matrix = partition * 1.5
            end_x_matrix = partition * 11.5
            end_y_matrix = partition * 8.5
            self.draw_matrix(map_matrix.board, map_matrix.row, map_matrix.col, start_x_matrix, start_y_matrix, end_x_matrix, end_y_matrix)

            start_x_note = partition * 12
            start_y_note = partition * 1.5
            end_x_note = partition * 15.5
            end_y_note = partition * 8.5
            self.draw_note(start_x_note, start_y_note, end_x_note, end_y_note)

            running = True
            while running:
                button_y = end_y_note - 70
                button_x = start_x_note + 90
                mouse_x, mouse_y = pygame.mouse.get_pos()
                button_rect = pygame.Rect(button_x, button_y , 100, 50)
                hover = button_rect.collidepoint(mouse_x, mouse_y)
                self.draw_button(button_x, button_y, "BEGIN", 100, 50, hover=hover)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        button_rect = pygame.Rect(button_x, button_y, 80, 50)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            running = False
                pygame.display.flip()
            
            running = True
            hiderPos = []
            path = []
            while running:
                goalPos = map_matrix.findMostValueCell()
                path = map_matrix.A_Star(goalPos[0], goalPos[1])
                # if path != None:
                # chắc chắn có path nên khỏi check path == None
                for matrix in path:
                    if matrix.checkHider(hiderPos):
                        self.draw_matrix(matrix.board, map_matrix.row, map_matrix.col, start_x_matrix, start_y_matrix, end_x_matrix, end_y_matrix)
                        time.sleep(0.2)
                        map_matrix = matrix
                        map_matrix.parent = None
                        break
                    self.draw_matrix(matrix.board, map_matrix.row, map_matrix.col, start_x_matrix, start_y_matrix, end_x_matrix, end_y_matrix)
                    time.sleep(0.2)
                    
                
                if hiderPos != []:
                    path = map_matrix.A_Star(hiderPos[0], hiderPos[1])
                    for matrix in path:
                        self.draw_matrix(matrix.board, map_matrix.row, map_matrix.col, start_x_matrix, start_y_matrix, end_x_matrix, end_y_matrix)
                        time.sleep(0.2) 
                    hiderPos.clear()
                    
                
                map_matrix = path[-1]
                map_matrix.parent = None

                
                # if hiderPos != []:
                #     path.clear()
                #     path = map_matrix.A_Star(hiderPos[0], hiderPos[1])
                #     print(path)
                #     for matrix in path:
                #         self.draw_matrix(matrix.board, map_matrix.row, map_matrix.col, start_x_matrix, start_y_matrix, end_x_matrix, end_y_matrix)
                #         time.sleep(0.2)
                #     map_matrix = path[-1]
                #     map_matrix.parent = None
                #     hiderPos.clear()


                        
                remaining_hiders = 0
                for i in range(map_matrix.row):
                    for j in range(map_matrix.col):
                        if map_matrix.board[i][j] % 20 == 2:
                            remaining_hiders += 1
                if remaining_hiders == 0:
                    running = False
                    break
                pygame.display.flip()

            running = True
            # running = True
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                pygame.display.flip()

    def level_screen(self):
        directory = "MAP"
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, directory)
        if self.level == 1:
            file_path = os.path.join(file_path, "Level1")
        elif self.level == 2:
            file_path = os.path.join(file_path, "Level2")
        elif self.level == 3:
            file_path = os.path.join(file_path, "Level3")
        files = [file for file in os.listdir(file_path) if file.endswith('.txt')]
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        directory = "IMAGES"
        background_path = os.path.join(current_dir, directory)
        background_path = os.path.join(background_path, "background.jpg")
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
        self.screen.blit(self.background, (0, 0))
        
        # Calculate button dimensions and positions
        button_width = 200
        button_height = 50
        button_spacing = 20
        num_buttons = len(files)
        total_height = num_buttons * button_height + (num_buttons - 1) * button_spacing
        start_y = (self.HEIGHT - total_height) // 2

        # Draw button based on option number
        if self.level == 1:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("Level 1", True, self.BLACK)
            text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 50))
            self.screen.blit(text_surface, text_rect)

        elif self.level == 2:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("Level 2", True, self.BLACK)
            text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 50))
            self.screen.blit(text_surface, text_rect)

        elif self.level == 3:
            font = pygame.font.Font(None, 50)
            text_surface = font.render("Level 3", True, self.BLACK)
            text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 50))
            self.screen.blit(text_surface, text_rect)

        elif self.level == 4:
                font = pygame.font.Font(None, 50)
                text_surface = font.render("Level 4", True, self.BLACK)
                text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 50))
                self.screen.blit(text_surface, text_rect)
                picture_path = os.path.join(current_dir, directory)
                picture_path = os.path.join(picture_path, "give up.jpg")
                picture = pygame.image.load(picture_path)
                partition = self.WIDTH // 16  
                picture = pygame.transform.scale(picture, (partition * 6 * 1.5, partition * 6))
                self.screen.blit(picture, (partition * 3.5, partition * 1.5))

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                    pygame.display.flip()

        running = True
        while running:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i, filename in enumerate(files):
                button_y = start_y + i * (button_height + button_spacing)
                button_rect = pygame.Rect(self.button_x, button_y, button_width, button_height)
                hover = button_rect.collidepoint(mouse_x, mouse_y)
                self.draw_button(self.button_x, button_y, filename, self.BUTTON_WIDTH, self.BUTTON_HEIGHT, hover=hover)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for i in range(num_buttons):
                        button_x = self.button_x
                        button_y = start_y + i * (button_height + button_spacing)
                        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            filepath = os.path.join(file_path, files[i])
                            matrix, HEIGHT, WIDTH = self.read_matrix(filepath)
                            return matrix, HEIGHT, WIDTH
            pygame.display.flip()

    def run(self):
        running = True
        font = pygame.font.Font(None, 80)
        text_surface = font.render("Hide and Seek", True, self.BLACK)
        text_rect = text_surface.get_rect(center=(self.WIDTH // 2, 100))
        self.screen.blit(text_surface, text_rect)

        while running:
            # Check current screen
            if self.level == 0:
                # Main screen with buttons
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for i in range(4):
                    button_y = self.button_y_start + i * (self.BUTTON_HEIGHT + self.button_spacing)
                    button_rect = pygame.Rect(self.button_x, button_y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
                    hover = button_rect.collidepoint(mouse_x, mouse_y)
                    self.draw_button(self.button_x, button_y, f"Level {i+1}", self.BUTTON_WIDTH, self.BUTTON_HEIGHT, hover=hover)
            else:
                # Option screen
                break

            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(4):
                        button_y = self.button_y_start + i * (self.BUTTON_HEIGHT + self.button_spacing)
                        button_rect = pygame.Rect(self.button_x, button_y, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
                        if button_rect.collidepoint(event.pos):
                            self.level = i + 1

            pygame.display.flip()
        matrix, height, width = self.level_screen()
        map_matrix = Map(matrix, height, width, 0, None, 0)
        self.solve_screen(map_matrix)


        pygame.quit()
        sys.exit()

# Usage example:
if __name__ == "__main__":
    gui = GUI(1280, 720)
    gui.run()
