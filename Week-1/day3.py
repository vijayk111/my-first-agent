def calculate_uptime(days, hours=0):
    return (days * 24)+hours

print(calculate_uptime(5))
print(calculate_uptime(5, hours=2))
print(calculate_uptime(5, 3))


def list_installed_apps(*apps):
    for app in apps:
        print(f"Installing {app} via uv...")

list_installed_apps("vlc", "sublime", "git")


def configure_server(hostname, **settings):
    print(f"Configuring {hostname}")
    for key, value in settings.items():
        print(f" - Setting {key} to {value}")

configure_server("web-prod-01", ip="192.0.0.1", port=80, firewall=True)


def get_user_id(username: str) -> int:
    return len(username)*100

print(f"User ID: {get_user_id("vijay")}")