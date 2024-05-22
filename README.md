Projeto de Segurança Informática
Descrição:
Este projeto é uma aplicação de segurança informática que permite a cifragem, decifragem, assinatura digital, verificação de assinaturas digitais, cálculo de hashes e verificação de integridade de arquivos. 
A aplicação é projetada para ser fácil de usar, com várias funcionalidades automatizadas que são ativadas quando arquivos são movidos para pastas específicas monitoradas pela aplicação.

Estrutura de Pastas:
A aplicação cria e monitoriza as seguintes pastas:

. Encrypt: Cifra os arquivos colocados nesta pasta, gerando automaticamente uma chave de cifragem e um vetor de inicialização. Os arquivos cifrados e os arquivos com a chave e o vetor são movidos para a pasta Encrypted.
. Encrypted: Armazena os arquivos cifrados e os arquivos com a chave (key-file.txt) e o vetor de inicialização (iv-file.txt).
. Decrypt: Decifra os arquivos colocados nesta pasta, usando os arquivos de chave e vetor correspondentes. Os arquivos decifrados são movidos para a pasta Decrypted.
. Decrypted: Armazena os arquivos decifrados.
. Sign: Assina digitalmente os arquivos colocados nesta pasta, usando uma chave privada. Os arquivos assinados são movidos para a pasta Signed.
. Assinado: Armazena os arquivos assinados.
. Verify: Verifica as assinaturas digitais dos arquivos colocados nesta pasta, usando uma chave pública. Os arquivos com assinaturas válidas são movidos para a pasta Valid-Sign, enquanto os arquivos com assinaturas inválidas são movidos para a pasta Not-Valid-Sign.
. Valid-Sign: Armazena os arquivos com assinaturas válidas.
. Not-Valid-Sign: Armazena os arquivos com assinaturas inválidas.
. Digest: Calcula os valores de hash dos arquivos colocados nesta pasta. Os arquivos e seus hashes são movidos para a pasta Hashes.
. Hashes: Armazena os arquivos e seus valores de hash.
. Integrity: Verifica a integridade dos arquivos colocados nesta pasta, comparando-os com os valores de hash fornecidos. Os arquivos com integridade verificada são movidos para a pasta Int-Valid, enquanto os arquivos com integridade comprometida são movidos para a pasta Int-not-Valid.
. Int-Valid: Armazena os arquivos com integridade verificada.
. Int-not-Valid: Armazena os arquivos com integridade comprometida.

Funcionalidades
. Cifrar Arquivos:
Gera automaticamente uma chave de cifragem e um vetor de inicialização.
Move os arquivos cifrados e os arquivos de chave e vetor para a pasta Encrypted.

. Decifrar Arquivos:
Usa os arquivos de chave e vetor para decifrar arquivos.
Move os arquivos decifrados para a pasta Decrypted.

. Assinatura Digital:
Usa uma chave privada para assinar digitalmente arquivos.
Move os arquivos assinados para a pasta Signed.

. Verificação de Assinatura Digital:
Usa uma chave pública para verificar assinaturas digitais.
Move os arquivos com assinaturas válidas para a pasta Valid_Sign.
Move os arquivos com assinaturas inválidas para a pasta NotValid_Sign.

. Cálculo de Hashes:
Calcula os valores de hash dos arquivos.
Move os arquivos e seus valores de hash para a pasta Hashes.

. Verificação de Integridade:
Verifica a integridade dos arquivos comparando-os com os valores de hash fornecidos.
Move os arquivos com integridade verificada para a pasta Integrity_Valid.
Move os arquivos com integridade comprometida para a pasta IntegrityNot_Valid.

Tecnologias Utilizadas:
. Python: Linguagem de programação principal usada para desenvolver a aplicação.
. Watchdog: Biblioteca usada para monitorar as pastas e detectar mudanças.
. PyCryptodome: Biblioteca usada para operações criptográficas.

Como Usar:
Instalação das Dependências:
Instale as bibliotecas necessárias usando o comando:
. pip install watchdog pycryptodome

Estrutura de Pastas:
Certifique-se de que todas as pastas necessárias estão criadas conforme a estrutura descrita acima.
Execução dos Scripts:
Execute cada script Python em terminais separados para iniciar os daemons que monitoram as pastas:
python cifrar.py
python decifrar.py
python assinar.py
python verificar_assinatura.py
python calcular_hash.py
python verificar_integridade.py

Movimentação de Arquivos:
Mova os arquivos para as pastas correspondentes conforme a operação desejada.

Segurança e Melhorias:
. Controle de Acesso: Restringir o acesso a pastas críticas.
. Verificação de Integridade: Implementar verificações de integridade para arquivos críticos.
. Logs e Auditoria: Manter registros detalhados das operações feitas.
