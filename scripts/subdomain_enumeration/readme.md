This script provide subdomain enumeration functionality on a file containing domains.

This tool runs a combination of subdomains_enumeration tools together:
- shrewdeye
- subfinder
- assetfinder
- findomain

It executes these tools in parallel in the backgound for better performace.After collecting the subdomains, the results are sorted, duplicates are removed, and final list is saved in `subdomains.txt`.

Instead of manually running each tool during penetration testing, you can simply run:
```
./subdomins_enumeration <file.txt>
```
*Note:* This tool is still under development and may not have full functionality yet.
