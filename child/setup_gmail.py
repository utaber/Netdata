from pathlib import Path


def set_config(path, key, val):
    path = Path(path)
    lines = path.read_text().splitlines()

    for i, line in enumerate(lines):
        if line.startswith(f"{key} "):
            lines[i] = f"{key} {val}"
#            break
#        else:
#            print("error")

        path.write_text("\n".join(lines) + "\n")


keys = ["from", "user", "password"]

for i in keys:
    val = input(f"set your {i}:")
    set_config("msmtprc", i, val)
