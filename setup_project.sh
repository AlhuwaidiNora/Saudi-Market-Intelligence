#!/bin/bash

# Navigate to your project root
cd ~/saudi-market-intelligence/Saudi-Market-Intelligence

# Backend additions
mkdir -p backend/app/tests
mkdir -p backend/app/alembic
mkdir -p backend/app/schemas
mkdir -p backend/app/middleware
mkdir -p backend/app/utils
touch backend/app/tests/__init__.py
touch backend/app/tests/test_main.py
touch backend/app/middleware/__init__.py
touch backend/app/middleware/auth.py
touch backend/app/middleware/logging.py
touch backend/app/schemas/__init__.py
touch backend/app/schemas/base.py
touch backend/app/utils/__init__.py
touch backend/app/utils/helpers.py

# Frontend additions
mkdir -p frontend/src/components
mkdir -p frontend/src/pages
mkdir -p frontend/src/styles
mkdir -p frontend/src/types
mkdir -p frontend/public
mkdir -p frontend/tests
touch frontend/src/components/index.ts
touch frontend/src/pages/index.ts
touch frontend/src/styles/globals.css
touch frontend/src/types/index.ts
touch frontend/tests/setup.ts

# Data Pipeline additions
mkdir -p data_pipeline/transformers
mkdir -p data_pipeline/tests
mkdir -p data_pipeline/configs
mkdir -p data_pipeline/logging
touch data_pipeline/transformers/__init__.py
touch data_pipeline/transformers/etl.py
touch data_pipeline/configs/pipeline_config.yaml
touch data_pipeline/logging/logger.py

# Root level additions
mkdir -p docs
mkdir -p scripts
mkdir -p monitoring
mkdir -p k8s

# Create documentation files
touch docs/README.md
touch docs/ARCHITECTURE.md
touch docs/API.md
touch docs/DEPLOYMENT.md

# Create basic configuration files
touch .env.example
touch scripts/setup.sh
touch scripts/deploy.sh
touch monitoring/prometheus.yml
touch k8s/deployment.yaml
touch k8s/service.yaml

# Make scripts executable
chmod +x scripts/setup.sh
chmod +x scripts/deploy.sh

# Create a basic .gitignore if it doesn't exist
if [ ! -f .gitignore ]; then
    echo "# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg

# Node
node_modules/
npm-debug.log
yarn-debug.log
yarn-error.log

# Environment variables
.env
.env.local
.env.*.local

# IDE
.idea/
.vscode/
*.swp
*.swo

# System
.DS_Store
Thumbs.db

# Project specific
/data_pipeline/logging/*.log
/monitoring/data/
" > .gitignore
fi

echo "Directory structure has been created successfully!"
