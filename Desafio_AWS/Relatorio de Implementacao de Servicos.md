# RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS - ABSTERGO PHARMA

**Data:** 04/01/2026
**Empresa:** Abstergo Pharma (Plataforma de Farmácia Virtual)
**Responsável:** Luiz

## Introdução
Este relatório detalha a arquitetura de serviços AWS implementada para a Abstergo Pharma. O projeto visa sustentar uma plataforma de e-commerce farmacêutico que exige alta disponibilidade, segurança rigorosa de dados sensíveis e escalabilidade para picos de acesso.

## Descrição do Projeto

### Etapa 1: Amazon EC2 (Elastic Compute Cloud) com Auto Scaling
- **Foco da ferramenta:** Processamento e Escalabilidade.
- **Descrição de caso de uso:** Hospedagem do servidor Back-end da farmácia. Através do Auto Scaling, a plataforma ajusta o número de instâncias ativas conforme a demanda de usuários, garantindo que o sistema não fique lento durante horários de pico e economizando recursos em períodos ociosos.

### Etapa 2: Amazon RDS (Relational Database Service)
- **Foco da ferramenta:** Banco de Dados Relacional Gerenciado.
- **Descrição de caso de uso:** Utilizado para gerenciar o inventário de medicamentos, registros de clientes e histórico de pedidos. O RDS oferece backups automáticos e alta disponibilidade via Multi-AZ, o que é crítico para manter a operação da farmácia 24/7 sem perda de dados.

### Etapa 3: Amazon S3 (Simple Storage Service)
- **Foco da ferramenta:** Armazenamento de Objetos.
- **Descrição de caso de uso:** O S3 é utilizado para hospedar o Front-end estático da aplicação e armazenar imagens de produtos e documentos digitalizados de receitas médicas. Isso remove a carga de armazenamento dos servidores de aplicação, reduzindo custos e aumentando a velocidade de entrega de conteúdo.

## Conclusão
A arquitetura proposta para a Abstergo Pharma utiliza o estado da arte em serviços de nuvem. A implementação resulta em uma infraestrutura resiliente e econômica, permitindo que a farmácia virtual opere com segurança e eficiência. Recomenda-se a futura implementação do AWS CloudFront para acelerar ainda mais o acesso global à plataforma.

## Anexos

### Arquitetura da Solução (Visualização ASCII)
```text
[ Usuário ] -> [ Route 53 ] -> [ CloudFront ] -> [ S3 (Frontend) ]
                                     |
                               [ Load Balancer ]
                                     |
                            [ EC2 Auto Scaling ] -> [ RDS (Database) ]