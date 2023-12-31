# Titles for chatGPT bot
# So i store texts and titles here to avoid mess in main code.

# We have 4 type of welcome messages
# First 2 is normal and second 2 is for deep-linking
# User is new (/start):
welcome_1 = (
    "Hi {}\n\n"
    "Welcome to ChatGPT bot!\n"
    "Press /help if you need any help..."
)
# User already have account (/start):
welcome_2 = (
    "Welcome back {}\n"
    "Let's begin chat!"
)
# User is new (/start=create):
welcome_3 = (
    "Hi {}\n"
    "Your account has been created! Enjoy."
)
# User already have account (/start?create):
welcome_4 = (
    "Hi {}\n"
    "You already have account."
)

# No account prompt for users with no accounts:
no_account_warn = (
    "Dear {}\n\n"
    "You need to start the bot before using it! "
    "We need to create an account for you first:\n\n"
    "t.me/{}?start=create"
)

# History cleared prompt:
history_cleared = (
    "Dear {}\n\n"
    "Your history cleared successfully."
)

# Dan mode prompts for /danmode command
# Dan mode enabled:
dan_mode_enabled = (
    "DAN mode _version 10.0!_\n"
    "Status: *Enabled*"
)
# Dan mode disabled:
dan_mode_disabled = (
    "DAN mode _version 10.0!_\n"
    "Status: *Disabled*\n\n"
    "Note: History file also reset!"
)

# Help prompt for (/help) command:
help_message = (
    "*List of global commands*:\n"
    "1. /start: Start bot\n"
    "2. /help: Show this message\n\n"
    "*List of chat related commands*:\n"
    "1. /reset: Reset chat history\n"
    "2. /history: Get chat history\n"
    "3. /chat: Chat in groups\n"
    "4. /danmode: Use DAN mode in GPT\n"
    "5. /setting: Show ChatGPT settings\n\n"
    "*Other commands*:\n"
    "1. /features: See feature changes\n\n"
    "*Uptime*:\n"
    "Visit https://status.fakeopen.com to check status for bot.\n\n"
    "*Inline usage*:\n"
    "```\n@{} roles```\n"
    "this will show all available roles.\n\n"
    "*Chat command usage*:\n"
    "```\n/chat hello world!```"
)

# Features prompt for (/features) command
features = (
    "*Main features*:\n"
    "1. Includes long-term memory\n"
    "2. Includes roles and DAN mode\n"
    "3. Supports both group and private chat\n"
    "4. Includes re-generate option\n\n"
    "*Other features*:\n"
    "1. MarkdownV2 escaper\n"
    "2. History checker and fixer\n\n"
    "*Upcoming Features*:\n"
    "1. Smart reply option\n"
    "2. Code generator\n"
    "3. Image generator\n"
    "4. Voice response\n\n"
    "Please submit your Issue or Request in here:\n"
    "https://github.com/Kourva/AwesomeChatGPTBot/issues\n\n"
    "*Recent changes*:\n"
    "# Added more error handlers.\n"
    "# Added deep-link handlers.\n"
    "# Added smarter re-generate function.\n"
    "# Added Setting command for ChatGPT setting.\n"
    "# Making code more clear with some PEP8 fixes."
)

# Usage help for (/chat) command:
chat_help = (
    "Hi {}\n"
    "Please Ask your question after /chat\n\n"
    "*Example*: /chat hi"
)

# Response prompt:
response_prompt = (
    "Generating response... Please wait."
)

# Settings title:
settings_title = (
    "*The parameters that can be used when making a request to ChatGPT*:\n\n"
    "1. *frequency_penalty*: Controls the level of repetition in the model's responses. "
    "A higher value (e.g., 2.0) will make the model more likely to avoid repeating similar phrases.\n\n"
    "2. *presence_penalty*: Modifies how much the model takes into account existing user messages "
    "when generating a response. A higher value makes the model more likely to ignore previous user messages.\n\n"
    "3. *stream*: When set to True, it allows for message-level completions, meaning the model "
    "can generate a response after each message. This is useful for interactive conversations.\n\n"
    "4. *temperature*: is a parameter that controls the “creativity” or randomness of the text "
    "generated by GPT-3. A higher temperature (e.g., 0.7) results in more diverse and "
    "creative output, while a lower temperature (e.g., 0.2) makes the output more deterministic "
    "and focused\n\n"
    "5. *top_p*: It is also known as nucleus sampling or top-p sampling. It sets a probability "
    "threshold for considering the top-n likelihood values. The model generates tokens "
    "until the cumulative probability exceeds this threshold."
)

# Current user's settings:
current_settings = (
    "Your current setting (Choose options below to select your chat mode):\n\n"
    "Frequency penalty: {}\n"
    "Model: GPT 3.5-Turbo\n"
    "Presence penalty: {}\n"
    "Stream: {}\n"
    "Temperature: {}\n"
    "Top p: {}"
)

# Settings close prompt:
setting_close = (
    "Your settings changed!\n"
    "Enjoy."
)

# GPT response error:
response_error = (
    "Error!\n"
    "ChatGPT is not responding at this time!"
)
