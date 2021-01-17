class Landmark:
    def __init__(self, name: str, wiki_link: str, landmark_id: int = None):
        self.__id = landmark_id
        self.__name = name
        self.__wiki_link = wiki_link

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def wiki_link(self):
        return self.__wiki_link

    @wiki_link.setter
    def wiki_link(self, value: str):
        self.__wiki_link = value

    def __repr__(self):
        return f'Id:{self.__id}; Name:{self.__name}; WikiLink:{self.__wiki_link}'


class DelfOutput:
    def __init__(self, locations: list, descriptors: list, id: int = None, landmark_id: int = None):
        self.__id = id
        self.__landmark_id = landmark_id
        self.__locations = locations
        self.__descriptors = descriptors

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = id

    @property
    def landmark_id(self) -> int:
        return self.__landmark_id

    @landmark_id.setter
    def landmark_id(self, value: int):
        self.__landmark_id = value

    @property
    def locations(self) -> list:
        return self.__locations

    @locations.setter
    def locations(self, value):
        self.__locations = value

    @property
    def descriptors(self) -> list:
        return self.__descriptors

    @descriptors.setter
    def descriptors(self, value):
        self.__descriptors = value

    def __repr__(self):
        return f'Id:{self.__id}; LandmarkId:{self.__landmark_id}; Locations:{self.__locations}; Descriptors:{self.__descriptors}'


class DelfEntry:
    def __init__(self, landmark: Landmark, delf_output: list):
        self.__landmark = landmark
        self.__delf_output = delf_output

    @property
    def landmark(self) -> Landmark:
        return self.__landmark

    @landmark.setter
    def landmark(self, value: Landmark):
        self.__landmark = value

    @property
    def delf_output(self):
        return self.__delf_output

    @delf_output.setter
    def delf_output(self, value: list):
        self.__delf_output = value

    def __repr__(self):
        return f'Landmark:[{repr(self.__landmark)}]; DelfOutput:[{repr(self.__delf_output)}]'


if __name__ == '__main__':
    landmark = Landmark('landmark', 'wiki_link', 1)
    delf_output = DelfOutput([1, 2], [1, 2], 1, 1)
    delf_entry = DelfEntry(landmark, [delf_output])

    print(repr(delf_entry))
