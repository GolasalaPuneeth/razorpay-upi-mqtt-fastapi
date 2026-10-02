
#!/bin/bash

set -e

echo "======================================"
echo " Docker Installation & Setup"
echo "======================================"

# Check if Docker is already installed
if command -v docker &> /dev/null; then
    echo "Docker is already installed."
    docker --version
else
    echo "Docker not found. Installing Docker..."

    sudo apt-get update

    sudo apt-get install -y ca-certificates curl

    sudo install -m 0755 -d /etc/apt/keyrings

    sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
        -o /etc/apt/keyrings/docker.asc

    sudo chmod a+r /etc/apt/keyrings/docker.asc

    sudo tee /etc/apt/sources.list.d/docker.sources > /dev/null <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

    sudo apt-get update

    sudo apt-get install -y \
        docker-ce \
        docker-ce-cli \
        containerd.io \
        docker-buildx-plugin \
        docker-compose-plugin

    echo "Docker installation completed."
fi

# Ensure Docker service is running
if ! systemctl is-active --quiet docker; then
    echo "Starting Docker service..."
    sudo systemctl enable --now docker
else
    echo "Docker service is already running."
fi

# Check Docker Compose
if docker compose version &> /dev/null; then
    echo "Docker Compose is available."
    docker compose version
else
    echo "Docker Compose plugin is missing. Installing..."

    sudo apt-get update
    sudo apt-get install -y docker-compose-plugin
fi

# Add current user to Docker group
if ! getent group docker > /dev/null; then
    sudo groupadd docker
fi

if ! id -nG "$USER" | grep -qw docker; then
    sudo usermod -aG docker "$USER"
    echo "User added to Docker group."
else
    echo "User already belongs to Docker group."
fi

echo ""
echo "======================================"
echo " Docker Setup Completed Successfully!"
echo "======================================"

docker --version
docker compose version

echo ""
echo "Run 'newgrp docker' to activate group permissions."