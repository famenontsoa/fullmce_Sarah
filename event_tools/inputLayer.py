import ntpath
from qgis.core import QgsVectorLayer, QgsField
from qgis.PyQt.QtCore import QVariant


class InputLayer:
    def __init__(self, path):
        self.path = path
        self.elements = []

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def setpath(self,path):
        self.path = path

    def setvlayer(self,vlayer):
        self.vlayer = vlayer

    def isValid(self):
        filename = ntpath.basename(self.path)
        self.name = filename.split('.')[0]
        vlayer = QgsVectorLayer(self.path,self.name,"ogr")
        if not vlayer.isValid():
            return False
        else:
            self.vlayer = vlayer
            return True

    def add_element (self,element):
        self.elements.append(element)

    def remove_element (self,element):
        self.elements.remove(element)

    def field_is_duplicated (self, type):
        list_field_idx = []
        for element in self.elements:
            if element.type == type:
                if element.field_idx in list_field_idx:
                    return True
                list_field_idx.append(element.field_idx)
        return False

    def newfieldname_exist (self, type, name):
        field_extension = "Fz" if type == "factor" else "Bl"
        new_field_name = name + field_extension
        if new_field_name in self.vlayer.fields().names():
            return True
        else:
            return False

    def newfieldname_is_duplicated (self,type):
        list_name = []
        field_extension = "Fz" if type == "factor" else "Bl"
        for element in self.elements:
            if element.type == type:
                new_field_name = element.name + field_extension
                if new_field_name in list_name:
                    return True
                list_name.append(new_field_name)
        return False

    def setreclass_output(self,output_path):
        self.reclass_output = output_path

    def add_new_field(self,new_field_name,typeName):
        vlayer_provider = self.vlayer.dataProvider()
        new_field_idx = self.vlayer.fields().indexOf(new_field_name)
        if new_field_idx == -1:
            type = QVariant.Double if typeName == "double" else QVariant.Int
            vlayer_provider.addAttributes([QgsField(new_field_name,type,typeName,10,3)]) # Round to 5 decimal places
            self.vlayer.updateFields()
            new_field_idx = self.vlayer.fields().indexOf(new_field_name)
        return new_field_idx

    def delete_new_field(self,field_name):
        new_field_idx = self.vlayer.fields().indexOf(field_name)
        if new_field_idx != -1:
            self.vlayer.dataProvider().deleteAttributes([new_field_idx])
            self.vlayer.updateFields()

    def __getattr__(self, item):
        return 'Source path does not have `{}` attribute.'.format(str(item))
