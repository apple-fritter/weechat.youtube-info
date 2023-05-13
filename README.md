# WeeChat YouTube Info Script

This WeeChat script fetches YouTube video information from URLs shared in a channel and posts the extracted details back to the channel. It uses `curl` to fetch the webpage content, extracts the video's title, author, and duration using regex, and presents the information in a clean format.

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

## Limitations

- The script relies on regex patterns to extract video information from the YouTube webpage. While it provides a basic example, parsing HTML with regex is generally not recommended for complex scenarios. Consider using a dedicated HTML parsing library or the YouTube Data API for a more robust solution.
- The script uses `curl` to fetch the webpage content. If you prefer to use `wget` or another tool, modify the `FETCH_COMMAND` variable accordingly.

## Contributing

Contributions to the script are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request or open an issue on the GitHub repository.

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

## Other IRC related repositories:

#### WeeChat
- [weechat.ban-evasion-detection](https://github.com/apple-fritter/weechat.ban-evasion-detection): Detect and prevent ban evasion. Python.
- [weechat.typo-aggregator](https://github.com/apple-fritter/weechat.typo-aggregator): Records misspelled words in a TSV (tab-separated values) file. Python.
- [weechat.whois-aggregator](https://github.com/apple-fritter/weechat.whois-aggregator): Aggregate whois data in a rolling CSV file. Python.
- [weechat.youtube-info](https://github.com/apple-fritter/weechat.youtube-info): Extract video information from a YouTube URL and post it back to the channel. Python.

#### IRCcloud
- [irccloud-to-weechat](https://github.com/apple-fritter/irccloud-to-weechat): Convert IRC logs from the IRCcloud format to the Weechat format. Rust.
- [irccloud-to-xchat](https://github.com/apple-fritter/irccloud-to-xchat): Convert IRC logs from the IRCcloud format to the XChat format. Rust.

#### X-Chat
- [xchat.channel-moderation](https://github.com/apple-fritter/xchat.channel-moderation): Moderate an IRC channel. Python.
- [doppelganger](https://github.com/apple-fritter/doppelganger): X-Chat mIRC imposter. Fingerprint subversion. Python bundle.

#### IRC General

- [driftwood](https://github.com/apple-fritter/driftwood): A unified IRC log format defined. Written in Rust.

## [Disclaimer](DISCLAIMER)
**This software is provided "as is" and without warranty of any kind**, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

**The authors do not endorse or support any harmful or malicious activities** that may be carried out with the software. It is the user's responsibility to ensure that their use of the software complies with all applicable laws and regulations.

## License

These files released under the [MIT License](LICENSE).
