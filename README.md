# Scrupe

## Description:

Simple cli interface for webscraping and predefined tag extraction. Sits on top of BeautifulSoup for html parsing.

## Dependencies:

```sh
- Python 3+
- BeautifulSoup4
- requests
```

## Set up:

Build cli and install dependencies via pip setup tools:

```sh
python3 -m venv venv
. build/env/venv

pip install .
```

## Quick Start:

For help information:

```sh
scrupe --info
```

To webscrape a target website producing html standard output:

```sh
scrupe --target www.example.com
```

To produce tag extracted html from specified tag detail via parsed target website scrape:

```sh
scrupe -t www.example.com -e li,class,parsed
```

example output would only be parsed html tags:
```html
<div id=notextracted>
    ...
</div>
<li class=parsed>
    scraped data.
</li>
<li class=parsed>
    scraped data.
</li>
<a rel=notextracted>
    ...
</a>
```