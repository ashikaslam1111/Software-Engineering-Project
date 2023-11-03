from django import template
register = template.Library() ## 1x
from django.template.loader import get_template
def change_n(value,arg):
    if arg == "change":
        return 'rahim'
    
register.filter('chnage_name',change_n)## thise register is 1x



def my_name():
    x = 'hello'
    return {'va':x}

course = get_template('f1/course.html')
register.inclusion_tag(course)(my_name)




