from curses import*

zigzag = [["o",".",".","."],
          ["o",".",".","."],
          ["o",".",".","."],
          ["o","o","o","o"],
          [".",".",".","o"],
          [".",".",".","o"],
          [".",".",".","o"]]
          
square = [["o","o","o","o"],
          ["o",".",".","o"],
          ["o",".",".","o"],
          ["o",".",".","o"],
          ["o",".",".","o"],
          ["o",".",".","o"],
          ["o","o","o","o"]]

# точка фигуры  не может оказаться в стакане, если 
#  точка в стакане  равна "o" 
#  точка другой фигуры не равна "."
glass = [[".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","."]]
         
         # поле 17(x) на 16(y)
         # фигура 7(y) на 4(x)      

# создать алгоритм, чтобы цикл печатал элементы снизу фигуры 
def turn_the_figure (figure):
    new_figure = []
    # проходит по столбику фигуры
    for x in range(0, len(figure[0])):
        sub_array = []
        # проходит по горизонтали фигуры
        for y in range(0, len(figure)):
            sub_array.append(figure[y][x])      
        
        new_figure.append(sub_array[::-1])
        
    

#abcd -> dcba
    return new_figure       
        
         
         
def projection(glass, y, x, figure):
    #glass[2+0][4+0] = figure[0][0]
    #glass[2+0][4+1] = figure[0][1]
    #glass[2+1][4+0] = figure[1][0]
    #glass[y+1][x+1] = figure[1][1]
    #glass[y+2][x+0] = figure[2][0]
    #glass[y+2][x+1] = figure[2][1]
    
    
    for v in range(0, len(figure)):
       for h in range(0, len(figure[0])):
           if glass[y+v][x+h] != "o":
              glass[y+v][x+h] = figure[v][h]

    return glass
    
# сделать функц по проверке хода фигуры (возможен ли ход фигурой)    


# подумать о перевороте фигуры 
         
def print_figure (figure):
    fig_el = figure[0]
    for y in range(0, len(figure)):
       print()
       for x in range (0, len(fig_el)):
          print(figure[y][x],end="")
       
def is_move_possible(glass, figure, y, x):
    for v in range (0, len(figure)):
        for h in range(0, len(figure[0])):
            
            if y+v >= len(glass) and figure[v][h] == "o":
                return False 
            if x+h >= len(glass[0]) and figure[v][h] == "o":
                return False 
            if x+h < 0 and figure[v][h] == "o":
                return False 
                
            if glass[v+y][x+h] == "o" and figure[v][h] == "o":
                return False  
            
             
    return True 
           

def interface (glass, figure, y ,x):
    screen = initscr()
    try:
        screen.addstr( 0, 0, "Hello")
        print_field_interface(screen, glass, 5, 5)
    
        for i in range(0, len(glass)):
            copied_glass = copy_glass(glass)
            #projection(copied_glass, (y+i), x, figure)
            #screen.getch()
    
            key = screen.getch()
            if key == 97 :
                #a - двигай влево
                projection(copied_glass, y, (x-i), figure)
            elif key == 100:
                projection(copied_glass, y, (x+i), figure)
                #d -  двигай вправо
            elif key == 115:
                projection(copied_glass, (y+1), x, figure)
                #s - двигай вниз
            print_field_interface(screen, copied_glass, 5, 5)
    finally:
        endwin()            

def print_field_interface (screen, glass, y, x):
    for v in range(0, len(glass)):
        for h in range(0, len(glass[0])):
            screen.addstr((y+v), (x+h), glass[v][h])
            
            
            
    
# написать фунцкию для копирования массива 
def copy_glass (glass):
    copy = []
    for y in range(0, len(glass)):
        sub_array = []
        for x in range(0, len(glass[0])):
            sub_array.append(glass[y][x])
        
        copy.append(sub_array)
    
    return copy 
    


#print_figure(projection(glass, 4, 6, zigzag))
##next_move = print_figure(projection(glass, 4, 6, zigzag))
next_move = projection(glass, 2, 4, zigzag)
next_move
#print_figure(projection(glass, 0, 0, zigzag))
print()
print_figure(zigzag)
print()
print("(glass[0])x-",len(glass[0]), "(glass)y-", len(glass))
print()
interface(glass, zigzag, 0, 0)
print(len(zigzag), len(zigzag[0]))
print()
#print_figure(copy_glass(glass))



#print(is_move_possible(glass, zigzag, 1, 5))
#next_move = print_figure(projection(glass, 1, 5, zigzag))
#print()
#print(len(zigzag[0]))
#print()

##zigzag[0][0]

