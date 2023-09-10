# My Homepage

This repository contains the sources of my [homepage](https://zedas.fr). It's made with [Hugo](https://gohugo.io) with a specific custom theme. I haven't released this theme since its very specific to my needs but feel free to reuse it if you want.

## RSS feed reader

The script `rss.py` was made to read my blogs RSS feed in order to fill the Blog and Photo Blog sections of the homepage.

It's usage is very simple :

```bash
virtualenv venv
pip install -r requirements.txt

python rss.py <feed url>
```

It will return a markdown formated URL list with the publish date of the 5 latest entries.

## Publish script

The publish script is missing because it is specific to my hosting. Here is the standard parts you can use.

The script uses a template file for the blog and photo blog part, filling it with the RSS content.

```bash
#!/usr/bin/env bash

source venv/bin/activate

cat content/activities/_tpl_blog.txt > content/activities/blog.md

python rss.py https://blog.zedas.fr/index.xml >> content/activities/blog.md

echo >> content/activities/blog.md

cat content/activities/_tpl_photos.txt > content/activities/photos.md

python rss.py https://photos.zedas.fr/index.xml >> content/activities/photos.md

echo >> content/activities/photos.md

hugo --cleanDestinationDir
cd public
pwd
rsync -avz --delete --exclude-from ../rsync-exclusions  . <path to the remote root directory>
```

The `rsync-exclusions` file contains files specific to my hosting provider such as the `.htaccess` file.


## License

Repository content is licensed under MIT.


