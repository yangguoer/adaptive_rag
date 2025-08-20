import getpass
import os


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

print(os.environ.get("OPENAI_API_KEY"))  # 检查是否已有值
print(os.environ.get("TAVILY_API_KEY"))  # 检查是否已有值


