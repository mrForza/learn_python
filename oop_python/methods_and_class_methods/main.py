import math


class IncorrectPoint:
    color: str = 'red'
    size: int = 3

    # The instance doesn't have a method attribute in his own namespace
    # It can only link to method attribute which locates in the class namespace
    def set_coordinates(self):  # The method is an attribute of class
        print("Enter x coordinate: ", sep='')
        self.x = int(input())  # We create a new attribute in instance namespace
        print("Enter y coordinate: ", sep='')
        self.y = int(input())  # We create a new attribute in instance namespace

    def get_coordinates(self):
        return self.x, self.y


class Point:
    # Instance initializer. This magic method calls when the instance has been crated
    # We use it to initialize local attributes
    def __init__(self, x: int = 0, y: int = 0, name: str = 'Undefined'):
        self.x = x
        self.y = y
        self.name = name

    # This magic method calls when the program finishes her work or when garbage collector delete this instance
    def __del__(self):
        print(f'The point {str(self)} has been successfully deleted!')

    def get_coordinates(self):
        return self.x, self.y

    def get_name(self):
        return self.name


class Vector:
    MIN_CORD = 0
    MAX_CORD = 100

    @classmethod
    def validate_cord(cls, cord):
        # classmethod we can call by class
        # If we call classmethod by self parametr, it pass a ref to class uh
        # classmethod has access only to class namespace
        return True if cls.MIN_CORD <= cord <= cls.MAX_CORD else False

    @staticmethod
    def get_length(x_cord: float, y_cord: float) -> float:
        # static method doesn't have access to class or object namespaces
        # we can also call staticmethod by class or by self
        return math.sqrt(x_cord**2 + y_cord**2)

    def __init__(self, x_cord: float, y_cord: float, name: str = 'vector_ab'):
        if not Vector.validate_cord(x_cord) or not self.validate_cord(y_cord):
            raise Exception('Incorrect cord!')
        self.x_cord = x_cord
        self.y_cord = y_cord
        self.name = name

    def __str__(self) -> str:
        return f'{self.name}({self.x_cord};{self.y_cord})'


def learn_methods():
    point_a = IncorrectPoint()
    point_b = IncorrectPoint()

    # print(point_a.get_coordinates()) # We cannot user get_coordinates if we didn't call set_coordinates
    # In set_coordinates method an instance get new attributes in its namespace

    # IncorrectPoint.set_coordinates() We cannot call methods through the class. We must call them through the instance
    point_a.set_coordinates()  # When we call method through the instance uh interpreter pass self argument
    # in this method. self - this is a link to current instance
    vector_ab = Vector(2, 4)
    print(vector_ab)
    print(Vector.__dict__)
    print(vector_ab.__dict__)
    print(vector_ab.get_length(3, 5))
    print(Vector.get_length(8, 5))


if __name__ == '__main__':
    learn_methods()
