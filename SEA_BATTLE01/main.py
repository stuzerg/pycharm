from random import choice, randint
import time


def get_cellboard_by_DOTobj(brd_name_array,
                            dot_):  # возвращает объект dot, если находится копия dot_ внутри brd_name_array
    try:
        i = brd_name_array.index(dot_)
        result = brd_name_array[i]
        return result
    except:
        return False


class PLAYER:
    def __init__(self, own_board, enemy_board):
        self.shot_list = []
        self.key_inp = ''
        self.own_board = own_board
        self.enemy_board = enemy_board
        self.current_shot = None
        self.nickname = ''
        self.enemy_fleet = 7   #все корабли
        self.lucky_shot = False
        pass

    def mov(self):
        cell_ = get_cellboard_by_DOTobj(self.enemy_board.array, self.current_shot)
        self.lucky_shot = False
        if not cell_:
            self.message = "---> ПРОМАХ! <-------------------------------- (переход хода)"
            self.enemy_board.field[self.current_shot.x][self.current_shot.y] = self.current_shot.status = '.'
            self.enemy_board.array.append(self.current_shot)
            #print(list(self.enemy_board.array))
        else:
            cell_.status == "V"
            le = (len(self.enemy_board.vessels_list))
            for i_ in range(0, le):
                if self.current_shot in self.enemy_board.vessels_list[i_].dotsarray:
                    ship_ = self.enemy_board.vessels_list[i_]
                    ship_.hp -= 1
                    self.message = "---> ЗАФИКСИРОВАНО ПОПАДАНИЕ! <-----> продолжайте стрелять"
                    self.lucky_shot = True
                    self.enemy_board.field[cell_.x][cell_.y] = cell_.status = 'I'
                    if ship_.hp == 0:
                        contour = OutLiner(ship_)
                        for a in ship_.dotsarray:
                            self.enemy_board.field[a.x][a.y] = a.status = 'X'

                        self.message = "---> НА ДНЕ! <-----"
                        self.enemy_fleet -= 1
                        for _ in contour.abrise:
                            if _ not in self.enemy_board.array:
                                self.enemy_board.field[_.x][_.y] = _.staus = '.'

                                self.enemy_board.array.append(_)

        self.enemy_board.mssg = self.message
        if not self.enemy_fleet:
            self.enemy_board.screen()
            print("Поздравляем, игра окончена! Победил ", self.nickname)
            raise OutOfRange("end of game")
        self.enemy_board.screen()
        #print('array =', len(self.enemy_board.array), "vessels =", len(self.enemy_board.vessels_list))

    def AskingShootin(self):
        while True:
            inp_str = input(' введите координаты выстрела '
                            'в формате строка столбец ')
            key_inp = ''
            for _ in inp_str:
                if _.isdigit():
                    key_inp += _
            if len(key_inp) == 2:
                self.key_inp = (int(key_inp[0]) - 1, int(key_inp[1]) - 1)
                try:
                    self.current_shot = dot(self.key_inp[0], self.key_inp[1])
                except:
                    print('очень далеко, чуть в МКС не попали')
                else:
                    if self.current_shot in self.enemy_board.array \
                            and (
                            get_cellboard_by_DOTobj(self.enemy_board.array, self.current_shot).status not in ['V']):
                        print("не надо опять сюда стрелять",
                              get_cellboard_by_DOTobj(self.enemy_board.array, self.current_shot).status)
                    else:
                        break
            else:
                print('ACHTUNG! Вводите, пожалуйста, всего лишь пару чисел от 1 до 6')


class human(PLAYER):
    # def __init__(self):
    #  ##self.asking()
    pass


class AI(PLAYER):

    def AskingShootin(self):
        print("AI прицеливается ...... ¯\_[-_-] _/¯   ", end='\b')
        time.sleep(1)
        for _ in range(9, 0, -1):
            print(_, '..  ', end='\b')
            time.sleep(.1)
        print(' Выстрел из орудия главного калибра !!')
        time.sleep(1)

        while True:
            xx = randint(0, 5)
            yy = randint(0, 5)
            self.key_inp = (xx, yy)
            self.current_shot = dot(xx, yy)

            if self.current_shot in self.enemy_board.array \
                    and (get_cellboard_by_DOTobj(self.enemy_board.array, self.current_shot).status not in ['V']):
                pass
                # print("не надо опять сюда стрелять", get_cellboard_by_DOTobj(self.enemy_board.array, self.current_shot).status)
            else:
                break


def DotArrayComparator(A, B):  ## функция сравнения списков с объектами dot, есть ли элементы из А в В
    for i in A:
        if i in B:
            return True


class BOARD:

    def __init__(self):
        self.array = []
        self.vessels_list = []
        self.hide_ships = False
        self.field = []
        self.mssg = ''

    def Vessel_Birth(self, vessel_length=3):  # ищет позицию и азимут корабля, чтоб просто попадал в поле 6*6

        still_trying = True

        while still_trying:
            u = randint(0, 5)
            v = randint(0, 5)
            az = choice(['⇔', '⇕'])
            try:
                curr_vessel = Ship(vessel_length, (u, v), az)
                still_trying = False

                return (curr_vessel)
            except:
                pass

    def FillingSea(self, l):  # принимает  правильно отгенерированнй корабль в рамках поля,
                              # проверяет на предмет перехлестов и границ с соседями
                              # и вставляет его в поле
        overflowing = OverflowVessel()
        playboard = self
        for _ in range(0, 2000):

            self.success_placing = False
            permission = True

            ship_ = self.Vessel_Birth(l)

            for tochka in ship_.dotsarray:

                if tochka in playboard.array:
                    permission = False
                    break
            if permission:
                outliner_ = OutLiner(ship_)
                if not DotArrayComparator(outliner_.abrise, playboard.array):
                    playboard.array.extend(ship_.dotsarray)
                    self.success_placing = True
                    playboard.vessels_list.append(ship_)

                    break
    def ffff(self):
        self.field = [['0' for _ in range(0, 6)] for _ in range(0, 6)]
        for __ in self.array:
            self.field[__.x][__.y] = 'V'
            # 'V' - судно
            # 'I' - раненный отсек
            # 'X' - убит
            # '0' - пусто


    def screen(self):  # вывод в экран игровой матрицы
        board_name = '  Это карта игрока "'+self.nickname +'"'
        print("        1                 2                 3                 4                 5                 6 \n",
              "       ↓                 ↓                 ↓                 ↓                 ↓                 ↓   ")
        for row in range(0, 6):  # строки игры

            for scan in range(0, 7):  # семь строк ячейки ( растр ячейки 7*18) разворачиваем в экран
                curr_scanline = ''
                for y in range(0, 6):  # столбы игры
                    curr_scanline += cell_type(self.hide_ships)[self.field[row][y]][scan * 18:(scan + 1) * 18]
                if scan == 3 and row == 5:
                    print(curr_scanline + ' ← ' + str(row + 1) + board_name)

                elif scan == 3:
                    print(curr_scanline + ' ← ' + str(row + 1))

                else:
                    print(curr_scanline)
        print("        ↑                 ↑                 ↑                 ↑                 ↑                 ↑\n",
              "       1                 2                 3                 4                 5                 6 ")
        print(self.mssg)
        self.mssg = ''

    def Generate(self):  # заполняет матрицу 6х6 Dotами и список Vesselями

        lenghts = [3, 2, 2, 1, 1, 1, 1]
        while True:
            self.array = []
            self.vessels_list = []
            for l in lenghts:
                self.FillingSea(l)  # ставит текущий корабль  в допустимом месте
            if self.success_placing:
                break


class OutOfRange(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):

        if self.message:
            return 'MyCustomError, {0} '.format(self.message)
        else:
            return 'OutOfRange in dots space'


class OverflowVessel(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):

        if self.message:
            return 'MyCustomError, {0} '.format(self.message)
        else:
            return 'Unsuccessful matching'


class OutLiner:  # класс для создания обводки от obj_for_outline,
                 # от него берется .dotsarray список со всеми точками

    def __init__(self, obj_for_outline):
        abrise = []
        for current_dot in obj_for_outline.dotsarray:
            for j in range(-1, 2):
                for i in range(-1, 2):
                    try:
                        ab_curr = dot(current_dot.x + j, current_dot.y + i)
                        if ab_curr not in obj_for_outline.dotsarray and ab_curr not in abrise \
                                and -1 < current_dot.x + j < 6 and -1 < current_dot.y + i < 6:
                            abrise.append(ab_curr)
                    except:
                        pass
        self.abrise = abrise  # + obj_for_outline.dotsarray


class dot:

    def __init__(self, x, y, status='0'):
        self.status = status
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    @property
    def x(self):

        return self._x

    @property
    def y(self):

        return self._y

    @x.setter
    def x(self, val):
        if 0 <= val < 6:
            self._x = val
        else:

            # self._y = 0
            raise OutOfRange

    @y.setter
    def y(self, val):
        if 0 <= val < 6:
            self._y = val
        else:

            # self._y = 0
            raise OutOfRange

    def __repr__(self):
        return f'DOT({self.x},{self.y}, {self.status})'


class Ship:

    def __init__(self, deck_len=3, coord=(2, 2), azimuth='⇔'):
        self.hp = deck_len
        az_adder = {'⇔': (0, 1), '⇕': (1, 0)}  # выбор дельты роста длины корабля - вертик или горизонт
        self.dotsarray = []
        # try:
        for _ in range(0, deck_len):
            u = coord[0] + _ * az_adder[azimuth][0]
            v = coord[1] + _ * az_adder[azimuth][1]
            if 0 <= u < 6 and 0 <= v < 6:
                self.dotsarray.append(dot(u, v, 'V'))
            else:
                self.dotsarray = []
                raise OutOfRange('wrong vessel positioning ')

    def __repr__(self):
        st = ''
        for i in self.dotsarray:
            st += str(i)
        return st


def cell_type(hide):
    if hide:
        return {
            'X': '┌────────────────┐│      ╔══╗      ││  ╔═══╝  ╚═══╗  ││  ╚═══╗  ╔═══╝  ││      ║  ║      ││      ║  ║      │└──────╨──╨──────┘',
            '0': '┌────────────────┐│                ││                ││                ││                ││                │└────────────────┘',
            'V': '┌────────────────┐│                ││                ││                ││                ││                │└────────────────┘',
            '.': '┌────────────────┐│                ││     ╭────╮     ││     │    │     ││     ╰────╯     ││                │└────────────────┘',
            'I': '┌────────────────┐│ ≈ ≈  ╔═╦═╦═╗ ≈ ││≈ ≈ ≈ ╚═╩═╩╗║≈ ≈││ ╭─────╥───╨╨─╮ ││ ≈\  ══╬══   /≈ ││≈ ≈\   ╩    /≈ ≈│└────────────────┘'
        }

    else:
        return \
            {
                'X': '┌────────────────┐│      ╔══╗      ││  ╔═══╝  ╚═══╗  ││  ╚═══╗  ╔═══╝  ││      ║  ║      ││      ║  ║      │└──────╨──╨──────┘',
                '0': '┌────────────────┐│                ││                ││                ││                ││                │└────────────────┘',
                'V': '┌────────────────┐│      ╔═╦═╦═╗   ││      ╚═╩═╩╗║   ││ ╭─────────╨╨─╮ ││  \          /  ││≈ ≈\        /≈ ≈│└────────────────┘',
                '.': '┌────────────────┐│                ││     ╭────╮     ││     │    │     ││     ╰────╯     ││                │└────────────────┘',
                'I': '┌────────────────┐│ ≈ ≈  ╔═╦═╦═╗ ≈ ││≈ ≈ ≈ ╚═╩═╩╗║≈ ≈││ ╭─────╥───╨╨─╮ ││ ≈\  ══╬══   /≈ ││≈ ≈\   ╩    /≈ ≈│└────────────────┘'
            }


class TheGame:
    def __init__(self, board1, board2, player1, player2):


        self.players_list = [player1, player2]
        self.boards_list = [board1, board2]
        self.TRIGGER = 0
    def RUN(self):

        str01 = "           Добро пожаловать в  игру\n"
        str015 = "            <-----МОРСКОЙ БОЙ----->\n"
        str02 = "              условные обозначения:\n"
        str03 = "┌────────────────┐           ┌────────────────┐\n" \
                "│                │           │      ╔═╦═╦═╗   │\n" \
                "│     ╭────╮     │           │      ╚═╩═╩╗║   │\n" \
                "│     │    │     │           │ ╭─────────╨╨─╮ │\n" \
                "│     ╰────╯     │           │  \          /  │\n" \
                "│                │           │≈ ≈\        /≈ ≈│\n" \
                "└────────────────┘           └────────────────┘\n" \
                "   выстрел мимо               ваш отсек судна\n" \
                "\n" \
                "┌────────────────┐           ┌────────────────┐\n" \
                "│ ≈ ≈  ╔═╦═╦═╗ ≈ │           │      ╔══╗      │\n" \
                "│≈ ≈ ≈ ╚═╩═╩╗║≈ ≈│           │  ╔═══╝  ╚═══╗  │\n" \
                "│ ╭─────╥───╨╨─╮ │           │  ╚═══╗  ╔═══╝  │\n" \
                "│ ≈\  ══╬══   /≈ │           │      ║  ║      │\n" \
                "│≈ ≈\   ╩    /≈ ≈│           │      ║  ║      │\n" \
                "└────────────────┘           └──────╨──╨──────┘\n" \
                "  раненный отсек                 кормит рыб\n"

        for _ in [str01, str015, str02, str03]:

            for s in _:
                print(s, '', end='\b')
                time.sleep(.0001)
        print( '            Игровое поле размером 6х6,\n'
              '  для места нанесения удара указывайте координаты\n'\
              '              ДВУМЯ цифрами от 1 до 6',
              end='\n')
        print("     сначала номер ряда, затем номер столбца. ")
        input("           для продолжения нажмите enter")
        self.boards_list[1-self.TRIGGER].screen()
        try:
            while True:
                self.players_list[self.TRIGGER].AskingShootin()
                self.players_list[self.TRIGGER].mov()
                time.sleep(3)
                if self.players_list[self.TRIGGER].lucky_shot:
                    self.TRIGGER = 1 - self.TRIGGER
                self.boards_list[self.TRIGGER].screen()
                self.TRIGGER = 1 - self.TRIGGER

        except OutOfRange:
            print("--------------------конец игры------------------------ ( нажмите 'ENTER' для выхода )")
            input()

        pass




board_H = BOARD()
board_AI = BOARD()
print(dir(board_AI))

board_H.Generate()
board_AI.Generate()

board_H.ffff()
board_AI.ffff()

board_H.hide_ships = False
board_AI.hide_ships = True

John = human(board_H, board_AI)
John.nickname = board_H.nickname = 'Человек'
HAL9000 = AI(board_AI, board_H)
HAL9000.nickname = board_AI.nickname = 'Центральный процессор'
IGRA = TheGame(board_H, board_AI, John, HAL9000)
IGRA.RUN()

