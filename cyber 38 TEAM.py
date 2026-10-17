
#!/usr/bin/env python3
import os
import ssl
import json
import socket
import urllib.request
import urllib.error
from datetime import datetime
from urllib.parse import urlparse

GREEN = "\033[92m"
WHITE = "\033[97m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "reports")
os.makedirs(REPORT_DIR, exist_ok=True)


def banner():
    os.system("clear")
    print(GREEN + r"""
   ____  __   __ ____  _____ ____      _____ ____
  / ___| \ \ / /| __ )| ____|  _ \    |_   _| ___|
 | |      \ V / |  _ \|  _| | |_) |     | | |___ \
 | |___    | |  | |_) | |___|  _ <     | |  ___) |
  \____|   |_|  |____/|_____|_| \_\    |_| |____/
""" + RESET)
    print(CYAN + "          CYBER 38 TEAM" + RESET)
    print(GREEN + "     PREMIUM SECURITY TOOLKIT" + RESET)
    print(WHITE + "   DEVELOPER BOY | MINISTER | HITTER" + RESET)
    print()


def pause():
    input(WHITE + "\nPress Enter to continue..." + RESET)


def get_host(value):
    value = value.strip()
    if "://" not in value:
        value = "https://" + value

    parsed = urlparse(value)

    if parsed.scheme not in ("http", "https"):
        raise ValueError("Only HTTP/HTTPS URLs are supported.")

    if not parsed.hostname:
        raise ValueError("Invalid domain.")

    if parsed.username or parsed.password:
        raise ValueError("Credentials in URLs are not allowed.")

    return value, parsed.hostname, parsed.port or (
        443 if parsed.scheme == "https" else 80
    )


def save_report(title, data):
    data["tool"] = "CYBER 38 TEAM"
    data["report_type"] = title
    data["created_at"] = datetime.now().isoformat(
        timespec="seconds"
    )

    filename = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    path = os.path.join(REPORT_DIR, filename + ".json")

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

    print(GREEN + "\n[+] Report saved: " + path + RESET)


def dns_check():
    host = input("Domain: ").strip()

    try:
        if "://" in host:
            host = urlparse(host).hostname

        if not host:
            raise ValueError("Invalid domain.")

        results = socket.getaddrinfo(host, None)
        addresses = sorted({item[4][0] for item in results})

        print(GREEN + "\n[+] DNS Results" + RESET)
        for address in addresses:
            print("  " + address)

        save_report("DNS Lookup", {
            "host": host,
            "addresses": addresses
        })

    except (socket.gaierror, ValueError, OSError) as error:
        print(RED + f"DNS Error: {error}" + RESET)


def web_check():
    raw = input("Authorized website URL: ").strip()

    try:
        url, host, port = get_host(raw)

        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "CYBER38-Security-Checker/1.0"
            }
        )

        try:
            with urllib.request.urlopen(
                request, timeout=10
            ) as response:
                status = response.status
                headers = dict(response.headers.items())

        except urllib.error.HTTPError as error:
            status = error.code
            headers = dict(error.headers.items())

        print(GREEN + f"\n[+] HTTP Status: {status}" + RESET)
        print(CYAN + "\nSecurity Headers:" + RESET)

        wanted = [
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "Referrer-Policy"
        ]

        normalized = {
            key.lower(): value
            for key, value in headers.items()
        }

        for name in wanted:
            value = normalized.get(name.lower())
            if value:
                print(GREEN + f"[+] {name}: Present" + RESET)
            else:
                print(RED + f"[-] {name}: Missing" + RESET)

        save_report("Website Check", {
            "url": url,
            "host": host,
            "port": port,
            "status": status,
            "headers": headers
        })

    except Exception as error:
        print(RED + f"Web Error: {error}" + RESET)


def ssl_check():
    raw = input("HTTPS Domain (e.g. example.com): ").strip()

    try:
        if "://" in raw:
            parsed = urlparse(raw)
            if parsed.scheme != "https":
                raise ValueError("An HTTPS URL is required.")
            host = parsed.hostname
            port = parsed.port or 443
        else:
            host = raw
            port = 443

        if not host:
            raise ValueError("Invalid domain.")

        context = ssl.create_default_context()

        with socket.create_connection(
            (host, port), timeout=10
        ) as sock:
            with context.wrap_socket(
                sock, server_hostname=host
            ) as secure:
                cert = secure.getpeercert()
                tls_version = secure.version()
                cipher = secure.cipher()

        print(GREEN + "\n[+] TLS: " + str(tls_version) + RESET)
        print("[+] Valid Until:", cert.get("notAfter", "N/A"))
        print("[+] Issuer:", cert.get("issuer", "N/A"))
        print("[+] Cipher:", cipher[0] if cipher else "N/A")

        save_report("SSL TLS Check", {
            "host": host,
            "tls_version": tls_version,
            "certificate": cert,
            "cipher": cipher
        })

    except Exception as error:
        print(RED + f"SSL Error: {error}" + RESET)


def network_check():
    host = input(
        "Test Host (default: example.com): "
    ).strip() or "example.com"

    print(CYAN + "\nNetwork Diagnostics" + RESET)

    try:
        addresses = sorted({
            item[4][0]
            for item in socket.getaddrinfo(host, None)
        })
        print(GREEN + "[+] DNS resolution successful" + RESET)
    except OSError as error:
        print(RED + f"DNS failed: {error}" + RESET)
        return

    results = []

    for port in (53, 80, 443):
        try:
            with socket.create_connection(
                (host, port), timeout=3
            ):
                result = "reachable"
                print(GREEN + f"[+] TCP {port}: reachable" + RESET)
        except OSError:
            result = "unreachable or filtered"
            print(RED + f"[-] TCP {port}: unavailable" + RESET)

        results.append({
            "port": port,
            "result": result
        })

    save_report("Network Diagnostics", {
        "host": host,
        "addresses": addresses,
        "ports": results
    })


def view_reports():
    files = sorted(
        name for name in os.listdir(REPORT_DIR)
        if name.endswith(".json")
    )

    if not files:
        print("No reports found.")
        return

    print(CYAN + "\nSaved Reports:" + RESET)

    recent = files[-10:]
    for index, name in enumerate(recent, 1):
        print(f"[{index}] {name}")

    choice = input("\nReport number (0 = Back): ").strip()

    if choice == "0":
        return

    try:
        index = int(choice)
        if index < 1 or index > len(recent):
            raise ValueError

        selected = recent[index - 1]

        with open(
            os.path.join(REPORT_DIR, selected),
            encoding="utf-8"
        ) as file:
            print(file.read())

    except (ValueError, IndexError):
        print(RED + "Invalid report number!" + RESET)


def main():
    while True:
        banner()

        print(WHITE + "[1] DNS Lookup")
        print("[2] Website Security Check")
        print("[3] SSL/TLS Certificate Check")
        print("[4] Network Diagnostics")
        print("[5] View Saved Reports")
        print("[0] Exit" + RESET)

        choice = input(CYAN + "\nCYBER38 >> " + RESET).strip()

        if choice == "1":
            dns_check()
            pause()
        elif choice == "2":
            web_check()
            pause()
        elif choice == "3":
            ssl_check()
            pause()
        elif choice == "4":
            network_check()
            pause()
        elif choice == "5":
            view_reports()
            pause()
        elif choice == "0":
            print(GREEN + "\nCYBER 38 TEAM - Goodbye!" + RESET)
            break
        else:
            print(RED + "Invalid option!" + RESET)
            pause()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(WHITE + "\nTool closed." + RESET)
        