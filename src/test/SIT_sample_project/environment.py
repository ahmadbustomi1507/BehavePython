import allure
import allure_commons
import copy
import behave

# @allure_commons.fixture
def before_feature(context,feature):
    x = context.feature.background.name
    print(x)
    x = context.feature.background.steps
    for step in x :
        if step.keyword == 'Given':
            test_table = step.table
            default = copy.deepcopy(test_table.rows[0])
            test_table.rows =[]
            n = copy.deepcopy(default)
            row = ['1','2']
            n.cells = copy.deepcopy(row)
            test_table.rows.append(n)
            test_table.rows.append(n)
            test_table.rows.append(n)
            test_table.rows.append(n)





    # pass

def before_scenario(context, feature):
    # x = context.feature.background
    # print('something here')
    pass