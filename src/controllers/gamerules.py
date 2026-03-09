

Board
CurrentBusinessman
Cubes
Cell

def try_make_move(self):

   points = self.__cubes.throw()

   current_position = self.__current_businessman.get_position()

   new_position = current_position + points

   if new_position > Board.MAX_POSITION:
       # дать кеш игроку
       new_position = new_position % Board.MAX_POSITION
       cell = self.__board.get_cell_by_position(new_position)  # запрос клетки у поля
       cell.land(self.__current_businessman) # клетка на тебя встали
