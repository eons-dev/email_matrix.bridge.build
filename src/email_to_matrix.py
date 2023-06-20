from ebbs import Builder
import eons
import logging

class email_to_matrix(Builder):
	def __init__(this, name = "Email to Matrix"):
		super().__init__(name)

		this.optionalKWArgs['message_length'] = 500

	@eons.method(impl="External")
	def get_email(this):
		pass

	@eons.method(impl="External")
	def send_message_to_matrix(this):
		pass

	def Build(this):
		emails = this.get_email()
		for email in emails:
			message = f"{email.subject}\n---\n"
			if (email.summary):
				message += email.summary
			elif (email.body):
				message += email.body[:this.message_length]
			message = message.replace("\\n", "<br />")
			message = message.replace("\n", "<br />")
			this.send_message_to_matrix(message=message)
