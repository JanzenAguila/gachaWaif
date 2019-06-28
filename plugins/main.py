from disco.bot import Plugin


class TutorialPlugin(Plugin):
	@Plugin.command('ping')

	def command_ping(self, event):
		event.msg.reply('Pong!')