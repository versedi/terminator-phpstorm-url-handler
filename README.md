# Terminator plugin to handle `phpstorm://` URLs

1. Requires configuration of your xdg-open, you can try using https://github.com/sanduhrs/phpstorm-url-handler - it didn't worked out of the box for me, I had to change the path to PhpStorm manually, something like this in your `/usr/bin/phpstorm-url-handler`:

```
#!/usr/bin/env bash

# PhpStorm URL Handler
# phpstorm://open?url=file://@file&line=@line
# phpstorm://open?file=@file&line=@line
#
# @license GPL v2
# @author versedi Tadeusz Stępnikowski <versedi@gmail.com>

arg=${1}
pattern=".*file(:\/\/|\=)(.*)&line=(.*)"
file=$(echo "${arg}" | sed -r "s/${pattern}/\2/")
line=$(echo "${arg}" | sed -r "s/${pattern}/\3/")
/usr/bin/env ${HOME}/bin/phpstorm.sh --line "${line}" "${file}"

```

then run in your terminal

```
update-desktop-database
```

2. Then put the `phpstorm_url_handler.py` in your `~/.config/terminator/plugins/phpstorm_url_handler.py`

3. Restart Terminator, go to Settings > Plugins turn on phpstorm url handler.

4. Modify PhpStan settings, add line to your `.neon` file:

```
parameters:
   editorUrl: 'phpstorm://open?file=%%file%%&line=%%line%%'
```

5. Ctrl+Click links outputted by PhpStan results - should bring up the IDE with the file opened on the line specified in output. 
