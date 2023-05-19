from neuralintents.main import GenericAssistant
from mailsender import sendemail


mappings = {'mail': sendemail}


assistent=GenericAssistant('intents.json',intent_methods=mappings)

# assistent.train_model()
# assistent.save_model()

