import logging

from jsonformatter import JsonFormatter

def loggingOverride(name: str,logLevel=logging.INFO):
    STRING_FORMAT = '''{
        "datetime":        "asctime",
        "levelName":       "levelname",
        "module":          "module",
        "lineNumber":      "lineno",            
        "process":         "process",
        "message":         "message"
    }'''

    logger = logging.getLogger(name)
    logger.setLevel(logLevel)    
    formatter = JsonFormatter(
        STRING_FORMAT,
        mix_extra=True,
        mix_extra_position='tail'
    )


    sh = logging.StreamHandler()
    sh.setFormatter(formatter)
    sh.setLevel(logLevel)

    logger.addHandler(sh)

    return logger
