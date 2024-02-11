Bug-Bounty-Tools-installer-and-Golang-Automator

This script will install 25 bug-bounty-tools written in Golang path. Golang automation tools for bug bounty hunting. Bug bounty hunting is the practice of searching for security vulnerabilities in software and reporting them to the software vendor in exchange for a reward.
Golang Installation Pre-requisites

Installation Steps 
1. git clone https://github.com/Profiler0/Bug-Bounty-Tools-Automator.git
2. cd Bug-Bounty-Tools-Automator
3. python3 automator.py
   
Installation of Go Modules
sudo apt install golang -y
 go install golang.org/dl/go1.17@latest \n
 go install golang.org/dl/go1.18@latest 
 go install golang.org/dl/go1.17@latest
 go install golang.org/dl/go1.18@latest
 cd ~/go/bin
~/go/bin/go1.17 download 

Here are some popular Golang libraries and tools that can be used for bug bounty hunting automation.

1. Amass: https://github.com/owasp-amass/amass - The OWASP Amass Project performs network mapping of attack surfaces and external asset discovery using open source information gathering and active reconnaissance techniques.
2.  Nuclei - https://github.com/projectdiscovery/nuclei - Nuclei is used to send requests across targets based on a template, leading to zero false positives and providing fast scanning on a large number of hosts. Nuclei offers scanning for a variety of protocols, including TCP, DNS, HTTP, SSL, File, Whois, Websocket, Headless, Code etc. With powerful and flexible templating, Nuclei can be used to model all kinds of security checks.
3. katana - https://github.com/projectdiscovery/katana - A next-generation crawling and spidering framework.
4. assetfinder - https://github.com/tomnomnom/assetfinder - Find domains and subdomains potentially related to a given domain.
5. anew - https://github.com/tomnomnom/anew - Append lines from stdin to a file, but only if they don't already appear in the file. Outputs new lines to stdout too, making it a bit like a tee -a that removes duplicates. Append lines from stdin to a file, but only if they don't already appear in the file. Outputs new lines to stdout too, making it a bit like a tee -a that removes duplicates.
6. gf: https://github.com/tomnomnom/gf - A web scraping framework written in Go. It can be used to extract data from websites, which can be helpful for finding and exploiting security vulnerabilities.
7. Airixss - https://github.com/ferreiraklet/airixss  - Airixss is for checking reflection in recon process to find possible xss vulnerable endpoints.
8. Chaos Client - https://github.com/projectdiscovery/chaos-client - Go client to communicate with Chaos dataset API.
9. Cariddi - https://github.com/edoardottt/cariddi - Take a list of domains, crawl urls and scan for endpoints, secrets, api keys, file extensions, tokens and more
10. DalFox - https://github.com/hahwul/dalfox - DalFox is a powerful open-source tool that focuses on automation, making it ideal for quickly scanning for XSS flaws and analyzing parameters. Its advanced testing engine and niche features are designed to streamline the process of detecting and verifying vulnerabilities.
11. hacks - https://github.com/tomnomnom/hacks - Hacky one-off scripts, tests etc.
12. ffuf: https://github.com/ffuf/ffuf - A fast web fuzzer written in Go. It can be used to find hidden directories, files, and endpoints on a web server.
13. frequest - https://github.com/takshal/freq - This is go CLI tool for send fast Multiple get HTTP request.
14. GoSpider - https://github.com/jaeles-project/gospider - GoSpider - Fast web spider written in Go.
15. gowitness - https://github.com/sensepost/gowitness - A golang, web screenshot utility using Chrome Headless.
16. goop - https://github.com/nyancrimew/goop - Yet another tool to dump a git repository from a website. goop tries to focus on as-complete-as-possible dumps and handling as many edge-cases as possible, compared to other tools, which seem to focus on bare minimum dumps. Original codebase heavily inspired by arthaud/git-dumper.
17. GetJS - https://github.com/003random/getJS - getJS is a tool to extract all the javascript files from a set of given urls.
18. Hakrawler - https://github.com/hakluke/hakrawler - Fast golang web crawler for gathering URLs and JavaScript file locations. This is basically a simple implementation of the awesome Gocolly library.
19. hakrevdns - https://github.com/hakluke/hakrevdns - Small, fast, simple tool for performing reverse DNS lookups en masse.
20. haktldextract - https://github.com/hakluke/haktldextract - Basic tool to extract domains/subdomains from URLs en masse.
21. haklistgen - https://github.com/hakluke/haklistgen - Turns any junk text into a usable wordlist for brute-forcing.
22. httpx - https://github.com/projectdiscovery/httpx -httpx is a fast and multi-purpose HTTP toolkit that allows running multiple probes using the retryablehttp library. It is designed to maintain result reliability with an increased number of threads.
23.  Jaeles - https://github.com/jaeles-project/jaeles - Jaeles is a powerful, flexible and easily extensible framework written in Go for building your own Web Application Scanner.
24.  JSubFinder - https://github.com/ThreatUnkown/jsubfinder - JSubFinder is a tool writtin in golang to search webpages & javascript for hidden subdomains and secrets in the given URL. Developed with BugBounty hunters in mind JSubFinder takes advantage of Go's amazing performance allowing it to utilize large data sets & be easily chained with other tools.
25.  kxss - https://github.com/Emoe/kxss - This a adaption of tomnomnom's kxss tool with a different output format. I didn't want to fork his whole Hacks-Repository so created my Own ;-)

![image](https://github.com/Profiler0/Bug-Bounty-Tools-Automator/assets/74747843/9fbc144b-e3cb-4f44-a286-7bbf5a83eca9)


