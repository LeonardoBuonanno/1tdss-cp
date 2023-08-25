def load_users_from_csv(filename):
    users = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        for line in lines[1:]:  # Skip header
            email, name = line.strip().split(',')
            users[email] = name
    except FileNotFoundError:
        pass
    return users

def save_users_to_csv(filename, users):
    with open(filename, 'w') as file:
        file.write("Email,Name\n")  # header
        for email, name in users.items():
            file.write(f"{email},{name}\n")

# Load existing users from CSV file (if any)
filename = "users.csv"
users = load_users_from_csv(filename)

while True:
    print("\nUser Manager:")
    print("1. Adicionar usuário")
    print("2. Remover usurário")
    print("3. Listar todos os usuários")
    print("4. Pesquisar usuário por e-mail")
    print("5. Sair")
    
    choice = input("Entre com a escolha: ")

    if choice == "1":
        name = input("Entre com nome: ")
        email = input("Entre com e-mail: ")
        
        if email in users:
            print("Já existe usuário com este endereço de email.")
        else:
            users[email] = name
            print(f"{name} Adicionado com sucesso!")
            save_users_to_csv(filename, users)  # Save updated users to CSV

    elif choice == "2":
        email = input("Entre com o e-mail para remover: ")
        
        if email in users:
            del users[email]
            print(f"Usuário com o e-mail {email} removido com sucesso!")
            save_users_to_csv(filename, users)  # Save updated users to CSV
        else:
            print("Usuário não encontrado")

    elif choice == "3":
        if not users:
            print("Nenhum usuário na lista.")
        else:
            for email, name in users.items():
                print(f"Nome: {name}, E-mail: {email}")

    elif choice == "4":
        email = input("Entre com o email para procurar: ")
        
        if email in users:
            print(f"Nome: {users[email]}, E-mail: {email}")
        else:
            print("Usuário não encontrado.")

    elif choice == "5":
        print("Tchau Tchau!")
        break
    else:
        print("Opção inválida, entre com uma opção válida")
