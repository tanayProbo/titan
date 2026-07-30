# Contributing to TITAN-X

Thank you for considering contributing to TITAN-X! Every contribution, big or small, is greatly appreciated.

## 🚀 How to Contribute

### Reporting Bugs
- Open a [GitHub Issue](https://github.com/tanayProbo/titan/issues) with a clear title and description.
- Include steps to reproduce, expected behavior, and actual behavior.
- Add relevant logs or screenshots where possible.

### Suggesting Features
- Open an issue with the `enhancement` label.
- Describe the feature and the problem it solves.

### Submitting Pull Requests

1. **Fork** the repository.
2. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Write clean, documented code** following the existing style.
4. **Run tests** before submitting:
   ```bash
   pytest titan/tests/
   ```
5. **Commit** your changes with a clear message:
   ```bash
   git commit -m "feat: add your feature description"
   ```
6. **Push** to your fork and open a **Pull Request** against `main`.

## 🧪 Development Setup

```bash
git clone https://github.com/tanayProbo/titan.git
cd titan
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 📐 Code Style
- Follow **PEP 8** guidelines.
- Add docstrings to all public classes and functions.
- Keep functions focused and small.

## 📜 License
By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
