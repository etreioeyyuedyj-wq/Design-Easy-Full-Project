def run_defp(code):
    variables = {}

    for line in code.splitlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith("say "):
            value = line[4:].strip()

            if value in variables:
                print(variables[value])
            elif value.startswith('"') and value.endswith('"'):
                print(value[1:-1])
            else:
                try:
                    print(eval(value, {"__builtins__": {}}, variables))
                except Exception:
                    print(value)

        elif line.startswith("set "):
            statement = line[4:]

            if "=" in statement:
                name, value = statement.split("=", 1)
                name = name.strip()
                value = value.strip()

                if value.startswith('"') and value.endswith('"'):
                    variables[name] = value[1:-1]
                else:
                    try:
                        variables[name] = eval(
                            value,
                            {"__builtins__": {}},
                            variables
                        )
                    except Exception:
                        variables[name] = value


if __name__ == "__main__":
    with open("examples/hello.defp", "r", encoding="utf-8") as file:
        code = file.read()

    run_defp(code)
