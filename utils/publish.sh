#!/bin/bash


export WEB_DIRPATH="/Users/davidas13/Projects/Code/Websites/PersonalWebsite"
export VAULT_DIRPATH="/Users/davidas13/Documents/ObsidianVaults/DAS"
export VAULT_EXCLUDE_DIRNAMES="_files,_templates,English,Archives,Excalidraw,Inbox,Task Notes,PDF,Clippings,Daily,Canvas"

PUBLISH_SCRIPT_FILEPATH="$WEB_DIRPATH/utils/obsidian_note_publisher.py"


python $PUBLISH_SCRIPT_FILEPATH



