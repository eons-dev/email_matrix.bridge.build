from ebbs import Builder
import eons
import logging

class email_to_matrix(Builder):
	def __init__(this, name = "Email to Matrix"):
		super().__init__(name)

	@eons.method(impl="External")
	def get_email(this):
		pass

	@eons.method(impl="External")
	def send_message_to_matrix(this):
		pass

	def Build(this):
		emails = this.get_email()
		for email in emails:
			this.send_message_to_matrix(message=email['summary'])
