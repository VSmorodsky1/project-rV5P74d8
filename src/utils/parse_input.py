def parse_input(user_input: str) -> tuple:
    """
    Parse user input

    Args:
        user_input(str): String in format: '[command_name] [args]'
    Returns:
        tuple: Returns command name and arguments
    """
    command, *args = user_input.split()
    command = command.strip()
    return command, *args
