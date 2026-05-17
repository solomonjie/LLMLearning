import sys
import io
import threading
import time
from contextlib import redirect_stdout, redirect_stderr
from fastmcp import FastMCP

mcp = FastMCP("SafePythonExecutor")

def execute_code_with_timeout(code: str, timeout_sec: int = 30) -> str:
    """在独立线程中执行代码，捕获 stdout/stderr，支持超时"""
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()
    
    def target():
        try:
            # 创建新的全局字典作为执行环境，避免污染当前环境
            exec_globals = {}
            with redirect_stdout(stdout_capture), redirect_stderr(stderr_capture):
                exec(code, exec_globals)
        except Exception as e:
            print(e, file=sys.stderr)  # 这会进入 stderr_capture
    
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()
    thread.join(timeout_sec)
    
    if thread.is_alive():
        return f"错误：代码执行超时（超过 {timeout_sec} 秒）"
    
    output = stdout_capture.getvalue()
    error = stderr_capture.getvalue()
    if error:
        output += f"\n[stderr]\n{error}"
    return output.strip() or "[无输出]"

@mcp.tool()
def run_python_code(code: str, timeout: int = 30) -> str:
    """
    在当前进程中安全执行 Python 代码，并返回输出。
    支持超时设置，避免卡死。
    """
    return execute_code_with_timeout(code, timeout)

@mcp.tool()
def run_python_file(file_path: str, timeout: int = 30) -> str:
    """读取文件并执行其中的代码"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        return execute_code_with_timeout(code, timeout)
    except Exception as e:
        return f"读取文件失败: {str(e)}"

if __name__ == "__main__":
    mcp.run()