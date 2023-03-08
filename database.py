from dispositivo import Dispositivo


class Database:

    def __init__(self, template: dict):
        self.database = []
        for each in template.get("dispositivos"):
            self.database.append(Dispositivo(each.get("id"), each.get(
                "nombre"), each.get("marca", ""), each.get("tipo", "")))

    def delete_by_id(self, id: int):
        to_delete = -1
        for position in range(len(self.database)):
            if self.database[position].id == id:
                to_delete = position
        if to_delete != -1:
            self.database.pop(to_delete)

    def add_dispositivo(self, dispositivo: Dispositivo):
        self.database.append(dispositivo)
