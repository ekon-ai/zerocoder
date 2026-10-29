# ZeroCoder

A collection of useful projects for zerocoders

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Building and Running](#building-and-running)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following installed:
- [Git](https://git-scm.com/downloads) (v2.30+)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (v0.4+)
- [Python](https://www.python.org/downloads/) (v3.9+) — optional, `uv` can install and manage Python for you

Verify installations:
```bash
git --version
uv --version
```

> **Installing uv:**
> - **Linux / macOS:** `curl -LsSf https://astral.sh/uv/install.sh | sh`
> - **Windows (PowerShell):** `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
> - **Via pipx:** `pipx install uv`

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ekon-ai/zerocoder.git
cd zerocoder/vpa
```

### 2. Sync dependencies with uv

`uv` automatically creates and manages the virtual environment (`.venv`) and installs all dependencies:

```bash
uv sync
```

If the project uses optional dependency groups (e.g. dev tools):

```bash
uv sync --all-extras
```

### 3. Activate the environment (optional)

`uv run vpa02` works without activation, but you can activate `.venv` if you prefer:

**Linux / macOS:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.\.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

## Building and Running

### Run the application

Use `uv run vpa02` to execute commands inside the managed environment without manual activation:

```bash
uv run vpa02
```


### Build a distributable package (optional)

```bash
uv build
```

This generates wheel (`.whl`) and source (`.tar.gz`) files in the `dist/` directory.

### Development mode

`uv sync` already installs the project in editable mode, so code changes take effect immediately. To update dependencies after editing `pyproject.toml`:

```bash
uv lock
uv sync
```

## Configuration

Copy the sample environment file and adjust the values:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
APP_ENV=development
API_KEY=your-api-key-here
DEBUG=true
```

## Contributing

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/my-new-feature
   ```
3. Add or update dependencies (if needed):
   ```bash
   uv add <package-name>
   uv add --dev <package-name>
   ```
4. Commit your changes:
   ```bash
   git commit -m "Add my new feature"
   ```
5. Push to your branch:
   ```bash
   git push origin feature/my-new-feature
   ```
6. Open a Pull Request.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and development process.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `uv: command not found` | Restart your shell or add `~/.local/bin` (Linux/macOS) or `%USERPROFILE%\.local\bin` (Windows) to your PATH |
| `uv sync` fails resolving dependencies | Run `uv lock --upgrade` to refresh the lockfile, then `uv sync` again |
| Wrong Python version selected | Pin it explicitly: `uv python pin 3.11` then `uv sync` |
| Permission denied on activation scripts | On Linux/macOS run `chmod +x .venv/bin/activate`; on Windows use `Set-ExecutionPolicy RemoteSigned` |

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
```