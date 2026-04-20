from datetime import datetime

class InputValidator:
   
    @staticmethod
    def get_float(mensagem: str):
        """Garante a leitura de um número decimal (float). Retorna None se o usuário cancelar ('c')."""
        while True:
            entrada = input(mensagem).strip()
            
            if not entrada:
                print("\n[!] Erro: O campo não pode ficar vazio.")
                continue
                
            if entrada.lower() == 'c':
                return None 
                
            try:
                return float(entrada)
            except ValueError:
                print("\n[!] Erro: Valor numérico inválido. Digite apenas números ou 'c' para cancelar.")

    @staticmethod
    def get_string(mensagem: str):
        """Garante a leitura de um texto que não seja vazio. Retorna None se o usuário cancelar ('c')."""
        while True:
            entrada = input(mensagem).strip()
            
            if not entrada:
                print("\n[!] Erro: O campo não pode ficar vazio. Por favor, preencha.")
                continue
                
            if entrada.lower() == 'c':
                return None
                
            return entrada

    @staticmethod
    def get_date(mensagem: str):
        """Garante a leitura de uma data válida. Retorna None se o usuário cancelar ('c')."""
        while True:
            entrada = input(mensagem).strip()
            
            if not entrada:
                print("\n[!] Erro: O campo não pode ficar vazio.")
                continue
                
            if entrada.lower() == 'c':
                return None
                
            try:
                return datetime.strptime(entrada, "%d-%m-%Y").date()
            except ValueError:
                print("\n[!] Erro: Formato de data inválido. Use o padrão dd-mm-aaaa (ex: 25-10-2005).")