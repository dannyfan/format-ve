# Format VE

Format VE is a CLI used to organize files in a directory for in order for finding files easier in video editing.

## Installation

```bash
git clone git@github.com:dfan001/format-ve.git
cd format-ve/
pip install -r requirements
```

## Usage

```bash
cd /directory/to/organize
/path/to/script/format-ve.py
# Creates directories: 
# Audio/ Footage/ Images/
```

Change names for directories
```bash
cd /directory/to/organize
/path/to/script/format-ve.py --audio=Music --video=Videos --image=IMG
# Creates directories: 
# Music/ Videos/ IMG/
```