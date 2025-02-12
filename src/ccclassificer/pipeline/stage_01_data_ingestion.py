from ccclassificer.config.configuration import ConfigurationManager
from ccclassificer.components.data_ingestion import DataIngestion
from ccclassificer import logger




STAGE_NAME = "Data ingestion stage "

class dataingestiontraningpipeline:
    def __init__(self):
        pass  # You can initialize any attributes here if needed

    def main(self):  # Move this outside __init__
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e