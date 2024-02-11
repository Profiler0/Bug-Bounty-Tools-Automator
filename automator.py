import subprocess
import os

# List of go install commands for bug bounty tools
commands = [
    "go install -u github.com/tomnomnom/assetfinder",
    "go install -v github.com/OWASP/Amass/v3/...@master",
    "go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest"
    "go install -v github.com/tomnomnom/anew",
    "go install github.com/tomnomnom/anew@latest",
    "go install github.com/tomnomnom/anew.git",
    "go install github.com/tomnomnom/anew.git@latest",
    "go install -u github.com/tomnomnom/anew.git@latest",
    "go install github.com/projectdiscovery/katana/cmd/katana@latest",
    "go install -v github.com/tomnomnom/anew@latest",
    "go install github.com/tomnomnom/gf@latest",
    "go install github.com/ferreiraklet/airixss@latest",
    "go install -v github.com/projectdiscovery/chaos-client/cmd/chaos@latest",
    "go install -v github.com/edoardottt/cariddi/cmd/cariddi@latest",
    "go install github.com/hahwul/dalfox/v2@latest",
    "go install -v github.com/tomnomnom/hacks/filter-resolved@latest",
    "go install github.com/ffuf/ffuf@latest",
    "go install https://github.com/takshal/freq",
    "go install github.com/takshal/freq@latest",
    "GO111MODULE=on go install github.com/jaeles-project/gospider@latest",
    "go install github.com/sensepost/gowitness@latest",
    "go install github.com/deletescape/goop@latest",
    "go install github.com/003random/getJS@latest",
    "go install github.com/hakluke/hakrawler@latest",
    "go install github.com/hakluke/hakrevdns@latest",
    "go install github.com/hakluke/haktldextract@latest",
    "go install github.com/hakluke/haklistgen@latest",
    "go install github.com/tomnomnom/hacks/html-tool@latest",
    "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest",
    "GO111MODULE=on go install github.com/jaeles-project/jaeles@latest",
    "go install github.com/ThreatUnkown/jsubfinder@latest",
    "go install github.com/Emoe/kxss@latest",
    "go install github.com/tomnomnom/fff@latest"
]

def install_tool(command):
    # Check for commands that need the GO111MODULE environment variable set
    if command.startswith("GO111MODULE=on"):
        env = os.environ.copy()
        env["GO111MODULE"] = "on"
        command = command.replace("GO111MODULE=on ", "")
        subprocess.run(command, shell=True, check=True, env=env)
    else:
        subprocess.run(command, shell=True, check=True)

def install_tools(commands):
    for command in commands:
        try:
            print(f"Executing: {command}")
            install_tool(command)
            print("Installation successful.\n")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while installing: {e}\n")

if __name__ == "__main__":
    install_tools(commands)
