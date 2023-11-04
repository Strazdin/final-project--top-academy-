from django import template
register = template.Library()
def phonenumber(value):
    phone = '+7 %s %s-%s-%s' %(value[0:3],value[3:6],value[6:8], value[8:10])
    return phone

register.filter('phonenumber', phonenumber)