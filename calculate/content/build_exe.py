#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
自动化打包脚本
使用PyInstaller将Python程序打包成可执行文件
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_pyinstaller():
    """检查PyInstaller是否已安装"""
    try:
        import PyInstaller
        print("✓ PyInstaller 已安装")
        return True
    except ImportError:
        print("✗ PyInstaller 未安装")
        return False

def install_pyinstaller():
    """安装PyInstaller"""
    print("正在安装 PyInstaller...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
        print("✓ PyInstaller 安装成功")
        return True
    except subprocess.CalledProcessError:
        print("✗ PyInstaller 安装失败")
        return False

def build_executable():
    """使用PyInstaller打包程序"""
    script_name = "calculate.py"
    app_name = "乘数组合计算器"
    
    if not Path(script_name).exists():
        print(f"✗ 找不到源文件: {script_name}")
        return False
    
    # PyInstaller命令参数
    cmd = [
        "pyinstaller",
        "--onefile",              # 打包成单个可执行文件
        "--windowed",             # Windows下不显示控制台窗口
        "--name", app_name,       # 指定可执行文件名称
        "--clean",                # 清理临时文件
        script_name
    ]
    
    print(f"正在打包 {script_name}...")
    try:
        subprocess.run(cmd, check=True)
        print("✓ 打包成功！")
        
        # 检查生成的文件
        dist_dir = Path("dist")
        if dist_dir.exists():
            exe_files = list(dist_dir.glob("*.exe"))
            if exe_files:
                print(f"✓ 可执行文件已生成: {exe_files[0]}")
            else:
                print("✓ 可执行文件已生成在 dist 目录中")
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ 打包失败: {e}")
        return False

def cleanup():
    """清理临时文件"""
    dirs_to_remove = ["build", "__pycache__"]
    files_to_remove = ["*.spec"]
    
    for dir_name in dirs_to_remove:
        if Path(dir_name).exists():
            shutil.rmtree(dir_name)
            print(f"✓ 已清理临时目录: {dir_name}")
    
    import glob
    for pattern in files_to_remove:
        for file_path in glob.glob(pattern):
            os.remove(file_path)
            print(f"✓ 已清理临时文件: {file_path}")

def main():
    """主函数"""
    print("=" * 50)
    print("乘数组合计算器 - 自动打包工具")
    print("=" * 50)
    
    # 检查并安装PyInstaller
    if not check_pyinstaller():
        if not install_pyinstaller():
            print("无法安装PyInstaller，请手动安装后重试")
            return
    
    # 打包程序
    if build_executable():
        print("\n" + "=" * 50)
        print("打包完成！")
        print("可执行文件位置: dist/乘数组合计算器.exe")
        print("您可以将这个文件复制到其他计算机上运行")
        print("=" * 50)
        
        # 询问是否清理临时文件
        response = input("\n是否清理临时文件？(y/n): ").lower()
        if response in ['y', 'yes', '是']:
            cleanup()
    else:
        print("打包失败，请检查错误信息")

if __name__ == "__main__":
    main() 