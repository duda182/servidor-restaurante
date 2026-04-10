import requests
from datetime import datetime


BASE_URL = 'http://localhost:5000/atendente'  


def converter_data_para_iso(data_input):

    try:
        return datetime.strptime(data_input, '%d-%m-%Y').strftime('%Y-%m-%d')
    except ValueError:
        raise ValueError("Data deve estar no formato DD-MM-YYYY")

def fazer_requisicao_post(url, dados):
    
    try:
        response = requests.post(url, json=dados)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200 and response.text.strip():
            print("✅ Sucesso:", response.json())
        else:
            print("❌ Erro ou resposta vazia:", response.text)
            
    except requests.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
    except ValueError as e:
        print(f"❌ Erro ao processar resposta JSON: {e}")
        print(f"Resposta recebida: {response.text}")

def fazer_requisicao_delete(url):
    
    try:
        response = requests.delete(url)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200 and response.text.strip():
            print("✅ Sucesso:", response.json())
        else:
            print("❌ Erro ou resposta vazia:", response.text)
            
    except requests.RequestException as e:
        print(f"❌ Erro na requisição: {e}")
    except ValueError as e:
        print(f"❌ Erro ao processar resposta JSON: {e}")
        print(f"Resposta recebida: {response.text}")

def criar_nova_reserva():
    
    print("\n=== CRIAR NOVA RESERVA ===")
    
    try:
        
        data_input = input("📅 Data (DD-MM-YYYY): ")
        data_iso = converter_data_para_iso(data_input)
        
        hora = input("🕐 Hora (HH:MM): ")
        mesa = int(input("🪑 Mesa: "))
        pessoas = int(input("👥 Quantidade de pessoas: "))
        responsavel = input("👤 Nome do responsável: ")
        
        dados_reserva = {
            'data': data_iso,
            'hora': hora,
            'mesa': mesa,
            'pessoas': pessoas,
            'responsavel': responsavel
        }
        
        url = f"{BASE_URL}/reserva"
        fazer_requisicao_post(url, dados_reserva)
        
    except ValueError as e:
        print(f"❌ Erro nos dados informados: {e}")
    except KeyboardInterrupt:
        print("\n⚠️ Operação cancelada pelo usuário")

def cancelar_reserva_existente():

    print("\n=== CANCELAR RESERVA ===")
    
    try:
        id_reserva = input("🔢 ID da reserva: ")
        
        if not id_reserva.isdigit():
            print("❌ ID deve ser um número válido")
            return
        
        url = f"{BASE_URL}/reserva/{id_reserva}"
        fazer_requisicao_delete(url)
        
    except KeyboardInterrupt:
        print("\n⚠️ Operação cancelada pelo usuário")


def main():
    
    print("=" * 50)
    print("🍽️  SISTEMA DE RESERVAS - CLIENTE")
    print("=" * 50)
    print("1 - Criar reserva")
    print("2 - Cancelar reserva")
    print("0 - Sair")
    print("-" * 50)
    
    try:
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            criar_nova_reserva()
        elif opcao == '2':
            cancelar_reserva_existente()
        elif opcao == '0':
            print("👋 Saindo do sistema...")
        else:
            print("❌ Opção inválida! Escolha 1, 2 ou 0.")
            
    except KeyboardInterrupt:
        print("\n\n👋 Sistema encerrado pelo usuário")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main()
