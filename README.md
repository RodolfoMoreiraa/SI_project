🔐 Projeto de Segurança Informática

Uma aplicação em Python que automatiza operações fundamentais de segurança informática através da monitorização de pastas. Com funcionalidades como cifragem, assinatura digital, hashes e verificação de integridade, esta aplicação permite aplicar técnicas de segurança de forma prática e transparente.

📦 Funcionalidades Principais

🔒 Cifragem e Decifragem de Arquivos

✍️ Assinatura Digital e Verificação

🧮 Cálculo de Hashes

🛡️ Verificação de Integridade de Arquivos

🗂️ Estrutura de Pastas
A aplicação monitoriza as seguintes pastas para executar automaticamente as operações:

Pasta
Encrypt/	Arquivos colocados aqui serão cifrados automaticamente

Encrypted/	Guarda os arquivos cifrados, a chave (key-file.txt) e o vetor (iv-file.txt)

Decrypt/	Decifra os arquivos usando a chave e vetor correspondentes

Decrypted/	Guarda os arquivos já decifrados

Sign/	Assina digitalmente os arquivos com chave privada

Signed/	Guarda os arquivos assinados

Verify/	Verifica a assinatura digital com chave pública

Valid-Sign/	Arquivos com assinatura válida

Not-Valid-Sign/	Arquivos com assinatura inválida

Digest/	Calcula o hash dos arquivos

Hashes/	Guarda os arquivos e os seus valores de hash

Integrity/	Verifica a integridade dos arquivos (com base nos hashes)

Int-Valid/	Arquivos com integridade confirmada

Int-not-Valid/	Arquivos com integridade comprometida

⚙️ Tecnologias Utilizadas
Python – Linguagem principal

Watchdog – Monitorização em tempo real das pastas

PyCryptodome – Operações criptográficas seguras

▶️ Como Usar
1. Instalação das Dependências

pip install watchdog pycryptodome

2. Criar a Estrutura de Pastas
Certifica-te que todas as pastas listadas acima estão criadas no diretório do projeto.

3. Executar os Scripts
Em terminais separados, executa cada um dos scripts para iniciar os daemons de monitorização:

python cifrar.py

python decifrar.py

python assinar.py

python verificar_assinatura.py

python calcular_hash.py

python verificar_integridade.py

4. Usar a Aplicação
Basta mover os arquivos para as pastas respetivas consoante a operação que pretendes realizar. O sistema faz o resto de forma automática. 🚀
