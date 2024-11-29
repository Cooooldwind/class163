import os
import importlib.util
import inquirer


def create_default_script():
    default_script_path = os.path.join("foo", "default.py")
    with open(default_script_path, "w") as f:
        f.write("def foo2():\n    print(__file__)\n")


def find_scripts_with_foo2():
    scripts_with_foo2 = []
    script_dir = os.path.join(os.getcwd(), "foo")

    if not os.path.exists(script_dir):
        os.makedirs(script_dir)
        create_default_script()
        return ["default.py"]

    for root, dirs, files in os.walk(script_dir):
        for file in files:
            if file.endswith(".py"):
                script_path = os.path.join(root, file)
                spec = importlib.util.spec_from_file_location(file[:-3], script_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, "foo2"):
                    scripts_with_foo2.append(file)

    if not scripts_with_foo2:
        create_default_script()
        return ["default.py"]

    return scripts_with_foo2


if __name__ == "__main__":
    scripts = find_scripts_with_foo2()

    questions = [
        inquirer.List(
            "script_choice",
            message="请选择要执行的包含foo2函数的脚本：",
            choices=scripts,
        )
    ]

    answers = inquirer.prompt(questions)

    if answers:
        selected_script = answers["script_choice"]
        spec = importlib.util.spec_from_file_location(
            selected_script[:-3], os.path.join("foo", selected_script)
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        module.foo2()
