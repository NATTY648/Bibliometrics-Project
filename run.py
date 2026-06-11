# run.py（调试版）
import sys
from pathlib import Path

# -------------- 基础路径检查 --------------
print("="*50)
print("[INFO] 调试日志开始")
print("当前工作目录:", Path.cwd())
print("run.py 所在目录:", Path(__file__).parent)

# 把 src 加入模块搜索路径
project_root = Path(__file__).parent
src_path = project_root / "src"
print("src 目录路径:", src_path)
print("src 目录是否存在?", src_path.exists())

sys.path.append(str(src_path))
print("sys.path 已添加 src:", src_path in sys.path)
print("="*50)

# -------------- 测试导入 bmmini 包 --------------
try:
    print("1/3 尝试导入 bmmini 包...")
    import bmmini
    print("[SUCCESS] 成功导入 bmmini 包")
    print("bmmini 包路径:", bmmini.__file__)
except Exception as e:
    print("[ERROR] 导入 bmmini 包失败")
    print("错误类型:", type(e).__name__)
    print("错误详情:", str(e))
    print("sys.path 内容:", sys.path)
    sys.exit(1)

# -------------- 测试导入 pipeline 主函数 --------------
try:
    print("\n2/3 尝试导入 pipeline.main 函数...")
    from bmmini.pipeline import main
    print("[SUCCESS] 成功导入 pipeline.main 函数")
except Exception as e:
    print("[ERROR] 导入 pipeline.main 函数失败")
    print("错误类型:", type(e).__name__)
    print("错误详情:", str(e))
    sys.exit(1)

# -------------- 执行主函数 --------------
# 如果命令行没有提供参数，则默认使用 --use-wos（用于运行期末作业的 WoS 癌症文献数据集）
if len(sys.argv) <= 1:
    print("\n3/3 准备调用 main() 函数，未检测到命令行参数，默认添加 --use-wos 参数...")
    sys.argv.append("--use-wos")
else:
    print(f"\n3/3 准备调用 main() 函数，使用提供的参数: {sys.argv[1:]}")

try:
    print("[RUNNING] 正在执行 pipeline 主流程...")
    main()
    print("\n[SUCCESS] pipeline 执行完成！")
except Exception as e:
    print("\n[ERROR] pipeline 执行中出错了")
    print("错误类型:", type(e).__name__)
    print("错误详情:", str(e))
    import traceback
    traceback.print_exc()
    sys.exit(1)