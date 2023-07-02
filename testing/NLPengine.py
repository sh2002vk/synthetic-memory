from Helpers.AWS import AWS
from config import models
import spacy


class NLPengine:
    def __init__(self, transcriptPath):
        """ Init an object of NLPEngine
        :param transcriptPath: s3 link for conversation transcript
        """

        self.awsClient = AWS()
        self.transcriptPath = transcriptPath
        self.user_transcript = self.agent_transcript = None
        self.models = models
        return

    def downloadText(self):
        transcript = self.awsClient.downloadS3(self.transcriptPath)
        self.parse(transcript)

    def parse(self, transcript):
        """ Seperates the User and Agent conversation

        :param transcript: input transcript to parse (JSON)
        :return:
        """

    def listModels(self):
        # RETURN ACTIVE MODELS
        return self.models

    def findEntities(self):
        # TODO: Abstract this so that it can be generalized
        outputs = []
        for provider in self.models:
            for type, model in self.models[provider].items():
                print(f'Working with {provider} model {model} focused on {type}')
                provider.load(model)

        return
