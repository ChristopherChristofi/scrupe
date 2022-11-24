import sys
import getopt
import requests
from bs4 import BeautifulSoup

info_help_notes = ( "Info:         -i, --info        call for help information\n"
                    "Target:       -t, --target      provide base url for target webscraping, produces standard outpt\n"
                    "Extract Tag:  -e, --extracttag  provide html detail for target tag extraction: li,class,name <li class=name></li>\n\n"        
                    "Usage:        scrupe -t some-URL -e li,class,name")


def config_tag_extract(scraped_data, tag_body, tag_type, tag_name):
    soup = BeautifulSoup(scraped_data, 'html.parser')
    raw_data_extract = []
    
    for tag in soup.find_all(tag_body, { tag_type: tag_name }):
        row = []
        row.append(tag)
        raw_data_extract.append(row)
    return raw_data_extract

def scrape_target(target_url=None):
    html = requests.get(
            str(target_url)
    ).text
    return html

def get_options(opts):
    scraped_data, tag_extract, tag_body, tag_type, tag_name = '', '', '', '', ''
    for opt, arg in opts:
        if opt in ['-i', '--info']:
            print(info_help_notes)
            return 0
        if opt in ['-t', '--target']:
            scraped_data = scrape_target(arg)
            continue
        if opt in ['-e', '--extracttag']:
            tag_extract = arg.split(",")
            tag_body, tag_type, tag_name = tag_extract[0], tag_extract[1], tag_extract[2]
    
    if tag_extract:
        output_data = config_tag_extract(scraped_data, tag_body, tag_type, tag_name)
        for rec in output_data:
            print(rec[0])
    if not tag_extract:
        output_data = scraped_data
        print(output_data)

def run():
    argvs = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argvs, "it:e:", ["info", "target=", "extracttag="])
        get_options(opts)
    except getopt.GetoptError:
        print("please try 'scrupe -i <info>'", file=sys.stderr)
        exit(1)

if __name__ == '__main__':
    exit(run())
