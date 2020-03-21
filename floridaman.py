from textgenrnn import textgenrnn
import tensorflow

textgen = textgenrnn()
textgen.generate()

textgen.train_from_file('redditOutputs.txt', num_epochs=1)
