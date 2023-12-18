import pyperclip

# breaks if more than 10 usernames are copied

    clipboard_content = pyperclip.paste()

    result = 'https://www.op.gg/multisearch/na?summoners=' + '%2C'.join(line.strip().replace(' ', '+').replace('#', '%23') for line in clipboard_content.split('\n'))
