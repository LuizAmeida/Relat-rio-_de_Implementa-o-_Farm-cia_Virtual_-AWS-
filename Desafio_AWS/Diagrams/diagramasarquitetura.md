graph TD
    A[Usuário/Cliente] -->|Acessa URL| B[Amazon CloudFront]
    B -->|Frontend Estático| C[Amazon S3 Bucket]
    B -->|API Requests| D[Application Load Balancer]
    D --> E[EC2 Auto Scaling Group]
    E --> F[Amazon RDS - Banco de Dados]
    E --> G[Amazon SNS - Alerta de Falta de Medicamento]