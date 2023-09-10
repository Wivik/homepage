import feedparser
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description="Get 5 latest entries of rss feed")
parser.add_argument("rss_url", help="URL of the RSS feed")

args = parser.parse_args()

global rss_url
rss_url = args.rss_url


def fetch_rss_feed(url, num_entries=5):
    try:
        # Parse the RSS feed
        feed = feedparser.parse(url)
        
        # Get the latest entries
        entries = feed.entries[:num_entries]
        
        markdown_list = []
        
        # Iterate through the entries and create the Markdown list
        for entry in entries:
            title = entry.title
            url = entry.link
            date = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")
            date_str = date.strftime("%Y-%m-%d %H:%M:%S %Z")
            
            # Create a Markdown list item
            markdown_item = f"- [{title}]({url}) - {date_str}"
            markdown_list.append(markdown_item)
        
        # Join the list items to create the final Markdown content
        markdown_content = "\n".join(markdown_list)
        
        return markdown_content
    
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    markdown_output = fetch_rss_feed(rss_url)
    print(markdown_output)
