import os
import sqlite3
import json
from delf_entry import DelfEntry, Landmark, DelfOutput
from environment import DB_PATH


class Repository:
    def __init__(self, db_path: str):
        self.__db_path = db_path
        self.__db_conn = sqlite3.connect(f"file:{db_path}", uri=True)

    def save(self, entry: DelfEntry) -> DelfEntry:
        self.__db_conn.execute("INSERT INTO Landmarks (name, wiki_link) VALUES (?,?);",
                               (
                                   entry.landmark.name,
                                   entry.landmark.wiki_link,
                               ))
        self.__db_conn.commit()
        entry.landmark = self.get_landmark_by_name(entry.landmark.name)
        for delf_output in entry.delf_output:
            self.__db_conn.execute("INSERT INTO DelfOutputs (locations, descriptors, landmark_id) VALUES (?,?,?);",
                                   (
                                       json.dumps(delf_output.locations),
                                       json.dumps(delf_output.descriptors),
                                       entry.landmark.id
                                   ))

        self.__db_conn.commit()
        return entry

    def get_landmark_by_name(self, name: str) -> Landmark:
        landmark = None
        for entry in self.__db_conn.execute("SELECT * FROM Landmarks WHERE name = (?);", (name,)):
            landmark = Landmark(
                entry[1],
                entry[2],
                entry[0]
            )

        return landmark

    def get_range(self) -> list:
        entries = []
        for entry in self.__db_conn.execute("SELECT * FROM Landmarks;"):
            landmark = Landmark(entry[1], entry[2], entry[0])
            delf_output = []
            for _entry in self.__db_conn.execute("SELECT * FROM DelfOutputs where landmark_id = (?);", (landmark.id,)):
                delf_output.append(DelfOutput(
                    json.loads(_entry[1]),
                    json.loads(_entry[2]),
                    _entry[0],
                    _entry[3]
                ))

            entries.append(DelfEntry(landmark, delf_output))

        return entries

    def __del__(self):
        self.__db_conn.close()


if __name__ == '__main__':
    path = os.path.join(os.getcwd(), DB_PATH)
    repo = Repository(path)

    landmark = Landmark('landmark', 'wiki_link', 1)
    delf_output = DelfOutput([1, 2], [1, 2], 1, 1)
    delf_entry = DelfEntry(landmark, [delf_output])

    delf_entry = repo.save(delf_entry)
    all = repo.get_range()
    print(all)
