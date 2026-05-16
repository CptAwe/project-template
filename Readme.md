# Project

A template for a project to show off git functionality and github CI/CD

## Development

VScode debugger:

```json
{
    "name": "Run",
    "type": "debugpy",
    "request": "launch",
    "python": "${workspaceFolder}/.venv/bin/python",
    "cwd": "${workspaceFolder}/src",
    "program": "${workspaceFolder}/src/main.py",
    "console": "integratedTerminal"
}
```

Swagger: `http://localhost:8000/docs`

Redocs: `http://localhost:8000/redoc`

## Deployment
