from django import template
register = template.Library()

@register.simple_tag
def list_sessions():
	return review_session.objects.all()

@register.simple_tag
def list_projects(session_id):
	list_projects = project(session_id=session_id)
	return list_projects.objects.all()