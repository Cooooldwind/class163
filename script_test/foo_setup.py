from cx_Freeze import setup, Executable

build_exe_options = {
    'packages': (),  # 默认可不填，程序会自动寻找依赖，如果运行时，提示有缺少的包，可以在这里添加
    'excludes': (),
    "include_files": ()  # 可以添加程序用到的其他文件，如配置文件等
}

setup(
    name="YourApp",
    version="0.1",
    description="A simple cx_Freeze example",
    options={"build_exe": build_exe_options},
    executables=[Executable("foo_test.py")]
)
