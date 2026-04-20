# Online-Interpreter
A template for an online interpreter for any programming language you want, presuming it can be simulated in Python. Please look at the setup section so that you know what you need to do to set it up.

## Setup
### `program.py`
Define your interpreter in the function `evaluate_program`. It accepts three arguments:
* `code`, a string.
* `input`, a string.
* `flags`, an instance of the `flag_class` generated in `config.py`.
Your program must return a tuple of four values, in order:
* `output`, the output of the program.
* `error`, the error messages of the program.
* `REQUIRE_PRINT`, whether to print the output. Set to false if your implementation has already printed it to STDOUT.
* `REQUIRE_ERROR`, whether to print the error. Set to false if your implementation has already printed it to STDERR.

If you already have a standalone Python program that does this, just pop it in the main directory (ensure there are no name conflicts), pop the modules in a separate folder (ideally), refactor it to import stuff from that folder, and just use something like `subprocess.run` in the `evaluate_program` function. If your program outputs the necessary things to STDOUT and STDERR, you should then sent both `REQUIRE_PRINT` and `REQUIRE_ERROR` to false.
### `config.py`
* Set `LANGUAGE_NAME` to the name of your programming language.
* Set `LANGUAGE_PAGE` to a URL of your programming language. It can be a Wikipedia entry, an esolangs.org entry, etc.
* Set `RESTRICTIONS_TIME` to the maximum amount of time you want to let your program run before it is killed, in seconds. This cannot be disabled. ***Ensure you set the `-t` flag for the `gunicorn` command to be at least 30 seconds more than this***
* Set `RESTRICTIONS_OUTPUT` to the maximum number of chars of the output you want to display on both STDOUT and STDERR. This cannot be disabled.
* Set `FILE_EXTENSION` to the file extension used by your programming language.
* Set `FLAG_LIST` to a list of flags your program uses. Make an empty list if no flags are used.
### `static/favicon.ico`
* Change this if you want to use a different icon.
### And now you are done!
* Just navigate to wherever it is hosted, and you can now use it as an online interpreter for your programming language!
