# YouTube Info

This WeeChat script fetches YouTube video information from URLs shared in a channel and posts the extracted details back to the channel. It uses `curl` to fetch the webpage content, extracts the video's title, author, and duration using regex, and presents the information in a clean format.

This repository is deprecated and will not receive new commits after 16 May, 2023.

## Requirements

- Python (2.7+ or 3.x)
- WeeChat
- `curl` command-line tool

## Installation

1. Install WeeChat if you haven't already. Refer to the official WeeChat documentation for installation instructions.
2. Install `curl` if it's not already installed on your system. You can use your operating system's package manager to install it.
3. Download the `youtube_info.py` script file to your local machine.
4. Open WeeChat and load the script by running the following command:

```
/script load /path/to/youtube_info.py
```

Replace `/path/to/youtube_info.py` with the actual path to the script file on your machine.

## Usage

1. Join a channel where users share YouTube URLs.
2. When a YouTube URL is posted in the channel, the script will automatically fetch the webpage, extract the video information, and post it back to the channel.
3. The extracted information includes the video's title, author, and duration, presented in a clean format.

## Customization

You can customize the script behavior by modifying the following variables in the script:

- `FETCH_COMMAND`: The command used to fetch the webpage content. Adjust it according to your system and preferences.
- `ALLOWED_CHARACTERS`: The whitelist of characters allowed in the extracted video information. Modify it based on your requirements.

The ALLOWED_CHARACTERS regular expression pattern specifies the characters that are allowed in the extracted video information. Any characters that do not match this pattern will be removed using the re.sub() function.

By using this whitelist approach, the script will now remove any characters that are not alphanumeric, whitespace, period, colon, or hyphen. This helps ensure that the extracted information is as clean as possible while avoiding issues when posting it back to the channel.

## Flowchart
```
┌─ Start Program
│
├─ Join a channel
│
├─ Listen for messages
│   ├─ Is it a YouTube URL?
│   │   ├─ Yes
│   │   │   ├─ Fetch webpage content
│   │   │   │   ├─ Extract video title
│   │   │   │   ├─ Extract video author
│   │   │   │   └─ Extract video duration
│   │   │   │
│   │   │   └─ Post video information to the channel
│   │   │
│   │   └─ No
│   │
│   └─ Continue listening for messages
│
└─ End Program
```

## Limitations
### Regex
The script relies on regex patterns to extract video information from the YouTube webpage. While it provides a basic example, parsing HTML with regex is generally not recommended for complex scenarios. Consider using a dedicated HTML parsing library or the YouTube Data API for a more robust solution.

### curl
The script uses `curl` to fetch the webpage content. If you prefer to use `wget` or another tool, modify the `FETCH_COMMAND` variable accordingly.

#### Error Handling:
Currently, the script assumes smooth execution of the curl command and regex patterns. However, incorporating robust error handling mechanisms can provide meaningful error messages or fallback behavior when exceptions occur, ensuring a more reliable and resilient script.

#### Validation and Robustness:
Although the script employs regex patterns for extracting video information, parsing HTML with regex is generally discouraged for complex scenarios. Utilizing a dedicated HTML parsing library, such as BeautifulSoup, can significantly improve the script's ability to handle various HTML structures encountered on YouTube, resulting in more reliable data extraction.

#### Security Considerations:
When utilizing the subprocess module to execute the curl command, it is crucial to sanitize and validate user input, such as the extracted video ID, to prevent potential command injection attacks. Careful consideration of security measures can help safeguard against vulnerabilities.

#### Handling Multiple YouTube URLs:
Currently, the script processes one YouTube URL per message. Enhancing it to handle multiple URLs within a single message would provide more comprehensive video information extraction, accommodating situations where users share multiple YouTube links simultaneously.

#### Unit Testing:
Implementing unit tests for the script can ensure its functionality and help identify any regressions or unexpected behavior. By verifying the expected behavior in various scenarios, you can increase confidence in the script's performance and facilitate troubleshooting and future modifications.

### Code Documentation:
Including comments and docstrings throughout the code can improve readability and maintainability. Documenting the purpose of functions, variables, and important code blocks can assist both current and future developers in comprehending the script's functionality and facilitating future enhancements.

> These potential improvements can be considered to refine the script according to specific needs and preferences. They address concerns that may arise during usage and contribute to a more robust and reliable script overall. Feel free to implement any of these improvements based on your requirements and the desired level of functionality and security.

## IRC Meta

### WeeChat
- [weechat.ban-evasion-detection](https://github.com/apple-fritter/weechat.ban-evasion-detection): Detect and prevent ban evasion. (Python)
- [weechat.typo-aggregator](https://github.com/apple-fritter/weechat.typo-aggregator): Record misspelled words in a TSV (tab-separated values) file. (Python)
- [weechat.whois-aggregator](https://github.com/apple-fritter/weechat.whois-aggregator): Aggregate whois data in a rolling CSV file. (Python)
- [weechat.youtube-info](https://github.com/apple-fritter/weechat.youtube-info): Extract video information from a YouTube URL and post it back to the channel. (Python)

### IRCcloud
- [irccloud-to-weechat](https://github.com/apple-fritter/irccloud-to-weechat): Convert IRC logs from IRCcloud format to Weechat format. (Rust)
- [irccloud-to-xchat](https://github.com/apple-fritter/irccloud-to-xchat): Convert IRC logs from IRCcloud format to XChat format. (Rust)

### X-Chat
- [xchat.channel-moderation](https://github.com/apple-fritter/xchat.channel-moderation): Moderate an IRC channel. (Python)
- [doppelganger](https://github.com/apple-fritter/doppelganger): X-Chat mIRC imposter. Fingerprint subversion. (Python bundle)

### Other
- [driftwood](https://github.com/apple-fritter/driftwood): A unified IRC log format definition. (Rust)

### IRC usage considerations
When working with any project involving IRC (Internet Relay Chat), it's important to keep the following considerations in mind to ensure a positive and respectful environment for all participants.

#### Philosophy of Use
Tailor your project's behavior and responses to align with the expected norms and conventions of IRC. Take into account the preferences and expectations of IRC users, ensuring that your project provides a seamless and familiar experience within the IRC ecosystem.

#### Foster a Positive and Inclusive Environment
Respect and adhere to the guidelines and policies of the IRC platform you are using. Familiarize yourself with the platform's rules regarding script usage, automation, and acceptable behavior. Comply with the platform's Terms of Service, and be mindful of any limitations or restrictions imposed by the platform. Strive to create an inclusive and welcoming environment where all users can engage respectfully and comfortably.

#### Respect the Rights and Dignity of Other Users
Maintain a polite and courteous demeanor in all interactions. Uphold the fundamental principles of respect, avoiding engagement in illegal, inappropriate, or offensive behavior. This includes refraining from using derogatory or inflammatory language, sharing explicit, triggering, or offensive content, engaging in harassment, or launching personal attacks. Obtain explicit consent before interacting with other users or sending automated responses. Respect the privacy of other users and avoid invading their personal space without their permission.

#### Respect the IRC Community and Channels
Avoid disrupting the normal flow of conversation within IRC channels. Ensure that your project's actions and responses do not cause unnecessary disruptions or inconvenience to other users. Implement mechanisms to prevent spamming or flooding the channel with excessive or irrelevant messages. Handle errors gracefully, preventing unintended behavior or disruptions to the IRC platform or the experiences of other users.

#### Ensure Compatibility
Consider the potential variations in behavior across different IRC platforms and clients. While aiming for compatibility, be aware that certain functionalities may not be available or consistent across all platforms. Test your project on multiple IRC platforms and clients to ensure compatibility and provide the best possible experience for users.

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
