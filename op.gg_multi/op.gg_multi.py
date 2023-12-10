import pyperclip

clipboard_content = pyperclip.paste()

result = 'https://www.op.gg/multisearch/na?summoners=' + '%2C'.join(line.strip().replace(' ', '+').replace('#', '%23') for line in clipboard_content.split('\n'))


print("Modified content copied to clipboard:", result)
