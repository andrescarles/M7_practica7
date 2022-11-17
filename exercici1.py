import xml.etree.ElementTree as ET

def creaXML():
    # Construim  estructura XML
    # root
    root = ET.Element('students')
    # Creem els childs del root
    for x in range(5):
        child = ET.SubElement(root, 'student')
        # Creem els subchilds de student
        n = ET.SubElement(child, 'name')
        n.text = input("Nom: ")
        sn = ET.SubElement(child, 'surname')
        sn.text = input("Cognom: ")
        e = ET.SubElement(child, 'email')
        e.text = input("email: ")
        d = ET.SubElement(child, 'DNI')
        d.text = input("DNI: ")

        #Afegim un Atribut a un element
        element = root[0]
        element.set('curs','DAW')

        #Guarda XML creat amb ElementTree
        tree = ET.ElementTree(root)
        tree.write('exercici1.xml')

        #Mostra l'XML per consola
        ET.dump(root)

creaXML()