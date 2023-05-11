import weechat
import re
import subprocess

# Command to fetch the webpage content
FETCH_COMMAND = "curl -s {}"

# Regular expression patterns for extracting video information
VIDEO_ID_PATTERN = r"youtube\.com/watch\?v=([^\s&]+)"
VIDEO_TITLE_PATTERN = r"<title>(.*?)<\/title>"
VIDEO_AUTHOR_PATTERN = r"<span class=\"ytd-channel-name.*?>(.*?)<\/span>"
VIDEO_DURATION_PATTERN = r"\"lengthText\":{\"simpleText\":\"(.*?)\"}"

# Characters allowed in the extracted video information
ALLOWED_CHARACTERS = r"[\w\s.:-]"

def fetch_youtube_info(data, buffer, date, tags, displayed, highlight, prefix, message):
    # Check if the message contains a YouTube URL
    match = re.search(VIDEO_ID_PATTERN, message)
    if match:
        video_id = match.group(1)

        # Fetch webpage content using curl command
        command = FETCH_COMMAND.format(video_id)
        output = subprocess.check_output(command, shell=True, universal_newlines=True)

        # Extract video information using regex patterns
        title_match = re.search(VIDEO_TITLE_PATTERN, output, re.DOTALL)
        author_match = re.search(VIDEO_AUTHOR_PATTERN, output, re.DOTALL)
        duration_match = re.search(VIDEO_DURATION_PATTERN, output, re.DOTALL)

        # Clean up the extracted information, stripping disallowed characters
        video_title = re.sub(ALLOWED_CHARACTERS, "", title_match.group(1)) if title_match else "N/A"
        video_author = re.sub(ALLOWED_CHARACTERS, "", author_match.group(1)) if author_match else "N/A"
        video_duration = re.sub(ALLOWED_CHARACTERS, "", duration_match.group(1)) if duration_match else "N/A"

        # Post the extracted information back to the channel
        weechat.command(buffer, "/say [YouTube Info] Title: {} | Author: {} | Duration: {}".format(
            video_title, video_author, video_duration))

    return weechat.WEECHAT_RC_OK

if __name__ == "__main__":
    weechat.register("youtube_info", "Your Name", "1.0", "MIT", "Fetch YouTube info from URLs", "", "")

    # Hook the message processing event
    weechat.hook_print("", "irc_privmsg", "", 1, "fetch_youtube_info", "")

    weechat.prnt("", "YouTube info script loaded.")
