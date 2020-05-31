from enum import Enum
import math


class Window(Enum):
    SCALE = 0.1

    GRID_WIDTH = 500
    GRID_HEIGHT = 500

    GRID_OFFSET_X = math.floor(0.035 * GRID_WIDTH)
    GRID_OFFSET_Y = math.floor(0.035 * GRID_HEIGHT)

    GRID_INNER_OFFSET_X = math.floor(0.015 * GRID_WIDTH)
    GRID_INNER_OFFSET_Y = math.floor(0.015 * GRID_HEIGHT)

    
    CELL_WIDTH = math.floor((GRID_WIDTH - 2 * (GRID_OFFSET_X + GRID_INNER_OFFSET_X)) / 3)
    CELL_HEIGHT = math.floor((GRID_HEIGHT - 2 * (GRID_OFFSET_Y + GRID_INNER_OFFSET_Y)) / 3)

    GRID_POSITION_X = math.floor((SCALE / 2) * GRID_WIDTH)
    GRID_POSITION_Y = CELL_HEIGHT + 2 * GRID_OFFSET_Y

    WIDTH = math.floor((1 + SCALE) * GRID_WIDTH)
    HEIGHT = math.floor(GRID_HEIGHT + 2 * (CELL_HEIGHT + 2 * GRID_OFFSET_Y))


    PIECE_SCALE = 0.9
    PIECE_WIDTH = math.floor(PIECE_SCALE * CELL_WIDTH)
    PIECE_HEIGHT = math.floor(PIECE_SCALE * CELL_HEIGHT)
    PIECE_OFFSET_X = math.floor(((1 - PIECE_SCALE) / 2) * CELL_WIDTH)
    PIECE_OFFSET_Y = math.floor(((1 - PIECE_SCALE) / 2) * CELL_HEIGHT)
    

    PAWN_WHITE_START_POSITION_X = GRID_POSITION_X + GRID_OFFSET_X + PIECE_OFFSET_X
    PAWN_WHITE_START_POSITION_Y = GRID_POSITION_Y - CELL_HEIGHT - GRID_OFFSET_Y + PIECE_OFFSET_Y
    PAWN_BLACK_START_POSITION_X = GRID_POSITION_X + GRID_OFFSET_X + PIECE_OFFSET_X
    PAWN_BLACK_START_POSITION_Y = GRID_POSITION_Y + GRID_HEIGHT + GRID_OFFSET_Y + PIECE_OFFSET_Y
    