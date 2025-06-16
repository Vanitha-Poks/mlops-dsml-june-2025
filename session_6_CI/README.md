# Session 6: Continuous Integration (CI) with Python, Flask, and Docker

This session demonstrates Continuous Integration practices using Python testing frameworks, Flask web applications, Docker containerization, and GitHub Actions workflows.

## 📋 Overview

This session covers:
- **Unit Testing** with pytest
- **Flask Web Application** development
- **Docker** containerization
- **GitHub Actions** CI/CD pipeline
- **Machine Learning** model deployment

## 🗂️ Project Structure

```
session_6_CI/
├── README.md                     # This file
├── base_file.py                  # Core mathematical functions
├── hello.py                      # Flask web application with ML prediction
├── test_some_random_code_v2.py   # Unit tests for base functions
├── test_flask.py                 # Flask application tests
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Container configuration
├── classifier.pkl                # Pre-trained ML model
├── train_ml.ipynb               # Model training notebook
├── demonstration.ipynb          # CI/CD demonstration
└── artefacts/
    └── requirements.txt         # Container-specific dependencies
```

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Docker (optional)
- Git

### Local Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Tests**
   ```bash
   pytest
   ```

3. **Start Flask Application**
   ```bash
   python -m flask --app hello.py run
   # Or using Flask CLI
   flask --app hello.py run
   ```

4. **Access Application**
   - Main page: http://127.0.0.1:5000/
   - Hello endpoint: http://127.0.0.1:5000/hello
   - Prediction endpoint: http://127.0.0.1:5000/predict

## 🧪 Testing Framework

### Unit Tests (`test_some_random_code_v2.py`)
Tests for basic mathematical operations:
- **Addition** - `test_first_test_of_this_lecture()`
- **Subtraction** - `test_subtract_but_can_be_anything()`
- **Multiplication** - `test_multiply()`
- **Division** - `test_divide()`

### Flask Tests (`test_flask.py`)
Tests for web application endpoints:
- **Hello endpoint** testing
- **ML prediction endpoint** testing
- **Pytest fixtures** for test client setup

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest test_some_random_code_v2.py

# Run with verbose output
pytest -v

# Run Flask tests
pytest test_flask.py
```

## 🌐 Flask Application Features

### Endpoints

1. **`/` (GET)** - Animated homepage with vibrant CSS animations
2. **`/hello` (GET)** - JSON response with greeting message
3. **`/predict` (POST)** - ML model prediction endpoint

### Prediction API
```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "feature1": 1.0,
    "feature2": 2.0,
    "feature3": 3.0,
    "feature4": 4.0
  }'
```

## 🐳 Docker Containerization

### Build Docker Image
```bash
docker build -t flask-ci-app .
```

### Run Container
```bash
# Run on port 8000
docker run -p 8000:8000 flask-ci-app

# Run with custom name
docker run -p 8000:8000 --name flask-ci-container flask-ci-app
```

### Docker Configuration
- **Base Image**: `python:3.10-slim`
- **Working Directory**: `/flask-loan-app`
- **Exposed Port**: 8000
- **Entry Command**: Flask application startup

## ⚙️ CI/CD Pipeline

### GitHub Actions Workflow (`.github/workflows/ci_cd.yaml`)

**Job 1: Testing**
- Checkout code
- Set up Python 3.10
- Install dependencies
- Run pytest

**Job 2: Docker Build & Deploy**
- Depends on Job 1 success
- Build Docker image
- Push to Docker Hub
- Deploy container

### Pipeline Triggers
- Push to `main` branch
- Push to `any-feature-branch`

### Secrets Configuration
Required GitHub secrets:
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

## 🤖 Machine Learning Integration

### Model Details
- **File**: `classifier.pkl`
- **Type**: Classification model
- **Features**: 4 input features expected
- **Framework**: scikit-learn

### Training
The model training process is documented in:
- `train_ml.ipynb` - Model training notebook
- `demonstration.ipynb` - CI/CD demonstration

## 📦 Dependencies

### Core Dependencies (`requirements.txt`)
```
Flask==3.0.3
scikit-learn==1.6.1
pytest==7.4.4
```

### Additional Libraries
- **joblib** - Model serialization
- **numpy** - Numerical computations

## 🔧 Development Workflow

1. **Write Code** - Implement features in Python
2. **Write Tests** - Create corresponding test cases
3. **Local Testing** - Run `pytest` locally
4. **Commit & Push** - Trigger CI pipeline
5. **Automated Testing** - GitHub Actions runs tests
6. **Docker Build** - Automatic containerization
7. **Deployment** - Container deployment

## 📈 Best Practices Demonstrated

- **Test-Driven Development** - Comprehensive test coverage
- **Code Organization** - Separation of concerns
- **Containerization** - Docker for consistent environments
- **Automation** - CI/CD pipeline automation
- **Error Handling** - Proper exception handling in divide function
- **Documentation** - Comprehensive README and docstrings

## 🚨 Common Issues & Solutions

### Test Failures
```bash
# Check test output
pytest -v -s

# Run specific failing test
pytest test_file.py::test_function_name
```

### Docker Issues
```bash
# Check container logs
docker logs <container_name>

# Remove all containers
docker container prune
```

### Flask Issues
```bash
# Check if port is in use
lsof -i :5000

# Run on different port
flask --app hello.py run --port 5001
```

## 📚 Learning Objectives

By completing this session, you will understand:
- **pytest** framework for Python testing
- **Flask** web application development
- **Docker** containerization principles
- **GitHub Actions** CI/CD setup
- **ML model** integration in web apps
- **Best practices** for software development lifecycle

## 🔗 Additional Resources

- [pytest Documentation](https://docs.pytest.org/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

**Note**: This session is part of the MLOps DSML June 2025 course curriculum focusing on DevOps practices for machine learning applications.
