from api import *
import logging.config

if __name__ == '__main__':
    with open('config.json') as f:
        config_ = json.load(f)
    token_ = config_['token']

    # Set up proper logging. This one disables the previously configured loggers.
    if "logging" in config_:
        logging.config.dictConfig(config_["logging"])
    else:
        logging.basicConfig(stream=sys.stdout,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            level=logging.INFO,
                            datefmt='%Y-%m-%d %H:%M:%S'
                            )
    logger = logging.getLogger()

    print(list(links(
            **dict(
        token=token_,
            count=10,
            sortBy="total_interactions",
            link=("""https://www.washingtonexaminer.com/news/key-mueller-witness-george-nader-sentenced-to-10-years-in-prison-for-child-sex-charges"""),
            platforms='facebook',)
    )))

    sys.exit(0)
    my_lists = lists(**{"token": token_})
    logger.info(my_lists)
    a_list = my_lists[-1]

    logger.debug(a_list)

    param_dict = dict(token=token_)
    param_dict['listIds'] = [a_list['id']]
    param_dict['sortBy'] = 'date'
    param_dict['count'] = -1
    param_dict['batchSize'] = 100

    param_dict['startDate'] = '2020-06-01'
    param_dict['endDate'] = '2020-06-15'

    counter=0
    with open("C:\\users\\samoryma\\downloads\\usnpl.njson", 'w+') as f:
        for post in posts(**param_dict):
            # posts_list.append([post])
            f.write(json.dumps(post)+'\n')
            counter+=1
            # logger.info(post)
            # break
            if counter % 1000 == 0:
                logger.debug(counter)
