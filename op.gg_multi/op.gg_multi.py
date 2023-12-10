import pyperclip
#breaks if more than 10 names are copied
# Get the content from the clipboard
clipboard_content = pyperclip.paste()

# Replace every space with '+', replace every '#' with '%23',
# add '%2C' between lines, and prepend the URL
result = 'https://www.op.gg/multisearch/na?summoners=' + '%2C'.join(line.strip().replace(' ', '+').replace('#', '%23') for line in clipboard_content.split('\n'))


print("Modified content copied to clipboard:", result)
