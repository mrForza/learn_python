import json

from enums import Color, AsciiEnum, LoggingStatus
from figures import Point


def learn_enums():
    print('The name of some symbolic name in Color enum: ', Color.RED.name)
    print('The value of some symbolic name in Color enum: ', Color.RED.value, '\n')

    # The attributes of Enum class in parsing will be converted to an instance of Enum.Attribute class
    # with attributes name and color

    # We can iterate through the Color enum
    for color in Color:
        print(f'{color.value["ansi"]}Name: {color.name}, Value: {color.value["hex"]}')
    print('\033[0m')

    # We can compare some value with enum value
    hex_color = '#e86b17'
    if hex_color == Color.ORANGE.value['hex']:
        print(f'The hex_color = {hex_color} match\'s to orange_color = {Color.ORANGE.value["hex"]}')
    else:
        print(f'The hex_color = {hex_color} does not match to orange_color = {Color.ORANGE.value["hex"]}')

    # We can compare only such enum's instances which values are integers and enum class inherit from enum.IntEnum
    try:
        if Color.RED < Color.GREEN:
            print(f'{Color.RED.name} less than {Color.GREEN.name}')
        else:
            print(f'{Color.RED.name} greate or equal than {Color.GREEN.name}')
    except TypeError:
        print(f'We cannot compare these enum\'s instances: {Color.RED.name} and {Color.GREEN.name}')

    if AsciiEnum.A < AsciiEnum.M:
        print('Ascii code of A less than ascii code of M\n')
    else:
        print('Ascii code of A greater than ascii code of M')

    # If we define an enum the second way, we will not be able to get the attribute of this enum by dot notation
    # We will be able to iterate through enum's names attribute
    for status in LoggingStatus:
        print(f'{status.name}: {status.value}')


def learn_class_attributes():
    # For every class an interpreter create his own namespace which consist of attributes, declared in class
    print(f'The base point\'s color: {Point.color}')
    print(f'The base point\'s circle: {Point.circle} px')

    # The instances of class have the same attribute's values like a class
    point_a = Point()  # point_a - the instance of Point class
    point_b = Point()  # point_b - the instance of Point class
    print(f'point_a.color = {point_a.color}')
    print(f'point_b.color = {point_b.color}\n')

    # If we change some attribute in class. Then every attribute an instances will be changed
    Point.color = '#cb3457'
    print(f'point_a.color = {point_a.color}')
    print(f'point_b.color = {point_b.color}\n')

    # If we change attribute in some instance. Another instances will not change their attributes
    point_a.color = '#bb8a44'
    print(f'point_a.color = {point_a.color}')
    print(f'point_b.color = {point_b.color}\n')

    # The attributes of class are common for each class's instances
    # The instances namespaces don't have any attributes. If we call point_a.color we link to class attribute
    # If we want to check the attributes and methods in namespace, we can call __dict__ attribute
    print('The attribute of Point class: ')
    for key, value in Point.__dict__.items():
        print(f'{key}: {value}')
    print()

    # If we call __dict__ magic attribute through the class we get an mappingProxy
    # If we call __dict__ magic attribute through the instance of class we get a dict
    print(f'class __dict__ type: {type(Point.__dict__)}\t instance __dict__ type: {type(Point().__dict__)}\n')

    # The point_b instance doesn't have any attributes in his namespace
    # If we call point_b.color or point_b.circle we link to class attributes
    print(f'The attributes of point_b namespace: {point_b.__dict__}')
    # But if we change the color of instance, a new variable will be created in his namespace
    point_b.color = '#1ee1b8'
    print(f'The attributes of point_b namespace after changing the color: {point_b.__dict__}\n')

    # We can use setattr() function if we want to add an extra attribute to our class or instance
    setattr(point_a, 'name', 'small-circle')
    # If we call non-existing attribute we can get AttributeError exception
    # That is why we should use getattr() function with default param
    print(getattr(Point, 'name', '-'))
    print(getattr(point_a, 'name', '-'))

    # We can check if attribute exists in our class using hasattr() function
    print(hasattr(Point, 'name'))
    print(hasattr(point_a, 'name'))
    print(hasattr(point_b, 'circle'))


if __name__ == '__main__':
    # learn_enums()
    learn_class_attributes()
