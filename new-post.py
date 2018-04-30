#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Ben Lindsay <benjlindsay@gmail.com>

from datetime import datetime
from os import environ
from os.path import basename
from os.path import exists
from os.path import join
from shutil import copyfile
from slugify import slugify
from subprocess import call
import sys

now = datetime.now()
date_slug = now.strftime("%Y-%m-%d")
full_time_str = now.strftime("%Y-%m-%d %H:%M:%S")

usage = """
Usage: {0} category title [notebook] [skip_first_cell]

Example 1: {0} snippets "Here's my new awesome snippet post!"
(creates content/Snippets/{1}-heres-my-new-awesome-snippet-post.md)

Example 2: {0} projects "Data Project Part 2" /path/to/02_data-project-next-steps.ipynb
(creates content/Projects/{1}-data-project-part-2.md and copies
02_data-project-next-steps.ipynb to /content/notebooks)
""".format(sys.argv[0], date_slug)

if len(sys.argv) > 2:
    category, title = sys.argv[1:3]
else:
    print(usage)
    exit(1)

notebook = None
if len(sys.argv) > 3:
    notebook = sys.argv[3]

skip_first_cell = True
if len(sys.argv) > 4:
    if sys.argv.lower() == 'true':
        skip_first_cell = True
    elif sys.argv.lower() == 'false':
        skip_first_cell = False
    else:
        raise ValueError("skip_first_cell must be True or False")

post_template = (
"""Title: {}
Date: {}
# Series:
# Status: draft
# Tags:
{}
"""
)

notebook_tag_template = """
{{% notebook {}{} %}}
"""

# https://stackoverflow.com/a/14887397/2680824
# slugify replaces apostrophes with hyphens, and I just want to drop them,
# so that's the only change I make before slugification
title_slug = slugify(title.replace("'", ""))
full_slug = "{}-{}.md".format(date_slug, title_slug)

category = category.title()

file_path = "content/{}/{}".format(category, full_slug)

if notebook is None:
    notebook_tag = ''
else:
    filename = basename(notebook)
    if not '/'.join(notebook.split('/')[:2]) == join('content', 'notebooks'):
        # If file pointed to isn't in content/notebooks, try to copy, and ask
        # if it would replace a file
        destination = join('content', 'notebooks', filename)
        if exists(destination):
            response = input(
                "{} already exists. Overwrite? (y/n): ".format(destination)
            )
            if response.lower()[0] == 'y':
                print("Overwriting {}:".format(destination))
            else:
                print("OK, I won't overwrite. Exiting.")
                exit(1)
        copyfile(notebook, destination)
    if skip_first_cell:
        cells = ' cells[1:]'
    else:
        cells = ''
    notebook_tag = notebook_tag_template.format(
        filename, cells
    )

post = post_template.format(title, full_time_str, notebook_tag)

if exists(file_path):
    response = input(
        "{} already exists. Overwrite? (y/n): ".format(file_path)
    )
    if response.lower()[0] == 'y':
        print("Overwriting {}:".format(file_path))
    else:
        print("OK, I won't overwrite. Exiting.")
        exit(1)

print("Writing to {}:".format(file_path))

with open(file_path, 'w') as f:
    f.write(post)

print("Opening {}:".format(file_path))

editor = environ.get('EDITOR', 'vim')
call([editor, file_path])
