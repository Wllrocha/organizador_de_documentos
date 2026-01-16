import os
import shutil

# Defina o caminho da pasta que você quer organizar
# Exemplo: r'C:\Users\Usuario\Downloads'
caminho = r'C:\Users\wallace.rocha\Downloads'

# Mapeamento de extensões para pastas
tipos_arquivos = {
    'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Instaladores': ['.exe', '.msi'],
    'Compactados': ['.zip', '.rar']
}

def organizar():
    # Entra na pasta
    for arquivo in os.listdir(caminho):
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()

        # Verifica cada tipo definido no dicionário
        for pasta, extensoes in tipos_arquivos.items():
            if extensao in extensoes:
                caminho_pasta = os.path.join(caminho, pasta)
                
                # Se a pasta não existir, cria ela
                if not os.path.exists(caminho_pasta):
                    os.makedirs(caminho_pasta)
                
                # Move o arquivo
                shutil.move(os.path.join(caminho, arquivo), os.path.join(caminho_pasta, arquivo))
                print(f"✅ Movido: {arquivo} -> {pasta}")

if __name__ == "__main__":
    organizar()
    print("\n🚀 Organização concluída!")