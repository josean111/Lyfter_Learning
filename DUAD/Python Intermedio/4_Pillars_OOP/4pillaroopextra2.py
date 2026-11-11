
# Cree una clase abstracta User con los siguientes métodos abstractos:
# - get_role()
# - has_permission(permission)
#
# Luego cree dos clases que hereden de ella:
# - AdminUser
# - RegularUser
#
# Cada una debe implementar los métodos.
# AdminUser siempre tiene permisos.
# RegularUser solo tiene permisos limitados ("read", por ejemplo).
#
# Ejemplo:
# user1 = AdminUser("Carlos")
# user2 = RegularUser("Andrea")
#
# print(user1.has_permission("delete")) # True
# print(user2.has_permission("delete")) # False

from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass

class AdminUser(User):
    def __init__(self, name):
        super().__init__(name)

    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        return True

class RegularUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.__permissions = ["read"]

    def get_role(self):
        return "Regular User"

    def has_permission(self, permission):
        return permission in self.__permissions

def main():
    user1 = AdminUser("Carlos")
    print(f"{user1.get_name()} - {user1.get_role()}")
    print(f"Can read: {user1.has_permission('read')}")
    print(f"Can delete: {user1.has_permission('delete')}")

    user2 = RegularUser("Andrea")
    print(f"\n{user2.get_name()} - {user2.get_role()}")
    print(f"Can read: {user2.has_permission('read')}")
    print(f"Can delete: {user2.has_permission('delete')}")

if __name__ == "__main__":
    main()
