"""Bachelor AI Study Assistant - V5."""

print("======================================")
print("🤖 BACHELOR AI STUDY ASSISTANT - V5")
print("======================================")

name = input("What is your name? ").strip()
age = int(input("how old are you?"))
hours = float(input("How many hours can you study today? "))
print(f"\nWelcome {name}! 👋")
if hours < 1:
	print("📚 Short session: focus on one subject.")
elif hours <= 2:
	print("📚 Good session: learn a concept and practice it.")
else:
	print("📚 Long session: try several subjects and a quiz!")

subjects = {
	"1": "Python Programming", "2": "Mathematics for AI",
	"3": "Data & Statistics", "4": "AI Fundamentals",
	"5": "French", "6": "English"
}
concepts = {
	"1": ("🐍 Python - Variables", "A variable stores information inside a program.", "age = 18\nname = 'Alex'\nprint(name)"),
	"2": ("📐 Mathematics - Functions", "A function connects an input to an output.", "f(x) = 2x + 3\nIf x = 2, then f(2) = 7."),
	"3": ("📊 Statistics - Mean", "The mean is the average of a group of values.", "(5 + 10 + 15) / 3 = 10"),
	"4": ("🤖 AI - Machine Learning", "Machine Learning allows computers to learn patterns from data instead of following only manually written rules.", ""),
	"5": ("🇫🇷 Français - Passé composé", "Le passé composé est utilisé pour parler d'une action terminée dans le passé.", "Exemple : J'ai étudié Python."),
	"6": ("🇬🇧 English - Past Simple", "The past simple describes completed actions.", "I studied Python yesterday."),
}
practice = {
	"1": ("What does this code display?\nx = 5\ny = 2\nprint(x + y)", "Answer: ", "7"),
	"2": ("Solve: 3x + 5 = 20", "x = ", "5"),
	"3": ("Find the mean: 10, 20, 30", "Answer: ", "20"),
	"4": ("What does ML stand for?", "Answer: ", "machine learning"),
	"5": ("Complétez: Hier, j'___ étudié.", "Réponse: ", "ai"),
	"6": ("What is the past tense of 'go'?", "Answer: ", "went"),
}
hints = {
	"1": "Python executes mathematical operations and print() displays the result.",
	"2": "Try to isolate x on one side of the equation.",
	"3": "Mean = sum of values / number of values.",
	"4": "Think about computers learning patterns from data.",
	"5": "Le passé composé utilise souvent avoir + participe passé.",
	"6": "'Go' is an irregular verb.",
}
quizzes = {
	"1": [("Which function displays text? (1=input, 2=print, 3=int)", "2"), ("What is 5 + 2 * 3?", "11"), ("Which symbol compares two values? (1==, 2==, 3=+)", "2")],
	"2": [("2x = 10. x = ", "5"), ("5 + 5 * 2 = ", "15"), ("Square root of 81 = ", "9")],
	"3": [("Mean of 2, 4, 6 = ", "4"), ("Median of 1, 3, 5 = ", "3"), ("Mean of 10, 20, 30 = ", "20")],
	"4": [("What does AI mean? (1=Artificial Intelligence, 2=Automatic Internet)", "1"), ("Machine Learning learns mainly from: (1=Data, 2=Screens)", "1"), ("Which is a Machine Learning method? (1=Supervised Learning, 2=Internet Learning)", "1")],
	"5": [("Je ___ étudiant : ", "suis"), ("Pluriel de 'cheval' : ", "chevaux"), ("J'___ étudié hier : ", "ai")],
	"6": [("I ___ a student: ", "am"), ("Past tense of 'go': ", "went"), ("Past tense of 'study': ", "studied")],
}

total_score = total_questions = 0
while True:
	print("\n======================================\n📚 SUBJECTS\n======================================")
	for number, title in subjects.items():
		print(f"{number} - {title}")
	print("7 - My results\n0 - Quit")
	subject = input("\nChoose a subject: ").strip()

	if subject == "7":
		print("\n📊 YOUR RESULTS")
		print(f"Correct answers: {total_score}\nQuestions answered: {total_questions}")
		if total_questions:
			percentage = total_score / total_questions * 100
			print(f"Success rate: {percentage:.1f}%")
			print("🔥 Excellent work!" if percentage >= 80 else "👍 Good progress!" if percentage >= 50 else "📚 Keep practicing!")
		else:
			print("You haven't answered any questions yet.")
		continue
	if subject == "0":
		print("\n======================================\n📊 FINAL RESULTS\n======================================")
		print(f"Student: {name}\nScore: {total_score}/{total_questions}")
		if total_questions:
			print(f"Success rate: {total_score / total_questions * 100:.1f}%")
		print(f"\nGoodbye {name}! 👋\nKeep learning AI! 🤖")
		break
	if subject not in subjects:
		print("❌ Invalid subject.")
		continue

	print("\n======================================\n🎯 STUDY MODE\n======================================")
	print("1 - Learn a concept\n2 - Practice exercise\n3 - Get a hint\n4 - Quiz test\n0 - Back")
	mode = input("\nChoose a mode: ").strip()
	if mode == "0":
		continue
	if mode not in {"1", "2", "3", "4"}:
		print("❌ Invalid mode.")
		continue
	if mode == "1":
		title, explanation, example = concepts[subject]
		print(f"\n📖 LEARN A CONCEPT\n\n{title}\n{explanation}")
		if example:
			print(f"Example:\n{example}")
	elif mode == "2":
		question, prompt, correct = practice[subject]
		print(f"\n✏️ PRACTICE EXERCISE\n{question}")
		answer = input(prompt).strip().lower()
		total_questions += 1
		if answer == correct:
			total_score += 1
			print("✅ Correct!")
		else:
			print(f"❌ Incorrect.\nCorrect answer: {correct}")
	elif mode == "3":
		print(f"\n💡 HINT\n{hints[subject]}")
	else:
		score = 0
		print("\n======================================\n🧠 QUIZ TEST\n======================================")
		for index, (question, correct) in enumerate(quizzes[subject], 1):
			answer = input(f"\nQuestion {index}/3\n{question}").strip().lower()
			if answer == correct:
				score += 1
				print("✅ Correct!")
			else:
				print("❌ Incorrect.")
		total_score += score
		total_questions += 3
		print(f"\n🏆 QUIZ RESULT\nScore: {score}/3\nPercentage: {score / 3 * 100:.1f}%")
		print("🔥 Perfect score!" if score == 3 else "👏 Good job!" if score == 2 else "📚 You should review this subject." if score == 1 else "💪 Let's study this subject again.")
