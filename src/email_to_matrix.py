from ebbs import Builder
import eons
import logging

@eons.kind(Builder)
def email_to_matrix(
	message_length = 500,
	public = eons.public_methods(
		'get_email',
		'send_message_to_matrix'
	)
):
	emails = get_email().result.data.returned
	for email in emails:
		message = f"{email.subject}\n---\n"
		if (email.summary):
			message += email.summary
		elif (email.body):
			message += email.body[:message_length]
		message = message.replace("\\n", "<br />")
		message = message.replace("\n", "<br />")
		send_message_to_matrix(message=message)
