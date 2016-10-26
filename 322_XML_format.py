from xml.etree import ElementTree

colors = {"red": 0, "green": 0, "blue": 0}
str_xml = input()
root = ElementTree.fromstring(str_xml)


def getChildren(root, level=1):
#- это моя рекурсивная функция, которая проходит по всем веткам, начиная с корня, учитывая уровень и собирает данные по цветам:
    colors[root.attrib['color']] += level #1. Увеличение в списке значения элемента цвета на level.
    for child in root:
#        print(level, child.attrib)        #2. Цикл по всем переданным root.
        getChildren(child, level+1)        #3. вызов функции с child и level+1.
    return
f = getChildren(root)
print(colors['red'], colors['green'], colors['blue'])
