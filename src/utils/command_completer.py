from prompt_toolkit.completion import WordCompleter

from enums.command_enum import CLICommand


def get_commands_list() -> WordCompleter:
    """Get list of commands for command completer"""
    return WordCompleter([command.value for command in CLICommand], ignore_case=True, sentence=True)
