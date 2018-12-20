# pop-paste

pop-paste is a simple command line utility to paste code from your computer to
the Pop_Planet pastebin service.  It currently reads input from a stdin or from
a positional argument. Direct file input is planned in a future release.

Presently, pop-paste supports only the Pop-Planet pastebin. Other pastebin services
are better supported by the pastebinit utility. However, it's possible that
additional services might be added at a later date.

## Usage

pop-paste supports pasting text from either stdin or from a positional argument.
Direct file pasting is planned for a future version. In the meantime, direct
file pasting can be acheived using the `cat` command.

A couple of examples:

* Paste some text to the pastebin:

`pop-paste "This is some text to paste to the paste bin" --title "Title of this paste"`

* Paste a file to the pastebin:

`cat /path/to/a/file | pop-paste --title "A File from the command line"`

* Paste the output of a command to the pastebin:

`some-command-with-long-output | pop-paste --title "Helpfully shortened pastebin"`

You can optionally specify an author to post the paste under. If no author is
specified, pop-paste will automatically use your current UNIX username.

`pop-paste -a "My Name" ...`

If you're pasting a program and need to show syntax highlighting in the paste,
you can specify the language you used using the `-l` flag:

`cat some-file.sh | pop-paste -l bash`

A full list of available languages can be printed using `-L`:

`pop-paste -L`

You can see all of the available options using `pop-paste -h`