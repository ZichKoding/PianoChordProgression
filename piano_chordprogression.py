'''GPL-3.0-or-later'''
'''Developed by ZichKoding on 07/14/2021'''

import os, sys
import random
import json
import datetime
from kivy.resources import resource_add_path, resource_find
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty


Builder.load_file('piano_chordprogression.kv')

# A function to call into each class for pulling a file from the correct directory.
def get_rando(directory):
	''' directory='enterfoldername/' '''
	mp3files = os.listdir(directory)
	randofile = directory + random.choice(mp3files)
	print('Selecting a random file from', directory)
	return randofile
	

# Difficulty Page
class Difficulty(Screen):
	easy = 0
	easy_incorrect_answer = 0
	medium = 0
	medium_incorrect_answer = 0
	hard = 0
	hard_incorrect_answer = 0
	store = {}
	current_time = datetime.datetime.now()
	progress_report = None
	popupWindow = None

	# Determining which difficulty was pressed for further use in the Piano class.
	diffi_cat = ''
	def diffi(self, button):
		Difficulty.diffi_cat = f'{button}/'
		print(Difficulty.diffi_cat)

	try:
		with open('localprogress.txt') as stored_progress:
			store = json.load(stored_progress)
			slash_removed = 'piano_easy'
			for easy_difficult_extraction in store[slash_removed]:
				easy = easy_difficult_extraction["easy"]
				easy_incorrect_answer = easy_difficult_extraction["incorrect_answer"]


		with open('localprogress.txt') as stored_progress:
			store = json.load(stored_progress)
			slash_removed = 'piano_medium'
			for medium_difficult_extraction in store[slash_removed]:
				medium = medium_difficult_extraction["medium"]
				medium_incorrect_answer = medium_difficult_extraction["incorrect_answer"]


		with open('localprogress.txt') as stored_progress:
			store = json.load(stored_progress)
			slash_removed = 'piano_hard'
			for hard_difficult_extraction in store[slash_removed]:
				hard = hard_difficult_extraction["hard"]
				hard_incorrect_answer = hard_difficult_extraction["incorrect_answer"]
	except:
		print('No previous progress.')

	# This will open the popup window for progress.
	def reset_progress(self):
		try:
			self.show = ResetWindow()
			Difficulty.popupWindow = Popup(title='Progress', content=self.show, size_hint=(None, None), size=(400,400))
			Difficulty.popupWindow.open()
			self.show.current_progress()
		except:
			self.show = ResetWindow()
			Difficulty.popupWindow = Popup(title='Progress', content=self.show, size_hint=(None, None), size=(400,400))
			Difficulty.popupWindow.open()

	# This will help close the popup window if need be.
	def closing_window(self):
		Difficulty.popupWindow.dismiss()





class ResetWindow(FloatLayout):
	# A method to reset the progress back to 0.
	def resetting(self):
		Difficulty.easy = 0
		Difficulty.easy_incorrect_answer = 0
		local_category = 'piano_easy'
		Difficulty.store[local_category] = []
		Difficulty.store[local_category].append({
				'easy': Difficulty.easy,
				'incorrect_answer': Difficulty.easy_incorrect_answer
			})
		with open('localprogress.txt', 'w') as local_json:
			json.dump(Difficulty.store, local_json, sort_keys=True)


		Difficulty.medium = 0
		Difficulty.medium_incorrect_answer = 0
		local_category = 'piano_medium'
		Difficulty.store[local_category] = []
		Difficulty.store[local_category].append({
				'medium': Difficulty.medium,
				'incorrect_answer': Difficulty.medium_incorrect_answer
			})
		with open('localprogress.txt', 'w') as local_json:
			json.dump(Difficulty.store, local_json, sort_keys=True)


		Difficulty.hard = 0
		Difficulty.hard_incorrect_answer = 0
		local_category = 'piano_hard'
		Difficulty.store[local_category] = []
		Difficulty.store[local_category].append({
				'hard': Difficulty.hard,
				'incorrect_answer': Difficulty.hard_incorrect_answer
			})
		with open('localprogress.txt', 'w') as local_json:
			json.dump(Difficulty.store, local_json, sort_keys=True)
		self.ids.cur_prog.text = f"Easy: Correct {Difficulty.easy} Incorrect {Difficulty.easy_incorrect_answer}\nMedium: Correct {Difficulty.medium} Incorrect {Difficulty.medium_incorrect_answer}\nHard: Correct {Difficulty.hard} Incorrect {Difficulty.hard_incorrect_answer}\n\n{Difficulty.current_time}"


	def closing(self):
		print('Attempting to close window......')
		try:
			with open('localprogress.txt') as stored_progress:
				Difficulty.store = json.load(stored_progress)
				slash_removed = 'piano_easy'
				for easy_difficult_extraction in Difficulty.store[slash_removed]:
					Difficulty.easy = easy_difficult_extraction["easy"]
					Difficulty.easy_incorrect_answer = easy_difficult_extraction["incorrect_answer"]


			with open('localprogress.txt') as stored_progress:
				Difficulty.store = json.load(stored_progress)
				slash_removed = 'piano_medium'
				for medium_difficult_extraction in Difficulty.store[slash_removed]:
					Difficulty.medium = medium_difficult_extraction["medium"]
					Difficulty.medium_incorrect_answer = medium_difficult_extraction["incorrect_answer"]


			with open('localprogress.txt') as stored_progress:
				Difficulty.store = json.load(stored_progress)
				slash_removed = 'piano_hard'
				for hard_difficult_extraction in Difficulty.store[slash_removed]:
					Difficulty.hard = hard_difficult_extraction["hard"]
					Difficulty.hard_incorrect_answer = hard_difficult_extraction["incorrect_answer"]	
			self.popupWindow = Difficulty()
			self.popupWindow.closing_window()
		except:
			self.popupWindow = Difficulty()
			self.popupWindow.closing_window()



	def current_progress(self):
		# Updates the current progress if not updated already.
		try:
			with open('localprogress.txt') as stored_progress:
				Difficulty.store = json.load(stored_progress)
				slash_removed = 'piano_easy'
				for easy_difficult_extraction in Difficulty.store[slash_removed]:
					Difficulty.easy = easy_difficult_extraction["easy"]
					Difficulty.easy_incorrect_answer = easy_difficult_extraction["incorrect_answer"]


			with open('localprogress.txt') as stored_progress:
				Difficulty.store = json.load(stored_progress)
				slash_removed = 'piano_medium'
				for medium_difficult_extraction in Difficulty.store[slash_removed]:
					Difficulty.medium = medium_difficult_extraction["medium"]
					Difficulty.medium_incorrect_answer = medium_difficult_extraction["incorrect_answer"]


			with open('localprogress.txt') as stored_progress:
				Difficulty.store = json.load(stored_progress)
				slash_removed = 'piano_hard'
				for hard_difficult_extraction in Difficulty.store[slash_removed]:
					Difficulty.hard = hard_difficult_extraction["hard"]
					Difficulty.hard_incorrect_answer = hard_difficult_extraction["incorrect_answer"]																		
			Difficulty.current_time = datetime.datetime.now()
			self.ids.cur_prog.text = f"Easy: Correct {Difficulty.easy} Incorrect {Difficulty.easy_incorrect_answer}\nMedium: Correct {Difficulty.medium} Incorrect {Difficulty.medium_incorrect_answer}\nHard: Correct {Difficulty.hard} Incorrect {Difficulty.hard_incorrect_answer}\n\n{Difficulty.current_time}"
		except:
			Difficulty.current_time = datetime.datetime.now()
			self.ids.cur_prog.text = f"No progress yet.\n\n{Difficulty.current_time}"


class Piano(Difficulty):
	easy = 0
	easy_incorrect_answer = 0
	medium = 0
	medium_incorrect_answer = 0
	hard = 0
	hard_incorrect_answer = 0

	store = {}


	# Integrate mp3 files based off difficulty and add randomness to it.
	sound = 0
	def dir_choice(self):
		# Extracting the users previous progress if any.
		try:
			if Difficulty.diffi_cat == 'easy/':
				with open('localprogress.txt') as self.stored_progress:
					self.store = json.load(self.stored_progress)
					self.slash_removed = 'piano_easy'
					for self.easy_difficult_extraction in self.store[self.slash_removed]:
						self.easy = self.easy_difficult_extraction["easy"]
						self.easy_incorrect_answer = self.easy_difficult_extraction["incorrect_answer"]

			if Difficulty.diffi_cat == 'medium/':
				with open('localprogress.txt') as self.stored_progress:
					self.store = json.load(self.stored_progress)
					self.slash_removed = 'piano_medium'
					for self.medium_difficult_extraction in self.store[self.slash_removed]:
						self.medium = self.medium_difficult_extraction["medium"]
						self.medium_incorrect_answer = self.medium_difficult_extraction["incorrect_answer"]

			if Difficulty.diffi_cat == 'hard/':
				with open('localprogress.txt') as self.stored_progress:
					self.store = json.load(self.stored_progress)
					self.slash_removed = 'piano_hard'
					for self.hard_difficult_extraction in self.store[self.slash_removed]:
						self.hard = self.auto_difficult_extraction["hard"]
						self.hard_incorrect_answer = self.hard_difficult_extraction["incorrect_answer"]
																					
		except:
			print("No previous progress in this category.")

		# Randomly choosing a sound clip from whichever difficulty was chosen.
		print('piano/' + Difficulty.diffi_cat)
		self.randofile = get_rando('piano/' + Difficulty.diffi_cat)
		print(self.randofile)
		Piano.sound = SoundLoader.load(self.randofile)

	# Creating the play, play again method
	def pg_press(self):
		self.ids.submit_button.disabled = False
		if self.ids.play_playagain.text == 'Play Again?':
			self.sound.stop()
			self.sound.play()
		else:
			self.dir_choice()
			self.sound.play()
			self.ids.chords_expected.text = f'[b]What is the chord progression?'
			self.ids.play_playagain.text = f'Play Again?'

	# Next Song Button
	def ns_press(self):
		self.sound.stop()
		self.ids.play_playagain.disabled = False
		self.ids.next_song.disabled = True
		self.ids.play_playagain.text = 'Play'
		self.ids.chords_expected.text = f'[b]What is the chord progression?'

	# Creating the chord button methods
	def press(self, button):
		# Creating variable
		chord = self.ids.chords_actual.text
		# Enter into the text input box
		self.ids.chords_actual.text = f'{button}'
		self.ids.chords_actual.text = f'{chord} {button}'

	# Creating a backspace button.
	def back_space(self):
		try:
			chord = self.ids.chords_actual.text
			if chord[-1] == '2-' or chord[-1] == '3-' or chord[-1] == '6-':
				self.ids.chords_actual.text = f'{chord[0:-2]}'
			elif chord[-1] == ' ':
				self.ids.chords_actual.text = f'{chord[0:-3]}'
			else:
				self.ids.chords_actual.text = f'{chord[0:-2]}'
		except:
			pass

	# Creating the submit method
	def sub_press(self):
		try:
			self.ids.next_song.disabled = False
			self.sound.stop()
			# Create variables for our widget
			user_answer = self.ids.chords_actual.text
			# Take away the spaces out of the user's answer.
			user_answer_nospaces = user_answer.replace(' ', '')
			# Take the chord progression from the file name.
			note = ''
			for notes in self.randofile:
				if notes == '1' or notes == '2' or notes == '3' or notes == '4' or notes == '5' or notes == '6' or notes == '-':
					if notes == '-':
						note += notes + ' '
					else:
						note += notes + ' '
				elif notes == '.':
					break
			# Get rid of all spaces and compare user's answer to actual answer.
			actual_answer = note.replace(' ', '')
			if user_answer_nospaces == '':
				self.ids.chords_expected.text = f'[b]No answer was given.'
			elif user_answer_nospaces != actual_answer:
				# Easy Difficulty sorting correct incorrect answers and 3 attempts makes you go to the next song.
				if Difficulty.diffi_cat == 'easy/':
					self.easy_incorrect_answer += 1
					self.ids.chords_expected.text = f'[b]{user_answer} is incorrect.\n[u]Easy[/u]: Correct: {self.easy} Incorrect: {self.easy_incorrect_answer}'
					if self.easy_incorrect_answer%3 == 0:
						self.ids.play_playagain.disabled = True
						self.ids.next_song.disabled = False
						self.ids.chords_expected.text = f"[b]The correct answer is {note}.\n Press 'Next Song.'\n[u]Easy[/u]: Correct: {self.easy} Incorrect: {self.easy_incorrect_answer}"

				# Medium Difficulty sorting incorrect answers and 3 attempts makes you go to the next song.
				if Difficulty.diffi_cat == 'medium/':
					self.medium_incorrect_answer += 1
					self.ids.chords_expected.text = f'[b]{user_answer} is incorrect.\n[u]Medium[/u]: Correct: {self.medium} Incorrect: {self.medium_incorrect_answer}'
					if self.medium_incorrect_answer%3 == 0:
						self.ids.play_playagain.disabled = True
						self.ids.next_song.disabled = False
						self.ids.chords_expected.text = f"[b]The correct answer is {note}.\n Press 'Next Song.'\n[u]Medium[/u]: Correct: {self.medium} Incorrect: {self.medium_incorrect_answer}"

				# Hard Difficulty sorting incorrect answers and 3 attempts makes you go to the next song.
				if Difficulty.diffi_cat == 'hard/':
					self.hard_incorrect_answer += 1
					self.ids.chords_expected.text = f'[b]{user_answer} is incorrect.\n[u]Hard[/u]: Correct: {self.hard} Incorrect: {self.hard_incorrect_answer}'
					if self.hard_incorrect_answer%3 == 0:
						self.ids.play_playagain.disabled = True
						self.ids.next_song.disabled = False
						self.ids.chords_expected.text = f"[b]The correct answer is {note}.\n Press 'Next Song.'\n[u]Hard[/u]: Correct: {self.hard} Incorrect: {self.hard_incorrect_answer}"
					
			else:
				self.ns_press()
				# Easy Difficulty sorting correct answers
				if Difficulty.diffi_cat == 'easy/':
					self.easy += 1
					self.ids.chords_expected.text = f"[b]Correct! The answer is {user_answer}.\n Press 'Play' to continue.\n[u]Easy[/u]: Correct: {self.easy} Incorrect: {self.easy_incorrect_answer}"
				# Medium Difficulty sorting correct answers
				elif Difficulty.diffi_cat == 'medium/':
					self.medium += 1
					self.ids.chords_expected.text = f"[b]Correct! The answer is {user_answer}.\n Press 'Play' to continue.\n[u]Medium[/u]: Correct: {self.medium} Incorrect: {self.medium_incorrect_answer}"
				# Hard Difficulty sorting correct answers
				elif Difficulty.diffi_cat == 'hard/':
					self.hard += 1		
					self.ids.chords_expected.text = f"[b]Correct! The answer is {user_answer}.\n Press 'Play' to continue.\n[u]Hard[/u]: Correct: {self.hard} Incorrect: {self.hard_incorrect_answer}"
				


			# Clear the input box.
			self.ids.chords_actual.text = ''
			self.randofile
			# Store progress locally for easy difficulty
			if Difficulty.diffi_cat == 'easy/':
				self.local_category = 'piano_easy'
				self.store[self.local_category] = []
				self.store[self.local_category].append({
						'easy': self.easy,
						'incorrect_answer': self.easy_incorrect_answer
					})
				print(self.store)
				with open('localprogress.txt', 'w') as self.local_json:
					json.dump(self.store, self.local_json, sort_keys=True)

			# Store progress locally for medium difficulty
			elif Difficulty.diffi_cat == 'medium/':
				self.local_category = 'piano_medium'
				self.store[self.local_category] = []
				self.store[self.local_category].append({
						'medium': self.medium,
						'incorrect_answer': self.medium_incorrect_answer
					})
				print(self.store)
				with open('localprogress.txt', 'w') as self.local_json:
					json.dump(self.store, self.local_json, sort_keys=True)

			# Store progress locally for hard difficulty
			elif Difficulty.diffi_cat == 'hard/':
				self.local_category = 'piano_hard'
				self.store[self.local_category] = []
				self.store[self.local_category].append({
						'hard': self.hard,
						'incorrect_answer': self.hard_incorrect_answer
					})
				print(self.store)
				with open('localprogress.txt', 'w') as self.local_json:
					json.dump(self.store, self.local_json, sort_keys=True)
		except:
			pass

	# Back to Starting Menu
	def back_to_cat(self):
		try:
			self.ids.chords_actual.text = ''
			self.ids.chords_expected.text = f'[b]What is the chord progression?'
			self.ids.play_playagain.text = f'Play'
			self.ids.play_playagain.disabled = False
			self.ids.next_song.disabled = True
			self.ids.submit_button.disabled = True
			self.sound.stop()
		except:
			pass

class HarmonicDictationApp(App):
	def build(self):
		sm = ScreenManager()
		sm.add_widget(Difficulty(name='difficulty'))
		sm.add_widget(Piano(name='PianoClips'))
		return sm


if __name__ == '__main__':
	if hasattr(sys, '_MEIPASS'):
		resource_add_path(os.path.join(sys._MEIPASS))
	HarmonicDictationApp().run()
