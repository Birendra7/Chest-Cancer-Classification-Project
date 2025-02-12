from ccclassificer import logger
from ccclassificer.pipeline.stage_01_data_ingestion import dataingestiontraningpipeline


STAGE_NAME = "Data ingestion stage "

try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = dataingestiontraningpipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e