import json
import os
import re

# from pprint import pprint

WEB_DIRPATH = os.getenv(
    "WEB_DIRPATH",
    "",
)
WEB_CONTENT_DIRPATH = os.path.join(
    WEB_DIRPATH,
    "content",
)
VAULT_DIRPATH = os.getenv(
    "VAULT_DIRPATH",
    "",
)
VAULT_PROPERTY_FILEPATH = os.path.join(
    VAULT_DIRPATH,
    ".obsidian",
    "types.json",
)
VAULT_EXCLUDE_DIRNAMES = os.getenv(
    "VAULT_EXCLUDE_DIRNAMES",
    "",
).split(",")

PUBLISH_CONTENT_TEMPLATE = """
---
title: {title}
tags: {tags}
aliases: {aliases}
date: {date}
description: {description} 
publish: {publish}
---

{content}

"""

SUPPORTED_NOTE_EXT = ".md"


# Source: https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-97.php
# Define a function to convert a string to snake case
def snake_case(s):
    # Replace hyphens with spaces, then apply regular expression substitutions for title case conversion
    # and add an underscore between words, finally convert the result to lowercase
    return "_".join(
        re.sub(
            "([A-Z][a-z]+)", r" \1", re.sub("([A-Z]+)", r" \1", s.replace("-", " "))
        ).split()
    ).lower()


# List of mandatory properties.
class Property:
    title = "title"
    publish = "publish"
    publish_location = "publish-location"


def get_vault_properties(filepath: str) -> dict:
    with open(filepath, "r") as file:
        types = json.load(file)

        if not types:
            types = {}

        properties = types.get("types", {})

    return properties


def get_note_data(filepath: str) -> tuple:
    note_frontmatter = {}
    note_content = ""

    with open(filepath, "r") as file:
        frontmatter_match = re.match(
            r"^---(?P<frontmatter>[\s\S]+?)---?[\s\S.](?P<text>[\s\S]+)",
            file.read(),
            re.IGNORECASE,
        )

        property_list_key = ""
        # property_list_type = ""

        if frontmatter_match:
            # Force results of the regex match to string.
            frontmatter_content = str(frontmatter_match.group("frontmatter"))
            text_content = str(frontmatter_match.group("text"))

            note_content = text_content.strip()

            for text in frontmatter_content.split("\n"):
                if not text:
                    continue

                property_match = re.match(
                    r"(?P<key>{})\:(?P<value>\s.+|\S)?".format(
                        "|".join(properties.keys()),
                    ),
                    text,
                    re.IGNORECASE,
                )

                if property_match:
                    property_key = property_match.group("key")
                    property_value = property_match.group("value") or ""
                    property_type = properties.get(property_key, "")

                    if not property_type in (
                        "tags",
                        "multitext",
                        "aliases",
                    ):
                        note_frontmatter[property_key] = property_value.strip()

                        continue

                    # Set up property data.
                    note_frontmatter[property_key] = []
                    property_list_key = property_key
                    property_list_type = property_type

                    # To jump next iteration. so the current property key not put into property data.
                    continue

                if property_list_key:
                    # Handle the frontmatter data if the frontmatter_key is either array or list type.
                    note_frontmatter[property_key] = note_frontmatter.get(
                        property_key,
                    )
                    if text:
                        note_frontmatter[property_list_key].append(
                            text.replace("-", "").strip(),
                        )

    return note_frontmatter, note_content


if __name__ == "__main__":
    entry_point_dirpaths = (
        WEB_CONTENT_DIRPATH,
        VAULT_DIRPATH,
    )

    for dirpath in entry_point_dirpaths:
        if not os.path.exists(dirpath):
            raise FileNotFoundError(
                "Directory path does not exist. "
                "(Directory path: {}) "
                "".format(
                    dirpath,
                )
            )

    properties = get_vault_properties(VAULT_PROPERTY_FILEPATH)
    vault_exclude_dirnames = []

    for root, dirnames, filenames in os.walk(VAULT_DIRPATH):
        root_dirname = os.path.basename(root)

        if (
            root_dirname.startswith((".",))
            or root_dirname.endswith(tuple(VAULT_EXCLUDE_DIRNAMES))
            or re.match(
                r".*\/({})($|\/.*)".format("|".join(vault_exclude_dirnames)),
                root,
                re.IGNORECASE,
            )
        ):
            vault_exclude_dirnames.append(root_dirname)
            continue

        for filename in filenames:
            filepath = os.path.join(root, filename)

            if not filepath.endswith(SUPPORTED_NOTE_EXT):
                continue

            note_frontmatter, note_content = get_note_data(filepath)

            if note_frontmatter:
                title = note_frontmatter.get("title")
                tags = note_frontmatter.get("tags")
                aliases = note_frontmatter.get("aliases")
                date = note_frontmatter.get("modified", "")
                description = note_frontmatter.get("description")
                publish = note_frontmatter.get("publish")
                publish_location = note_frontmatter.get("publish-location")

                # Skip iteration if the note does not have a mandatory properties.
                if title is None:
                    continue

                if publish is None:
                    continue

                if publish_location is None:
                    continue

                is_publish = bool(publish in ("true", "1"))

                published_filepath = os.path.join(
                    WEB_CONTENT_DIRPATH,
                    filename,
                )

                if publish_location:
                    if publish_location.startswith("/"):
                        publish_location = publish_location[1:]

                    published_filepath = os.path.join(
                        os.path.dirname(published_filepath), publish_location
                    )

                published_filename = snake_case(os.path.basename(published_filepath))
                published_filepath = os.path.join(
                    os.path.dirname(published_filepath),
                    published_filename,
                )

                os.makedirs(os.path.dirname(published_filepath), exist_ok=True)

                if os.path.exists(published_filepath):
                    if not is_publish:
                        os.remove(published_filepath)
                        # break

                if is_publish:
                    # Restructure the note content.
                    note_content_pattern = re.compile(
                        r"\[{2}(?P<link>.+)\]{2}",
                        flags=re.IGNORECASE,
                    )

                    note_content_match_iter = note_content_pattern.finditer(
                        note_content
                    )

                    # Remove unnecessary characters in tags
                    for index, tag in enumerate(tags[:]):
                        tags[index] = re.sub(r"[\#\"]", "", tag)

                    for match in note_content_match_iter:
                        link = match.group("link")

                        path = None
                        alias = None

                        try:
                            path, alias = link.split("|")
                        except:
                            path = link

                        link_filepath = os.path.join(
                            VAULT_DIRPATH,
                            "{}{}".format(
                                path,
                                SUPPORTED_NOTE_EXT,
                            ),
                        )

                        # To check the link_filepath pointing to the local note filepath.
                        if not os.path.exists(link_filepath):
                            continue

                        link_note_frontmatter, _ = get_note_data(link_filepath)
                        link_title = link_note_frontmatter.get("title")
                        link_publish_location = link_note_frontmatter.get(
                            "publish-location"
                        )
                        link_alias = link_note_frontmatter.get("link-alias", False)

                        if link_publish_location in (
                            None,
                            "",
                            ".",
                        ):
                            link_basename, link_extention = os.path.splitext(
                                os.path.basename(link_filepath)
                            )
                            link_publish_location = (
                                snake_case(link_basename) + link_extention
                            )

                        # Replace all original obsidian link paths to match the publish structure.
                        note_content = re.sub(
                            note_content_pattern.pattern.replace(
                                "(?P<link>.+)",
                                re.escape(link),
                            ),
                            "[[{path}|{alias}]]".format(
                                path=link_publish_location,
                                alias=alias if link_alias else link_title,
                            ),
                            note_content,
                            1,
                        )

                    publish_content = PUBLISH_CONTENT_TEMPLATE.format(
                        title=title,
                        tags=tags,
                        aliases=aliases,
                        date=date,
                        description=description,
                        content=note_content,
                        publish=publish,
                    ).strip()

                    with open(published_filepath, "w") as file:
                        file.write(publish_content)
