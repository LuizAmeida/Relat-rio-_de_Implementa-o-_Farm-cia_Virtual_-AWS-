import json

# Simulação de conexão com o banco de dados RDS da Abstergo Pharma
def lambda_handler(event, context):
    """
    Simula uma função AWS Lambda que verifica o estoque da farmácia virtual.
    """
    print("Conectando ao banco de dados RDS...")
    
    # Mock de dados de estoque
    estoque_farmacia = {
        "produto_id": 101,
        "nome": "Vitamina C 1g",
        "quantidade_disponivel": 150,
        "status": "Em estoque"
    }
    
    return {
        'statusCode': 200,
        'body': json.dumps(estoque_farmacia)
    }

if __name__ == "__main__":
    # Teste local do script
    print("Executando verificação de estoque local...")
    resultado = lambda_handler(None, None)
    print(f"Resultado: {resultado['body']}")