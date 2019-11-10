from django import template
register = template.Library()

@register.simple_tag
def list_sessions():
	return review_session.objects.all()