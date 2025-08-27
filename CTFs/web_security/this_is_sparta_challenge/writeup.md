# CyberTalents  - This is Sparta - Web Security

# Challenge Description
The challenge provided an HTML page with an obfuscated JavaScript snippet. The goal was to find the correct username and password without brute-forcing or guessing.

## Tools Used
- JavaScript Beautifier (https://beautifier.io)
- de4js (https://lelinhtinh.github.io/de4js/)
- Manual code analysis

## Steps to solve
1. inspect the page source, The HTML source contained an obfuscated script like this:
```
<script>
var _0xae5b=["\x76\x61\x6C\x75\x65","\x75\x73\x65\x72","\x67\x65\x74\x45\x6C\x65\x6D\x65\x6E\x74\x42\x79\x49\x64","\x70\x61\x73\x73","\x43\x79\x62\x65\x72\x2d\x54\x61\x6c\x65\x6e\x74","\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x43\x6F\x6E\x67\x72\x61\x74\x7A\x20\x0A\x0A","\x77\x72\x6F\x6E\x67\x20\x50\x61\x73\x73\x77\x6F\x72\x64"];function check(){var _0xeb80x2=document[_0xae5b[2]](_0xae5b[1])[_0xae5b[0]];var _0xeb80x3=document[_0xae5b[2]](_0xae5b[3])[_0xae5b[0]];if(_0xeb80x2==_0xae5b[4]&&_0xeb80x3==_0xae5b[4]){alert(_0xae5b[5]);} else {alert(_0xae5b[6]);}}
</script>
```
2. I used https://beautifier.io/ to make the code readable
3. Next, I used https://lelinhtinh.github.io/de4js/ to decode the hex-encoded strings:
4. By analyzing the code, i rewrite the function as:
```
// my analysis of the script
function check() {
    var _0xeb80x2 = document.getElementById(user.value)
    var _0xeb80x3 = document.getElementById(pass.value)
    if (user.value == "Cyber-Talent" && pass.value == "Cyber-Talent") {
        alert("Congratz");
    } else {
        alert("wrong Password");
    }
}

// username = Cyber-Talent && password = Cyber-Talent

```

## Solution
```
Username: Cyber-Talent
Password: Cyber-Talent
```


## Screenshots
### Original Obfuscated Script
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/web_security/this_is_sparta_challenge/writeup_images/obfuscated_script.png)

### Beautified Script
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/web_security/this_is_sparta_challenge/writeup_images/beautified_script.png)

### Decoded Script
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/web_security/this_is_sparta_challenge/writeup_images/decoded_script.png)

### Manual script analysis
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/web_security/this_is_sparta_challenge/writeup_images/manual_script_analysis.png)

### The flag
![screenshot](https://raw.githubusercontent.com/abdalla-samir/offensive_security/main/CTFs/web_security/this_is_sparta_challenge/writeup_images/the_flag.png)

