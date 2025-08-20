import getpass
import os


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

# 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
# _set_env("OPENAI_API_KEY")
# _set_env("COHERE_API_KEY")
# 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
# _set_env("TAVILY_API_KEY")
print(os.environ.get("OPENAI_API_KEY"))  # 检查是否已有值
print(os.environ.get("TAVILY_API_KEY"))  # 检查是否已有值
os.environ['OPENAI_API_KEY'] = "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"
os.environ['TAVILY_API_KEY'] = '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'
print(os.environ.get("OPENAI_API_KEY"))  # 检查是否已有值
print(os.environ.get("TAVILY_API_KEY"))  # 检查是否已有值
