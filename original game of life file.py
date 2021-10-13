import pygame
from random import *
import io
import os.path

if __name__=="__main__":
    
    w = 64
    h = 64
    z = 8
    
    loop = False
    borders = True
    
    fps=0
    
    pygame.init()
#     running = False
    bg = (100,100,100)
    white = (255,255,255)
    black = (0,0,0)
    
    window = pygame.display.set_mode((w*z,h*z))# , pygame.SHOWN
    window.fill(bg)
    
    clock = pygame.time.Clock()
    
    filename = ""
    
    
    
#     state = [[column%2 for column in range(h)] for row in range(w)]
#     state[0][0] = 1
#     state[w-1][0] = 1
    
    
#     state = [[0,0,0,0,0,0,0,0],
#              [0,0,1,0,0,0,0,0],
#              [1,0,1,0,0,0,0,0],
#              [0,1,1,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0],
#              [0,0,0,0,0,0,0,0]]
    
    
    def clearstate():
        return [[0 for column in range(h)] for row in range(w)]
    
    def randomstate():
        return [[randint(0,1) for column in range(h)] for row in range(w)]
    
    def filestate(f,state=None):
        name = str(f)
        if os.path.isfile(name):
            file = io.open(name)
            lines = eval(file.read())
            file.close()
            if type(lines)==list:
                if (False if [len(lines[y]) for y in range(len(lines))].count(h)!=w or len(lines)!=w else True): return lines
        elif state!=None: return state
        else: return None
    
    
    def minmax(minimum,maximum,value):
        return max(min(value,maximum),minimum)
    
    def get3(x,y,grid):
        neighbors = 0
        if loop:
            neighbors += grid[x%w][(y-1)%h]
            neighbors += grid[x%w][y%h]
            neighbors += grid[x%w][(y+1)%h]
        else:
            neighbors += grid[x][y-1] if -1<x<w and 0<y-1<h else 0
            neighbors += grid[x][y] if -1<x<w and 0<y<h else 0
            neighbors += grid[x][y+1] if -1<x<w and 0<y+1<h else 0
        return neighbors
        
    
    def getneighbors(x,y,grid):
        neighbors = 0
        neighbors += get3(x-1,y,grid)
        neighbors += get3(x,y,grid)
        neighbors += get3(x+1,y,grid)
        neighbors -= grid[x][y]==1
        return neighbors
    
        neighbors = grid[(x-1)%w][(y-1%h)]



    def updatecell(x,y,grid):
        neighbors = getneighbors(x,y,grid)
        if neighbors == 3: return 1
        elif neighbors == 2 and grid[x][y] == 1: return 1
        else: return 0
        
        pass
        #end
    
#     state = np.array(np.random.randint(low=0,high=2,size=(w,h)))
#     newstate = np.array(np.zeros((w,h)))
#     newstate = np.array([list(map(lambda x: x*2,state[i])) for i in range(w)])
    
    
#     state = [[0, 0, 0, 0],
#              [0, 1, 1, 1],
#              [0, 0, 0, 1],
#              [0, 0, 1, 0]]
    
#     getneighbors(1,3,state)
#     newstate = [[updatecell(x,y,state) for y in range(h)] for x in range(w)]
    
#     test = [[0, 0, 1, 0],
#             [0, 0, 0, 1],
#             [1, 0, 1, 1],
#             [1, 0, 1, 0]]
    
#     pygame.display.quit()
    
    
    
    
    
    state = clearstate()
    
    state = randomstate()
    
    state = filestate(filename,state)
    
    
    
    
    
    mainloop = True
    while mainloop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
#                 print("quit")
#                 pygame.display.quit()
                pygame.quit()
#                 exit()
                mainloop = False
        if not mainloop:
            break
        Alive=0
        ##rendering Cells
        if z>=3 and borders:
            for row in range(w):
                for column in range(h):
                    rect = pygame.Rect(row*z+1,column*z+1,z-1,z-1)
                    pygame.draw.rect(window, white if state[row][column]==1 else black, rect)#, border_radius=2
        else:
            for row in range(w):
                for column in range(h):
                    rect = pygame.Rect(row*z,column*z,z,z)
                    pygame.draw.rect(window, white if state[row][column]==1 else black, rect)#, border_radius=2
        
        
        #render loop(rendering the grid was about 2x slower)
#         for row in range(w):
#             for column in range(h):
#                 rect = pygame.Rect(row*z,column*z,z,z)
#                 pygame.draw.rect(window, white if state[row][column]==1 else black, rect)#, border_radius=2
#                 if z>=4 and borders:
#                     border = pygame.Rect(row*z,column*z,z,z)
#                     pygame.draw.rect(window, bg, border,1)
        
        
#         newstate = [[updatecell(x,y,state) for y in range(h)] for x in range(w)]
#         
#         state = newstate
        
        state = [[updatecell(x,y,state) for y in range(h)] for x in range(w)]
        
        pygame.display.update()
        clock.tick(fps)
    
    
    #pygame.rect(0,0,16,16)
    
    
    
    
    
