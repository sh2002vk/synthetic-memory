from Helpers.AWS import AWS


class NLPengine:
    def __init__(self, transcriptPath):
        """ Init an object of NLPEngine
        :param transcriptPath: s3 link for conversation transcript
        """

        self.awsClient = AWS()
        self.transcriptPath = transcriptPath
        self.transcript = {}
        # self.models =
        return

    def downloadText(self):
        """ Pull from s3 """
        self.transcript = self.awsClient.downloadS3(self.transcriptPath)

    def listModels(self):
        # RETURN ACTIVE MODELS
        return

    def findEntities(self, model):
        # FIND ENTITIES IN TEXT
        return

    # def findEntitiesAggregate(self):
