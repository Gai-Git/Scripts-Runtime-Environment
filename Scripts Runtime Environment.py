import subprocess
import time
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    start_time = time.time()
    try:
        #安装所需的Python库
        install("pandas")
        install("sqlalchemy")
        install("openpyxl")
        install("pyarrow")
        install("PyQt6")
        install("beautifulsoup4")
        install("apscheduler")
        install("PyObjC")
        # 提示用户安装ODBC驱动
        print("The Message: 请确保安装了ODBC Driver 17 for SQL Server。")

        # Oracle客户端安装提示
        print("The Message: 请确保安装了Oracle客户端，并正确配置了环境变量。")

        # 其他必要的配置或安装步骤
        # 例如，您可能还需要提示用户进行特定的配置设置或安装额外的软件。

        print("The Message: 环境配置完成。现在您可以运行您的脚本了。")
    except Exception as e:
        print(f"The Error: 安装过程中出现错误：{e}")
    end_time = time.time()
    execution = end_time - start_time
    print(f"{execution}")

if __name__ == "__main__":
    main()
