# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Shaft:
    """
    Класс описывающий вал
    """
    def __init__(self, lenght: int, diameter: int):
        """
               Инициализация класса
               :param lenght: Длина вала в мм
               :param diameter: диаметр вала в мм
               >>> shaft = Shaft(500, 60)  # инициализация экземпляра класса
        """
        if not isinstance(lenght, int):
            raise TypeError("Длина должна быть целой")
        if lenght < 0:
            raise ValueError("Длина должна быть положительной")
        self.lenght = lenght
        if not isinstance(lenght, int):
            raise TypeError("Диаметр должен быть целым")
        if lenght < 0:
            raise ValueError("Диаметр должен быть положительным")
        self.diameter = diameter

    def cut_shaft(self, cut1):
        """
        Метод, дающий возможность уменьшить длину вала
        >>> shaft = Shaft(500, 60)
        >>> shaft.cut_shaft(20)
        """
        pass

    def substract_diameter(self, substract1):
        """
        Метод, дающий возможность уменьшить диаметр вала
        >>> shaft = Shaft(500, 60)
        >>> shaft.substract_diameter(5)
        """
        pass

class Impeller:
    """
       Класс описывающий рабочее колесо
    """
    def __init__(self, num_of_vanes: int, output: float):
        """
        Инициализация класса
        :param num_of_vanes: количество лопаток
        :param output: расход ступени в л^3/с
        >>> impeller = Impeller(10, 45.6)  # инициализация экземпляра класса
        """
        if not isinstance(num_of_vanes, int):
            raise TypeError("Количество должно быть целым")
        if num_of_vanes <= 1:
            raise ValueError("Количество не может быть меньше двух")
        self.num_of_vanes = num_of_vanes
        if not isinstance(output, float):
            raise TypeError("Подача должна быть числом")
        if output < 0:
            raise ValueError("Подача не может быть отрицательной")
        self.output = output

    def add_vane(self, vane):
        """
        Метод, дающий возможность добавить лопасть к колесу
        >>> impeller = Impeller(10, 45.6)
        >>> impeller.add_vane(1)
        """
        pass

    def substract_vane(self, cut1):
        """
        Метод, дающий возможность убрать одну лопасть
        >>> impeller = Impeller(10, 45.6)
        >>> impeller.substract_vane(1)
        """
        pass

class Tube:
    """
       Класс описывающий трубу
    """
    def __init__(self, lenght: int, diameter: int, wall_thicness: float ):
        """
               Инициализация класса
               :param lenght: Длина трубы в мм
               :param diameter: диаметр трубы в мм
               :param wall_thicness: толщина стенки трубы
               >>> tube = Tube(150, 20, 3.5)  # инициализация экземпляра класса
        """
        if not isinstance(lenght, int):
            raise TypeError("Длина должна быть целой")
        if lenght < 0:
            raise ValueError("Длина должна быть положительной")
        self.lenght = lenght
        if not isinstance(lenght, int):
            raise TypeError("Длина должна быть целой")
        if lenght < 0:
            raise ValueError("Диаметр должен быть положительным")
        self.diameter = diameter
        if not isinstance(wall_thicness, float):
            raise TypeError("Толщина должна быть числом")
        if lenght <= 0:
            raise ValueError("Толщина должна быть положительной")
        self.wall_thicness = wall_thicness

    def get_inner_diam(self, cut1):
        """
        Метод, позволяющий вычислить внутренний диаметр
        >>> tube = Tube(150, 20, 3.5)
        >>> tube.get_inner_diam()
        """
        pass

    def cut_tube(self, substract1):
        """
        Метод, дающий возможность Укоротить трубу на заданную величину
        >>> tube = Tube(150, 20, 3.5)
        >>> tube.cut_tube(6)
        """
        pass

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации

