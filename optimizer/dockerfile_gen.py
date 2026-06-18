class DockerfileOptimizer:
    def optimize(self, path):
        return [
            "Use multi-stage builds",
            "Combine RUN commands to reduce layers",
            "Use .dockerignore",
            "Pin package versions",
            "Use distroless/Alpine base images"
        ]
    def multi_stage(self, lang="python"):
        if lang == "python":
            return "FROM python:3.11-slim AS b\nWORKDIR /app\nCOPY . .\nRUN pip install -r requirements.txt\n\nFROM python:3.11-slim\nCOPY --from=b /app /app\nCMD [\"python\", \"main.py\"]"
