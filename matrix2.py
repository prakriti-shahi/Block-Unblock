    # Puzzle 2
tim, moves,points = 0,0,0
def puzzle2():
    #importing the modules
    import pygame
    import sys
    import time
    # initialising the interface and screen
    pygame.init()
    pygame.mixer.music.load("E:/Prot/School stuff grade 12/Computer Science/Project/Library/ES_Wear Me Out (Instrumental Version) - Gamma Skies.mp3")
    win_sound=pygame.mixer.Sound("Multiple-FireWorks-with-Whistling (mp3cut.net).mp3")
    screen = pygame.display.set_mode((700, 700))
    pygame.mixer.music.play(-1)
    #setting some variables
    global moves
    x1=2    
    y1=282
    
    cod={'rect2':[72, 72, 208, 68], 'rect3':[72, 142, 208, 68],'rect4':[352, 2, 348, 68],'rect5':[352, 72, 68, 348],'rect6':[422, 72, 68, 348],'rect7':[492, 72, 68, 348],'rect8':[72, 422, 68, 208],'rect9':[562, 352, 68, 208],'rect10':[212, 422, 348, 68], 'rect11':[72, 632, 348, 68], 'rect12':[562, 562, 68, 138]} 
    codog={'rect2':[72, 72, 208, 68], 'rect3':[72, 142, 208, 68],'rect4':[352, 2, 348, 68],'rect5':[352, 72, 68, 348],'rect6':[422, 72, 68, 348],'rect7':[492, 72, 68, 348],'rect8':[72, 422, 68, 208],'rect9':[562, 352, 68, 208],'rect10':[212, 422, 348, 68], 'rect11':[72, 632, 348, 68], 'rect12':[562, 562, 68, 138]} 
    vel=70 #you don't need to change the value of this
    x = 0
    y = 0
    run=True

    pygame.draw.rect(screen, (255,215,0), [72, 72, 208, 68]) #2
    pygame.draw.rect(screen, (255,215,0), [72, 142, 208, 68]) #3
    pygame.draw.rect(screen, (255,215,0), [352, 2, 348, 68]) #4
    pygame.draw.rect(screen, (255,215,0), [352, 72, 68, 348]) #5 
    pygame.draw.rect(screen, (255,215,0), [422, 72, 68, 348]) #6 
    pygame.draw.rect(screen, (255,215,0), [492, 72, 68, 348]) #7 
    pygame.draw.rect(screen, (255,215,0), [72, 422, 68, 208]) #8 
    pygame.draw.rect(screen, (255,215,0), [562, 352, 68, 208]) #9 
    pygame.draw.rect(screen, (255,215,0), [212, 422, 348, 68]) #10 
    pygame.draw.rect(screen, (255,215,0), [72, 632, 348, 68]) #11
    pygame.draw.rect(screen, (255,215,0), [562, 562, 68, 138]) #12

    #main block
    pygame.draw.rect(screen, (255,174,201), [x1, y1, 208, 68])   #[x,y,width,length]
    x1n=x1
    y1n=y1
    c1=()

    while run:
        for event in pygame.event.get():
            #for main block
            c=()
            keys=pygame.key.get_pressed()
            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
            c = screen.get_at((x,y)) #getting position where clicked 
            
            if c == ((255,174,201,255)):
                if keys[pygame.K_RIGHT] and x1n+208<700:
                    c1=screen.get_at((x1n+230, y1n+20))
                    if c1==(0,0,0,255):
                        moves += 1
                        x1n+=vel
                        pygame.draw.rect(screen, (255,174,201),[x1n,y1n,208,68])
                        pygame.draw.rect (screen, (0,0,0),[x1n-70,y1,70,70])
                        x += vel
                if keys[pygame.K_LEFT] and x1n>2:
                    c1= screen.get_at((x1n-20, y1n))
                    if c1==(0,0,0,255):
                        moves += 1
                        x1n-=vel
                        pygame.draw.rect(screen, (255,174,201),[x1n,y1n,208,68])
                        pygame.draw.rect(screen, (0,0,0),[x1n+210,y1,70,70])
                        x -= vel
                if x1n+208 == 700:
                    pygame.draw.rect(screen, (255,255,255),[492,282,208,68])
                    global tim
                    tim = time.perf_counter()
                    global points
                    if moves <=100 and tim <= 300:
                        points = (100 - moves) + ((300-tim)/2)
                    stats()
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(win_sound)

                    run = False             
                          
            #for all other blocks       
            if c == ((255,215,0,255)):
                for i in cod:
                    if (cod[i][0]<=int(x)) and (int(x)<=(cod[i][0]+cod[i][2])) and (cod[i][1]<=int(y)) and (int(y)<=(cod[i][1]+cod[i][3])):
                        r=i
                if cod[r][2]<cod[r][3]:
                    #for vertical blocks
                    if keys[pygame.K_UP] and cod[r][1]>2:
                        c1=screen.get_at((cod[r][0], cod[r][1]-20))
                        if c1==(0,0,0,255):
                            moves += 1
                            cod[r][1]-=vel
                            pygame.draw.rect(screen,(255,215,0),[cod[r][0],cod[r][1],cod[r][2],cod[r][3]])
                            pygame.draw.rect (screen, (0,0,0),[cod[r][0],cod[r][1]+cod[r][3],70,70])
                            y -= vel
                    if keys[pygame.K_DOWN] and cod[r][1]+cod[r][3]<698:
                        c1= screen.get_at((cod[r][0], cod[r][1]+cod[r][3]+20))
                        if c1==(0,0,0,255):
                            moves += 1
                            cod[r][1]+=vel
                            pygame.draw.rect(screen, (255,215,0),[cod[r][0],cod[r][1],cod[r][2],cod[r][3]])
                            pygame.draw.rect(screen, (0,0,0),[cod[r][0],cod[r][1]-70,70,70])
                            y += vel
                            
                else:
                    #for horizontal blocks
                    if keys[pygame.K_RIGHT] and cod[r][0]+cod[r][2]<698:
                        c1=screen.get_at((cod[r][0]+cod[r][2]+20,cod[r][1]))
                        if c1==(0,0,0,255):
                            moves += 1
                            cod[r][0]+=vel
                            pygame.draw.rect(screen, (255,215,0),[cod[r][0],cod[r][1],cod[r][2],cod[r][3]])
                            pygame.draw.rect (screen, (0,0,0),[cod[r][0]-70,cod[r][1],70,70])
                            x += vel
                    if keys[pygame.K_LEFT] and cod[r][0]>2:
                        c1= screen.get_at((cod[r][0]-20, cod[r][1]))
                        if c1==(0,0,0,255):
                            moves += 1
                            cod[r][0]-=vel
                            pygame.draw.rect(screen, (255,215,0),[cod[r][0],cod[r][1],cod[r][2],cod[r][3]])
                            pygame.draw.rect(screen, (0,0,0),[cod[r][0]+cod[r][2],cod[r][1],70,70])
                            x -= vel
                   
        #to quit the game
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        pygame.display.flip()

def stats():
    return ("No. of moves = ",moves,'\n',"Time taken: ", round(tim,2),'\n', "No. of points: ", round(points,0))
    

        

