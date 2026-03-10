# The Ubuntu Command builder

def build_ubuntu_cmd(base_cmd: str, *packages, **options) -> str:
    full_cmd= f"{base_cmd} {' '.join(packages)}"

    for key, value in options.items():
        if value is True:
            full_cmd+=f" --{key}"
        else:
            full_cmd+=f" --{key}={value}"
    
    return full_cmd

my_script = build_ubuntu_cmd("sudo apt install", "curl", "wget", "git", quite=True, retry=5)
print(f"Generated Command: \n{my_script}")