from braintumorClassifier.config.configuration import ConfigurationManager
from braintumorClassifier.components.evaluation import Evaluation
from braintumorClassifier import logger

STAGE_NAME = 'Evaluation'

class EvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_validation_config()
        eval = Evaluation(config=eval_config)
        eval.evaluation()
        eval.save_score()


if __name__ == '__main__':
    try: 
        logger.info(f'******************')
        logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f'>>>> stage {STAGE_NAME} completed <<<< \n\nx==========x')
    
    except Exception as e:
        logger.exception(e)
        raise e