
# classes are "blueprints" for objects.
class Moon:

    # constructor - used to initialize a new moon (instance of Moon)
    #
    #   make an instance, then the blueprint has to have a way to
    #   refer to "itself".  In python, that is "self"
    def __init__(self,size : int,color : str, phase : int = 0) -> None:

        # properties...
        self._size : int = size
        self._color : str = color
        self._phase : int = phase

    def isNewMoon(self) -> bool:
        return self._phase == 0

    def cycle(self) -> None:
        self._phase = (self._phase + 1) % 4

    @property
    def phase(self) -> int:
        return self._phase

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self,value : str) -> None:
        if not value in ['grey','blue','white','silver']:
            raise ValueError('invalid moon color')
        self._color = value

    @property
    def size(self):
        return self._size



    

