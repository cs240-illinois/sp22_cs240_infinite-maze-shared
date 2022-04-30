class GlobalMaze:
    '''Class to store global maze state and encapsulate logic'''
    __state = {}
    __is_empty = True
    
    def get_state(self, row: int, col: int):
        '''Returns maze segment data in current state for given coords'''
        return self.__state.get((row, col))

    def set_state(self, row: int, col: int, data: dict):
        '''Modify current state of the maze'''
        self.__state[(row, col)] = data
        self.__is_empty = False
    
    def reset(self):
        '''Reset maze state'''
        if not self.__is_empty:
            self.__state = {}
            self.__is_empty = True

    def get_full_state(self):
        '''Get state of all segments'''
        output = {}
        for key, val in self.__state.items():
            output[f'{key[0]}_{key[1]}'] = val
        return output

    def is_empty(self) -> bool:
        '''Return `True` if no data is present, else return `False`'''
        return self.__is_empty
    
    def get_free_space(self, row: int, col: int, radius: int) -> set:
        '''Return set of free spaces in given radius centered on given coords'''
        output = set()
        for r in range(row - radius, row + radius + 1):
            for c in range(col - radius, col + radius + 1):
                if (r, c) not in self.__state.keys():
                    output.add((r, c))
        return output