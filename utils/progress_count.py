import math
from colorama import init, Fore


class ProgressCount:
    def __init__(self, count, step=1, multiplicity=1000, start_message='', percentage=True, newline_at_the_end=True):
        self.count = count
        if self.count > 100:
            self.__by_hundredth = True
        else:
            self.__by_hundredth = False
        self.__hundredth = math.floor(count / 100)
        self.__len_count = len(str(count))
        self.step = step

        self.multiplicity = multiplicity
        self.__multiplicity_10 = self.multiplicity / 10

        self.start_message = start_message
        self.__i = 0
        self.proc = 0
        self.__percentage = percentage
        self.__newline_at_the_end = newline_at_the_end
        init(True)
        if start_message:
            print(self.start_message)

    def next(self):
        if self.__percentage:
            self.__i += self.step
            self.proc = math.ceil(self.__i * 100 / self.count)
            if (self.__by_hundredth and self.__i % self.__hundredth == 0) or not self.__by_hundredth or self.__i == 1:
                print(f'\r{Fore.BLUE}{self.proc}% ({self.count})', end=' ')
            if self.__i == self.count and self.__newline_at_the_end:
                print()
        else:
            self.__i += self.step
            if self.__i % self.multiplicity == 0 or self.__i == 1:
                if self.__i != 1:
                    print()
                print(f'{Fore.BLUE}{str(self.__i).zfill(self.__len_count)} ({self.count})', end=' ')
            elif self.__i % self.__multiplicity_10 == 0:
                print('.', end=' ')
