class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = []

    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)
        if "wife" in person_dict and person_dict["wife"]:
            person._wife_name = person_dict["wife"]
        elif "husband" in person_dict and person_dict["husband"]:
            person._husband_name = person_dict["husband"]

    for person in person_list:
        if hasattr(person, "_wife_name"):
            person.wife = Person.people[person._wife_name]
            delattr(person, "_wife_name")
        elif hasattr(person, "_husband_name"):
            person.husband = Person.people[person._husband_name]
            delattr(person, "_husband_name")

    return person_list
