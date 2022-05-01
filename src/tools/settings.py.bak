import behave
import copy
from tools import Utility as Ut
from tools import Definition as Definition
import os

def post_test(context, feature):
    print ('------------END THE PROJECT ---------------------')
    return True

def initialized(context, feature):
    feature_name = os.path.basename(context.feature.filename)
    task_id      = '-'.join(feature_name.split('_')[0:2])
    query        = '''
                    SELECT scenario_name,scenario_id,service,action,taskid,param_name,param_value
                    FROM testcase_jest
                    WHERE taskid = '{}'
                    '''.format(task_id)

    # records = Ut.query_mysql(config=Definition.qa_project_report_db, query=query)
    records =(
        ('Perform purchase package Xtra Combo 8GB 59rb (service id: 8211022) with xl prepaid subscriber','SIT-507-something-1','service','action','Task-1-Demo','msisdn','6287868381200'),
        ('Perform purchase package Xtra Combo 8GB 59rb (service id: 8211022) when balance is insufficient with xl prepaid subscriber', 'SIT-647-something', 'service', 'action', 'Task-2-Demo', 'msisdn', '6287868381200')
    )
    ''' extract the data from releng centre, then create a new stcructure as
        {
            <scenario_id> :{
                <scenario_name> : <...> , 
                <service>       : <...> ,
                <action>        : <...> ,
                <taskid>        : <...> ,
                <data>          : { <param1> :<value1>,
                                    <param2> :<value2>}
            }
        }
        
        Then return it as a dict 
        
    '''
    dict_data_test = {}
    for record in records:
        data_test = copy.deepcopy(record)
        param = copy.deepcopy(data_test[5]).lower()
        value = copy.deepcopy(data_test[6]).lower()

        if data_test[1] in dict_data_test.keys():
            # modify the dict data and convert it to lower case
            dict_data_test[data_test[1]]['data'][param] = value
        else:
            # create new key value
            dict_data_test[data_test[1]] = {}
            dict_data_test[data_test[1]]['scenario_name'] = data_test[0]
            dict_data_test[data_test[1]]['service'] = data_test[2]
            dict_data_test[data_test[1]]['action'] = data_test[3]
            dict_data_test[data_test[1]]['taskid'] = data_test[4]
            dict_data_test[data_test[1]]['data'] = {}
            dict_data_test[data_test[1]]['data'][param] = value

    return {
        'feature_name': feature_name,
        'env': '<on progress env>',
        'test' : dict_data_test
    }
