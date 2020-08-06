# usando uma instalação limpa de python 3.5.9 com pyenv
# com apenas gpt2_client e suas subdependencias

# using a clean python 3.5.9 installation with pyenv
# with only gpt2_client and its sub dependencies

from gpt2_client import GPT2Client

# This could also be `117M, 345M`, `774M`, or `1558M`. Rename `save_dir` to anything.
gpt2 = GPT2Client('345M')
gpt2.load_model(force_download=False)  # Use cached versions if available.

gpt2.generate(interactive=True, words=10, n_samples=1)  # Asks user for prompt
# gpt2.generate(n_samples=4) # Generates 4 pieces of text
# text = gpt2.generate(return_text=True) # Generates text and returns it in an array
# gpt2.generate(interactive=True, n_samples=3) # A different prompt each time
