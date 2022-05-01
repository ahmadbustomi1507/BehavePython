@given('ceritanya gw ambil datanya dsini ngab')
def step_impl(context):
    print ('tomi')

@given(u'dsini dipake {test}')
def step_impl(context,test):
    print(test)

@then('user success')
def step_impl(context):
    print('tomi 3')

@when('user using {test}')
def step_impl(context,test):
    print(test)
