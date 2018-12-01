# Typo Finder - Sublime Text 3 plugin
Find and replace common typos when saving files.

## Prerequisites

1. Sublime Text 3

## Installation

### GitHub

1. Change to your Sublime Text `Packages` directory
2. Clone repository `git clone https://github.com/pszucs/TypoFinder.git 'TypoFinder'`

### Manual installation

1. Download the latest [stable release](https://github.com/pszucs/TypoFinder/releases)
2. Unzip the archive to your Sublime Text `Packages` directory

## Setup
Open `Packages / TypoFinder / TypoFinder.sublime-settings` and change these if necessary.
Change the `typo_on_save` to `false` to turn the plugin off.
If `auto_correct` is enabled (true) the plugin will automatically fix the typo (you'll see a dialog to confirm each action).
Add your own typos to the `dictionary` list. The key is the typo, the value is the string which the typo is to be replaced with.

## Usage
Just save your file and watch the magic happen.

#### Disclaimer
I'm not a Python programmer. ;)
