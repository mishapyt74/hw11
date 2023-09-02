import json

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({'name': name, 'phone': phone})

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.contacts, file)

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query in contact['name'] or query in contact['phone']:
                results.append(contact)
        return results

def main():
    address_book = AddressBook()
    filename = '../address_book.json'

    address_book.load_from_file(filename)

    while True:
        print("\nМеню:")
        print("1. Додати контакт")
        print("2. Знайти контакт або контакти")
        print("3. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            name = input("Введіть ім'я: ")
            phone = input("Введіть номер телефону: ")
            address_book.add_contact(name, phone)
            address_book.save_to_file(filename)
            print("Ви успішно додали контакт!")

        elif choice == '2':
            query = input("Введіть запит для пошуку: ")
            results = address_book.search_contacts(query)
            if results:
                print("Результати пошуку:")
                for contact in results:
                    print(f"Ім'я: {contact['name']}, Телефон: {contact['phone']}")
            else:
                print("Не знайдено жодного контакту.")

        elif choice == '3':
            print("До побачення!")
            break

if __name__ == "__main__":
    main()
