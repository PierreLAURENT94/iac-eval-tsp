FROM ubuntu:22.04

WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget curl unzip git bash build-essential && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Terraform
RUN wget https://releases.hashicorp.com/terraform/1.5.6/terraform_1.5.6_linux_amd64.zip && \
    unzip terraform_1.5.6_linux_amd64.zip && \
    mv terraform /usr/local/bin/ && \
    rm terraform_1.5.6_linux_amd64.zip

# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

# Install OPA
RUN wget https://openpolicyagent.org/downloads/v0.60.0/opa_linux_amd64_static && \
    chmod +x opa_linux_amd64_static && \
    mv opa_linux_amd64_static /usr/local/bin/opa

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/conda && \
    rm miniconda.sh
ENV PATH="/opt/conda/bin:$PATH"

# Copy environment.yml and setup.sh
COPY environment.yml setup.sh ./

# Create and activate Conda environment
RUN conda env create -f environment.yml && conda clean -a
ENV PATH="/opt/conda/envs/iac-eval/bin:$PATH"
ENV CONDA_DEFAULT_ENV=iac-eval

COPY entrypoint-iac-eval.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Copy project files
COPY . .